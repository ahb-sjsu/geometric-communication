## Appendix B: The eris-ketos Toolkit

This appendix provides a practical reference for the **eris-ketos** Python package (v0.2.0), which implements the geometric analysis pipeline described in Chapters 5--7 and applied to 8,719 annotated sperm whale codas from the Dominica Sperm Whale Project. The package is open-source (MIT licence) and available on PyPI and GitHub. Everything reported in the cetacean chapters of this book can be reproduced using the code documented here.

The name *ketos* (Greek: *ketos*, from which "cetacean" derives) reflects the package's focus on whale communication; *eris* situates it within the broader ErisML geometric analysis family. The toolkit provides four analysis modules --- hyperbolic embeddings, topological data analysis, SPD manifold metrics, and adversarial robustness testing --- each capturing a different geometric aspect of cetacean vocalisation structure.

---

### B.1 Installation

The core package requires Python 3.10 or later and depends on NumPy, SciPy, PyTorch, and librosa:

```bash
pip install eris-ketos
```

Optional dependency groups are available for topological data analysis, machine learning utilities, and data loading:

```bash
pip install eris-ketos[tda]       # adds ripser, persim
pip install eris-ketos[ml]        # adds timm, torchaudio, scikit-learn
pip install eris-ketos[data]      # adds datasets (HuggingFace), pandas
pip install eris-ketos[all]       # everything including dev tools
```

The `[tda]` extra is required for persistent homology computation (`compute_persistence`, `tda_feature_vector`). The `[data]` extra is required for the `load_dswp()` convenience function that downloads the DSWP dataset from HuggingFace. All other modules work with the core installation.

For development and testing:

```bash
git clone https://github.com/ahb-sjsu/eris-ketos.git
cd eris-ketos
pip install -e ".[all]"
pytest
```

The package is built with Hatch and uses ruff for linting and mypy for type checking. All public functions carry full type annotations.

---

### B.2 Module Overview

The package is organised into five modules, each corresponding to a distinct geometric analysis method:

| Module | Purpose | Key exports | Dependencies |
|---|---|---|---|
| `poincare_coda` | Hyperbolic embeddings of hierarchical coda structure | `PoincareBall`, `HyperbolicMLR`, `embed_taxonomy_hyperbolic` | torch |
| `tda_clicks` | Topological data analysis of click timing patterns | `compute_persistence`, `tda_feature_vector`, `time_delay_embedding` | ripser (optional) |
| `spd_spectral` | SPD manifold analysis of spectral covariance | `SPDManifold`, `spd_features_from_spectrogram`, `compute_spectral_trajectory` | torch |
| `acoustic_transforms` | Parametric acoustic perturbations | `AcousticTransform`, `make_acoustic_transform_suite`, `TransformChain` | numpy |
| `decoder_robustness` | Adversarial robustness benchmarking | `DecoderRobustnessIndex`, `CodaSemanticDistance`, `DRIResult` | numpy |

All public symbols are re-exported from the package root, so both `from eris_ketos import PoincareBall` and `from eris_ketos.poincare_coda import PoincareBall` work identically.

The modules are designed to be composed: `acoustic_transforms` feeds into `decoder_robustness`; `poincare_coda` provides the embedding space for classification; `tda_clicks` and `spd_spectral` extract complementary feature vectors that can be concatenated for downstream tasks. The overall pipeline, as applied in Chapter 7, runs: raw signal (or ICI annotations) through three parallel geometric analyses (hyperbolic embedding, TDA, SPD), then through adversarial robustness evaluation.

---

### B.3 API Reference

#### B.3.1 poincare_coda --- Hyperbolic Embeddings

**`PoincareBall(c: float = 1.0)`**

The core class implementing Mobius gyrovector operations on the Poincare ball model of hyperbolic space, $\mathbb{B}^d_c = \{x \in \mathbb{R}^d : c\|x\|^2 < 1\}$. The curvature parameter `c` controls how aggressively distances grow toward the boundary; higher `c` increases hyperbolic spread.

Methods:

- **`expmap0(v: Tensor) -> Tensor`** --- Exponential map from the origin. Maps a tangent vector $v$ at the origin to a point on the ball via $\exp_0(v) = \tanh(\sqrt{c}\|v\|) \cdot v / (\sqrt{c}\|v\|)$. This is the primary mechanism for placing features onto the ball.

- **`logmap0(y: Tensor) -> Tensor`** --- Logarithmic map to the origin. The inverse of `expmap0`: maps a ball point back to the tangent space at the origin via $\log_0(y) = \text{arctanh}(\sqrt{c}\|y\|) \cdot y / (\sqrt{c}\|y\|)$.

- **`mobius_add(x: Tensor, y: Tensor) -> Tensor`** --- Mobius addition, the hyperbolic analogue of vector addition. Defined as:

$$x \oplus y = \frac{(1 + 2c\langle x,y\rangle + c\|y\|^2)x + (1 - c\|x\|^2)y}{1 + 2c\langle x,y\rangle + c^2\|x\|^2\|y\|^2}$$

- **`dist(x: Tensor, y: Tensor) -> Tensor`** --- Geodesic distance on the ball: $d(x, y) = (2/\sqrt{c}) \cdot \text{arctanh}(\sqrt{c}\|(-x) \oplus y\|)$. This grows exponentially as points approach the boundary, which is why trees embed naturally: exponential volume growth in hyperbolic space matches exponential branching in trees.

- **`dist_to_origin(x: Tensor) -> Tensor`** --- Cheaper special case of `dist` when one point is the origin.

- **`midpoint(x: Tensor, y: Tensor) -> Tensor`** --- Einstein midpoint of two points, computed via conformal factors.

- **`project(x: Tensor, eps: float = 1e-5) -> Tensor`** --- Projects points onto the open ball by clamping norms to $1/\sqrt{c} - \epsilon$. Called internally by other methods to maintain numerical stability.

All methods operate on batched tensors (arbitrary leading dimensions) and are differentiable through PyTorch autograd.

**`HyperbolicMLR(embed_dim: int, num_classes: int, c: float = 1.0)`**

Hyperbolic Multinomial Logistic Regression. An `nn.Module` that classifies points on the Poincare ball by computing negative scaled geodesic distances to learned prototypes. Each class has a prototype (stored as a tangent vector at the origin, mapped to the ball via `expmap0`) and a learnable temperature parameter.

- **`forward(x: Tensor) -> Tensor`** --- Computes logits as $-d(x, p_k) \cdot \exp(s_k)$ for each class $k$, where $p_k$ is the prototype and $s_k$ is the log-scale.

- **`init_from_taxonomy(embeddings: Tensor) -> None`** --- Initialises prototypes from pre-computed taxonomic embeddings (e.g., from `embed_taxonomy_hyperbolic`). This is the key mechanism for encoding prior structural knowledge: classes that are taxonomically close start with nearby prototypes.

- **`prototypes`** (property) --- Returns the current prototype positions on the ball.

**`embed_taxonomy_hyperbolic(dist_matrix: ndarray, embed_dim: int, c: float = 1.0, scale: float = 0.7) -> Tensor`**

Embeds a taxonomic distance matrix into the Poincare ball via spectral decomposition of a Gaussian kernel. The `scale` parameter controls the maximum norm relative to the ball radius (must be in $(0, 1)$). Returns a tensor of shape `[n, embed_dim]`.

**`build_distance_matrix(species_info: dict, levels: tuple) -> ndarray`**

Constructs an integer-valued taxonomic distance matrix from a dictionary of species (or coda type) metadata. Distance is the shallowest taxonomic level at which two entries first differ. For the coda system, typical levels are `('variant', 'click_count', 'rhythm_class')`, finest to coarsest.

#### B.3.2 tda_clicks --- Topological Data Analysis

**`time_delay_embedding(signal: ndarray, delay: int = 10, dim: int = 3) -> ndarray`**

Takens' time-delay embedding. Given a 1D signal $x(t)$, constructs vectors $v(t) = [x(t), x(t+\tau), \ldots, x(t+(d-1)\tau)]$. By Takens' theorem, for generic delay $\tau$ and embedding dimension $d \geq 2m+1$ (where $m$ is the attractor dimension), this reconstructs the topology of the underlying dynamical system. Returns a point cloud of shape `[n_points, dim]`.

The `signal` argument accepts either raw audio samples or inter-click interval sequences. For ICI-based analysis (as in Chapter 7), the "signal" is the vector of measured intervals.

**`compute_persistence(signal: ndarray, delay: int = 10, dim: int = 3, max_points: int = 1000, max_homology_dim: int = 1, thresh: float = 2.0, seed: int | None = None) -> PersistenceResult`**

The primary TDA pipeline function. Executes four steps:

1. Time-delay embeds the signal into $\mathbb{R}^{\text{dim}}$.
2. Subsamples the point cloud to at most `max_points` for computational tractability.
3. Normalises to zero mean and unit variance.
4. Computes Vietoris-Rips persistent homology via ripser up to dimension `max_homology_dim`.

Returns a `PersistenceResult` dataclass containing:
- `diagrams`: list of persistence diagrams (one per homology dimension), each an array of shape `[n_features, 2]` with columns `(birth, death)`.
- `cloud`: the normalised point cloud used for computation.
- `max_dim`: the maximum homology dimension computed.

Raises `ImportError` if ripser is not installed (requires the `[tda]` extra).

**`tda_feature_vector(result: PersistenceResult) -> ndarray`**

Extracts a fixed-length summary vector from persistence diagrams: 8 statistics per homology dimension, yielding $8 \times (d_{\max} + 1)$ features total. With the default `max_homology_dim=1`, this produces 16 features.

The 8 per-dimension statistics are:

| Index | Feature | Description |
|---|---|---|
| 0 | count | Number of finite-lifetime features |
| 1 | mean_lifetime | Average persistence |
| 2 | std_lifetime | Spread of persistence values |
| 3 | max_lifetime | Most persistent feature |
| 4 | p75_lifetime | 75th percentile of lifetimes |
| 5 | mean_birth | Average birth time |
| 6 | total_persistence | Sum of squared lifetimes ($L^2$ norm) |
| 7 | normalized_persistence | $\sqrt{\text{total}} / \text{count}$ |

The H0 features (connected components) capture cluster structure: regular codas with uniform ICI patterns produce tight clusters (low H0 persistence), while compound codas with multi-component timing produce elevated H0 persistence. The H1 features (loops) capture cyclic patterns: irregular codas with variable timing produce topological loops (high H1 persistence), while regular codas do not.

#### B.3.3 spd_spectral --- SPD Manifold Analysis

**`SPDManifold`**

Static methods implementing the log-Euclidean Riemannian metric on the manifold of symmetric positive definite matrices $\text{SPD}(n) = \{S \in \mathbb{R}^{n \times n} : S = S^\top, S \succ 0\}$.

- **`log_map(S: Tensor) -> Tensor`** --- Matrix logarithm via eigendecomposition: $\log(S) = U \cdot \text{diag}(\log \lambda) \cdot U^\top$. Maps from the SPD manifold to the tangent space (symmetric matrices).

- **`exp_map(X: Tensor) -> Tensor`** --- Matrix exponential: the inverse of `log_map`. Maps symmetric matrices back to the SPD manifold.

- **`distance(S1: Tensor, S2: Tensor) -> Tensor`** --- Log-Euclidean distance: $d_{LE}(S_1, S_2) = \|\log(S_1) - \log(S_2)\|_F$. This is a proper metric on SPD(n) that is more discriminative than the Frobenius norm $\|S_1 - S_2\|_F$ because it respects the curved geometry of the positive-definite cone. In particular, it correctly captures the fact that two covariance matrices can be far apart in spectral structure while being close in Frobenius norm (if they differ primarily in the orientation of their eigenvectors).

- **`frechet_mean(matrices: Tensor, weights: Tensor | None = None) -> Tensor`** --- Log-Euclidean Frechet mean: $\bar{S} = \exp(\sum_i w_i \log(S_i))$. The Riemannian-aware "average" covariance matrix, used to compute per-type centroids in the SPD feature space.

All methods support batched inputs with arbitrary leading dimensions.

**`compute_covariance(spectrogram: ndarray, n_bands: int = 16, regularize: float = 1e-4) -> ndarray`**

Computes a frequency-band covariance matrix from a mel spectrogram. Groups mel frequency bins into `n_bands` equal-sized bands, averages within each band across frequencies, then computes the time-domain covariance across bands. Adds `regularize * I` to guarantee positive definiteness. Returns a matrix of shape `[n_bands, n_bands]`.

**`spd_features_from_spectrogram(spectrogram: ndarray, n_bands: int = 16, regularize: float = 1e-4) -> ndarray`**

The end-to-end SPD feature extraction function. Computes the covariance matrix, applies the log-Euclidean map, and extracts the upper triangle of $\log(\text{Cov})$ as a feature vector. Returns a vector of length $n_{\text{bands}} \times (n_{\text{bands}} + 1) / 2$. With the default `n_bands=16`, this yields 136 features; with `n_bands=8`, it yields 36.

**`compute_spectral_trajectory(spectrogram: ndarray, n_bands: int = 16, window_frames: int = 32, hop_frames: int = 16, sr: int = 32000, hop_length: int = 512, regularize: float = 1e-4) -> SpectralTrajectory`**

Computes a time-varying trajectory on the SPD manifold by sliding a window across the spectrogram and computing a covariance matrix at each position. Returns a `SpectralTrajectory` dataclass with:

- `matrices`: the sequence of SPD matrices, shape `[n_windows, n_bands, n_bands]`.
- `timestamps`: centre time (in seconds) of each window.
- `geodesic_deviation`: the ratio $(L_{\text{path}} - d_{\text{geodesic}}) / d_{\text{geodesic}}$, where $L_{\text{path}}$ is the summed log-Euclidean distance along consecutive windows and $d_{\text{geodesic}}$ is the direct distance between the first and last matrices. A deviation of 0 means the spectral structure evolved along a perfect geodesic (a smooth, "straight" transition between two vowel states); higher values indicate a more complex, wandering trajectory.

This function is the computational implementation of the diphthong analysis described in Chapter 7, Section 7.3.

#### B.3.4 acoustic_transforms --- Parametric Perturbations

**`AcousticTransform`**

A dataclass wrapping a parametric acoustic perturbation function. Each transform has:

- `name: str` --- Identifier (e.g., `"additive_noise"`, `"doppler_shift"`).
- `fn: Callable[[ndarray, int, float], ndarray]` --- The transform function, taking `(signal, sample_rate, intensity)` and returning a perturbed signal.
- `intensity_range: tuple[float, float]` --- Valid intensity range (default: `(0.0, 1.0)`).
- `is_invariant: bool` --- Whether a correct decoder should be invariant to this transform.

Calling `transform(signal, sr, intensity)` applies the perturbation. At intensity 0.0, the signal is always unchanged.

**`make_acoustic_transform_suite() -> list[AcousticTransform]`**

Returns the full suite of nine acoustic transforms used in the DRI analysis:

| Transform | Type | Behaviour at intensity=1.0 |
|---|---|---|
| `amplitude_scale` | Invariant | Scale by 0.1x to 10x (log-uniform) |
| `time_shift` | Invariant | Circular shift up to 25% of signal |
| `additive_noise` | Invariant | Gaussian white noise at ~0 dB SNR |
| `pink_noise` | Invariant | 1/f noise at ~0 dB SNR |
| `doppler_shift` | Stress | ~5% frequency shift |
| `multipath_echo` | Stress | Echo at ~50ms delay, 30% attenuation |
| `time_stretch` | Stress | Up to +/-20% speed change |
| `spectral_mask` | Stress | Zero out up to 40% of spectrum |
| `click_dropout` | Stress | Zero out up to 30% of signal in random segments |

The invariant/stress distinction matters for DRI interpretation: high omega on invariant transforms indicates a decoder bug; high omega on stress transforms may be legitimate.

**`TransformChain`**

Composes multiple transforms into a chain for compound distortion testing. Created from a list of `(transform, intensity)` pairs and called on a signal to apply each transform sequentially. The class method `TransformChain.generate_chains()` produces random chains for systematic testing.

#### B.3.5 decoder_robustness --- Decoder Robustness Index

**`CodaDecoder` (Protocol)**

Any object with a `classify(signal: ndarray, sr: int) -> str` method. The DRI framework is decoder-agnostic: implement this interface to plug in any classifier, from a nearest-centroid baseline to a deep learning model like WhAM.

**`CodaSemanticDistance(feature_weights: dict | None = None, coda_features: dict | None = None)`**

Computes graduated semantic distance between coda type predictions. When both predictions have known feature decompositions (rhythm, tempo, rubato, ornamentation), the distance is weighted by feature importance:

$$\omega(y, \hat{y}) = \max\left(0.5, \; 0.5 + 0.5 \cdot \frac{\sum_f w_f \cdot \mathbf{1}[y_f \neq \hat{y}_f]}{\sum_f w_f}\right)$$

Default weights: rhythm = 1.0, tempo = 0.7, rubato = 0.4, ornamentation = 0.2. The minimum 0.5 penalty ensures any classification flip is registered. When feature decompositions are unavailable, falls back to a binary mismatch penalty of 0.75.

**`DecoderRobustnessIndex(transforms: list[AcousticTransform], semantic_distance: CodaSemanticDistance | None = None)`**

The main adversarial fuzzing engine. Key methods:

- **`measure(decoder, signals, sr=32000, intensities=None, n_chains=30, chain_max_length=3) -> DRIResult`** --- Full DRI measurement. Applies all transforms at each intensity level, generates and tests compositional chains, and runs adversarial threshold search. Returns a `DRIResult` containing:
  - `dri`: the scalar index ($0.5 \bar{\omega} + 0.3 \omega_{75} + 0.2 \omega_{95}$).
  - `dri_invariant`: DRI computed only on invariant transforms.
  - `dri_stress`: DRI computed only on stress transforms.
  - `per_transform`: dict mapping each transform name to its mean omega.
  - `adversarial_thresholds`: dict mapping each transform to its minimal flip intensity.
  - `chain_results`: list of (chain description, mean omega) for compositional tests.

- **`sensitivity_profile(decoder, signals, sr) -> dict[str, float]`** --- Quick profile mapping each transform to its mean omega at full intensity.

- **`intensity_sweep(decoder, signals, sr, transform, n_points=10) -> list[tuple[float, float]]`** --- Sweeps a single transform from intensity 0 to 1, returning the (intensity, mean_omega) curve. Reveals the activation threshold where the decoder starts failing.

- **`find_adversarial_threshold(decoder, signal, sr, transform, tolerance=0.01) -> float`** --- Binary search for the minimal intensity that flips the decoder output on a single signal. Returns 1.0 if no flip is found at any intensity.

---

### B.4 Worked Examples

The examples below demonstrate the four core analysis pipelines. All code is self-contained and runnable with the appropriate `[tda]` or `[data]` extras installed.

#### B.4.1 Embedding Coda Features on the Poincare Ball

This example constructs the coda type taxonomy described in Chapter 5, embeds it into the Poincare ball, and trains a hyperbolic classifier.

```python
import torch
import numpy as np
from eris_ketos.poincare_coda import (
    PoincareBall,
    HyperbolicMLR,
    build_distance_matrix,
    embed_taxonomy_hyperbolic,
)

# Define the coda type taxonomy
# Each entry maps a coda type to its feature decomposition
coda_taxonomy = {
    "5R1": {"rhythm_class": "regular", "click_count": "5", "variant": "1"},
    "5R2": {"rhythm_class": "regular", "click_count": "5", "variant": "2"},
    "5R3": {"rhythm_class": "regular", "click_count": "5", "variant": "3"},
    "4R1": {"rhythm_class": "regular", "click_count": "4", "variant": "1"},
    "4R2": {"rhythm_class": "regular", "click_count": "4", "variant": "2"},
    "3R1": {"rhythm_class": "regular", "click_count": "3", "variant": "1"},
    "5D1": {"rhythm_class": "deceleration", "click_count": "5", "variant": "1"},
    "5D2": {"rhythm_class": "deceleration", "click_count": "5", "variant": "2"},
    "4D1": {"rhythm_class": "deceleration", "click_count": "4", "variant": "1"},
    "4i":  {"rhythm_class": "irregular", "click_count": "4", "variant": "0"},
    "5i":  {"rhythm_class": "irregular", "click_count": "5", "variant": "0"},
    "1+1+3": {"rhythm_class": "compound", "click_count": "1+1+3", "variant": "0"},
    "2+3":   {"rhythm_class": "compound", "click_count": "2+3", "variant": "0"},
}

# Build taxonomic distance matrix
# Levels from finest to coarsest: variant -> click_count -> rhythm_class
dist_matrix = build_distance_matrix(
    coda_taxonomy,
    levels=("variant", "click_count", "rhythm_class"),
)
print(f"Distance matrix: {dist_matrix.shape}")
print(f"Unique distances: {sorted(set(dist_matrix.flatten()))}")
# -> [0.0, 1.0, 2.0, 3.0, 4.0]

# Embed into Poincare ball
embed_dim = 16
embeddings = embed_taxonomy_hyperbolic(dist_matrix, embed_dim=embed_dim, c=1.0)
print(f"Embeddings: {embeddings.shape}")
print(f"Max norm: {embeddings.norm(dim=-1).max():.4f}")  # must be < 1.0

# Verify: taxonomically close types should have small hyperbolic distances
ball = PoincareBall(c=1.0)
d_5R1_5R2 = ball.dist(embeddings[0:1], embeddings[1:2]).item()
d_5R1_4i  = ball.dist(embeddings[0:1], embeddings[9:10]).item()
print(f"d(5R1, 5R2) = {d_5R1_5R2:.3f}")   # small: same rhythm, same clicks
print(f"d(5R1, 4i)  = {d_5R1_4i:.3f}")     # large: different rhythm class

# Train a classifier with taxonomy-initialised prototypes
n_classes = len(coda_taxonomy)
classifier = HyperbolicMLR(embed_dim=embed_dim, num_classes=n_classes, c=1.0)
classifier.init_from_taxonomy(embeddings)

# Map feature vectors onto the ball and classify
features = torch.randn(100, embed_dim) * 0.1  # synthetic features
on_ball = ball.expmap0(features * 0.3)         # scale to stay inside ball
logits = classifier(on_ball)                   # [100, n_classes]
predictions = logits.argmax(dim=1)             # predicted class indices
```

The Poincare ball embedding places taxonomically related types (e.g., 5R1, 5R2, 5R3) near each other and taxonomically distant types (e.g., 5R1, 1+1+3) far apart, with the exponential growth of hyperbolic distance providing natural separation between hierarchy levels.

#### B.4.2 Computing Persistence Diagrams from Click Patterns

This example computes persistent homology on inter-click interval point clouds and extracts topological feature vectors.

```python
import numpy as np
from eris_ketos.tda_clicks import (
    time_delay_embedding,
    compute_persistence,
    tda_feature_vector,
)

# Simulate inter-click intervals for different coda types
# Regular coda: uniform timing
regular_icis = np.array([0.35, 0.35, 0.36, 0.34, 0.35, 0.36, 0.35, 0.34, 0.35])

# Irregular coda: variable timing
irregular_icis = np.array([0.20, 0.50, 0.15, 0.45, 0.25, 0.55, 0.18, 0.42, 0.30])

# Compound coda: grouped timing (1+1+3 pattern)
compound_icis = np.array([0.80, 0.75, 0.20, 0.21, 0.19, 0.00, 0.00, 0.00, 0.00])

# Approach 1: Direct ICI point cloud (as used in Chapter 7)
# Build a point cloud from multiple codas of the same type
n_codas = 100
regular_cloud = np.array([
    regular_icis + np.random.normal(0, 0.02, 9) for _ in range(n_codas)
])
print(f"ICI point cloud shape: {regular_cloud.shape}")  # [100, 9]

# Approach 2: Time-delay embedding of audio signal
# Reconstruct the vocal attractor from a 1D signal
audio_signal = np.random.randn(32000).astype(np.float32)  # placeholder
cloud = time_delay_embedding(audio_signal, delay=10, dim=3)
print(f"Delay-embedded cloud: {cloud.shape}")  # [n_points, 3]

# Compute persistent homology
result = compute_persistence(
    audio_signal,
    delay=10,        # time delay tau (samples)
    dim=3,           # embedding dimension
    max_points=1000, # subsample for tractability
    max_homology_dim=1,  # compute H0 and H1
    thresh=2.0,      # maximum filtration value
    seed=42,         # for reproducible subsampling
)
print(f"H0 diagram: {result.diagrams[0].shape}")  # [n_components, 2]
print(f"H1 diagram: {result.diagrams[1].shape}")  # [n_loops, 2]

# Extract fixed-length feature vector
features = tda_feature_vector(result)
print(f"TDA feature vector: {features.shape}")  # [16] = 8 features x 2 dimensions
print(f"H0 features: {features[:8]}")
print(f"H1 features: {features[8:]}")

# Compare topological signatures across coda types
for name, icis in [("Regular", regular_icis), ("Irregular", irregular_icis)]:
    # Tile into a point cloud (simulating multiple codas with noise)
    cloud = np.array([icis + np.random.normal(0, 0.03, len(icis))
                      for _ in range(200)])
    # Use ripser directly on the ICI point cloud
    res = compute_persistence(cloud.flatten(), delay=1, dim=len(icis),
                              max_points=200)
    feat = tda_feature_vector(res)
    print(f"{name}: H0_count={feat[0]:.0f}, H1_count={feat[8]:.0f}, "
          f"H1_max_life={feat[11]:.4f}")
```

The key insight is that regular codas produce tight clusters with low H1 persistence (no topological loops), while irregular codas produce spread distributions with detectable loops --- the topological fingerprint of timing variability. These signatures are invariant to monotone transformations of the distance metric, making them robust to amplitude scaling and recording conditions.

#### B.4.3 Extracting SPD Features from Spectrograms

This example demonstrates the SPD manifold analysis pipeline: from raw audio to frequency-band covariance matrices to Riemannian feature vectors.

```python
import numpy as np
import torch
import librosa
from eris_ketos.spd_spectral import (
    SPDManifold,
    compute_covariance,
    spd_features_from_spectrogram,
    compute_spectral_trajectory,
)

# Load or synthesise a coda signal
sr = 32000
duration = 1.0
t = np.linspace(0, duration, int(sr * duration))
# Synthetic click train: 5 clicks at ~0.2s intervals
signal = np.zeros_like(t, dtype=np.float32)
for click_time in [0.1, 0.3, 0.5, 0.7, 0.9]:
    click_idx = int(click_time * sr)
    click_len = int(0.003 * sr)
    for k in range(click_len):
        if click_idx + k < len(signal):
            env = np.exp(-0.5 * ((k - click_len/2) / (click_len/5))**2)
            signal[click_idx + k] = env * np.sin(2 * np.pi * 5000 * k / sr)

# Compute mel spectrogram
mel_spec = librosa.feature.melspectrogram(
    y=signal, sr=sr, n_mels=64, n_fft=1024, hop_length=256
)
mel_db = librosa.power_to_db(mel_spec + 1e-10)
print(f"Spectrogram shape: {mel_db.shape}")  # [64, n_frames]

# Extract SPD covariance features (one-shot)
features = spd_features_from_spectrogram(mel_db, n_bands=16)
print(f"SPD feature vector: {features.shape}")  # [136] = 16*17/2

# With n_bands=8 (as used in Chapter 7 for cetacean analysis)
features_8 = spd_features_from_spectrogram(mel_db, n_bands=8)
print(f"SPD feature vector (8 bands): {features_8.shape}")  # [36] = 8*9/2

# Compute the raw covariance matrix for inspection
cov = compute_covariance(mel_db, n_bands=8, regularize=1e-4)
print(f"Covariance matrix: {cov.shape}")  # [8, 8]
print(f"Eigenvalues: {np.linalg.eigvalsh(cov)}")  # all positive (SPD)

# SPD manifold distances between two codas
cov1 = torch.tensor(cov, dtype=torch.float32)
cov2 = torch.tensor(
    compute_covariance(mel_db + np.random.randn(*mel_db.shape) * 0.1,
                       n_bands=8),
    dtype=torch.float32,
)
d_le = SPDManifold.distance(cov1, cov2)
print(f"Log-Euclidean distance: {d_le.item():.4f}")

# Frechet mean of multiple covariance matrices
matrices = torch.stack([cov1, cov2])
mean_cov = SPDManifold.frechet_mean(matrices)
print(f"Frechet mean eigenvalues: {torch.linalg.eigvalsh(mean_cov).numpy()}")

# Compute spectral trajectory (diphthong analysis)
trajectory = compute_spectral_trajectory(
    mel_db,
    n_bands=8,
    window_frames=16,   # window size in spectrogram frames
    hop_frames=8,       # hop size
    sr=sr,
    hop_length=256,
)
print(f"Trajectory: {len(trajectory.timestamps)} windows")
print(f"Geodesic deviation: {trajectory.geodesic_deviation:.4f}")
# Low deviation = smooth vowel transition (geodesic on SPD manifold)
# High deviation = complex spectral evolution
```

The geodesic deviation metric is the key output for diphthong analysis (Chapter 7, Section 7.3): a coda whose spectral covariance evolves along a geodesic on the SPD manifold is undergoing a smooth, vowel-like transition between two spectral states. Higher deviations indicate more complex spectral dynamics --- potentially encoding additional information beyond the basic coda type.

#### B.4.4 Running Adversarial Robustness (DRI) Analysis

This example demonstrates the full Decoder Robustness Index pipeline, from building a decoder to interpreting the diagnostic output.

```python
import numpy as np
from eris_ketos.acoustic_transforms import (
    make_acoustic_transform_suite,
    TransformChain,
)
from eris_ketos.decoder_robustness import (
    DecoderRobustnessIndex,
    CodaSemanticDistance,
    DRIResult,
)

# Step 1: Define a decoder (any object with classify(signal, sr) -> str)
class SimpleICIDecoder:
    """Nearest-centroid decoder based on inter-click intervals."""

    def __init__(self, centroids: dict[str, np.ndarray]):
        self.centroids = centroids

    def _extract_icis(self, signal: np.ndarray, sr: int) -> np.ndarray:
        """Detect clicks via energy peaks and measure intervals."""
        frame_len = int(0.005 * sr)
        hop = frame_len // 2
        energy = np.array([
            np.sum(signal[i:i+frame_len]**2)
            for i in range(0, len(signal) - frame_len, hop)
        ])
        threshold = np.mean(energy) + 2 * np.std(energy)
        peaks = []
        in_peak = False
        for i, e in enumerate(energy):
            if e > threshold and not in_peak:
                peaks.append(i * hop / sr)
                in_peak = True
            elif e <= threshold:
                in_peak = False
        icis = np.zeros(9, dtype=np.float32)
        for i in range(min(len(peaks) - 1, 9)):
            icis[i] = peaks[i + 1] - peaks[i]
        return icis

    def classify(self, signal: np.ndarray, sr: int) -> str:
        icis = self._extract_icis(signal, sr)
        best_type, best_dist = "", float("inf")
        for coda_type, centroid in self.centroids.items():
            d = np.linalg.norm(centroid - icis)
            if d < best_dist:
                best_type, best_dist = coda_type, d
        return best_type

# Step 2: Build centroids from annotated ICI data
centroids = {
    "5R1": np.array([0.35, 0.35, 0.35, 0.35, 0, 0, 0, 0, 0], dtype=np.float32),
    "5R3": np.array([0.30, 0.30, 0.30, 0.30, 0, 0, 0, 0, 0], dtype=np.float32),
    "1+1+3": np.array([0.80, 0.75, 0.20, 0.20, 0, 0, 0, 0, 0], dtype=np.float32),
}
decoder = SimpleICIDecoder(centroids)

# Step 3: Prepare test signals (synthetic click trains)
def make_click_train(icis, sr=32000):
    total = sum(icis) + 0.05
    signal = np.zeros(int(total * sr), dtype=np.float32)
    t = 0.01
    click_n = int(0.003 * sr)
    for ici in [0.0] + list(icis):
        t += ici
        idx = int(t * sr)
        for k in range(click_n):
            if idx + k < len(signal):
                env = np.exp(-0.5 * ((k - click_n/2) / (click_n/5))**2)
                signal[idx + k] = env * np.sin(2 * np.pi * 5000 * k / sr)
    return signal

test_signals = [
    make_click_train([0.35, 0.35, 0.35, 0.35]),  # 5R1
    make_click_train([0.30, 0.30, 0.30, 0.30]),  # 5R3
    make_click_train([0.80, 0.75, 0.20, 0.20]),  # 1+1+3
]

# Step 4: Run full DRI measurement
transforms = make_acoustic_transform_suite()
semantic_distance = CodaSemanticDistance()
dri = DecoderRobustnessIndex(transforms, semantic_distance)

result = dri.measure(
    decoder,
    test_signals,
    sr=32000,
    intensities=[0.3, 0.6, 1.0],  # three intensity levels
    n_chains=15,                    # compositional chains to test
    chain_max_length=2,             # max transforms per chain
)

# Step 5: Interpret results
print(f"Overall DRI: {result.dri:.4f}")
print(f"  Invariant transforms: {result.dri_invariant:.4f}")
print(f"  Stress transforms:    {result.dri_stress:.4f}")

# Sensitivity profile: which transforms cause the most damage?
print("\nPer-transform sensitivity:")
for name, omega in sorted(result.per_transform.items(), key=lambda x: -x[1]):
    print(f"  {name:>20s}: omega = {omega:.4f}")

# Adversarial thresholds: how little perturbation flips the decoder?
print("\nAdversarial thresholds (lower = more vulnerable):")
for name, thresh in sorted(result.adversarial_thresholds.items(),
                            key=lambda x: x[1]):
    print(f"  {name:>20s}: threshold = {thresh:.3f}")

# Step 6: Detailed intensity sweep for the most disruptive transform
worst_transform = max(result.per_transform, key=result.per_transform.get)
for t in transforms:
    if t.name == worst_transform:
        curve = dri.intensity_sweep(decoder, test_signals, 32000, t, n_points=11)
        print(f"\nIntensity sweep for '{worst_transform}':")
        for intensity, omega in curve:
            bar = "#" * int(omega * 40)
            print(f"  intensity={intensity:.1f}: omega={omega:.4f} |{bar}")
        break
```

The DRI output tells you three things: (1) the overall robustness of the decoder on a 0--1 scale; (2) which specific acoustic conditions cause the most degradation (the sensitivity profile); and (3) how little perturbation is needed to flip the decoder's output (adversarial thresholds). A robust decoder should have low DRI on invariant transforms (amplitude scaling, time shift, mild noise) and may legitimately show higher DRI on stress transforms (Doppler shift, click dropout).

---

### B.5 Reproducing the Chapter 7 Results

This section provides step-by-step instructions for reproducing all cetacean analysis results reported in Chapter 7 of this book.

#### B.5.1 Environment Setup

```bash
# Create a clean environment
python -m venv eris-env
source eris-env/bin/activate        # Linux/macOS
# eris-env\Scripts\activate         # Windows

# Install all dependencies
pip install eris-ketos[all]
pip install matplotlib seaborn adjustText jupytext

# Verify installation
python -c "from eris_ketos import PoincareBall; print('OK')"
```

#### B.5.2 Data Acquisition

The analysis uses two data sources:

1. **DSWP coda annotations** (Sharma et al., 2024): 8,719 annotated codas with inter-click intervals, coda type labels, social unit and individual whale identifiers.

```python
import pandas as pd

# Download from the Sharma et al. GitHub repository
url = ("https://raw.githubusercontent.com/pratyushasharma/"
       "sw-combinatoriality/main/data/DominicaCodas.csv")
df = pd.read_csv(url)
print(f"Loaded {len(df)} codas, {df['CodaType'].nunique()} types")
```

2. **DSWP raw audio** (HuggingFace): 1,501 coda recordings with waveforms.

```python
from datasets import load_dataset

ds = load_dataset("orrp/DSWP", split="train", streaming=True)
```

The annotation dataset is approximately 2 MB and downloads in seconds. The audio dataset is larger and is best accessed via HuggingFace streaming mode.

#### B.5.3 Running the Full Analysis

The complete analysis notebook is provided in the repository as `notebooks/cetacean_geometric_analysis.py` in Jupytext percent format. It can be executed as a Jupyter notebook or as a Python script:

```bash
# As a Jupyter notebook
jupytext --to notebook notebooks/cetacean_geometric_analysis.py
jupyter lab notebooks/cetacean_geometric_analysis.ipynb

# As a Python script
python notebooks/cetacean_geometric_analysis.py
```

The notebook produces all figures reported in the paper and in Chapter 7 of this book:

| Figure | Content | Notebook Section |
|---|---|---|
| fig1 | Coda type distribution | Section 1: Data Loading |
| fig2 | Poincare ball vs. Euclidean embeddings | Section 2: Poincare Embedding |
| fig3 | Distortion analysis | Section 2: Poincare Embedding |
| fig4 | Classification comparison | Section 3: HyperbolicMLR |
| fig5 | Persistence diagrams by coda type | Section 4: TDA |
| fig6 | Topological feature summary | Section 4: TDA |
| fig7 | SPD manifold analysis | Section 5: SPD |
| fig8 | DRI results | Section 6: DRI |
| fig9 | Spectral trajectories (raw audio) | Section 7: Raw Audio |
| fig10 | Social unit dialect structure | Section 8: Dialects |
| fig11 | Adversarial boundary discovery | Section 9: Fuzzing |
| fig12 | Linguistic universals | Section 10: Linguistics |

#### B.5.4 Reproducing Specific Results

**Menzerath's law** ($r = -0.269$, $p < 10^{-144}$):

```python
from scipy.stats import spearmanr

ici_cols = [c for c in df.columns if c.startswith("ICI")]
mean_ici = df[ici_cols].mean(axis=1)
r, p = spearmanr(df["nClicks"], mean_ici)
print(f"Menzerath's law: r = {r:.3f}, p = {p:.2e}")
```

**Poincare embedding classification** (74.3% accuracy):

The notebook's Section 3 trains a `HyperbolicMLR` classifier on 11-dimensional features (9 duration-normalised ICIs, log-duration, normalised click count) with taxonomy-initialised prototypes and cosine-annealed Adam optimisation. The exact accuracy depends on the random split seed; the reported result uses `random_state=42` and an 80/20 stratified split. Note that this split does not account for within-individual correlations; leave-one-whale-out cross-validation would yield a more conservative estimate.

**DRI measurement**:

The notebook's Section 6 constructs a nearest-centroid ICI decoder from the DSWP annotations, synthesises test signals, and runs the full DRI measurement with 9 transforms at 3 intensity levels plus 15 compositional chains. Runtime is approximately 2--5 minutes on a modern CPU.

**Boundary asymmetry** (mean = 0.87):

The notebook's Section 9 applies all 9 transforms at 11 intensity levels to synthesised codas from the 8 most frequent types and records all classification boundary crossings. The transition matrix reveals the strong directionality reported in the paper.

#### B.5.5 Expected Runtime

On a standard workstation (no GPU required for any analysis):

| Analysis | Approximate time |
|---|---|
| Data loading and preprocessing | 10 seconds |
| Poincare embedding + classification | 30 seconds |
| TDA (10 coda types, ripser) | 1--2 minutes |
| SPD features (6 types, 50 codas each) | 30 seconds |
| DRI measurement (20 signals, 9 transforms) | 2--5 minutes |
| Full notebook end-to-end | 10--15 minutes |

The TDA computation is the bottleneck and scales with point cloud size. The `max_points` parameter in `compute_persistence` controls this trade-off; 1,000 points is sufficient for the DSWP analysis.

---

### B.6 Data Requirements and Formats

#### B.6.1 DSWP Coda Annotations

The primary data source is the `DominicaCodas.csv` file from the Sharma et al. (2024) repository. Required columns:

| Column | Type | Description |
|---|---|---|
| `CodaType` | string | Coda type label (e.g., `"5R1"`, `"1+1+3"`) |
| `nClicks` | int | Number of clicks in the coda |
| `Duration` | float | Total coda duration in seconds |
| `ICI1` ... `ICI9` | float | Inter-click intervals in seconds (NaN-padded) |
| `Unit` | string | Social unit identifier (optional) |
| `IDN` | string | Individual whale identifier (optional) |

For the exchange-level analyses (Markov structure, turn-taking), the dialogues dataset provides additional columns:

| Column | Type | Description |
|---|---|---|
| `RhythmType` | string | Rhythm class label |
| `WhaleID` | string | Individual whale in the exchange |
| `Timestamp` | float | Time within the recording session |

#### B.6.2 Audio Format

Raw audio for the DRI and SPD trajectory analyses should be:

- **Sample rate**: 32,000 Hz (the DSWP recording rate; can be resampled)
- **Format**: 1D NumPy array of `float32` values
- **Duration**: typically 0.5--3 seconds per coda

The DSWP HuggingFace dataset provides audio in this format. For custom recordings, any format loadable by librosa or soundfile is acceptable:

```python
import librosa
signal, sr = librosa.load("recording.wav", sr=32000)
```

#### B.6.3 Custom Data

The eris-ketos modules are not restricted to sperm whale data. To apply the toolkit to another species or acoustic communication system:

1. **Poincare embedding**: Provide a taxonomic distance matrix (integer-valued, symmetric) and a taxonomy dictionary mapping each type to its hierarchical features. The `build_distance_matrix` function handles arbitrary levels.

2. **TDA**: Provide either raw audio signals (for time-delay embedding) or precomputed feature vectors (for direct point cloud persistence). Any 1D time series or set of feature vectors is valid input.

3. **SPD features**: Provide mel spectrograms as NumPy arrays of shape `[n_mels, n_frames]`. The `n_bands` parameter should be chosen to match the frequency resolution relevant to the species: 16 bands for broadband signals, 8 bands for narrowband.

4. **DRI**: Implement the `CodaDecoder` protocol (a single `classify(signal, sr) -> str` method) for your decoder. The `CodaSemanticDistance` class can be initialised with custom feature weights and decompositions for your type system.

The 156-dimensional geometric feature vector described in Chapter 8 (birdsong) combines 136 SPD features (`n_bands=16`, yielding `16 * 17 / 2 = 136`), 4 spectral trajectory features (geodesic deviation and related statistics), and 16 TDA features (8 per homology dimension). This same decomposition can be applied to any acoustic signal by calling `spd_features_from_spectrogram`, `compute_spectral_trajectory`, and `tda_feature_vector` on the appropriate inputs.

#### B.6.4 Coda Type Naming Convention

The DSWP coda type labels follow a systematic convention:

- **`nR`*v***: Regular rhythm with *n* clicks, variant *v*. Example: `5R1`, `5R3`.
- **`nD`*v***: Decelerating rhythm with *n* clicks, variant *v*. Example: `5D1`, `4D1`.
- **`ni`**: Irregular rhythm with *n* clicks. Example: `4i`, `5i`.
- **`a+b+c`**: Compound rhythm with click groups of sizes *a*, *b*, *c*. Example: `1+1+3`, `2+3`.

The `parse_coda_type` function in the analysis notebook converts these labels to structured dictionaries with `rhythm_class`, `click_count`, and `variant` fields. For the DRI's graduated semantic distance calculation, the four combinatorial features (rhythm, tempo, rubato, ornamentation) identified by Sharma et al. must be provided via the `coda_features` parameter of `CodaSemanticDistance`.

---

### B.7 Relationship to the ErisML Framework

The eris-ketos toolkit adapts two core components from the ErisML geometric ethics framework:

1. **Adversarial fuzzing architecture**: The DRI is a direct adaptation of the Bond Index. The mathematical structure is identical --- graduated semantic distance, adversarial threshold search via binary search, sensitivity profiling, and compositional chain testing --- with domain-specific substitutions (acoustic transforms for scenario transforms, coda semantic distance for option semantic distance). The weighting formula $\text{DRI} = 0.5\bar{\omega} + 0.3\omega_{75} + 0.2\omega_{95}$ is the Bond Index convention, emphasising tail behaviour.

2. **Parametric transform design**: The `AcousticTransform` and `TransformChain` classes mirror ErisML's `ParametricTransform` and `TransformChain`. The identity property (intensity 0.0 = no change) and the invariant/stress classification are inherited from the ethics framework, where they distinguish between perturbations that a well-calibrated evaluator should tolerate and perturbations that may legitimately change the evaluation.

This structural homology is not accidental. It reflects the central claim of this book: the same geometric tools apply across communication domains. The adversarial robustness framework developed for ethical reasoning (do moral judgments change under surface-level reframing?) transfers directly to bioacoustics (do coda classifications change under acoustic perturbation?) because both are instances of the same problem --- testing gauge invariance of a decoder on a communication manifold.

---

### B.8 Version History and Compatibility

The results in this book were produced with eris-ketos v0.2.0. The package requires Python 3.10+ and has been tested on Python 3.10, 3.11, and 3.12.

Core dependencies and their minimum versions:

| Package | Minimum version | Purpose |
|---|---|---|
| numpy | 1.24.0 | Array operations |
| scipy | 1.10.0 | Statistical tests, eigendecomposition |
| torch | 2.0.0 | Poincare ball operations, SPD manifold, HyperbolicMLR |
| librosa | 0.10.0 | Audio loading, mel spectrograms |
| ripser | 0.6.0 | Vietoris-Rips persistence (optional, `[tda]`) |
| persim | 0.3.0 | Persistence diagram utilities (optional, `[tda]`) |
| scikit-learn | 1.3.0 | Euclidean baselines (optional, `[ml]`) |
| datasets | 2.14.0 | HuggingFace data loading (optional, `[data]`) |

The package has no GPU requirement. All computations, including PyTorch operations in the Poincare ball and SPD modules, run on CPU. The full analysis notebook completes in under 15 minutes on a standard workstation. For Kaggle deployment or constrained environments, the `[tda]` extra (ripser) is the only non-trivial dependency; all other modules rely on standard scientific Python packages.

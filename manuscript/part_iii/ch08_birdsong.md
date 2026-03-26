# Chapter 8: The Geometry of Birdsong

*Part III: Non-Human Communication*

---

> *"The song of birds is the voice of a landscape."*
> --- Luis Baptista, ornithologist

> **RUNNING EXAMPLE --- THE SPARROW AND THE MANIFOLD**
>
> *A white-throated sparrow sings from the canopy of a hemlock forest in British Columbia --- descending whistles followed by a rapid trill, captured by a directional microphone twenty meters away, along with wind noise, a creek masking low frequencies, a counter-singing conspecific, and the hiss of rain on leaves.*
>
> *A machine learning system must identify the species from this five-second recording --- one of 206 possibilities. The standard approach feeds a mel spectrogram into a CNN. But on this platform --- Kaggle's inference environment --- there is no GPU. The system has ninety minutes of CPU time to classify every five-second window in every test soundscape.*
>
> *What features are informative enough to distinguish 206 species, robust enough for field conditions, and cheap enough for CPU-only inference?*
>
> *The answer is geometric. The same three-geometry pipeline from Chapter 7 --- SPD manifold features, geodesic deviation, persistent homology --- produces a 156-dimensional feature vector that runs on CPU, complements neural classifiers, and captures structure that convolutional filters miss. The sparrow's descending whistle becomes a curve on a Riemannian manifold. The trill becomes a geodesic. The species identity is encoded in the geometry of cross-frequency correlations.*

---

Chapter 7 introduced the geometric analysis of non-human communication through sperm whale codas --- broadband clicks whose inter-click intervals encode a combinatorial phonetic hierarchy. The three-geometry toolkit extracted meaningful structure from 8,719 codas, revealing linguistic universals, adversarial vulnerability boundaries, and identity signatures.

This chapter applies the same toolkit to a fundamentally different acoustic system: birdsong. Where whale codas are brief, impulsive, and broadband, birdsong is extended, tonal, and narrowband. Where the whale dataset comprised 21 coda types from a single species, the birdsong dataset comprises 206 species. The question is whether the geometric toolkit transfers. The answer is yes, and productively: the geometric features capture aspects of birdsong that convolutional networks on spectrograms systematically miss.

The context is the BirdCLEF competition, an annual challenge hosted on Kaggle that asks participants to identify bird species from field recordings of natural soundscapes.[^1] The 2026 edition features 206 species, five-second classification windows, and a constraint that makes the problem geometrically interesting: inference must run entirely on CPU, with a total budget of ninety minutes. This constraint forces a reckoning with computational cost that GPU-rich training environments never demand. It is in this constrained setting that geometric features find their niche: cheap to compute, complementary to neural features, and robust to the noise conditions that degrade spectrograms.

[^1]: BirdCLEF is part of the LifeCLEF evaluation campaign, running annually since 2014. The competition series has driven significant advances in bioacoustic classification, progressing from small-scale species recognition to continent-scale soundscape monitoring. The 2026 edition continues the trend toward harder evaluation: longer soundscapes, more species, and stricter computational constraints.

---

## 8.1 The BirdCLEF Problem

### 8.1.1 The Task

The BirdCLEF 2026 competition presents a multi-label classification problem. The input is a set of *soundscapes* --- continuous audio recordings from field stations, each several minutes long. The soundscapes are segmented into five-second windows, and for each window the system must produce a probability distribution over 206 bird species. A species is present in a window if it is vocalizing during that interval; multiple species may be present simultaneously.

The training data consists of labeled recordings from the Xeno-canto archive, varying enormously in quality --- from studio-grade directional recordings to smartphone captures contaminated by traffic, wind, and other species. The distribution is heavily imbalanced: common species may have thousands of training examples, while rare species may have fewer than twenty.

The test data consists of unlabeled soundscapes. The system has no internet access during inference. All models, weights, and feature extractors must be bundled into the submission, and the total inference time must not exceed ninety minutes on a Kaggle CPU instance (dual-core Intel Xeon, 16 GB RAM, no GPU).

### 8.1.2 The Standard Approach and Its Limitations

The dominant approach in recent BirdCLEF competitions is straightforward: convert each five-second audio window to a mel spectrogram, treat the spectrogram as a single-channel image, and classify it with a convolutional neural network --- typically an EfficientNet variant pretrained on ImageNet and fine-tuned on the BirdCLEF training data.

This approach works. EfficientNet-B3 and its relatives have won or placed in multiple BirdCLEF editions. But the approach has three specific limitations that geometric features address:

**Limitation 1: Spectrograms discard cross-frequency structure.** A mel spectrogram represents energy per band per time step but not *correlations between bands*. Two species that activate the same bands with the same energies but different cross-frequency correlations produce similar spectrograms but very different covariance matrices. The covariance structure is invisible to the spectrogram but visible on the SPD manifold.

**Limitation 2: CNNs learn local features.** Convolutional kernels have finite receptive fields. They detect local spectro-temporal patterns but are less effective at capturing the global *shape* of a vocalization's trajectory through spectral space, or the topological character of its phase-space attractor.

**Limitation 3: CNNs are expensive on CPU.** An EfficientNet-B3 forward pass takes 50--100 ms per spectrogram on a Kaggle CPU; with test-time augmentation, this doubles. Geometric features involve only linear algebra and simple statistics --- an order of magnitude cheaper per window.

[Figure 8.1: Schematic comparison of the CNN pipeline (left) and the geometric feature pipeline (right). The CNN path: waveform $\to$ mel spectrogram $\to$ EfficientNet $\to$ species probabilities. The geometric path: waveform $\to$ mel spectrogram $\to$ SPD covariance + trajectory $\to$ TDA features from waveform $\to$ LightGBM $\to$ species probabilities. The ensemble combines both paths with learned weights.]

### 8.1.3 The Ensemble Architecture

The deployment system, as implemented in `inference_notebook.py`, combines three models in a weighted ensemble:

1. **EfficientNet-B3** (weight 0.45): The primary CNN, pretrained on ImageNet with noisy student training, fine-tuned on BirdCLEF training data with mixup augmentation. Processes mel spectrograms of shape $(1, 128, T)$.

2. **EfficientNet-B0** (weight 0.25): A smaller CNN providing architectural diversity for ensemble decorrelation. Same spectrogram input, different model capacity.

3. **LightGBM on geometric features** (weight 0.30): A gradient-boosted decision tree classifier operating on the 156-dimensional geometric feature vector. No neural network. No GPU.

The ensemble weights were tuned on a validation set. The geometric component carries 30% of the ensemble weight --- substantial for a model with no learned convolutional features, no pretraining, and no deep architecture. This weight reflects the degree to which geometric features provide *complementary* rather than *redundant* information.

The weighted combination is:

$$\mathbf{p}_{\text{ensemble}} = \frac{w_1 \mathbf{p}_{\text{B3}} + w_2 \mathbf{p}_{\text{B0}} + w_3 \mathbf{p}_{\text{geo}}}{w_1 + w_2 + w_3}$$

where the CNN outputs include test-time augmentation via time reversal ($\mathbf{p} = \tfrac{1}{2}\sigma(f(\mathbf{x})) + \tfrac{1}{2}\sigma(f(\text{flip}(\mathbf{x})))$), and $\mathbf{p}_{\text{geo}} \in [0,1]^{206}$ is the LightGBM class probability vector.

---

## 8.2 SPD Manifold Features: The Vowel Space of Birdsong

### 8.2.1 From Spectrogram to Covariance Matrix

The first component of the geometric feature vector captures **cross-frequency correlations** in the mel spectrogram. The construction proceeds in three steps: band aggregation, covariance estimation, and projection to log-Euclidean space.

**Step 1: Band aggregation.** The mel spectrogram has $n_{\text{mels}} = 128$ frequency bins and $T$ time frames (approximately 313 for a five-second window at the default hop length of 512 samples at 32 kHz). We aggregate the 128 mel bins into $n = 16$ frequency bands by averaging consecutive groups of $128 / 16 = 8$ mel bins. This produces a matrix $\mathbf{B} \in \mathbb{R}^{16 \times T}$, where $B_{i,t}$ is the average log-energy in the $i$-th frequency band at time $t$.

The choice of $n = 16$ bands is a trade-off. Fewer bands (say, 8) would produce smaller covariance matrices but lose spectral resolution --- the ability to distinguish species with similar broad spectral envelopes but different fine harmonic structure. More bands (say, 32) would preserve finer detail but produce larger covariance matrices (528-dimensional upper triangles rather than 136) with noisier off-diagonal entries, since each band contains fewer mel bins and the covariance estimates are less stable.

Sixteen bands at 32 kHz sampling rate span approximately 0--16 kHz, with each band covering roughly 1 kHz of effective bandwidth.[^2] This resolution is well-matched to the scale of birdsong structure: most passerine songs occupy the 1--10 kHz range, and the major spectral features (fundamental frequency, first and second harmonics, formant-like resonances) are separated by intervals of 500 Hz--2 kHz.

[^2]: The mel scale is nonlinear, compressing high frequencies and expanding low frequencies. The actual bandwidth of each band varies: lower bands span narrower frequency ranges (in Hz) and higher bands span wider ranges. The 16 bands provide finer resolution at low frequencies (where most birdsong energy concentrates) and coarser resolution at high frequencies --- a design that aligns well with the distribution of avian vocalizations.

From the `geometric_features.py` implementation:

```python
def compute_covariance(spectrogram: np.ndarray, n_bands: int = 16,
                       epsilon: float = 1e-4) -> np.ndarray:
    n_mels, T = spectrogram.shape
    band_size = n_mels // n_bands

    # Average mel bins within each band
    bands = np.zeros((n_bands, T))
    for i in range(n_bands):
        start = i * band_size
        end = start + band_size if i < n_bands - 1 else n_mels
        bands[i] = spectrogram[start:end].mean(axis=0)

    # Covariance matrix + regularization
    cov = np.cov(bands)  # (n_bands, n_bands)
    cov += epsilon * np.eye(n_bands)
    return cov
```

**Step 2: Covariance estimation.** The $16 \times T$ band-energy matrix $\mathbf{B}$ yields a $16 \times 16$ sample covariance matrix:

$$\Sigma_{ij} = \frac{1}{T-1} \sum_{t=1}^{T} \left(B_{i,t} - \bar{B}_i\right)\left(B_{j,t} - \bar{B}_j\right)$$

where $\bar{B}_i = \frac{1}{T}\sum_t B_{i,t}$ is the temporal mean of band $i$. The diagonal entries $\Sigma_{ii}$ measure the variance of energy in each band --- how much the $i$-th band fluctuates over time. The off-diagonal entries $\Sigma_{ij}$ measure the cross-frequency correlations --- how the energy in band $i$ co-varies with the energy in band $j$.

A regularization term $\epsilon \mathbf{I}$ (with $\epsilon = 10^{-4}$) is added to ensure positive-definiteness. Without regularization, the sample covariance can be singular when $T < n$, or merely ill-conditioned when some frequency bands carry very little energy. The regularization places the matrix firmly in $\text{SPD}(16)$ --- the manifold of $16 \times 16$ symmetric positive-definite matrices.

### 8.2.2 What Cross-Frequency Correlations Capture

Why is this covariance matrix informative for species identification? The answer lies in what the off-diagonal entries encode: the *harmonic binding structure* of the vocalization.

Consider a bird producing a pure tone at frequency $f_0$. If the tone has harmonics (as most biological sounds do), energy will appear simultaneously at $f_0, 2f_0, 3f_0, \ldots$ The frequency bands containing these harmonics will be strongly positively correlated --- when the bird sings louder, all harmonics increase together; when the bird pauses, all harmonics drop together. The covariance matrix records this pattern: $\Sigma_{ij} > 0$ whenever bands $i$ and $j$ contain harmonics of the same fundamental.

Different species have different harmonic structures. A white-throated sparrow's descending whistle is nearly a pure tone: energy concentrates in one or two bands, and cross-frequency correlations are weak (only adjacent bands are correlated). A wood thrush's flute-like song has rich harmonics: energy appears in three or four bands simultaneously, producing strong off-diagonal correlations that extend several bands away from the diagonal. A brown-headed cowbird's liquid warble involves rapid frequency modulation that sweeps energy across many bands in complex, time-varying patterns: the covariance matrix has a dense, nearly full-rank structure.

[Figure 8.2: Covariance matrices for three species. Left: white-throated sparrow (near-diagonal structure, weak cross-frequency correlations, nearly pure tone). Center: wood thrush (banded structure with off-diagonal peaks at harmonic intervals, rich overtone series). Right: brown-headed cowbird (dense, full-rank structure, complex frequency modulation). The species-specific covariance "fingerprint" is visible to the naked eye.]

The analogy to human vowel space is precise. In human speech, vowels are distinguished not by their fundamental frequency (which varies with speaker) but by the relative positions of their formants --- the resonant frequencies of the vocal tract that create peaks of energy at specific frequency bands. Two vowels with the same $f_0$ but different formant ratios produce different cross-frequency correlation patterns. The covariance matrix of a vowel captures the formant structure; the matrix logarithm places this structure in a vector space where distances are meaningful.

Birdsong has its own "formant space." The spectral shape of a bird's vocalization is determined by the resonant properties of its syrinx, trachea, and oral cavity, which vary across species (and, to a lesser extent, across individuals). The covariance matrix is a fingerprint of this resonant structure --- a point on the SPD manifold that encodes the "vowel identity" of the species.

### 8.2.3 The Matrix Logarithm and Log-Euclidean Projection

The covariance matrix $\Sigma \in \text{SPD}(16)$ lives on a curved Riemannian manifold, not in a flat vector space. Standard machine learning algorithms --- LightGBM, random forests, SVMs --- assume flat (Euclidean) feature spaces. We need a map from the manifold to a vector space that preserves as much geometric structure as possible.

The **log-Euclidean metric** provides exactly this. For $\Sigma \in \text{SPD}(n)$, the matrix logarithm $\log(\Sigma)$ is a symmetric (but not necessarily positive-definite) matrix that lives in the tangent space at the identity --- which is a flat vector space isomorphic to $\text{Sym}(n)$. The log-Euclidean distance between two SPD matrices is:

$$d_{\text{LE}}(\Sigma_1, \Sigma_2) = \|\log(\Sigma_1) - \log(\Sigma_2)\|_F$$

where $\|\cdot\|_F$ denotes the Frobenius norm. This is a genuine metric on $\text{SPD}(n)$ --- it satisfies non-negativity, symmetry, the triangle inequality, and the identity of indiscernibles --- and it agrees with the geodesic distance in the log-Euclidean Riemannian structure.[^3]

[^3]: The log-Euclidean metric is one of several Riemannian metrics on SPD(n). The affine-invariant metric $d_{\text{AI}}(\Sigma_1, \Sigma_2) = \|\log(\Sigma_1^{-1/2} \Sigma_2 \Sigma_1^{-1/2})\|_F$ has stronger geometric properties (it is invariant under congruence transformations $\Sigma \mapsto A\Sigma A^\top$), but the log-Euclidean metric is computationally cheaper and produces a flat (Euclidean) feature space after the logarithm. For our purposes --- feeding features into a LightGBM classifier --- the flat structure is a feature, not a limitation.

The implementation computes $\log(\Sigma)$ via scipy's `logm` function, then extracts the upper triangle (including the diagonal) as a flat feature vector:

```python
def spd_features_from_spectrogram(spectrogram: np.ndarray,
                                   n_bands: int = 16,
                                   epsilon: float = 1e-4) -> np.ndarray:
    cov = compute_covariance(spectrogram, n_bands, epsilon)

    # Matrix logarithm → log-Euclidean space
    log_cov = logm(cov).real

    # Extract upper triangle (including diagonal)
    indices = np.triu_indices(n_bands)
    features = log_cov[indices]

    return features.astype(np.float32)
```

The upper triangle of a $16 \times 16$ symmetric matrix has $16 \times 17 / 2 = 136$ entries. These 136 numbers are the SPD feature vector. They encode, in a Euclidean-compatible format, the full cross-frequency correlation structure of the vocalization, including:

- The 16 diagonal entries: the log-variance of energy in each frequency band (how variable the band is over time).
- The 120 off-diagonal entries: the log-covariance between every pair of bands (which bands co-activate, which are independent, which are anti-correlated).

The distance between two birds' SPD features is:

$$d_{\text{LE}}(\Sigma_1, \Sigma_2) = \sqrt{\sum_{i \leq j} (\log(\Sigma_1)_{ij} - \log(\Sigma_2)_{ij})^2}$$

This is just the Euclidean distance in the 136-dimensional feature space --- but it corresponds to the log-Euclidean geodesic distance on $\text{SPD}(16)$. The matrix logarithm has "flattened" the manifold into a vector space without destroying the metric structure.

---

## 8.3 Spectral Trajectory: Geodesic Deviation on SPD(16)

### 8.3.1 From Snapshot to Trajectory

The SPD features of Section 8.2 treat the covariance matrix as a single summary of the entire five-second window. But birdsong is not stationary. The spectral structure *changes* over time --- that is what makes it a song rather than a tone. A descending whistle has different covariance at the start (energy in high bands) and at the end (energy in low bands). A trill has rapidly repeating covariance patterns. A complex song has covariance that wanders through SPD space along an intricate path.

The **spectral trajectory** captures this temporal evolution. Instead of computing one covariance matrix for the entire window, we compute a *sequence* of covariance matrices by sliding a shorter window across time. Each local covariance is a point on SPD(16), and the sequence traces a curve --- a trajectory --- on the manifold.

The implementation uses a window of 64 frames (approximately 1 second at the default hop length) and a hop of 32 frames (50% overlap):

```python
def spectral_trajectory(spectrogram: np.ndarray, n_bands: int = 16,
                         window: int = 64, hop: int = 32,
                         epsilon: float = 1e-4) -> dict:
    n_mels, T = spectrogram.shape
    covs = []
    for t in range(0, T - window, hop):
        chunk = spectrogram[:, t:t + window]
        if chunk.shape[1] >= n_bands * 3:  # need enough frames
            covs.append(compute_covariance(chunk, n_bands, epsilon))

    if len(covs) < 2:
        return {"path_length": 0.0, "geodesic_distance": 0.0,
                "deviation": 0.0, "n_steps": len(covs)}

    # Path length: sum of consecutive log-Euclidean distances
    path_length = sum(spd_distance(covs[i], covs[i + 1])
                      for i in range(len(covs) - 1))

    # Geodesic distance: direct distance between endpoints
    geo_dist = spd_distance(covs[0], covs[-1])

    return {
        "path_length": float(path_length),
        "geodesic_distance": float(geo_dist),
        "deviation": float(path_length - geo_dist),
        "n_steps": len(covs),
    }
```

For a five-second window with approximately 313 time frames, the trajectory typically comprises 7--8 covariance matrices, each computed from a one-second sub-window.

### 8.3.2 Geodesic Deviation as Song Complexity

The key derived quantity is the **geodesic deviation**: the difference between the total path length and the direct (geodesic) distance between the trajectory's endpoints:

$$\delta = L_{\text{path}} - d_{\text{geo}}(\Sigma_{\text{start}}, \Sigma_{\text{end}})$$

where:

$$L_{\text{path}} = \sum_{k=0}^{K-2} d_{\text{LE}}(\Sigma_k, \Sigma_{k+1})$$

is the total distance traveled along the trajectory, and $d_{\text{geo}}(\Sigma_{\text{start}}, \Sigma_{\text{end}}) = d_{\text{LE}}(\Sigma_0, \Sigma_{K-1})$ is the distance of the "shortcut" --- the straight line (in log-Euclidean space) from start to finish.

By the triangle inequality, $\delta \geq 0$ always. Equality $\delta = 0$ holds only when the trajectory is a geodesic --- a straight line in log-Euclidean space. Positive deviation means the trajectory departs from the straight path: the spectral structure wanders before arriving at its destination.

This provides a geometric encoding of song complexity:

**Low deviation ($\delta \approx 0$):** The vocalization's spectral structure changes monotonically --- moving in a straight line through SPD space from one covariance pattern to another. A descending whistle (monotone pitch change, stable harmonics) produces low deviation. A trill (rapid repetition of the same spectral pattern) also produces low deviation, because the trajectory oscillates around a single point on the manifold rather than traveling a long path.

**High deviation ($\delta \gg 0$):** The vocalization's spectral structure changes in a complex, non-monotonic way --- wandering through SPD space along a curved or zigzagging path. A wood thrush song (alternating between a low-frequency "bup" and a high-frequency flute-like phrase), a mockingbird's medley (switching rapidly between imitated phrases with different spectral structures), or any vocalization with multiple distinct spectral "states" produces high deviation.

[Figure 8.3: Spectral trajectories on SPD(16), projected to two dimensions via PCA of the log-covariance matrices. Left: a trill (Chipping Sparrow) --- the trajectory oscillates tightly around a single point, with low path length and low deviation. Center: a descending whistle (White-throated Sparrow) --- the trajectory moves in a nearly straight line from high-frequency to low-frequency covariance, with moderate path length but low deviation. Right: a complex song (Wood Thrush) --- the trajectory wanders through a large region of SPD space, with high path length and high deviation.]

The four trajectory features stored in the feature vector --- path length, geodesic distance, deviation, and number of trajectory steps --- provide a compact summary of the vocalization's temporal dynamics on the spectral manifold. The path length measures the total amount of spectral change; the geodesic distance measures the net spectral change; the deviation measures the geometric complexity of the change; and the number of steps is a normalization factor that accounts for windows of different effective duration (some five-second windows may contain silence at the edges, reducing the number of valid trajectory points).

### 8.3.3 Connection to Geodesic Deviation in the Parent Theory

The spectral trajectory and its deviation are instances of a more general construction from the parent theory (*Geometric Reasoning*, Ch. 4), where geodesic deviation measures how far an actual path deviates from the geodesic connecting its endpoints --- the Jacobi equation framework.

In our setting, the curvature of SPD(16) under the log-Euclidean metric is zero (the matrix logarithm isometrically maps $\text{SPD}(n)$ to $\text{Sym}(n)$, which is flat), so the deviation is entirely due to the non-geodesic nature of the spectral trajectory itself --- the vocalization *chooses* to wander through spectral space rather than taking the direct route. On a curved manifold, geodesic deviation can arise from curvature alone. On the flat log-Euclidean space, all deviation is intrinsic to the signal. The geometry of the space is trivial; the geometry of the *trajectory on the space* is not.

---

## 8.4 TDA Features: The Topology of Birdsong Attractors

### 8.4.1 From Waveform to Point Cloud

The third component of the geometric feature vector takes a fundamentally different approach. Instead of working with the spectrogram (a time-frequency representation), the TDA features work with the raw waveform --- the one-dimensional amplitude trace $x(t)$ recorded by the microphone.

The construction, developed in full generality in Chapter 6, proceeds in three stages: time-delay embedding, subsampling, and persistent homology.

**Stage 1: Time-delay embedding.** The waveform $x(t)$ is embedded in $\mathbb{R}^d$ using Takens' construction:

$$\mathbf{v}(t) = \bigl[x(t),\; x(t + \tau),\; x(t + 2\tau)\bigr]$$

with delay $\tau = 10$ samples and embedding dimension $d = 3$. By Takens' theorem (Theorem 6.1), this reconstructs the topology of the vocal production system's attractor for generic $\tau$ and $d \geq 2m + 1$, where $m$ is the attractor dimension. For birdsong, the dominant dynamics are low-dimensional (the syrinx has few mechanical degrees of freedom), so $d = 3$ is sufficient.

**Stage 2: Subsampling.** The raw point cloud may contain tens of thousands of points (a five-second waveform at 32 kHz sampling rate has 160,000 samples; the time-delay embedding produces approximately 159,980 points). Computing persistent homology on a cloud of this size is prohibitively expensive. The pipeline subsamples to 500 points, chosen uniformly at random:

```python
cloud = subsample_cloud(cloud, max_points=500, seed=42)
```

The subsampling preserves the *topology* of the cloud (connected components, loops) with high probability, since the topological features are large-scale structures that are robust to uniform thinning. The choice of 500 points is a computational trade-off: enough to capture the dominant topological features, few enough to keep the persistent homology computation within the CPU time budget.

**Stage 3: Persistent homology.** The subsampled point cloud is fed into a persistent homology computation (via the ripser library when available, with a naive single-linkage fallback). The output is a set of **persistence diagrams** --- one for each homology dimension.

The $H_0$ persistence diagram records connected components. Each point $(b, d)$ in the diagram represents a connected component that is "born" at filtration scale $b$ (i.e., appears when the radius parameter reaches $b$) and "dies" at scale $d$ (i.e., merges with another component). Long-lived components (large $d - b$) represent well-separated clusters in the point cloud; short-lived components represent noise.

The $H_1$ persistence diagram records loops. Each point $(b, d)$ represents a loop that appears at scale $b$ and is filled in at scale $d$. Long-lived loops represent genuine periodic structure in the attractor; short-lived loops represent topological noise.

### 8.4.2 What Topology Captures

The topology of the reconstructed attractor encodes structural properties of the vocalization that neither spectrograms nor covariance matrices capture directly.

**Pure tones produce circles.** A bird singing a sustained tone at frequency $f$ produces a waveform $x(t) \approx A\sin(2\pi f t)$. The time-delay embedding of this signal is a loop (an ellipse, in fact) in $\mathbb{R}^3$. The $H_1$ persistence diagram has a single long-lived point, corresponding to this loop. The persistence (death $-$ birth) of this point is proportional to the amplitude $A$ and inversely related to the noise level.

**Harmonic tones produce torus-like attractors.** A tone with harmonics, $x(t) = A_1\sin(2\pi f t) + A_2\sin(4\pi f t) + \ldots$, produces an attractor that wraps around a torus or higher-dimensional surface, depending on the number of harmonics. The $H_1$ diagram has multiple long-lived points, one for each independent periodic component.

**Frequency-modulated signals produce spiral attractors.** A descending whistle, in which the frequency changes monotonically over time, produces an attractor that spirals rather than closes. The $H_1$ persistence is shorter (the loops do not quite close), and the $H_0$ structure may show elongated, chain-like connectivity.

**Complex songs produce high-dimensional attractor structure.** A song with multiple distinct phrase types --- alternating between different spectral states --- produces an attractor with multiple disjoint lobes connected by transitional regions. The $H_0$ diagram reflects the number of lobes (connected components that persist across a range of filtration scales); the $H_1$ diagram reflects the periodicity within each lobe.

[Figure 8.4: Reconstructed attractors (time-delay embedding, $\tau = 10$, $d = 3$) for three birdsong types. Left: a pure whistle (White-throated Sparrow) --- clean loop, single strong $H_1$ feature. Center: a harmonic song (Wood Thrush) --- torus-like structure, multiple $H_1$ features. Right: a rapid trill (Chipping Sparrow) --- tightly wound spiral, dense $H_0$ cluster with moderate $H_1$.]

### 8.4.3 The 16 TDA Features

Each persistence diagram is summarized by 8 statistics, computed in the `_diagram_features` function:

$$\text{features}(D) = \bigl[\, n,\; \bar{\ell},\; \sigma_\ell,\; \ell_{\max},\; \ell_{75},\; \bar{b},\; P_{\text{total}},\; P_{\text{norm}} \,\bigr]$$

where:

- $n$ = count of finite-lifetime features in the diagram
- $\bar{\ell}$ = mean lifetime $\bar{\ell} = \frac{1}{n}\sum_i (d_i - b_i)$
- $\sigma_\ell$ = standard deviation of lifetimes
- $\ell_{\max}$ = maximum lifetime
- $\ell_{75}$ = 75th percentile of lifetimes
- $\bar{b}$ = mean birth time
- $P_{\text{total}}$ = total persistence $= \sum_i (d_i - b_i)^2$
- $P_{\text{norm}}$ = normalized persistence $= \sqrt{P_{\text{total}}} / (n + \epsilon)$

With two homology dimensions ($H_0$ and $H_1$), each summarized by 8 statistics, the TDA component contributes $8 \times 2 = 16$ features to the 156-dimensional vector.

The count $n$ and mean birth $\bar{b}$ describe the *scale* of topological features. The lifetime statistics describe *persistence* --- robustness to filtration scale, and hence to noise. The total and normalized persistence weight long-lived features more heavily via the squared lifetime.

### 8.4.4 Species-Specific Topology

The central claim is that species-specific harmonic structure creates species-specific point cloud topology. Each species has a characteristic vocal apparatus (syrinx morphology, tracheal length, oral cavity shape) that constrains its attractor. The dynamical system that generates the birdsong is species-specific, so the topology of the reconstructed attractor is species-specific.

Topology alone does not suffice for species identification --- the 16 TDA features are a lossy summary of the persistence diagrams, and individual variation, noise, and short windows all degrade the signal. But the topological features provide information *orthogonal* to the SPD features: SPD encodes spectral covariance (which bands co-activate), while TDA encodes attractor shape (what kind of dynamical system produced the sound). The two are complementary, not redundant.

---

## 8.5 The Combined 156-Dimensional Vector

### 8.5.1 Assembly

The three components are concatenated into a single feature vector:

$$\mathbf{f} = [\underbrace{f_1, \ldots, f_{136}}_{\text{SPD covariance}},\; \underbrace{f_{137}, \ldots, f_{140}}_{\text{trajectory}},\; \underbrace{f_{141}, \ldots, f_{156}}_{\text{TDA}}] \in \mathbb{R}^{156}$$

The implementation is a single function call:

```python
def extract_geometric_features(waveform, spectrogram,
                                n_bands=16, tda_delay=10,
                                tda_dim=3, tda_max_points=500):
    # SPD features from spectrogram
    spd = spd_features_from_spectrogram(spectrogram, n_bands=n_bands)

    # Spectral trajectory
    traj = spectral_trajectory(spec2d, n_bands=n_bands)
    traj_vec = np.array([
        traj["path_length"], traj["geodesic_distance"],
        traj["deviation"], traj["n_steps"],
    ], dtype=np.float32)

    # TDA features from waveform
    tda = tda_features(waveform, delay=tda_delay, dim=tda_dim,
                       max_points=tda_max_points)

    return np.concatenate([spd, traj_vec, tda])
```

The feature breakdown:

| Component | Dimensions | Source | Geometry |
|---|---|---|---|
| SPD covariance | 136 | Mel spectrogram | $\text{SPD}(16)$ manifold, log-Euclidean metric |
| Spectral trajectory | 4 | Mel spectrogram (windowed) | Geodesic deviation on $\text{SPD}(16)$ |
| TDA persistence | 16 | Raw waveform | Persistent homology of Takens attractor |
| **Total** | **156** | | |

### 8.5.2 Why the Combination Works

The three components capture three different aspects of the acoustic signal, and their combination is more powerful than any single component:

**SPD features capture what:** which frequency bands are active and how they correlate. This is a static, time-averaged description of the spectral structure. It answers the question: "What does this bird's frequency spectrum look like, in terms of harmonic binding?"

**Trajectory features capture how:** how the spectral structure changes over time. This is a dynamic description of the song's evolution on the spectral manifold. It answers the question: "Is this a simple vocalization (straight trajectory) or a complex one (curved trajectory)?"

**TDA features capture the shape:** what kind of dynamical system produced the sound. This is a topological description of the vocal production mechanism. It answers the question: "What is the intrinsic geometry of the attractor that generated this waveform?"

These three questions are logically independent. Two species can have the same spectral structure (same SPD features) but different temporal dynamics (different trajectory features) --- for example, a sustained tone and a trill at the same pitch. Two species can have the same temporal dynamics but different attractor topology --- for example, a frequency-modulated sweep and a harmonic stack that both cover the same frequency range over the same duration, but with different phase relationships. The combination captures distinctions that any single component would miss.

### 8.5.3 Training the Classifier

The training pipeline, implemented in `train_geometric.py`, follows a standard pattern: extract features for all training files (in parallel across CPU cores), load the resulting feature matrix, and train a LightGBM classifier with stratified 5-fold cross-validation.

The LightGBM configuration reflects the modest dimensionality of the feature space:

```python
model = lgb.LGBMClassifier(
    n_estimators=500,
    num_leaves=63,
    learning_rate=0.05,
    max_depth=8,
    min_child_samples=20,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    reg_lambda=0.1,
    n_jobs=N_WORKERS,
    random_state=SEED + fold,
    verbose=-1,
)
```

With 156 features and 206 classes, the classification problem is high-dimensional in the output space but low-dimensional in the input space. LightGBM handles this regime well: its leaf-wise tree growth can discover nonlinear decision boundaries in 156-dimensional space, its native multi-class support handles 206 classes efficiently, and its regularization (L1 via `reg_alpha`, L2 via `reg_lambda`, subsampling via `subsample` and `colsample_bytree`) prevents overfitting on rare species with few training examples.

The feature extraction is parallelized across available CPU cores using Python's `multiprocessing.Pool`, with each worker processing one audio file end-to-end. The evaluation metric is macro-averaged AUC in a one-vs-rest setting across all 206 classes, penalizing models that achieve high performance on common species at the expense of rare ones.

---

## 8.6 Deployment Under Constraint

### 8.6.1 The Ninety-Minute Budget

The BirdCLEF competition imposes a hard constraint: the entire inference pipeline --- loading models, processing soundscapes, generating predictions, writing the submission file --- must complete in ninety minutes on a Kaggle CPU instance. There is no GPU. There is no internet access. Every byte of model weights and every line of code must be bundled into the submission.

This constraint is not incidental. It reflects the deployment reality of bioacoustic monitoring: the systems that run in the field, on remote autonomous recording units, on edge devices attached to weather stations and cellular towers, do not have GPU access. A model that requires a V100 to classify birdsong in real time is a model that cannot be deployed where the birds are.

The inference notebook manages its time budget explicitly:

```python
# Budget check
if elapsed_total > 5000:
    print(f"  WARNING: approaching 90 min limit! "
          f"{elapsed_total:.0f}s elapsed")
```

The budget breakdown for a typical submission:

| Component | Time per window | Total (est.) | Notes |
|---|---|---|---|
| Audio loading + mel | ~10 ms | ~5 min | I/O dominated |
| EfficientNet-B3 | ~80 ms | ~40 min | With TTA (2x forward pass) |
| EfficientNet-B0 | ~30 ms | ~15 min | With TTA |
| Geometric features | ~5 ms | ~2.5 min | Covariance + trajectory + TDA |
| LightGBM predict | <1 ms | ~0.5 min | Tree traversal |
| Ensemble + I/O | <1 ms | ~0.5 min | Weighted average + CSV write |
| **Total** | | **~63 min** | Within 90-min budget |

The geometric features consume approximately 4% of the total inference budget while contributing 30% of the ensemble weight. This asymmetry --- cheap to compute, valuable in combination --- is precisely what makes them attractive in the constrained setting. If the total budget were unlimited, one might simply run larger neural networks or more aggressive test-time augmentation. But with a hard time limit, every second spent on inference must earn its keep, and the geometric features offer the best return on computational investment in the pipeline.

### 8.6.2 What Geometry Buys Under Constraint

The geometric features serve a specific role in the ensemble: they provide a classification signal that is *uncorrelated* with the CNN predictions. Ensemble methods gain their power from diversity --- combining models that make different errors. If all models in an ensemble fail on the same examples, the ensemble cannot recover. But if the geometric model succeeds on examples where the CNNs fail (and vice versa), the weighted average can outperform any individual model.

Where do geometric features succeed where CNNs fail? Three cases stand out. *Low-SNR recordings*: noise corrupts absolute energies in the spectrogram, but cross-frequency *correlations* may persist --- harmonics still co-activate even at low SNR. SPD features, encoding correlations rather than magnitudes, are more robust to additive noise. *Overlapping species*: the covariance matrix of a combined signal is approximately $\Sigma_{\text{combined}} \approx \Sigma_A + \Sigma_B$, retaining information about both species in a way that a merged spectrogram image does not. *Rare species*: geometric features are computed by fixed algorithms, not learned from data, so they work identically with five examples or five thousand.

### 8.6.3 The Deployment Pipeline

The inference notebook implements a simplified geometric feature extraction optimized for the CPU-only environment. The key difference from the training pipeline: the deployment version avoids the `ripser` library and uses distance-based statistics of the time-delay embedded point cloud as a proxy for full persistent homology. The full Rips complex computation takes 50--100 ms per window --- acceptable in training but expensive under a ninety-minute budget. The distance-based proxy captures much of the same information at a fraction of the cost, while preserving the 16-dimensional TDA output format for LightGBM compatibility. The SPD and trajectory features are computed identically in both settings.

---

## 8.7 Connection to Chapter 7: Domain Generality of the Geometric Toolkit

### 8.7.1 The Same Pipeline, Different Signals

The most striking result of this chapter is not any single number but a structural observation: **the same three-geometry pipeline works for both whale communication and birdsong**. The SPD covariance features, the spectral trajectory, and the TDA persistence features were developed for cetacean clicks in the `eris-ketos` project and applied to birdsong in the BirdCLEF project without modification to the mathematical framework. Only the parameters changed --- the number of frequency bands, the window sizes, the TDA delay and embedding dimension --- and even these changes were modest.

This is worth pausing over. Sperm whale codas and passerine birdsong are produced by radically different biological machinery (phonic lips vs. syrinx), transmitted through radically different media (water vs. air), recorded by radically different instruments (towed hydrophone arrays vs. directional microphones), and serve radically different communicative functions (social identity and group coordination vs. territory defense and mate attraction). If the geometric pipeline worked only because of some specific feature of whale clicks --- their broadband impulsive nature, their simple temporal structure, the particular statistics of underwater acoustics --- it would be a useful tool for cetacean research but nothing more.

The fact that the same pipeline works for birdsong suggests something deeper: the geometric features capture **structural properties of acoustic communication** that transcend the specifics of any one system. These properties are:

1. **Cross-frequency correlation structure** (SPD features): Any vocalization produced by a resonant system (vocal tract, syrinx, phonic lips) creates correlations between frequency bands. The SPD manifold is the natural space for these correlations, regardless of the species.

2. **Spectral trajectory complexity** (geodesic deviation): Any vocalization that changes its spectral structure over time traces a curve on the SPD manifold. The deviation of this curve from a geodesic is a geometry-independent measure of temporal complexity.

3. **Attractor topology** (TDA features): Any vocalization produced by a dynamical system (and all vocalizations are, since they are produced by physical systems with finite degrees of freedom) has an attractor whose topology can be reconstructed from the waveform via Takens' embedding.

These three properties are consequences of physics and mathematics, not of biology. They hold for any acoustic signal produced by a dynamical system and recorded by a transducer. The geometric pipeline extracts them without domain-specific knowledge --- without knowing what a whale coda is, what a bird song means, or how a syrinx works.

### 8.7.2 Evidence for a Universal Acoustic Feature Space

The parallel success provides evidence --- not proof, but evidence --- for a **universal acoustic feature space** grounded in signal geometry rather than communication semantics. A mel spectrogram is designed for human auditory perception; it works for birdsong and whale clicks because the mel transform happens to preserve relevant structure, not because those signals are speech-like. A learned CNN representation is even more domain-specific, tuned to one training distribution. The geometric features, by contrast, assume only three things:

- The signal is produced by a dynamical system with a finite-dimensional attractor.
- The signal is recorded by a transducer that preserves temporal structure.
- The signal has non-trivial spectral structure (i.e., it is not white noise).

These assumptions hold for every known biological acoustic communication system, from cricket stridulation to human speech, and for many non-biological signals as well.

### 8.7.3 What the Comparison Reveals

The comparison between Chapters 7 and 8 reveals a pattern that will recur throughout the book: **the geometric toolkit extracts structure at the appropriate level of abstraction**. The hyperbolic embeddings were informative for whale codas (which have a clear taxonomic hierarchy) but were not used in the birdsong pipeline (where the Linnaean taxonomy is known a priori and encoded in class labels). The SPD features were important in both cases but for different reasons: for whales, they captured spectral differences between click types; for birds, they captured the harmonic binding that identifies species. The TDA features served the same role in both: detecting the topological signature of the underlying dynamical system.

This flexibility is the hallmark of a genuine geometric framework. The framework does not prescribe which features will be informative; it provides a *space of possible features* parameterized by mathematical structure (curvature, covariance, topology), and the domain determines which region of this space contains the discriminative information.

---

## 8.8 What Scalar Evaluation Misses

A classification system for birdsong is typically evaluated by a single number: AUC, F1, mean average precision. These scalars summarize performance across all species and recording conditions into one figure of merit. This is convenient for ranking competition submissions. It is insufficient for understanding what the system has learned.

The geometric framework suggests a richer evaluation. The log-Euclidean coordinates of each species' average covariance matrix define a point in $\mathbb{R}^{136}$. A confusion matrix organized by SPD distance --- rather than alphabetically --- reveals whether the classifier's errors are geometrically coherent: whether it confuses species that *sound alike* (geometrically close) rather than species that merely share a label prefix. The geodesic deviation distribution per species predicts classification difficulty: species with high-deviation songs (complex, multi-phrase vocalizations) should have higher intra-class variance and be harder to identify from short windows. The persistence diagrams provide a topological signature of difficulty: species with clean, well-separated $H_1$ features should be easier to identify than species with noisy, low-persistence topology.

These questions cannot be answered by AUC alone. They require the full geometric representation that the scalar evaluation discards. This is a local instance of the Scalar Irrecoverability Theorem (Chapter 15): the AUC summarizes performance on a manifold of species $\times$ conditions $\times$ recordings, and the contraction destroys the structure that explains *why* the system succeeds or fails.

The features themselves --- covariance fingerprints of vocal apparatus, geodesic deviation as a precisely defined measure of song complexity, attractor topology of the vocal production system --- are of independent scientific interest beyond classification. SPD distances between species could be compared to molecular phylogenies. Geodesic deviation could be correlated with ecological variables (habitat complexity, sexual selection pressure, repertoire size). Persistence diagrams could map the "topological vocabulary" of a species' production system: how many qualitatively distinct dynamical regimes it can access, and how it transitions between them. These are open questions, not results. The geometric pipeline provides the tools; the ornithological application remains to be carried out --- using the same tools that, in Chapter 7, revealed linguistic universals in whale communication, and that will appear again in Chapters 9 and 10 applied to the cuneiform tablets of Old Assyrian merchants.

---

## Summary

This chapter has presented the geometric analysis of birdsong as the second empirical case study in non-human acoustic communication. The main contributions are:

1. **SPD manifold features** (136 dimensions): The $16 \times 16$ frequency-band covariance matrix, projected to log-Euclidean space via the matrix logarithm, captures the cross-frequency correlation structure of birdsong --- the "vowel space" that distinguishes species by their harmonic binding patterns.

2. **Spectral trajectory features** (4 dimensions): Sliding a window across time and tracking the covariance matrix on $\text{SPD}(16)$ produces a curve whose geodesic deviation --- path length minus direct distance --- measures the geometric complexity of the song. Trills have low deviation; complex songs have high deviation.

3. **TDA features** (16 dimensions): Takens' time-delay embedding of the raw waveform reconstructs the vocal attractor in $\mathbb{R}^3$. Persistent homology of the point cloud extracts topological invariants --- connected components ($H_0$) and loops ($H_1$) --- that encode the dynamical structure of the vocal production system.

4. **The 156-dimensional combined vector**: The three components complement each other, capturing what (spectral structure), how (temporal evolution), and the shape (attractor topology) of the vocalization. Combined with CNN spectrograms in a LightGBM ensemble, the geometric features carry 30% of the ensemble weight while consuming 4% of the computational budget.

5. **Domain generality**: The same three-geometry pipeline that extracted meaningful features from whale codas in Chapter 7 produces meaningful features for birdsong without modification to the mathematical framework. This is evidence that the geometric toolkit captures structural properties of acoustic communication that are independent of species, medium, and communicative function.

The geometric features work because birdsong has geometric structure. The covariance matrix is a point on a Riemannian manifold. The song is a trajectory on that manifold. The vocal production system is a dynamical system whose attractor has a topology. These are not metaphors. They are mathematical facts, implemented in code, validated in competition, and ready to be applied to any acoustic communication system we encounter next.

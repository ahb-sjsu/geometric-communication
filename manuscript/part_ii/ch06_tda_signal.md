# Chapter 6: Topological Data Analysis of Signal

> *"The purpose of computing is insight, not numbers."*
> --- Richard Hamming, *Numerical Methods for Scientists and Engineers* (1962)

> **RUNNING EXAMPLE --- THE WHALE AND THE WREN**
>
> *Consider two acoustic signals, each recorded in the field under adverse conditions.*
>
> *Signal A: a sperm whale coda --- five broadband clicks separated by inter-click intervals of roughly 0.35, 0.35, 0.22, and 0.22 seconds. The recording is saturated with shipping noise, reverberant multipath echoes, and the clicks of at least three other whales at varying distances. The hydrophone is a towed array moving at six knots; the whale is diving at depth. Amplitude is meaningless. Absolute timing is approximate.*
>
> *Signal B: a Pacific wren's song --- a cascade of rapid notes spanning 4--8 kHz, recorded from a distance of 30 meters with wind buffeting the microphone, a nearby stream masking frequencies below 1 kHz, and a second wren counter-singing in partial temporal overlap. The gain was set for a closer bird and has clipped the loudest notes.*
>
> *In both cases, the standard approach --- compute a spectrogram, extract Mel-frequency features, train a neural classifier --- works, but poorly. The noise, the gain mismatch, the reverb, the overlapping conspecifics all corrupt the representation. What we need are features that do not care about amplitude, that tolerate noise, that are robust to recording distance. We need features that capture the shape of the signal --- its topology --- rather than its magnitude.*
>
> *This chapter develops those features.*

---

In Chapter 4, we introduced the three-geometry toolkit for communication: hyperbolic embeddings for hierarchy, SPD manifold features for spectral covariance, and persistent homology for shape. Chapter 5 developed the first of these --- the Poincare ball model applied to the hierarchical structure of communication systems, from coda taxonomies to cuneiform sign hierarchies. This chapter develops the third: topological data analysis (TDA) of communication signals.

The central idea is deceptively simple. A one-dimensional signal --- a time series of inter-click intervals, a waveform amplitude trace, an energy contour from a spectrogram --- is the observable output of a higher-dimensional dynamical system. The whale's vocal production apparatus has internal state: muscle tensions, air pressure in the phonic lips, neural firing patterns. The bird's syrinx has its own state space. The signal we record is a one-dimensional projection of this multi-dimensional dynamics. Takens' embedding theorem tells us that, under generic conditions, we can reconstruct the *topology* of the original dynamical system from this one-dimensional projection, by the simple device of stacking time-delayed copies of the signal into vectors.

Once we have reconstructed a point cloud in a higher-dimensional space, persistent homology extracts its topological features --- connected components, loops, voids --- in a way that is provably stable under small perturbations. These features are invariant to amplitude scaling, robust to additive noise, and insensitive to recording distance. They capture the *shape* of the vocal attractor, not its magnitude. For field recordings of non-human communication, this is not a theoretical nicety. It is a practical necessity.

The code is real, the data is real, and the results are reproducible.

---

## 6.1 From Signal to Point Cloud: Takens' Embedding Theorem

### 6.1.1 The Problem of Dimensional Poverty

Every recording device produces a one-dimensional signal: a scalar value that varies over time. This is a lossy projection. The dynamical system that produced the signal --- a whale's vocal apparatus, a bird's syrinx, a human larynx --- operates in a state space of many dimensions, and the recording collapses all of that structure onto a single axis.

Takens' embedding theorem tells us that we can undo this collapse --- at least topologically. Under generic conditions, the topology of the original dynamical system can be recovered from a single time series by constructing vectors from time-delayed copies of the observed signal. The reconstruction is not exact in a metric sense --- distances in the embedding space do not generally match distances in the original state space --- but it is exact in a topological sense. The embedding preserves the qualitative shape: connected components, loops, voids, and all higher-order topological features.

### 6.1.2 The Construction

Let $x(t)$ be a scalar-valued time series --- for concreteness, the amplitude of a whale click recording sampled at discrete times $t = 0, 1, 2, \ldots, N-1$. Choose two parameters:

- $\tau$ --- the **time delay**, measured in samples, and
- $d$ --- the **embedding dimension**, a positive integer.

Construct the **time-delay embedding** by forming the $d$-dimensional vectors

$$\mathbf{v}(t) = \bigl[x(t),\; x(t + \tau),\; x(t + 2\tau),\; \ldots,\; x(t + (d-1)\tau)\bigr]$$

for $t = 0, 1, \ldots, N - (d-1)\tau - 1$. This produces a set of $n = N - (d-1)\tau$ points in $\mathbb{R}^d$ --- a **point cloud** that lives in the reconstructed phase space.

[Figure 6.1: Schematic of the time-delay embedding. Left: a 1D signal $x(t)$ with marked sample points at times $t$, $t + \tau$, and $t + 2\tau$. Right: the corresponding 3D point $\mathbf{v}(t) = [x(t), x(t+\tau), x(t+2\tau)]$ in the reconstructed phase space. Multiple time steps trace out a curve (the reconstructed attractor).]

The implementation is direct. From the `geometric_features.py` pipeline:

```python
def time_delay_embedding(signal: np.ndarray, delay: int = 10,
                          dim: int = 3) -> np.ndarray:
    """Takens' time-delay embedding: reconstruct attractor from 1D series.

    Given a signal x(t), constructs vectors:
        v(t) = [x(t), x(t+τ), x(t+2τ), ..., x(t+(d-1)τ)]

    By Takens' theorem, for generic τ and d ≥ 2m+1 (m = attractor
    dimension), this reconstructs the topology of the original
    dynamical system.
    """
    n = len(signal) - (dim - 1) * delay
    if n <= 0:
        return np.zeros((1, dim))
    embedded = np.empty((n, dim))
    for d in range(dim):
        embedded[:, d] = signal[d * delay: d * delay + n]
    return embedded
```

The code is deliberately minimal. No windowing, no smoothing, no normalization at the embedding stage. The theorem works on the raw signal; preprocessing is a choice, not a requirement.

### 6.1.3 Takens' Theorem: The Formal Statement

The result that justifies this construction is due to Floris Takens (1981), with important refinements by Sauer, Yorke, and Casdagli (1991).

**Theorem 6.1** (Takens' Embedding Theorem). *Let $\mathcal{M}$ be a compact manifold of dimension $m$, and let $\Phi: \mathcal{M} \to \mathcal{M}$ be a smooth diffeomorphism (the dynamics). Let $h: \mathcal{M} \to \mathbb{R}$ be a smooth observation function. For generic[^1] $(\Phi, h)$, the delay map*

$$F_{\Phi, h}: \mathcal{M} \to \mathbb{R}^{2m+1}$$

*defined by $F_{\Phi, h}(\mathbf{x}) = \bigl(h(\mathbf{x}),\; h(\Phi(\mathbf{x})),\; \ldots,\; h(\Phi^{2m}(\mathbf{x}))\bigr)$ is an embedding --- that is, an injective immersion.*

[^1]: "Generic" here means "for all $(\Phi, h)$ except a set of measure zero in the appropriate function space." This is an open and dense condition, which means that almost every choice of dynamics and observation function works. It does not mean *every* choice works --- pathological cases exist, but they require precise tuning and do not arise in practice.

The theorem has three critical implications for our purposes:

1. **Topological faithfulness.** Because $F_{\Phi,h}$ is an embedding (not merely a continuous map), it preserves the topology of $\mathcal{M}$. Connected components, loops, and voids in the original state space appear as connected components, loops, and voids in the reconstructed point cloud. This is why persistent homology on the embedded point cloud recovers genuine dynamical structure.

2. **The dimension bound $d \geq 2m + 1$.** The embedding dimension must be at least $2m + 1$, where $m$ is the dimension of the attractor. For a periodic orbit ($m = 1$), $d = 3$ suffices. For a strange attractor on a surface ($m = 2$), $d = 5$ suffices. In practice, the attractor dimension is rarely known *a priori*, but low-dimensional embeddings ($d = 3$ or $d = 5$) work well for acoustic signals because the dominant dynamics are low-dimensional --- the vocal production apparatus has far fewer degrees of freedom than the sampling rate would suggest.

3. **Genericity of $\tau$.** The theorem holds for *generic* delay $\tau$ --- almost every value works. But "almost every" is a topological statement, not a practical one. Some values of $\tau$ work much better than others in finite, noisy data. If $\tau$ is too small, consecutive coordinates are nearly identical and the point cloud collapses to the diagonal. If $\tau$ is too large, consecutive coordinates are nearly independent and the embedding captures noise rather than dynamics. The choice of $\tau$ matters in practice, even though it does not matter in principle.

### 6.1.4 Choosing $\tau$ and $d$ in Practice

Two parameters must be set: the delay $\tau$ and the embedding dimension $d$. The theoretical guarantee requires only $d \geq 2m + 1$ and generic $\tau$, but finite noisy data demands more care.

**Delay $\tau$.** The standard heuristic for $\tau$ is the **first minimum of the mutual information** between $x(t)$ and $x(t + \tau)$ (Fraser and Swinney, 1986). At this delay, consecutive coordinates are maximally informative about each other in a nonlinear sense --- they are neither redundant (too small $\tau$) nor independent (too large $\tau$). An alternative is the **first zero-crossing of the autocorrelation function**, which is faster to compute but assumes linear dependence.

For the BirdCLEF pipeline, we use $\tau = 10$ samples, which corresponds to roughly 0.5 ms at a typical audio sample rate of 22,050 Hz. For sperm whale codas, the relevant signal is the inter-click interval sequence (not the raw audio), and the appropriate delay depends on the number of clicks per coda. The eris-ketos pipeline operates on ICI vectors directly, constructing point clouds in $\mathbb{R}^9$ from zero-padded ICI sequences --- effectively using the raw ICI vector as the embedding, which is equivalent to a Takens embedding with $\tau = 1$ on the ICI time series.[^2]

[^2]: This is a common pattern when the signal is already a summary sequence (like ICIs) rather than a raw waveform. The "time delay" is then one step along the sequence, and the "embedding dimension" is the length of the ICI vector. Takens' theorem still applies: the ICI sequence is an observation function on the dynamical system (the whale's vocal production), and the delay map reconstructs the attractor topology.

**Dimension $d$.** The standard method for choosing $d$ is the **false nearest neighbors** algorithm (Kennel, Brown, and Abarbanel, 1992). The idea: in too low a dimension, points that are far apart in the true state space are forced close together by the projection (false neighbors). As $d$ increases, false neighbors are eliminated. The embedding dimension is the smallest $d$ at which the fraction of false neighbors drops to zero (or below a threshold).

In practice, for acoustic signals, $d = 3$ is often sufficient. The vocal attractors of interest are typically one- or two-dimensional (periodic orbits for sustained tones, limit cycles for trills, low-dimensional chaos for complex calls), and $d = 3$ satisfies the $2m + 1$ bound for $m = 1$. The BirdCLEF and eris-ketos pipelines both default to $d = 3$, with the eris-ketos whale analysis using the full ICI vector dimension ($d = 9$) as an upper bound.

[Figure 6.2: Effect of delay and dimension on the reconstructed point cloud. A synthetic periodic signal $x(t) = \sin(2\pi t / T)$ embedded with (a) $\tau$ too small: the cloud collapses to the diagonal; (b) $\tau$ optimal: the cloud forms a clean ellipse; (c) $\tau$ too large: the cloud fills a rectangle. Below: (d) $d = 2$: a circle (correct topology); (e) $d = 3$: a torus knot (correct topology, higher resolution); (f) $d = 10$: same topology, unnecessary dimensions.]

---

## 6.2 Persistent Homology: Extracting Topology from Point Clouds

### 6.2.1 The Challenge of Noisy Point Clouds

The time-delay embedding produces a point cloud --- a finite set of points in $\mathbb{R}^d$. The cloud is not a manifold; it is a discrete approximation to a manifold, corrupted by noise and finite sampling. We need a method that extracts topological features from finite, noisy point data.

This is the domain of **persistent homology**, the central construction of topological data analysis. The key insight is to analyze the point cloud not at a single scale, but across *all* scales simultaneously, and to identify topological features that *persist* across a range of scales as the genuine structure of the underlying space. Short-lived features are noise; long-lived features are signal.

### 6.2.2 The Vietoris--Rips Complex

The first step is to build a combinatorial object --- a simplicial complex --- from the point cloud. The standard construction for TDA is the **Vietoris--Rips complex**.

**Definition 6.2** (Vietoris--Rips Complex). *Let $X = \{x_1, \ldots, x_n\} \subset \mathbb{R}^d$ be a finite point cloud and let $\varepsilon \geq 0$ be a scale parameter. The Vietoris--Rips complex $\mathrm{VR}(X, \varepsilon)$ is the abstract simplicial complex whose $k$-simplices are subsets $\{x_{i_0}, x_{i_1}, \ldots, x_{i_k}\} \subseteq X$ such that*

$$d(x_{i_j}, x_{i_l}) \leq \varepsilon \quad \text{for all } 0 \leq j, l \leq k.$$

In words: a set of points forms a simplex if and only if *every pair* of points in the set is within distance $\varepsilon$ of each other. At $\varepsilon = 0$, the complex consists of isolated vertices (each point is its own 0-simplex). As $\varepsilon$ increases, edges appear between nearby points (1-simplices), then triangles fill in between triples of mutually close points (2-simplices), and so on.

The Rips complex is a computationally tractable proxy for the Cech complex (which uses balls of radius $\varepsilon/2$ and takes $k$-simplices when $k+1$ balls have a common intersection). The Rips complex requires only pairwise distance comparisons, while the Cech complex requires $k$-fold intersection tests. For TDA applications, the Rips complex is standard.[^3]

[^3]: The Rips and Cech complexes are not identical, but they are interleaved: $\mathrm{Cech}(X, \varepsilon) \subseteq \mathrm{VR}(X, \varepsilon) \subseteq \mathrm{Cech}(X, \sqrt{2}\,\varepsilon)$ in Euclidean space. This means the persistence diagrams from the two complexes are at most a factor of $\sqrt{2}$ apart in the bottleneck distance, which is negligible for our purposes.

### 6.2.3 Filtration and Persistence

The key idea of persistent homology is to study the Rips complex not at a single $\varepsilon$, but across the entire filtration --- the nested family of complexes obtained by increasing $\varepsilon$ from 0 to $\infty$:

$$\mathrm{VR}(X, 0) \subseteq \mathrm{VR}(X, \varepsilon_1) \subseteq \mathrm{VR}(X, \varepsilon_2) \subseteq \cdots$$

As $\varepsilon$ increases, topological features appear (**birth**) and disappear (**death**). A connected component is born when a vertex is added and dies when an edge merges it with another component. A loop (1-cycle) is born when a cycle of edges forms and dies when a 2-simplex fills it in. Each feature has a birth time $b$ and a death time $d$, and its **lifetime** (or **persistence**) is $\ell = d - b$.

**Definition 6.3** (Persistence Diagram). *The persistence diagram $\mathrm{Dgm}_k(X)$ for homology dimension $k$ is the multiset of birth-death pairs $\{(b_i, d_i)\}$ for all $H_k$ features in the filtration, together with the diagonal $\{(x, x) : x \in \mathbb{R}\}$ counted with infinite multiplicity.*

Each persistence diagram is a scatter plot in the upper half of the plane (since $d > b$ for every genuine feature). Points far from the diagonal have high persistence --- they represent robust topological features that persist over a wide range of scales. Points near the diagonal are short-lived and typically represent noise.

[Figure 6.3: The Vietoris--Rips filtration. Top row: a point cloud at four increasing values of $\varepsilon$, with the Rips complex drawn. Bottom row: the corresponding persistence diagram, accumulating birth-death pairs as $\varepsilon$ increases. A long-lived $H_1$ loop (the central ring) appears far from the diagonal; short-lived components near the diagonal are noise.]

### 6.2.4 Homology Dimensions and Their Interpretation

For communication signals, two homology dimensions carry the primary information:

**$H_0$: Connected components.** The zeroth homology group counts the connected components of the simplicial complex. In the filtration, every point is born as its own component at $\varepsilon = 0$, and components merge as $\varepsilon$ increases. The persistence diagram for $H_0$ records the death times of the components that merge --- the longer a component survives before merging, the more isolated it was from the rest of the cloud.

For acoustic signals, $H_0$ persistence reflects the **cluster structure** of the reconstructed attractor. A signal with distinct harmonic components (e.g., a chord with well-separated frequencies) produces a point cloud with well-separated clusters, yielding high $H_0$ persistence. A signal with a single dominant frequency produces a single tight cluster with low $H_0$ persistence.

**$H_1$: Loops.** The first homology group counts the independent loops (1-cycles) in the complex. In the filtration, a loop is born when a cycle of edges forms and dies when a 2-simplex fills it in. Persistent $H_1$ features indicate robust cyclic structure in the point cloud.

For acoustic signals, $H_1$ persistence reflects **periodic structure** in the reconstructed attractor. A purely periodic signal (a sine wave) produces a point cloud that is a closed loop in the embedding space --- a single persistent $H_1$ feature. A signal with multiple periodicities produces multiple loops. An aperiodic signal produces no persistent loops. This is the topological encoding of periodicity: loops in the point cloud correspond to recurrent patterns in the signal.

Higher homology dimensions ($H_2$: voids, $H_3$: cavities, etc.) capture progressively more complex topological structure. For the acoustic signals considered here, $H_0$ and $H_1$ suffice --- the vocal attractors are low-dimensional, and higher homology is typically empty or dominated by noise. The eris-ketos and BirdCLEF pipelines both compute homology up to dimension 1.

### 6.2.5 The Stability Theorem

The most important theoretical property of persistent homology for applications is **stability**: small perturbations of the input produce small perturbations of the output.

**Theorem 6.4** (Stability of Persistence Diagrams; Cohen-Steiner, Edelsbrunner, and Harer, 2007). *Let $f, g: X \to \mathbb{R}$ be two functions on a topological space $X$, and let $\mathrm{Dgm}(f)$ and $\mathrm{Dgm}(g)$ be their persistence diagrams. Then*

$$d_B\bigl(\mathrm{Dgm}(f),\, \mathrm{Dgm}(g)\bigr) \leq \|f - g\|_\infty$$

*where $d_B$ is the bottleneck distance between persistence diagrams.*

The bottleneck distance measures the worst-case displacement of any single point in the diagram. The theorem says: if two functions differ by at most $\delta$ in the supremum norm, their persistence diagrams differ by at most $\delta$ in the bottleneck distance. Birth-death pairs can shift by at most $\delta$; features with persistence less than $\delta$ can appear or disappear; but features with persistence much greater than $\delta$ are guaranteed to survive.

For our purposes, this means: additive noise of magnitude $\delta$ can shift birth-death pairs by at most $\delta$ but cannot destroy topological features with persistence much greater than $\delta$. The long-lived features in the persistence diagram --- the ones far from the diagonal --- are the stable ones. The short-lived features near the diagonal are the ones that noise can create or destroy. This is why persistence provides a natural signal/noise separation: the diagonal is the noise floor, and distance from the diagonal is the signal-to-noise ratio.[^4]

[^4]: The stability theorem has been strengthened in several directions. Chazal, de Silva, Glisse, and Oudot (2016) proved stability for the Wasserstein distance (which averages over all points in the diagram, rather than taking the worst case). Lesnick (2015) extended stability to multi-parameter persistence. For our single-parameter Rips filtrations, the original bottleneck stability is sufficient.

---

## 6.3 Feature Extraction from Persistence Diagrams

### 6.3.1 The Vectorization Problem

Persistence diagrams are multisets of points in the plane. Machine learning algorithms require fixed-length vectors. The **vectorization problem** is: how do we extract a fixed-length feature vector from a persistence diagram that preserves the information we care about?

There are several approaches in the literature --- persistence landscapes (Bubenik, 2015), persistence images (Adams et al., 2017), kernel methods (Reininghaus et al., 2015) --- each with different theoretical guarantees. For the BirdCLEF and eris-ketos pipelines, we use a simpler approach: **summary statistics** of the birth-death pairs. This sacrifices some information (the spatial arrangement of points in the diagram is lost) but produces a compact, interpretable feature vector that is fast to compute and works well in practice.

### 6.3.2 The Eight Summary Statistics

For each homology dimension $k$, the pipeline extracts eight summary statistics from the persistence diagram $\mathrm{Dgm}_k(X)$. Let $\{(b_i, d_i)\}_{i=1}^n$ be the finite birth-death pairs (excluding infinite-persistence features), and let $\ell_i = d_i - b_i$ be the lifetime of the $i$-th feature.

The eight statistics are:

1. **Count** ($n$): The number of finite-lifetime features in dimension $k$. This measures the topological complexity at the given scale --- how many independent components ($k=0$) or loops ($k=1$) were detected.

2. **Mean lifetime** ($\bar{\ell} = \frac{1}{n}\sum_{i} \ell_i$): The average persistence of features. High mean lifetime indicates that topological features are robust; low mean lifetime indicates that they are ephemeral and likely noise.

3. **Standard deviation of lifetime** ($\sigma_\ell$): The dispersion of persistence values. High standard deviation indicates a mixture of persistent and ephemeral features --- some genuine structure and some noise. Low standard deviation indicates homogeneous features (either all robust or all noisy).

4. **Maximum lifetime** ($\max_i \ell_i$): The persistence of the single most prominent feature. This is the most stable statistic under noise (by the stability theorem, the longest-lived feature is the last to be destroyed by perturbation).

5. **75th percentile of lifetime** ($\ell_{75}$): A robust alternative to the maximum, less sensitive to outliers. Captures the persistence of the "typical prominent feature."

6. **Mean birth time** ($\bar{b} = \frac{1}{n}\sum_i b_i$): The average scale at which features appear. For $H_0$, all features are born at $\varepsilon = 0$ (every point is its own component at zero scale), so the mean birth is identically zero --- but for $H_1$, the mean birth time indicates the scale at which cyclic structure begins to appear. Early birth means cycles at small scales (fine-grained periodicity); late birth means cycles at large scales (coarse periodicity).

7. **Total persistence** ($L^2 = \sum_i \ell_i^2$): The sum of squared lifetimes. This is the $L^2$ norm of the persistence, which weights long-lived features more heavily than short-lived ones. It provides a single scalar measure of the total topological complexity, with the quadratic weighting serving as a natural importance filter.

8. **Normalized persistence** ($\hat{L} = \sqrt{L^2} / (n + \epsilon)$): The root-mean-square lifetime, or equivalently the $L^2$ norm divided by the count. This compensates for the number of features: a diagram with one very persistent loop has higher normalized persistence than a diagram with many short-lived loops, even if their total persistence is similar.

The implementation from `geometric_features.py`:

```python
def _diagram_features(dgm: np.ndarray) -> np.ndarray:
    """Extract 8 summary statistics from a persistence diagram."""
    if len(dgm) == 0:
        return np.zeros(8, dtype=np.float32)

    finite_mask = np.isfinite(dgm[:, 1])
    finite = dgm[finite_mask]

    if len(finite) == 0:
        return np.zeros(8, dtype=np.float32)

    lifetimes = finite[:, 1] - finite[:, 0]
    n = len(lifetimes)
    total = float(np.sum(lifetimes ** 2))

    return np.array([
        n,
        lifetimes.mean(),
        lifetimes.std() if n > 1 else 0.0,
        lifetimes.max(),
        np.percentile(lifetimes, 75),
        finite[:, 0].mean(),
        total,
        np.sqrt(total) / (n + 1e-10),
    ], dtype=np.float32)
```

Computing these eight statistics for each of $H_0$ and $H_1$ produces a **16-dimensional TDA feature vector** --- the topological component of the full 156-dimensional geometric feature vector (136 SPD + 4 trajectory + 16 TDA) used in the BirdCLEF pipeline.

### 6.3.3 Why These Eight?

The choice is motivated by the stability theorem and the practical requirements of acoustic classification. The **count** captures complexity. The **lifetime statistics** (mean, std, max, p75) capture the persistence distribution --- by the stability theorem, only features with lifetime greater than the noise magnitude are reliable, and the maximum lifetime is the most noise-robust single number. The **mean birth time** captures scale: for $H_1$ features, it indicates the characteristic scale of periodic structure. The **total and normalized persistence** provide aggregate measures that weight long-lived features more heavily; the normalization by count distinguishes "one strong feature" (clean periodic signal) from "many weak features" (broadband noise).

These eight statistics are not the only possible summary --- persistence landscapes and persistence images retain more spatial information about the diagram. But for the 206-species birdsong and 21-type whale coda classification problems, the summary statistics capture sufficient structure. The tradeoff --- information loss in exchange for interpretability, speed, and a compact 16-dimensional representation --- is favorable.

[Figure 6.4: The eight summary statistics, illustrated on two persistence diagrams. Left: a diagram with few, persistent $H_1$ features (a clean periodic signal). Right: a diagram with many, short-lived $H_1$ features (a noisy aperiodic signal). The statistics distinguish the two: the left diagram has low count, high max lifetime, high normalized persistence; the right has high count, low max lifetime, low normalized persistence.]

---

## 6.4 Empirical Case: Whale Click Patterns

### 6.4.1 Codas and Inter-Click Intervals

Sperm whale codas are stereotyped sequences of 3--12 broadband clicks, with inter-click intervals (ICIs) ranging from roughly 0.1 to 0.8 seconds. The ICI pattern defines the coda type: regular codas have approximately equal intervals, accelerating codas have decreasing intervals, compound codas have distinct groups of clicks with different internal timing (Sharma et al., 2024). The Dominica Sperm Whale Project (DSWP) dataset contains 8,719 annotated codas spanning 28 coda types.

For each coda, the relevant signal is the ICI vector --- a sequence of $k-1$ intervals for a $k$-click coda. This is already a one-dimensional time series (interval as a function of position within the coda), and it can be analyzed directly as a point cloud or embedded via the Takens delay map.

### 6.4.2 Point Cloud Construction

The eris-ketos pipeline constructs ICI point clouds in $\mathbb{R}^9$. For each coda type with at least 40 samples, the ICI vectors of all codas of that type are collected. Shorter vectors are zero-padded to a common dimensionality of 9 (accommodating codas with up to 10 clicks). Each ICI vector becomes a point in $\mathbb{R}^9$; the collection of all codas of a given type forms the point cloud for that type.[^5]

[^5]: Strictly, this is not a Takens embedding of a single time series but rather a collection of ICI vectors --- each coda contributes one point, and the point cloud represents the *distribution* of timing patterns within a coda type. The topological analysis then characterizes the shape of this distribution. This is complementary to the Takens approach (which would embed a single long ICI sequence and characterize the dynamics of production) and is the natural construction when each coda is a short, discrete event.

Point clouds exceeding 300 points are randomly subsampled (seed = 42) for computational tractability. This subsampling is justified by the stability of persistent homology: removing a finite number of points can only remove topological features or shorten their lifetimes by an amount bounded by the minimum distance to the removed points. For uniformly sampled clouds, the effect is negligible.

### 6.4.3 Topological Signatures by Rhythm Class

Vietoris--Rips persistent homology computed to dimension 1 using Ripser (Bauer, 2021; Tralie et al., 2018) reveals systematic topological differences across rhythm classes:

**Regular codas (xR).** Codas with approximately equal inter-click intervals --- the most common type in many social units --- produce tight, roughly spherical point clouds in ICI space. The ICI vectors cluster tightly because the timing is consistent both within and across productions. The persistence diagrams show:

- **Low $H_0$ persistence**: components merge quickly, indicating a single tight cluster with no well-separated sub-groups.
- **Low $H_1$ persistence**: no persistent loops, indicating no cyclic structure in the timing distribution.

This is the topological signature of temporal regularity: a point mass in ICI space, or more precisely, a noisy ball centered on the prototypical ICI vector. The topology is trivial --- one connected component, no loops, no voids --- and this triviality is itself informative.

**Irregular codas (xi).** Codas with variable inter-click intervals produce more dispersed point clouds. The timing variability means that ICI vectors spread across a larger region of $\mathbb{R}^9$, and the resulting cloud has non-trivial topology:

- **Moderate $H_0$ persistence**: some sub-clusters persist before merging, indicating that the timing variability has structure (not just uniform noise).
- **Higher $H_1$ persistence**: persistent loops appear, indicating cyclic patterns in the timing distribution. This is consistent with a production mechanism that cycles through a repertoire of timing variants.

**Compound codas (x+y).** Codas with distinct groups of clicks (e.g., three fast clicks followed by two slow clicks) produce point clouds with **elevated $H_0$ persistence** --- the two click groups correspond to two sub-clusters in ICI space that merge only at large scale. This is the most intuitively clear topological signature: the internal structure of the coda (two distinct groups) manifests directly as two components in the point cloud.

[Figure 6.5: Persistence diagrams for three coda types, reproduced from the eris-ketos analysis (Bond, 2026). Left: regular coda (5R) --- tight cluster, low persistence. Center: irregular coda (5i) --- dispersed cloud, elevated $H_1$. Right: compound coda (3+1+1) --- multi-component structure, elevated $H_0$. $H_0$ features in blue, $H_1$ features in orange. Points far from the diagonal indicate persistent topological features.]

[Figure 6.6: Topological feature summary across coda types. Left: $H_1$ loop count versus maximum $H_1$ lifetime for each coda type, colored by rhythm class. Right: total $H_1$ persistence ranked by coda type. Irregular and compound types show systematically higher topological complexity.]

### 6.4.4 Topological Content vs. Metric Identity

A striking feature of the cetacean analysis (detailed in Chapter 7) is the clean separation between **topological content** and **metric identity**. The topology of the ICI point cloud encodes *coda type*: different rhythm classes have different topological signatures, invariant to the precise inter-click intervals. But individual whales produce the same coda type with statistically distinguishable ICI patterns (Kolmogorov--Smirnov $p < 0.001$ for all tested pairs). Identity is encoded in the *metric* --- the precise distances between points --- not the topology.

This is a geometric decomposition of communicative content: topology carries the message (what coda type), and the metric carries the identity (who is producing it). The decomposition is natural --- topology is invariant under continuous deformation; metric is the structure that deformation can change --- and it may reflect a genuine functional property of the communication system.

---

## 6.5 Empirical Case: Birdsong Spectral Topology

### 6.5.1 From Waveform to Topological Features

The BirdCLEF geometric feature pipeline applies the same TDA machinery to birdsong, but starting from a different signal: the raw audio waveform rather than a sequence of inter-click intervals.

The full pipeline, from the `tda_features` function in `geometric_features.py`:

```python
def tda_features(signal: np.ndarray, delay: int = 10, dim: int = 3,
                  max_points: int = 1000, max_homology_dim: int = 1,
                  thresh: float = 2.0, seed: int = 42) -> np.ndarray:
    """Extract topological features from an audio signal.

    Full pipeline: signal → Takens embedding → subsample →
    persistent homology → feature vector.
    """
    # Normalize signal
    signal = signal.astype(np.float64)
    signal = (signal - signal.mean()) / (signal.std() + 1e-10)

    # Time-delay embedding
    cloud = time_delay_embedding(signal, delay=delay, dim=dim)

    # Subsample for tractability
    cloud = subsample_cloud(cloud, max_points=max_points, seed=seed)

    # Normalize point cloud
    cloud = (cloud - cloud.mean(axis=0)) / (cloud.std(axis=0) + 1e-10)

    # Persistent homology
    diagrams = _persistence_diagrams_ripser(cloud, max_dim=max_homology_dim,
                                             thresh=thresh)

    # Extract features per homology dimension
    features = []
    for d in range(max_homology_dim + 1):
        if d < len(diagrams):
            features.append(_diagram_features(diagrams[d]))
        else:
            features.append(np.zeros(8, dtype=np.float32))

    return np.concatenate(features)
```

The pipeline operates in five stages:

1. **Normalization.** The signal is zero-centered and scaled to unit variance. This removes absolute amplitude information, which is desirable: we want features that are invariant to recording gain and distance. The normalization also ensures that the Rips complex threshold ($\varepsilon = 2.0$) is calibrated to the signal's intrinsic scale.

2. **Time-delay embedding.** The normalized 1D signal is embedded in $\mathbb{R}^3$ with delay $\tau = 10$ samples. For birdsong recorded at 22,050 Hz, this corresponds to a delay of approximately 0.45 ms --- well within the timescale of individual harmonic cycles for birdsong in the 2--8 kHz range (where one cycle takes 0.125--0.5 ms).

3. **Subsampling.** The point cloud is subsampled to at most 1,000 points (or 500 in the combined feature pipeline). Ripser's computational complexity is approximately $O(n^3)$ in the number of points, and subsampling to 1,000 points keeps the TDA computation under a fraction of a second per recording --- critical for the BirdCLEF submission constraint of 90 minutes for the full test set on CPU.

4. **Cloud normalization.** The point cloud is re-centered and rescaled per coordinate. This is a second normalization, applied in the embedding space rather than the signal space, and it ensures that the Rips filtration explores the relevant scale range regardless of the signal's absolute characteristics.

5. **Persistent homology.** The Vietoris--Rips complex is computed to dimension 1 with a filtration threshold of $\varepsilon_{\max} = 2.0$. Features beyond this threshold are unlikely to represent genuine structure (they would correspond to topological features at scales larger than two standard deviations in the normalized cloud).

### 6.5.2 Species-Specific Topology

Different bird species produce vocalizations with different dynamical structure, and this structure manifests as different point cloud topology. Four broad categories illustrate the pattern:

- **Sustained tonal songs** (thrushes, warblers): the time-delay embedding of a frequency-modulated tone produces a loop or torus knot. TDA features: high $H_1$ maximum lifetime, low $H_0$ persistence.
- **Trills** (wrens, chipping sparrows): rapid repetitions create thickened loops from multiple attractor traversals. TDA features: high $H_1$ count, moderate maximum lifetime.
- **Complex broadband songs** (mockingbirds, starlings): variable, aperiodic vocalizations fill the embedding space without loop structure. TDA features: low $H_1$ persistence, high $H_0$ persistence from syllable-type sub-clusters.
- **Click-based calls** (woodpeckers, corvids): discrete impulses create separated clusters, qualitatively similar to the whale coda analysis. TDA features: high $H_0$ persistence, low $H_1$ persistence.

[Figure 6.7: Point clouds and persistence diagrams for four vocalization types. (a) Sustained tone (Swainson's thrush): clean elliptical loop, single persistent $H_1$ feature. (b) Trill (Pacific wren): thickened loop, multiple $H_1$ features. (c) Complex song (Northern mockingbird): filled region, low $H_1$ persistence. (d) Click train (Downy woodpecker): separated clusters, high $H_0$ persistence.]

### 6.5.3 Complementarity with SPD Features

The 16 TDA features capture structure that the 136 SPD features cannot, and vice versa. SPD features encode **spectral covariance** --- which frequencies co-occur. TDA features encode **temporal topology** --- the qualitative dynamics of the signal (periodic, quasiperiodic, chaotic, impulsive). Two species can have nearly identical spectral envelopes but different temporal structure (one sustains a tone, the other trills); TDA distinguishes them. Conversely, two species can have different spectral content but similar dynamics; SPD distinguishes them. The spectral trajectory features (4 dims) bridge the two, tracking how covariance evolves on the SPD manifold. The three components provide complementary geometric views, and the combined pipeline extracts richer structure than any single view.

[Figure 6.8: Feature importance for species classification (LightGBM on 156-dimensional geometric features). The top 20 features include contributions from all three components. No single component dominates.]

---

## 6.6 Robustness: Why Topology Succeeds Where Amplitude Fails

### 6.6.1 The Field Recording Problem

Bioacoustic field recordings are hostile to standard feature extraction. Amplitude varies with distance. Background noise varies unpredictably. Reverberation distorts temporal structure. Equipment introduces frequency-dependent gain. Two recordings of the same vocalization, made 10 meters apart with different equipment, can differ dramatically in amplitude, noise floor, and spectral coloration. Standard spectral features --- MFCCs, spectrograms, fundamental frequency --- are sensitive to all of these distortions, and these sensitivities are the dominant sources of error in deployed bioacoustic classifiers.

### 6.6.2 Topological Invariance Properties

Topological features have three specific invariance properties that make them robust to field recording conditions:

**Invariance to amplitude scaling.** Let $x(t)$ be a signal and $y(t) = \alpha \cdot x(t)$ be a scaled version (different gain, different distance). The time-delay embeddings of $x$ and $y$ are related by $\mathbf{v}_y(t) = \alpha \cdot \mathbf{v}_x(t)$ --- the point clouds are identical up to a global scale factor. After the cloud normalization step (centering and scaling to unit variance), the two clouds are *identical*. Their persistence diagrams are therefore identical. The topological features are exactly invariant to amplitude scaling.

This is not true of spectral features: a spectrogram of $\alpha \cdot x(t)$ has amplitudes scaled by $\alpha$ (or $\alpha^2$ for power spectrograms), and even after log-scaling, the absolute level differs. Normalization helps, but the normalization must be done carefully to avoid introducing artifacts. For topological features, the invariance is built in.

**Robustness to additive noise.** Let $x(t)$ be a signal and $y(t) = x(t) + \eta(t)$ be a noisy version, where $\|\eta\|_\infty \leq \delta$. By the stability theorem (Theorem 6.4), the persistence diagrams of the embedded point clouds satisfy

$$d_B\bigl(\mathrm{Dgm}(x),\, \mathrm{Dgm}(y)\bigr) \leq C \cdot \delta$$

for a constant $C$ that depends on the embedding parameters but not on the signal. Topological features with persistence much greater than $C \cdot \delta$ are unaffected by the noise; only features with persistence comparable to $C \cdot \delta$ can be created or destroyed.

In practice, this means that persistent topological features --- the ones that dominate the summary statistics --- survive moderate noise. Short-lived features (near the diagonal of the persistence diagram) may be corrupted, but these are precisely the features that the summary statistics downweight (the maximum lifetime, 75th percentile, and normalized persistence all emphasize long-lived features).

**Invariance to monotone distance transformations.** Persistent homology depends only on the *ordering* of pairwise distances, not on the distances themselves. If we replace the Euclidean distance $d(x, y) = \|x - y\|_2$ with any monotone transformation $\tilde{d}(x, y) = f(d(x, y))$ where $f$ is strictly increasing, the Rips filtration produces the same nested sequence of simplicial complexes (though at different scale parameters). The persistence diagram is reparameterized but has the same topology --- the same birth-death pairs, in the same order.

This means that any distortion of the signal that preserves the *ordering* of temporal correlations --- a broad class that includes many forms of nonlinear gain, soft clipping, and moderate reverberation --- leaves the topological features invariant. Spectral features have no such invariance: any nonlinear transformation of the signal changes the spectral content in ways that are difficult to correct.

### 6.6.3 Empirical Evidence from Cetacean Decoders

The eris-ketos adversarial robustness framework provides direct evidence. Nine parametric acoustic transforms were applied at 11 intensity levels to synthesized coda waveforms. The topological features showed: **complete invariance to amplitude scaling** (identical TDA vectors across all levels, as predicted); **strong robustness to additive noise** (stable to ~5 dB SNR, with high-persistence statistics surviving longer than spectral baselines); **moderate sensitivity to click dropout** (expected --- dropout changes the signal itself, though TDA degraded more gracefully than Euclidean ICI features); and **near-complete invariance to spectral masking** (the Takens embedding operates in the time domain, making it insensitive to frequency-dependent recording artifacts).

### 6.6.4 The Invariance Hierarchy

The robustness properties of topological features can be organized into a hierarchy, from exact invariances to approximate robustness:

| Property | Invariance type | Theoretical basis |
|---|---|---|
| Amplitude scaling | Exact | Cloud normalization |
| Monotone gain | Exact | Monotone distance invariance |
| Additive noise ($\|\eta\|_\infty \leq \delta$) | $\delta$-approximate | Stability theorem |
| Recording distance | Exact (via amplitude) | Inverse-square → scaling |
| Spectral coloration | Approximate | Time-domain embedding |
| Time stretch (moderate) | Approximate | Reparameterization of the attractor |
| Signal destruction (dropout, clipping) | Not invariant | Signal change, not representation change |

[Figure 6.9: Robustness comparison across feature types under increasing noise. Horizontal axis: signal-to-noise ratio (dB). Vertical axis: classification accuracy for coda type. Lines: TDA features (16-dim), SPD features (136-dim), MFCCs (13-dim). TDA features maintain accuracy longest as SNR decreases, followed by SPD, followed by MFCCs. Below approximately 3 dB, all feature types degrade.]

This hierarchy is precisely what field recordings demand. Amplitude and distance variation are ubiquitous and uncontrollable --- exact invariance to these is essential. Noise is always present but bounded --- approximate robustness proportional to the noise magnitude is the best one can hope for. Signal destruction (a whale that swims behind a rock, a bird that flies away mid-recording) changes the signal itself and cannot be compensated by any feature extraction method.

---

## 6.7 The Full TDA Pipeline: From Raw Signal to Feature Vector

### 6.7.1 Assembling the Pipeline

The complete TDA pipeline chains the components developed in this chapter:

$$\text{raw signal} \xrightarrow{\text{normalize}} \text{unit-variance signal} \xrightarrow{\tau, d} \text{point cloud in } \mathbb{R}^d \xrightarrow{\text{subsample}} \text{reduced cloud} \xrightarrow{\text{Rips}} \text{persistence diagrams} \xrightarrow{\text{summarize}} \mathbb{R}^{16}$$

Each arrow is a well-defined operation with known information-theoretic properties. Normalization removes absolute amplitude while preserving all temporal and frequency structure. Takens embedding introduces no information loss (for generic parameters, by theorem). Subsampling has bounded effect (by the stability theorem). Rips homology extracts complete topological invariants of the filtration. Summary statistics compress the diagrams, losing the spatial arrangement of birth-death pairs but preserving the distribution of lifetimes and births.

The pipeline is **CPU-only** --- no GPU is required at any stage. With subsampling to 500--1,000 points, Ripser runs in under 0.5 seconds per recording on a single core. For the BirdCLEF competition (~15,000 test recordings), the full TDA extraction completes in under 15 minutes --- well within the 90-minute CPU submission constraint.[^6]

[^6]: This computational efficiency is a non-trivial practical advantage. The 156-dimensional geometric feature vector (SPD + trajectory + TDA) can be extracted for the entire test set in under 90 minutes on CPU, enabling deployment of geometric methods in settings where neural network inference would be prohibitively slow.

### 6.7.2 Integration with the Full Geometric Vector

The 16 TDA features form one component of the 156-dimensional geometric feature vector:

$$\mathbf{f} = [\underbrace{f_1, \ldots, f_{136}}_{\text{SPD (log-Euclidean covariance)}},\; \underbrace{f_{137}, \ldots, f_{140}}_{\text{trajectory (geodesic deviation)}},\; \underbrace{f_{141}, \ldots, f_{156}}_{\text{TDA (persistent homology)}}]$$

The three components probe three different mathematical spaces --- the SPD manifold (what frequencies co-occur), curves on the SPD manifold (how spectral shape evolves), and the topology of Euclidean point clouds (the shape of the signal in phase space). Their orthogonality is what makes the combination powerful. In the BirdCLEF experiments, ablation studies showed that removing any one component reduced classification accuracy, and the full 156-dimensional vector outperformed any subset.

---

## 6.8 Theoretical Foundations and Limitations

### 6.8.1 When Takens' Theorem Fails

Takens' theorem holds for *generic* observation functions and dynamics. The non-generic cases where it fails are instructive:

**Symmetric observation functions.** If the observation function $h$ respects a symmetry of the dynamics --- for example, $h(\mathbf{x}) = h(R\mathbf{x})$ for some rotation $R$ --- then the delay map cannot distinguish states related by $R$, and the embedding is not injective. In acoustic signals, this corresponds to an observation that does not break the symmetry of the vocal production: for instance, recording the amplitude (which is symmetric under phase inversion) loses the phase information. In practice, the waveform amplitude is sufficient for our purposes because the dynamics are not phase-symmetric (the vocal tract has asymmetric resonances).

**Insufficient embedding dimension.** If $d < 2m + 1$, the embedding is generically *not* injective --- there exist points in the state space that map to the same point in the embedding space. In practice, this means that $d = 3$ can fail for attractors with dimension $m \geq 2$. For the acoustic signals considered here, $d = 3$ is adequate because the dominant dynamics are low-dimensional, but for more complex signals (e.g., orchestral music with many simultaneous instruments), a higher embedding dimension would be needed.

**Noise beyond the stability bound.** The stability theorem guarantees robustness up to the noise magnitude. When the noise is comparable to or larger than the signal (SNR $\lesssim 0$ dB), the persistence diagram of the noise dominates, and the topological features of the signal are lost. There is no magic: topology is robust, not invulnerable.

### 6.8.2 What Topology Does Not Capture

Persistent homology captures the *shape* of the point cloud --- its connected components, loops, and voids. It does not capture:

- **Metric structure**: Two point clouds can have identical persistence diagrams but different metrics. A circle of radius 1 and a circle of radius 10 have the same topology (one $H_1$ loop) but different metrics. For classification, metric information matters --- it tells us *which* frequency, *how fast* the trill, *what size* the loop. The SPD features capture this metric structure; TDA does not.

- **Orientation**: Persistent homology is not sensitive to orientation. A clockwise spiral and a counterclockwise spiral have the same persistence diagram. For acoustic signals, orientation in the embedding space can carry information (e.g., rising vs. falling frequency sweeps), and this information is lost in the topological summary.

- **Fine-grained distributional structure**: The eight summary statistics compress the full persistence diagram into a coarse summary. The spatial arrangement of birth-death pairs --- which features are born at similar scales, which die together --- is lost. Persistence landscapes and persistence images preserve more of this structure, at the cost of higher dimensionality.

These limitations are precisely why TDA is one component of a three-geometry pipeline, not a standalone solution. The SPD features capture metric structure. The trajectory features capture directional dynamics. TDA captures topology. Together, they cover more of the geometric content of the signal than any single method.

### 6.8.3 Connections to the Communication Manifold

The TDA pipeline operates on the signal manifold $S$ --- the first factor of the communication manifold $M = S \times P \times C$ introduced in Chapter 3. The topological features characterize the *shape of the signal space*, not the pragmatic or semantic content. This is a feature, not a limitation. The signal manifold is the most directly accessible factor of $M$, and characterizing its topology is the necessary first step before ascending the Rosetta trajectory (Chapter 16) toward hierarchy and meaning. TDA tells us that whale coda types have distinct topological signatures; it does not tell us what they mean. But by providing a robust, noise-invariant representation, it enables downstream methods to operate on stable inputs. The topology is the foundation on which meaning analysis is built.

---

## 6.9 Summary

This chapter has developed the full TDA pipeline for communication signals: Takens' embedding theorem reconstructs attractor topology from a 1D time series ($\S$6.1); persistent homology extracts topological invariants --- connected components ($H_0$) and loops ($H_1$) --- across the Vietoris--Rips filtration, with stability guaranteed under perturbation ($\S$6.2); eight summary statistics per homology dimension yield a compact 16-dimensional feature vector ($\S$6.3). Applied to whale codas, the pipeline distinguishes rhythm classes by topological signature while cleanly separating coda-type content from individual identity ($\S$6.4). Applied to birdsong, it captures species-specific dynamical structure that complements SPD spectral features ($\S$6.5). The practical payoff is robustness: exact invariance to amplitude scaling, approximate robustness to noise, and insensitivity to spectral coloration --- precisely the properties that field recordings demand ($\S$6.6).

The TDA pipeline completes the three-geometry toolkit: hyperbolic embeddings for hierarchy (Chapter 5), persistent homology for topology (this chapter), and SPD manifold features for covariance (Part III). In Part III, we apply the full toolkit to non-human communication --- whale codas in Chapter 7, birdsong in Chapter 8 --- building the evidence that communication, across species and across millions of years of evolutionary divergence, has geometric structure that scalar evaluation destroys.

---

**Notes on computation.** All TDA computations in this chapter use the Ripser library (Bauer, 2021) for Vietoris--Rips persistent homology. The `geometric_features.py` pipeline includes a naive fallback (`_persistence_diagrams_naive`) that computes $H_0$ via single-linkage clustering when Ripser is unavailable, but $H_1$ computation requires Ripser or an equivalent. The full pipeline (Takens embedding + subsampling + Ripser + feature extraction) runs in under 0.5 seconds per recording on a single CPU core for clouds subsampled to 500--1,000 points. The eris-ketos toolkit provides an independent implementation (`tda_clicks` module) optimized for ICI-based point clouds rather than raw waveforms.

**Series cross-references.** The mathematical foundations of persistent homology are developed in *Geometric Methods* (Bond, 2026a), Ch. 5. The stability theorem and its implications for robust feature extraction are treated in GM Ch. 5.3--5.4. The SPD manifold features that complement the TDA pipeline are developed in GM Ch. 4.6. The communication manifold $M = S \times P \times C$ on which TDA operates (specifically, on the $S$ factor) is defined in Ch. 3 of this volume. The empirical applications to cetacean communication and birdsong are developed in Ch. 7 and Ch. 8, respectively.

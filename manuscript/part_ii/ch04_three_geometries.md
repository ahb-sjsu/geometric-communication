# Chapter 4: Three Geometries for Communication

*Part II: The Geometric Toolkit*

---

> *"Geometry is not true, it is advantageous."*
> --- Henri Poincare, *Science and Hypothesis*, 1902

> **RUNNING EXAMPLE --- THE WHALE, THE BIRD, AND THE SCRIBE**
>
> *A sperm whale surfaces in the eastern Caribbean and produces a coda --- five rapid clicks separated by precisely timed silences. The inter-click intervals encode the coda's identity: a "1+1+3" rhythm (two short intervals, then a longer pause, then three more clicks). This coda is one of 21 types produced by the whale's social unit, organized in a combinatorial hierarchy of rhythm, tempo, rubato, and ornamentation.*
>
> *Eight thousand kilometers away, a white-throated sparrow sings a descending whistle --- a sequence of pure tones whose harmonic structure and spectral transitions identify it as unambiguously as a fingerprint identifies a human. The bird's song is one of 206 species-specific vocal signatures in the BirdCLEF database.*
>
> *And in the British Museum, a clay tablet dating to approximately 1900 BCE records an Old Assyrian business transaction. The cuneiform signs are organized in a three-level hierarchy: sign form, reading, and word. The sign* 𒀭 *can be read as AN ("heaven"), DINGIR ("god"), or Anu (a personal name), depending on context.*
>
> *Three communication systems. Three biological kingdoms. Four thousand years. What geometric framework could possibly apply to all three?*
>
> *This chapter introduces the answer: not one geometry, but three. Each captures a different kind of structure --- hierarchy, covariance, and shape --- and together they span the structural space of communication in a way that no single geometry could.*

---

In Chapter 3, we constructed the communication manifold $M = S \times P \times C$ and equipped it with a metric, a heuristic field, and a gauge group. The manifold provides the *stage*. This chapter provides the *instruments* --- the concrete mathematical tools that measure structure on $M$ and convert it into computable features.

The core insight is that communication has at least three kinds of geometric structure, and they are orthogonal. **Hierarchical structure** --- the tree-like organization of categories, taxonomies, and levels of abstraction --- is best captured by hyperbolic geometry. **Covariance structure** --- the correlations between frequency bands, the joint variation of acoustic features --- is best captured by Riemannian geometry on the manifold of symmetric positive-definite matrices. **Topological structure** --- the shape of attractors, the periodicity of signals, the connected components of a dynamical system --- is best captured by persistent homology from algebraic topology.

No single geometry suffices. Hyperbolic embeddings capture the whale's coda hierarchy but cannot encode the spectral "vowel space" of each click. SPD manifold features capture the bird's harmonic correlations but cannot detect the rhythmic periodicity of a coda sequence. Persistent homology captures the shape of a vocal attractor but says nothing about where a coda type sits in the taxonomic tree. The three geometries are not competing descriptions of the same structure. They are complementary descriptions of different structures, and their combination --- a 156-dimensional feature vector comprising 136 SPD features, 4 trajectory features, and 16 topological features --- captures more than the sum of its parts.

This chapter proceeds in five stages. Section 4.1 introduces hyperbolic geometry through the Poincare ball model, developing the exponential map, logarithmic map, Mobius addition, and geodesic distance with full formal definitions and worked examples. Section 4.2 introduces Riemannian geometry on SPD manifolds, developing the log-Euclidean metric, the covariance computation, and the spectral trajectory, grounded in the actual implementation from our codebase. Section 4.3 introduces persistent homology via Takens' time-delay embedding, the Rips complex, and persistence diagrams. Section 4.4 shows how the three geometries combine into the 156-dimensional feature vector and explains why the combination works. Section 4.5 draws the connections to the communication manifold of Chapter 3 and previews the empirical applications of Chapters 5--8.

---

## 4.1 Hyperbolic Geometry: The Poincare Ball

### 4.1.1 Why Hyperbolic?

Consider a binary tree of depth $k$. The tree has $2^k - 1$ nodes, and any embedding must place each node at a location that reflects its position in the hierarchy: parent above child, siblings close together, distant cousins far apart. How much space does this require?

In Euclidean space $\mathbb{R}^d$, the volume of a ball of radius $r$ grows as $r^d$ --- polynomially in $r$ for fixed $d$. But the number of nodes at depth $k$ in a binary tree grows as $2^k$ --- exponentially. To embed the tree without distortion, we need the space to accommodate exponential growth, which means either using exponentially many dimensions (impractical) or accepting distortion that grows with depth.

In hyperbolic space of constant negative curvature $-c$, the volume of a ball of radius $r$ grows as $e^{(d-1)\sqrt{c}\,r}$ --- exponentially in $r$ for any fixed dimension $d > 1$.[^1] This exponential volume growth matches the exponential branching of the tree. A binary tree of arbitrary depth embeds in hyperbolic space of dimension $O(\log 2) = O(1)$ with bounded distortion, whereas Euclidean embedding requires dimension $O(2^k)$ for a tree of depth $k$.[^2]

[^1]: The precise formula for the volume of a geodesic ball of radius $r$ in $d$-dimensional hyperbolic space of curvature $-c$ is $V_d(r) = \omega_{d-1} \int_0^r \left(\frac{\sinh(\sqrt{c}\,t)}{\sqrt{c}}\right)^{d-1} dt$, where $\omega_{d-1}$ is the volume of the unit $(d-1)$-sphere. For large $r$, this is dominated by the exponential term $e^{(d-1)\sqrt{c}\,r}$. See *Geometric Methods* (Bond, 2026a), Ch. 4.3 for the derivation.

[^2]: This is the Bourgain embedding theorem applied to tree metrics. Sarkar (2011) showed that any weighted tree on $n$ nodes can be embedded in the Poincare disk (2-dimensional hyperbolic space) with arbitrarily low distortion $1 + \epsilon$, using coordinates of $O(\log n / \epsilon)$ bits of precision. See Sala et al. (2018) for the multi-dimensional generalization.

This is not an abstract curiosity. Every communication system we study in this book has hierarchical structure:

- **Whale codas**: The 21 coda types form a combinatorial hierarchy indexed by click count, rhythm class, tempo, rubato, and ornamentation (Sharma et al., 2024).
- **Birdsong**: Species are organized in a Linnaean taxonomy (species $\subset$ genus $\subset$ family $\subset$ order) with at least four levels.
- **Cuneiform**: Signs are organized in a three-level hierarchy --- sign form $\to$ reading $\to$ word --- where a single sign can have multiple readings and each reading can map to multiple words.
- **Semantic concepts**: WordNet organizes English nouns in a hypernymy tree with an average depth of 8 and a maximum branching factor of over 400.

In each case, the hierarchy is not a convenient organizational device. It is an intrinsic structural feature of the communication system, and any representation that ignores it --- such as a flat Euclidean feature vector --- discards information that matters.

### 4.1.2 The Poincare Ball Model

The Poincare ball model represents $d$-dimensional hyperbolic space of curvature $-c$ as the open ball

$$\mathbb{B}^d_c = \left\{ \mathbf{x} \in \mathbb{R}^d : c\|\mathbf{x}\|^2 < 1 \right\}$$

equipped with the Riemannian metric tensor

$$g_{\mathbf{x}} = \left(\lambda_{\mathbf{x}}^c\right)^2 g^E$$

where $g^E$ is the Euclidean metric and $\lambda_{\mathbf{x}}^c = \frac{2}{1 - c\|\mathbf{x}\|^2}$ is the **conformal factor**. The conformal factor diverges as $\mathbf{x}$ approaches the boundary of the ball ($c\|\mathbf{x}\|^2 \to 1$), which means distances stretch infinitely near the boundary --- there is "room" for the exponentially many leaves of a tree.

**Definition 4.1** (Poincare Ball). *The Poincare ball of dimension $d$ and curvature parameter $c > 0$ is the Riemannian manifold $(\mathbb{B}^d_c, g)$ where $\mathbb{B}^d_c = \{\mathbf{x} \in \mathbb{R}^d : c\|\mathbf{x}\|^2 < 1\}$ and $g_{\mathbf{x}} = (\lambda_{\mathbf{x}}^c)^2 g^E$ with conformal factor $\lambda_{\mathbf{x}}^c = 2/(1 - c\|\mathbf{x}\|^2)$. The sectional curvature is $-c$ everywhere.*

The curvature parameter $c$ controls the "spread" of the ball. Higher $c$ means more hyperbolic distortion: the boundary is closer (at radius $1/\sqrt{c}$), the conformal factor grows faster, and hierarchical structures are spread more aggressively. Lower $c$ makes the geometry more Euclidean near the origin. The choice of $c$ is a modeling decision --- it sets the trade-off between resolving fine structure near the root of a hierarchy and resolving fine structure near the leaves.

In the `eris-ketos` implementation, the ball is parameterized as:

```python
class PoincareBall:
    def __init__(self, c: float = 1.0) -> None:
        self.c = c
        self.sqrt_c = c ** 0.5
```

The default $c = 1.0$ is standard for exploratory work. For deep hierarchies (cuneiform signs with three taxonomic levels), smaller values of $c$ can prevent leaves from collapsing near the boundary; for shallow hierarchies (whale coda types with one or two levels), larger values can increase separation.

### 4.1.3 The Four Fundamental Operations

Working on the Poincare ball requires four operations: the exponential map (moving from tangent space to the ball), the logarithmic map (the inverse), Mobius addition (the hyperbolic analogue of vector addition), and geodesic distance.

**The Exponential Map.** The exponential map at the origin takes a tangent vector $\mathbf{v} \in T_{\mathbf{0}}\mathbb{B}^d_c \cong \mathbb{R}^d$ and maps it to the point on the ball reached by following the geodesic from the origin in the direction of $\mathbf{v}$ for a distance equal to $\|\mathbf{v}\|$.

**Definition 4.2** (Exponential Map at the Origin). *The exponential map $\exp_{\mathbf{0}}^c: T_{\mathbf{0}}\mathbb{B}^d_c \to \mathbb{B}^d_c$ is*

$$\exp_{\mathbf{0}}^c(\mathbf{v}) = \tanh\!\left(\sqrt{c}\,\|\mathbf{v}\|\right) \cdot \frac{\mathbf{v}}{\sqrt{c}\,\|\mathbf{v}\|}$$

For small $\|\mathbf{v}\|$, $\tanh(\sqrt{c}\,\|\mathbf{v}\|) \approx \sqrt{c}\,\|\mathbf{v}\|$, so $\exp_{\mathbf{0}}^c(\mathbf{v}) \approx \mathbf{v}$ --- the exponential map is approximately the identity near the origin, where hyperbolic space is approximately Euclidean. For large $\|\mathbf{v}\|$, $\tanh(\sqrt{c}\,\|\mathbf{v}\|) \to 1$, so $\exp_{\mathbf{0}}^c(\mathbf{v})$ approaches the boundary $\|\mathbf{x}\| = 1/\sqrt{c}$ but never reaches it. No finite tangent vector maps to the boundary --- the boundary is at infinity, as it should be in a space of infinite volume.

In the implementation:

```python
def expmap0(self, v: torch.Tensor) -> torch.Tensor:
    v_norm = v.norm(dim=-1, keepdim=True).clamp_min(1e-15)
    return self.project(
        torch.tanh(self.sqrt_c * v_norm) * v / (self.sqrt_c * v_norm)
    )
```

The `clamp_min(1e-15)` prevents division by zero for the zero vector. The `project` call ensures numerical stability by clamping the norm to be strictly less than $1/\sqrt{c}$.

**The Logarithmic Map.** The logarithmic map is the inverse of the exponential map: it takes a point on the ball and returns the tangent vector at the origin whose exponential map is that point.

**Definition 4.3** (Logarithmic Map to the Origin). *The logarithmic map $\log_{\mathbf{0}}^c: \mathbb{B}^d_c \to T_{\mathbf{0}}\mathbb{B}^d_c$ is*

$$\log_{\mathbf{0}}^c(\mathbf{y}) = \operatorname{arctanh}\!\left(\sqrt{c}\,\|\mathbf{y}\|\right) \cdot \frac{\mathbf{y}}{\sqrt{c}\,\|\mathbf{y}\|}$$

The logarithmic map "unwraps" the ball back to Euclidean tangent space. Points near the boundary, which are at large hyperbolic distance from the origin, are mapped to tangent vectors with large Euclidean norm --- the logarithmic map is an expansion that undoes the compression of the exponential map.

**Mobius Addition.** In Euclidean space, translating a point $\mathbf{x}$ by a vector $\mathbf{y}$ is simply addition: $\mathbf{x} + \mathbf{y}$. On the Poincare ball, the analogous operation is Mobius addition, which accounts for the curvature of the space.

**Definition 4.4** (Mobius Addition). *The Mobius addition of $\mathbf{x}, \mathbf{y} \in \mathbb{B}^d_c$ is*

$$\mathbf{x} \oplus_c \mathbf{y} = \frac{(1 + 2c\langle\mathbf{x},\mathbf{y}\rangle + c\|\mathbf{y}\|^2)\mathbf{x} + (1 - c\|\mathbf{x}\|^2)\mathbf{y}}{1 + 2c\langle\mathbf{x},\mathbf{y}\rangle + c^2\|\mathbf{x}\|^2\|\mathbf{y}\|^2}$$

Mobius addition is not commutative: in general $\mathbf{x} \oplus_c \mathbf{y} \neq \mathbf{y} \oplus_c \mathbf{x}$. It forms a **gyrogroup** --- a generalization of a group where commutativity is replaced by a weaker symmetry mediated by the gyration operator. The non-commutativity reflects the fact that parallel transport on a curved manifold is path-dependent: translating from $\mathbf{x}$ to $\mathbf{y}$ and then to $\mathbf{z}$ is not the same as translating from $\mathbf{x}$ directly to $\mathbf{z}$ and then adjusting.

Note the structure of the formula. When $c \to 0$ (the Euclidean limit), all terms involving $c$ vanish, and $\mathbf{x} \oplus_c \mathbf{y} \to \mathbf{x} + \mathbf{y}$. When $\mathbf{x} = \mathbf{0}$, $\mathbf{0} \oplus_c \mathbf{y} = \mathbf{y}$ --- the origin is the identity element. The denominator ensures the result stays inside the ball.

In the implementation:

```python
def mobius_add(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    x2 = (x * x).sum(-1, keepdim=True)
    y2 = (y * y).sum(-1, keepdim=True)
    xy = (x * y).sum(-1, keepdim=True)
    num = (1 + 2 * self.c * xy + self.c * y2) * x + (1 - self.c * x2) * y
    denom = 1 + 2 * self.c * xy + self.c**2 * x2 * y2
    return self.project(num / denom.clamp_min(1e-15))
```

**Geodesic Distance.** The distance between two points on the Poincare ball is the length of the geodesic connecting them. This is the metric that defines "closeness" in hyperbolic space.

**Definition 4.5** (Hyperbolic Distance). *The geodesic distance between $\mathbf{x}, \mathbf{y} \in \mathbb{B}^d_c$ is*

$$d_c(\mathbf{x}, \mathbf{y}) = \frac{2}{\sqrt{c}} \operatorname{arctanh}\!\left(\sqrt{c}\,\|(-\mathbf{x}) \oplus_c \mathbf{y}\|\right)$$

The distance formula composes Mobius addition with arctanh. The factor $2/\sqrt{c}$ normalizes by the curvature. For points near the origin, $d_c(\mathbf{x}, \mathbf{y}) \approx 2\|\mathbf{x} - \mathbf{y}\|$ (approximately twice the Euclidean distance). For points near the boundary, the distance grows logarithmically with the Euclidean distance to the boundary --- points that look close in the ambient Euclidean space are actually far apart on the ball.

This asymmetric stretching is precisely what makes hyperbolic embeddings work for hierarchies. The root of a tree is placed near the origin, where the space is approximately Euclidean and the root has roughly equal distance to all children. The leaves are placed near the boundary, where there is exponentially more room --- enough to accommodate the exponentially many leaves of a deep tree.

In the implementation:

```python
def dist(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    neg_x = -x
    add_result = self.mobius_add(neg_x, y)
    norm = add_result.norm(dim=-1).clamp(max=(1 / self.sqrt_c) - 1e-5)
    return (2.0 / self.sqrt_c) * torch.arctanh(self.sqrt_c * norm)
```

[Figure 4.1] *The Poincare disk (2D ball with $c = 1$). Left: a binary tree of depth 5 embedded in the disk, with the root at the center and leaves near the boundary. Geodesics (shortest paths) are arcs of circles perpendicular to the boundary. Right: concentric geodesic circles at equal distance increments from the origin. The circles bunch together in Euclidean coordinates near the boundary but are equally spaced in hyperbolic distance, illustrating the exponential volume growth.*

### 4.1.4 Classification via Hyperbolic Prototypes

The fundamental operations above provide the vocabulary for hyperbolic computation. To use them for classification --- assigning a whale coda to a type, a birdsong to a species, a cuneiform sign to a reading --- we need a classification head that respects the hyperbolic geometry.

The standard approach is **Hyperbolic Multinomial Logistic Regression** (HypMLR): place a learned prototype $\mathbf{p}_k$ on the ball for each class $k$, and classify a point $\mathbf{x}$ by its distances to the prototypes:

$$\text{logit}_k(\mathbf{x}) = -\alpha_k \cdot d_c(\mathbf{x}, \mathbf{p}_k)$$

where $\alpha_k = e^{s_k}$ is a per-class learnable temperature and $s_k$ is the log-scale parameter. The negative sign converts distance to similarity: closer to a prototype means higher logit.

The prototypes are parameterized in tangent space at the origin and mapped to the ball via the exponential map, which ensures they remain inside the ball throughout training:

```python
class HyperbolicMLR(nn.Module):
    def __init__(self, embed_dim: int, num_classes: int, c: float = 1.0):
        super().__init__()
        self.ball = PoincareBall(c)
        self.proto_tangent = nn.Parameter(
            torch.randn(num_classes, embed_dim) * 0.01
        )
        self.log_scale = nn.Parameter(torch.zeros(num_classes))

    @property
    def prototypes(self) -> torch.Tensor:
        return self.ball.expmap0(self.proto_tangent)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        protos = self.prototypes
        dists = self.ball.dist(x.unsqueeze(1), protos.unsqueeze(0))
        return -dists * self.log_scale.exp()
```

The prototypes can be initialized from a taxonomic tree. Given a distance matrix encoding the hierarchical relationships between classes (e.g., same family = distance 1, same order = distance 2, different order = distance 3), spectral decomposition of a Gaussian kernel over the matrix produces an initial embedding where taxonomically close classes start near each other on the ball:

$$K_{ij} = \exp\!\left(-\frac{d_{\text{tax}}(i,j)^2}{2}\right)$$

$$\mathbf{p}_i^{(0)} = \sum_{k=1}^{d} \sqrt{|\lambda_k|}\, v_{ik}$$

where $\lambda_k$ and $v_k$ are the top-$d$ eigenvalues and eigenvectors of $K$. This initialization means the classifier does not need to "discover" the hierarchy from scratch --- it begins with a geometrically faithful representation and refines it during training.

### 4.1.5 The Curvature Parameter

The curvature parameter $c$ is the single most important hyperparameter of hyperbolic embeddings, and it deserves explicit discussion.

Setting $c$ too low makes the ball nearly Euclidean near the origin and wastes the hyperbolic advantage. Setting $c$ too high concentrates all points near the boundary, where numerical precision suffers and gradient signals are weak (because the conformal factor amplifies small perturbations into large distance changes).

The optimal $c$ depends on the branching factor and depth of the hierarchy. For a tree with branching factor $b$ and depth $k$, a heuristic that has proven reliable in practice is:

$$c \approx \frac{(\log b)^2}{4k^2}$$

This ensures that the first level of the hierarchy (direct children of the root) occupies the middle band of the ball (neither too close to the origin nor too close to the boundary), leaving room for deeper levels without requiring extreme precision.

For the empirical systems in this book:

- **Whale codas** ($b \approx 5$, $k = 3$): $c \approx 0.07$, though the implementations use $c = 1.0$ for simplicity and compensate by scaling the initial tangent vectors.
- **Cuneiform signs** ($b \approx 10$, $k = 3$): $c \approx 0.15$.
- **WordNet nouns** ($b \approx 400$, $k = 8$): $c \approx 0.14$, which is close to the $c = 0.1$ used in the original Nickel and Kiela (2017) Poincare embedding paper.

[Figure 4.2] *Effect of curvature parameter $c$ on the same tree embedding. Left: $c = 0.1$ (mildly hyperbolic) --- the tree is compact, with leaves well inside the ball. Center: $c = 1.0$ (moderately hyperbolic) --- the tree fills the ball, with leaves near but not at the boundary. Right: $c = 10.0$ (strongly hyperbolic) --- leaves are compressed against the boundary, with poor numerical resolution. The optimal $c$ places the deepest leaves in the outer half of the ball without exceeding $\|\mathbf{x}\| > 0.95/\sqrt{c}$.*

### 4.1.6 Applications in Communication

Hyperbolic geometry applies wherever communication exhibits hierarchical organization. In this book, it appears in three principal roles:

1. **Coda taxonomy** (Chapter 5). The 21 sperm whale coda types embed in a 32-dimensional Poincare ball with prototypes initialized from the combinatorial hierarchy (click count $\times$ rhythm class $\times$ ornamentation). Hyperbolic classification achieves 74.3% accuracy versus 72.8% Euclidean --- a modest improvement in accuracy, but a substantial improvement in interpretability, because the embedding directly reflects the biological taxonomy.

2. **Cuneiform sign hierarchy** (Chapter 9). The three-level structure of Akkadian writing (sign $\to$ reading $\to$ word) is encoded as an additive attention bias in a transformer: tokens whose signs are hierarchically close attend to each other more strongly, with the bias computed as the hyperbolic distance between sign embeddings on the Poincare ball. This is a fixed geometric prior, not a learned embedding --- it injects Assyriological knowledge directly into the model architecture.

3. **Semantic taxonomies** (Chapter 11). The Hohfeldian relations (Right, Duty, Liberty, No-Right) form a shallow hierarchy that embeds trivially in hyperbolic space. The deeper insight is that the *connections* between normative positions --- the D4 symmetry group explored in Chapter 13 --- are naturally represented as isometries of the ball.

---

## 4.2 Riemannian Geometry: The SPD Manifold

### 4.2.1 Why Covariance?

A spectrogram is a matrix. Each column is a snapshot of the frequency content at a single moment in time; each row is the evolution of a single frequency band across the duration of the signal. Standard machine learning treats the spectrogram as a flat image --- a grid of pixels to be fed to a convolutional neural network. This works well enough for classification, but it discards a specific and important kind of structure: the *correlations between frequency bands*.

Consider a bird that produces a whistle with a strong fundamental frequency at 3 kHz and a harmonic at 6 kHz. These two frequency bands are not independent: when the fundamental rises, the harmonic rises in lockstep. This correlation is invisible in the spectrogram's pixel values (which record only the energy at each time-frequency point) but is captured by the **covariance matrix** of the frequency bands. The covariance matrix records how each pair of bands co-varies across time, encoding the harmonic structure --- the "vowel space" --- of the vocalization.[^3]

[^3]: The term "vowel space" is borrowed from Begus et al. (2025), who discovered that sperm whale clicks exhibit formant-like spectral structure analogous to the vowel formants of human speech. Whether this analogy reflects a genuine functional similarity or a convergent acoustic phenomenon remains an open question. For our purposes, the mathematical structure --- cross-frequency correlations encoded in an SPD matrix --- is the same regardless of the functional interpretation.

The covariance matrix of $n$ frequency bands is an $n \times n$ symmetric positive-definite (SPD) matrix. The space of all such matrices is not a vector space --- it is a **Riemannian manifold** with rich geometric structure. Using Euclidean distance on SPD matrices (the Frobenius norm of their difference) violates the manifold geometry: it can produce "distances" that fail to respect the positive-definite constraint, and it treats the space as flat when it is intrinsically curved. The correct distance requires a Riemannian metric that respects the manifold's curvature.

### 4.2.2 The Space SPD(n)

**Definition 4.6** (SPD Manifold). *The manifold of $n \times n$ symmetric positive-definite matrices is*

$$\operatorname{SPD}(n) = \left\{ S \in \mathbb{R}^{n \times n} : S = S^\top,\, S \succ 0 \right\}$$

*where $S \succ 0$ means all eigenvalues of $S$ are strictly positive. $\operatorname{SPD}(n)$ is an open cone in the vector space of symmetric matrices, and is a smooth Riemannian manifold of dimension $n(n+1)/2$.*

The dimension $n(n+1)/2$ arises because a symmetric $n \times n$ matrix has $n$ diagonal entries and $n(n-1)/2$ off-diagonal entries (the lower triangle equals the upper triangle), giving $n + n(n-1)/2 = n(n+1)/2$ independent parameters. For $n = 16$ (our default number of frequency bands), this gives $16 \times 17 / 2 = 136$ independent parameters --- 136 features that encode the complete cross-frequency correlation structure of the vocalization.

The manifold $\operatorname{SPD}(n)$ is an *open cone*: if $S$ is SPD and $\alpha > 0$, then $\alpha S$ is SPD. It is not a vector space, because the zero matrix is not SPD (it has zero eigenvalues) and the difference of two SPD matrices is not necessarily SPD (the eigenvalues of $S_1 - S_2$ can be negative). This non-linearity is precisely why Euclidean methods fail: the "straight line" between two SPD matrices in the ambient Euclidean space can pass through non-positive-definite matrices, exiting the manifold entirely.

### 4.2.3 The Log-Euclidean Metric

Several Riemannian metrics have been proposed for $\operatorname{SPD}(n)$: the affine-invariant metric, the Bures-Wasserstein metric, the power-Euclidean family, and the log-Euclidean metric. We use the log-Euclidean metric throughout this book because it offers the best trade-off between geometric fidelity and computational tractability.

**Definition 4.7** (Log-Euclidean Distance). *The log-Euclidean distance between $S_1, S_2 \in \operatorname{SPD}(n)$ is*

$$d_{LE}(S_1, S_2) = \left\| \log(S_1) - \log(S_2) \right\|_F$$

*where $\log$ is the matrix logarithm and $\|\cdot\|_F$ is the Frobenius norm.*

The matrix logarithm of an SPD matrix $S$ with eigendecomposition $S = U \Lambda U^\top$ is

$$\log(S) = U \operatorname{diag}(\log \lambda_1, \ldots, \log \lambda_n) U^\top$$

where $\lambda_i > 0$ are the eigenvalues of $S$. Because all eigenvalues are positive, their logarithms are well-defined (and real), so the matrix logarithm maps $\operatorname{SPD}(n)$ into the vector space of $n \times n$ symmetric matrices. This mapping is a diffeomorphism --- it is smooth, invertible (the inverse is the matrix exponential $\exp$), and structure-preserving.

The key insight is that the log-Euclidean metric "flattens" the SPD manifold: after applying the matrix logarithm, the resulting symmetric matrices live in a genuine vector space where Euclidean distance is meaningful. This means standard machine learning methods --- linear regression, SVMs, gradient boosting --- can operate directly on the log-mapped features without special manifold-aware modifications.

In the `eris-ketos` implementation, the log map is computed via eigendecomposition:

```python
@staticmethod
def log_map(S: torch.Tensor) -> torch.Tensor:
    eigvals, eigvecs = torch.linalg.eigh(S)
    eigvals = eigvals.clamp_min(1e-10)
    return eigvecs @ torch.diag_embed(eigvals.log()) @ eigvecs.transpose(-2, -1)
```

The `clamp_min(1e-10)` prevents numerical issues from near-zero eigenvalues, which can arise from regularization rounding errors.

In the BirdCLEF feature extraction pipeline, the same computation appears in NumPy form:

```python
def spd_distance(cov1: np.ndarray, cov2: np.ndarray) -> float:
    diff = logm(cov1).real - logm(cov2).real
    return np.linalg.norm(diff, 'fro')
```

Here `logm` is SciPy's matrix logarithm, and `.real` discards the (numerically zero) imaginary component that floating-point arithmetic can introduce.

**Why not Euclidean distance?** To see why the log-Euclidean metric matters, consider two SPD matrices $S_1$ and $S_2$ that differ only in one eigenvalue: $S_1$ has eigenvalues $(1, 1, \ldots, 1, 0.01)$ and $S_2$ has eigenvalues $(1, 1, \ldots, 1, 0.001)$. The Frobenius distance is $|0.01 - 0.001| = 0.009$ --- tiny. The log-Euclidean distance is $|\log(0.01) - \log(0.001)| = |\log 10| \approx 2.3$ --- substantial. The log-Euclidean metric correctly identifies that the ratio between the smallest eigenvalues has changed by a factor of 10, which represents a qualitative shift in the covariance structure (a frequency band that was weakly correlated has become an order of magnitude less correlated). The Frobenius distance, measuring absolute change, misses this.

This ratio-sensitivity is exactly what we need for acoustic signals, where the dynamic range of covariance eigenvalues can span several orders of magnitude. A bird species with tightly correlated harmonics (large eigenvalues, small eigenvalue spread) and a bird species with diffuse spectral energy (small eigenvalues, large eigenvalue spread) are qualitatively different, and the log-Euclidean metric captures this difference while the Frobenius norm does not.

### 4.2.4 Computing the Covariance Matrix

The starting point for SPD features is a mel spectrogram --- a time-frequency representation of the audio signal, typically with 128 mel-spaced frequency bins and a variable number of time frames. We group the mel bins into $n$ frequency bands (default $n = 16$), compute the mean energy in each band at each time step, and then compute the covariance matrix of the resulting $n$ band-energy time series.

**Definition 4.8** (Frequency-Band Covariance). *Given a mel spectrogram $\mathbf{X} \in \mathbb{R}^{n_{\text{mel}} \times T}$ with $n_{\text{mel}}$ mel bins and $T$ time frames, partition the mel bins into $n$ bands of approximately equal size. Let $\mathbf{b}_i(t) \in \mathbb{R}$ be the mean energy in band $i$ at time $t$, and let $\mathbf{B} \in \mathbb{R}^{n \times T}$ be the matrix of band energies. The frequency-band covariance matrix is*

$$\Sigma = \frac{1}{T-1} (\mathbf{B} - \bar{\mathbf{B}})(\mathbf{B} - \bar{\mathbf{B}})^\top + \epsilon \mathbf{I}_n$$

*where $\bar{\mathbf{B}}$ is the temporal mean and $\epsilon > 0$ is a regularization parameter guaranteeing positive definiteness.*

The regularization $\epsilon \mathbf{I}_n$ (default $\epsilon = 10^{-4}$) is essential. Without it, the covariance matrix could have zero eigenvalues (if two bands are perfectly correlated or a band has zero variance), placing it on the boundary of $\operatorname{SPD}(n)$ where the log map is undefined. The regularization shifts all eigenvalues away from zero, ensuring the matrix is strictly positive definite. This is not a hack --- it is a Bayesian prior, equivalent to assuming a small amount of independent noise in each frequency band.

In the BirdCLEF pipeline:

```python
def compute_covariance(spectrogram: np.ndarray, n_bands: int = 16,
                       epsilon: float = 1e-4) -> np.ndarray:
    n_mels, T = spectrogram.shape
    band_size = n_mels // n_bands
    bands = np.zeros((n_bands, T))
    for i in range(n_bands):
        start = i * band_size
        end = start + band_size if i < n_bands - 1 else n_mels
        bands[i] = spectrogram[start:end].mean(axis=0)
    cov = np.cov(bands)
    cov += epsilon * np.eye(n_bands)
    return cov
```

The output is a $16 \times 16$ SPD matrix. The diagonal entries encode the variance of each frequency band (how much the energy in that band fluctuates over time). The off-diagonal entries encode the covariance between bands (how much two bands fluctuate together). A large positive off-diagonal entry between bands $i$ and $j$ means those bands tend to be energetic at the same times --- they are harmonically related. A near-zero entry means they are approximately independent.

### 4.2.5 From SPD Matrix to Feature Vector

The covariance matrix is a point on $\operatorname{SPD}(16)$. To use it as input to standard machine learning methods, we map it to a vector in Euclidean space via the log-Euclidean map and extract the upper triangle (including the diagonal), which contains all independent information since the matrix is symmetric.

**Proposition 4.1** (SPD Feature Dimension). *The log-Euclidean feature vector of an $n \times n$ SPD matrix has dimension $n(n+1)/2$. For $n = 16$, this is $16 \times 17/2 = 136$.*

In the implementation:

```python
def spd_features_from_spectrogram(spectrogram: np.ndarray,
                                   n_bands: int = 16,
                                   epsilon: float = 1e-4) -> np.ndarray:
    cov = compute_covariance(spectrogram, n_bands, epsilon)
    log_cov = logm(cov).real
    indices = np.triu_indices(n_bands)
    features = log_cov[indices]
    return features.astype(np.float32)
```

The pipeline is: spectrogram $\to$ band energies $\to$ covariance matrix $\Sigma \in \operatorname{SPD}(16)$ $\to$ matrix logarithm $\log(\Sigma)$ $\to$ upper triangle extraction $\to$ 136-dimensional feature vector $\in \mathbb{R}^{136}$. Each step is deterministic, differentiable, and computationally cheap (the dominant cost is the eigendecomposition for the matrix logarithm, which is $O(n^3) = O(4096)$ for $n = 16$ --- negligible).

### 4.2.6 The Spectral Trajectory

A single covariance matrix captures the cross-frequency correlations of a vocalization as a whole. But vocalizations are not static --- they evolve over time. A bird's song may begin with a descending whistle (strong correlation between adjacent bands) and transition to a trill (rapid alternation between two frequency ranges, creating a different correlation pattern). A whale coda may begin with clicks rich in low-frequency energy and shift to clicks rich in high-frequency energy (the "diphthong" structure observed by Begus et al., 2025).

To capture this temporal evolution, we slide a window across the spectrogram and compute a covariance matrix at each position. The result is a **trajectory on the SPD manifold**: a sequence of points $\Sigma_1, \Sigma_2, \ldots, \Sigma_K \in \operatorname{SPD}(n)$ that traces the evolution of spectral structure over time.

**Definition 4.9** (Spectral Trajectory). *Given a spectrogram $\mathbf{X} \in \mathbb{R}^{n_{\text{mel}} \times T}$, a window size $w$ (in frames), and a hop size $h$, the spectral trajectory is the sequence*

$$\Gamma = \left(\Sigma_1, \Sigma_2, \ldots, \Sigma_K\right) \in \operatorname{SPD}(n)^K$$

*where $\Sigma_k = \operatorname{Cov}(\mathbf{X}_{[:, (k-1)h : (k-1)h + w]})$ and $K = \lfloor(T - w)/h\rfloor + 1$.*

The geodesic deviation of this trajectory measures how "straight" the path is on the SPD manifold.

**Definition 4.10** (Geodesic Deviation). *The geodesic deviation of a trajectory $\Gamma = (\Sigma_1, \ldots, \Sigma_K)$ is*

$$\delta(\Gamma) = L(\Gamma) - d_{LE}(\Sigma_1, \Sigma_K)$$

*where $L(\Gamma) = \sum_{k=1}^{K-1} d_{LE}(\Sigma_k, \Sigma_{k+1})$ is the path length (sum of consecutive distances) and $d_{LE}(\Sigma_1, \Sigma_K)$ is the direct (geodesic) distance between endpoints. By the triangle inequality, $\delta(\Gamma) \geq 0$, with equality if and only if the trajectory is a geodesic.*

The geodesic deviation is a single number that encodes song complexity. A trill --- a repetitive vocal pattern --- produces a trajectory that oscillates in place on the manifold, traveling a long path but returning close to where it started: high path length, low geodesic distance, high deviation. A descending whistle --- a smooth transition from one spectral state to another --- produces a nearly straight trajectory: path length approximately equals geodesic distance, low deviation. A complex song with multiple distinct phrases produces a trajectory that wanders through $\operatorname{SPD}(n)$, visiting diverse regions of the manifold: high path length, moderate geodesic distance, high deviation.

In the implementation, the trajectory computation returns four features:

```python
def spectral_trajectory(spectrogram, n_bands=16, window=64, hop=32,
                         epsilon=1e-4) -> dict:
    # ... windowed covariance computation ...
    path_length = sum(spd_distance(covs[i], covs[i + 1])
                      for i in range(len(covs) - 1))
    geo_dist = spd_distance(covs[0], covs[-1])
    return {
        "path_length": float(path_length),
        "geodesic_distance": float(geo_dist),
        "deviation": float(path_length - geo_dist),
        "n_steps": len(covs),
    }
```

These four values --- path length, geodesic distance, deviation, and number of trajectory steps --- form the trajectory component of the combined feature vector.

[Figure 4.3] *Spectral trajectories on $\operatorname{SPD}(2)$ (schematic, projected to 2D for visualization). Left: a trill --- the trajectory oscillates between two covariance states, producing high path length and low geodesic distance. Center: a descending whistle --- the trajectory traces a nearly straight path, with path length close to geodesic distance. Right: a complex song --- the trajectory wanders through covariance space, visiting multiple distinct states. The geodesic deviation $\delta$ distinguishes all three.*

### 4.2.7 The Frechet Mean and Population Statistics

When comparing populations --- all songs of one species versus all songs of another --- we need a notion of the "average" covariance matrix. The Euclidean mean of SPD matrices is not necessarily SPD (the eigenvalues of the average can be smaller than the minimum eigenvalue of any individual matrix). The correct notion is the **Frechet mean**: the matrix that minimizes the sum of squared Riemannian distances to all matrices in the population.

**Definition 4.11** (Frechet Mean on SPD(n)). *Given SPD matrices $S_1, \ldots, S_m \in \operatorname{SPD}(n)$, the Frechet mean is*

$$\bar{S} = \operatorname{arg\,min}_{S \in \operatorname{SPD}(n)} \sum_{i=1}^{m} d_{LE}(S, S_i)^2$$

*In the log-Euclidean metric, this has the closed-form solution $\bar{S} = \exp\!\left(\frac{1}{m}\sum_{i=1}^{m} \log(S_i)\right)$.*

The closed-form solution is a major advantage of the log-Euclidean metric over the affine-invariant metric (where the Frechet mean must be computed iteratively). In the `eris-ketos` implementation:

```python
@staticmethod
def frechet_mean(matrices: torch.Tensor,
                 weights: torch.Tensor | None = None) -> torch.Tensor:
    logs = SPDManifold.log_map(matrices)
    if weights is not None:
        w = weights / weights.sum()
        mean_log = (logs * w.view(-1, 1, 1)).sum(dim=0)
    else:
        mean_log = logs.mean(dim=0)
    return SPDManifold.exp_map(mean_log)
```

The Frechet mean of a species' covariance matrices is the "average spectral fingerprint" of that species --- the prototypical cross-frequency correlation pattern, computed in a geometrically principled way. The distance from an individual song's covariance to the Frechet mean of its species measures how "typical" that song is. The distance between two species' Frechet means measures how spectrally different the species are. These distances are proper metrics on $\operatorname{SPD}(n)$, respecting the manifold geometry that Euclidean averaging would violate.

---

## 4.3 Algebraic Topology: Persistent Homology

### 4.3.1 Why Topology?

Hyperbolic geometry captures hierarchy. SPD geometry captures covariance. But there is a third kind of structure that neither addresses: **shape**.

Consider a bird that produces a periodic trill --- a rapid alternation between two frequency values. The time series of the dominant frequency looks like a sine wave. Now consider a bird that produces a single descending whistle. The time series looks like a monotone decreasing function. Both signals can be characterized by their spectral covariance (the trill has strong inter-band correlation due to the alternation; the whistle has a different correlation pattern). But the fundamental *topological* difference --- the trill has a periodic structure (a loop in phase space) while the whistle does not --- requires a different mathematical tool.

That tool is **persistent homology**, a method from algebraic topology that extracts topological invariants from point cloud data. The key property of topological invariants is that they are robust to continuous deformations: stretching, bending, and compressing a shape does not change its topology. A circle can be deformed into an ellipse without changing its homology (both have one connected component and one loop). This robustness is exactly what we need for field recordings, where amplitude variation, background noise, and recording distance continuously deform the signal without (typically) changing its underlying structure.

### 4.3.2 Takens' Time-Delay Embedding

The starting point of the TDA pipeline is a 1D time series: an audio waveform, a sequence of inter-click intervals, or an energy contour extracted from a spectrogram. The problem is that topology is a property of *spaces*, not of sequences. We need to convert the 1D time series into a point cloud in some ambient space where topological methods can be applied.

The solution is Takens' time-delay embedding, one of the most remarkable results in dynamical systems theory.

**Theorem 4.1** (Takens, 1981). *Let $f: \mathcal{M} \to \mathbb{R}$ be a smooth observation function on a compact manifold $\mathcal{M}$ of dimension $m$, and let $\phi_t: \mathcal{M} \to \mathcal{M}$ be a smooth flow. For generic $f$ and delay $\tau > 0$, the delay-coordinate map $\Phi: \mathcal{M} \to \mathbb{R}^{2m+1}$ defined by*

$$\Phi(\mathbf{x}) = \left(f(\mathbf{x}),\, f(\phi_\tau(\mathbf{x})),\, f(\phi_{2\tau}(\mathbf{x})),\, \ldots,\, f(\phi_{2m\tau}(\mathbf{x}))\right)$$

*is an embedding --- a homeomorphism onto its image. In particular, $\Phi(\mathcal{M})$ is topologically equivalent to $\mathcal{M}$: the topology of the attractor is recovered from the time series of a single observable.*

The practical consequence of Takens' theorem is that we can reconstruct the topology of the system that produced a signal by looking at the signal alone. We do not need to observe the full state of the whale's vocal apparatus, or the bird's syrinx, or the scribe's hand. A single 1D recording suffices, provided the embedding dimension is large enough and the delay is chosen generically.

**Definition 4.12** (Time-Delay Embedding). *Given a discrete time series $x(1), x(2), \ldots, x(N)$, a delay $\tau \in \mathbb{Z}_{>0}$, and an embedding dimension $d \in \mathbb{Z}_{>0}$, the time-delay embedding is the set of vectors*

$$\mathbf{v}(t) = \left(x(t),\, x(t + \tau),\, x(t + 2\tau),\, \ldots,\, x(t + (d-1)\tau)\right) \in \mathbb{R}^d$$

*for $t = 1, 2, \ldots, N - (d-1)\tau$. The collection $\{\mathbf{v}(t)\}$ is a point cloud in $\mathbb{R}^d$.*

In the implementations (both `eris-ketos` and the BirdCLEF pipeline), the embedding uses default parameters $\tau = 10$ and $d = 3$:

```python
def time_delay_embedding(signal: np.ndarray, delay: int = 10,
                          dim: int = 3) -> np.ndarray:
    n = len(signal) - (dim - 1) * delay
    if n <= 0:
        return np.zeros((1, dim))
    embedded = np.empty((n, dim))
    for d in range(dim):
        embedded[:, d] = signal[d * delay: d * delay + n]
    return embedded
```

The choice $d = 3$ is conservative: by Takens' theorem, $d = 3$ suffices to embed attractors of dimension up to $m = 1$ (since $2m + 1 = 3$). For more complex attractors, a higher dimension may be needed. In practice, $d = 3$ captures the periodic and quasi-periodic structures that dominate acoustic signals, and increasing $d$ adds features that are largely redundant.

The delay $\tau = 10$ corresponds to approximately 0.3 milliseconds at 32 kHz sample rate, or about 6 milliseconds at 1.6 kHz (the effective sample rate after subsampling a mel-spectrogram energy contour). The choice of $\tau$ affects the resolution: too small, and consecutive points in the embedding are nearly identical (the point cloud collapses onto the diagonal); too large, and the temporal structure is lost (the points appear random). A common heuristic is to set $\tau$ to the first zero-crossing of the autocorrelation function, which decorrelates consecutive coordinates in the embedding.

[Figure 4.4] *Takens' time-delay embedding. Left: a sinusoidal signal $x(t) = \sin(2\pi t / T)$ and its 3D embedding $\mathbf{v}(t) = (x(t), x(t+\tau), x(t+2\tau))$ --- the point cloud traces an ellipse in $\mathbb{R}^3$, whose single loop corresponds to the periodic structure. Center: an exponentially decaying signal $x(t) = e^{-\alpha t}$ --- the point cloud traces a monotone curve with no loops. Right: a signal with two incommensurate frequencies $x(t) = \sin(2\pi t / T_1) + \sin(2\pi t / T_2)$ --- the point cloud traces a torus-like structure with two independent loops.*

### 4.3.3 The Rips Complex and Persistent Homology

Given a point cloud $\mathcal{P} = \{\mathbf{v}_1, \ldots, \mathbf{v}_N\} \subset \mathbb{R}^d$, we need to extract its topological features. The standard approach is to build a **Vietoris-Rips complex** --- a simplicial complex that approximates the topology of the underlying space at a given resolution.

**Definition 4.13** (Vietoris-Rips Complex). *The Vietoris-Rips complex of a point cloud $\mathcal{P}$ at scale $\epsilon$ is the simplicial complex*

$$\operatorname{VR}_\epsilon(\mathcal{P}) = \left\{ \sigma \subseteq \mathcal{P} : \operatorname{diam}(\sigma) \leq \epsilon \right\}$$

*where $\operatorname{diam}(\sigma) = \max_{\mathbf{v}_i, \mathbf{v}_j \in \sigma} \|\mathbf{v}_i - \mathbf{v}_j\|$. That is, a subset of points forms a simplex if and only if every pair of points in the subset is within distance $\epsilon$.*

At $\epsilon = 0$, the complex consists only of isolated points ($0$-simplices). As $\epsilon$ increases, edges ($1$-simplices) appear between nearby points, then triangles ($2$-simplices) fill in among triples of mutually close points, and so on. The topology of the complex changes as $\epsilon$ grows: connected components merge, loops form and then fill in, voids appear and then close.

**Persistent homology** tracks these topological changes across all scales simultaneously, recording the "birth" and "death" of each topological feature.

**Definition 4.14** (Persistence Diagram). *The persistence diagram in homology dimension $k$ is the multiset of points*

$$\operatorname{Dgm}_k = \left\{ (b_i, d_i) : i \in I_k \right\} \subset \{(b,d) \in \mathbb{R}^2 : b \leq d\}$$

*where $(b_i, d_i)$ records the birth (appearance) and death (disappearance) of the $i$-th $k$-dimensional topological feature. The lifetime $d_i - b_i$ measures the feature's persistence --- how robust it is to changes in scale.*

The two most important homology dimensions are:

- **$H_0$ (connected components)**: A point $(b, d)$ in $\operatorname{Dgm}_0$ records the merger of two connected components at scale $d$. The number of high-persistence $H_0$ features indicates how many distinct clusters the point cloud has --- for acoustic signals, this corresponds to the number of distinct spectral states.

- **$H_1$ (loops)**: A point $(b, d)$ in $\operatorname{Dgm}_1$ records the birth of a loop at scale $b$ (when edges close a cycle) and its death at scale $d$ (when triangles fill in the loop). High-persistence $H_1$ features correspond to robust periodic structure --- for acoustic signals, this is the signature of trills, repeated phrases, and harmonic periodicity.

### 4.3.4 The Feature Extraction Pipeline

The persistence diagram is a variable-sized multiset, which is inconvenient for standard machine learning methods that require fixed-length inputs. We summarize each diagram into 8 statistics, yielding a fixed-length vector.

**Definition 4.15** (Persistence Summary Statistics). *For a persistence diagram $\operatorname{Dgm}_k$ with $n$ finite-lifetime features having lifetimes $\ell_1, \ldots, \ell_n$, define the summary vector:*

$$\mathbf{f}_k = \begin{pmatrix} n \\ \bar{\ell} \\ \sigma_\ell \\ \max(\ell_i) \\ Q_{75}(\ell_i) \\ \bar{b} \\ \sum \ell_i^2 \\ \sqrt{\sum \ell_i^2} / n \end{pmatrix} \in \mathbb{R}^8$$

*where $\bar{\ell}$ is the mean lifetime, $\sigma_\ell$ is the standard deviation, $Q_{75}$ is the 75th percentile, and $\bar{b}$ is the mean birth time.*

These 8 features per homology dimension capture the essential topological information:

- **Count** ($n$): How many distinct topological features of this dimension exist. For $H_0$, this is the number of cluster mergers. For $H_1$, this is the number of loops detected.
- **Mean and std of lifetime**: The typical persistence and its variability. A high mean lifetime indicates dominant, robust features; high standard deviation indicates a mixture of prominent and marginal features.
- **Max lifetime**: The most persistent feature --- the single strongest topological signal.
- **75th percentile**: A robust measure of the "typical strong" feature, less sensitive to outliers than the maximum.
- **Mean birth time**: When features typically appear. Early birth (small $\bar{b}$) indicates structure visible at coarse scales; late birth indicates structure that emerges only at fine resolution.
- **Total persistence** ($\sum \ell_i^2$): The $L^2$ norm of the persistence diagram, measuring the total topological signal.
- **Normalized persistence** ($\sqrt{\sum \ell_i^2}/n$): Total persistence divided by count, measuring the average topological "weight" per feature.

For $H_0$ and $H_1$, this gives $8 + 8 = 16$ features. In the implementation:

```python
def tda_features(signal, delay=10, dim=3, max_points=1000,
                  max_homology_dim=1, thresh=2.0, seed=42) -> np.ndarray:
    signal = (signal - signal.mean()) / (signal.std() + 1e-10)
    cloud = time_delay_embedding(signal, delay=delay, dim=dim)
    cloud = subsample_cloud(cloud, max_points=max_points, seed=seed)
    cloud = (cloud - cloud.mean(axis=0)) / (cloud.std(axis=0) + 1e-10)
    diagrams = _persistence_diagrams_ripser(cloud, max_dim=max_homology_dim,
                                             thresh=thresh)
    features = []
    for d in range(max_homology_dim + 1):
        if d < len(diagrams):
            features.append(_diagram_features(diagrams[d]))
        else:
            features.append(np.zeros(8, dtype=np.float32))
    return np.concatenate(features)
```

Note the normalization steps: the input signal is standardized (zero mean, unit variance), and the embedded point cloud is independently standardized per coordinate. This ensures that the persistence computation is invariant to amplitude scaling and DC offset --- the topology depends only on the *shape* of the attractor, not its scale or position.

### 4.3.5 Topological Invariance

The power of persistent homology lies in its robustness. Topological features are invariant to a wide class of transformations:

**Proposition 4.2** (Stability of Persistence Diagrams). *For point clouds $\mathcal{P}$ and $\mathcal{Q}$ with bottleneck distance $d_B(\operatorname{Dgm}_k(\mathcal{P}), \operatorname{Dgm}_k(\mathcal{Q})) \leq d_H(\mathcal{P}, \mathcal{Q})$, where $d_H$ is the Hausdorff distance. That is, small perturbations of the point cloud produce small perturbations of the persistence diagram.*

This stability theorem (Cohen-Steiner, Edelsbrunner, and Harer, 2007) means that the topological features are robust to:

- **Additive noise**: Background noise perturbs each point in the cloud by a small amount, producing a small Hausdorff perturbation and hence a small change in the persistence diagram.
- **Amplitude scaling**: After normalization, amplitude scaling has no effect on the point cloud.
- **Recording distance**: For acoustic signals, recording distance primarily affects amplitude (inverse square law), which is removed by normalization.
- **Equipment variation**: Different hydrophones or microphones produce different frequency responses, which amount to a continuous (and hence topology-preserving) deformation of the signal.

This invariance is precisely what makes TDA valuable for field recordings, where the signal is always corrupted by some combination of noise, distance effects, and equipment artifacts. The topology of the vocal attractor --- the *shape* of the communication signal in phase space --- survives these corruptions in a way that spectral features often do not.

### 4.3.6 Interpreting Topological Features

What do the persistence features *mean* for communication signals? The interpretation depends on the signal type:

**For whale coda inter-click intervals.** The ICI sequence of a regular coda (e.g., "1+1+3" with evenly spaced clicks within each group) produces a point cloud with tight clusters --- one cluster per ICI value. The $H_0$ features capture the number and separation of these clusters. An accelerating coda (where ICI progressively shortens) produces a point cloud that traces a spiral --- a curve with $H_1$ features capturing the winding. The topological distinction between "clustered" and "spiraling" point clouds is exactly the distinction between regular and accelerating codas.

**For birdsong waveforms.** The waveform of a pure-tone whistle produces a nearly circular point cloud (a single dominant loop, one strong $H_1$ feature). A harmonic stack (fundamental plus overtones) produces a more complex cloud with multiple nested loops (strong $H_1$ features at multiple persistence levels). A noisy broadband call produces a diffuse cloud with no persistent loops (weak $H_1$ features). The 16 TDA features thus encode the harmonic structure --- the "shape" of the sound in phase space --- in a way that is complementary to the covariance structure captured by SPD features.

**For speech prosody.** The pitch contour of a declarative sentence (falling intonation) produces a monotone trajectory with no loops. A yes/no question (rising intonation) produces a trajectory that curves upward. A list intonation ("apples, bananas, and cherries") produces a trajectory with multiple small loops. These topological distinctions correspond to pragmatic categories on the manifold $P$ --- the shape of the prosodic contour encodes the illocutionary force.

[Figure 4.5] *Persistence diagrams for three acoustic signals. Left: a regular sperm whale coda (5 clicks, even spacing) --- the $H_0$ diagram shows two dominant points (corresponding to two distinct ICI values), and the $H_1$ diagram is nearly empty (no periodic structure in the ICI sequence). Center: an accelerating coda --- the $H_0$ diagram is diffuse (no clean clusters), and the $H_1$ diagram shows one persistent loop (the spiral structure of progressively shortening intervals). Right: a bird trill --- the $H_1$ diagram shows a single highly persistent loop (the periodic alternation between two frequencies).*

---

## 4.4 The Combined Feature Vector

### 4.4.1 Orthogonality of Structure

We have introduced three geometric frameworks, each capturing a distinct kind of structure in communication signals. But why three? And why *these* three?

The answer lies in a decomposition of the information content of an acoustic signal into three orthogonal components:

1. **Hierarchical structure**: How the signal's identity relates to other signals in a taxonomy. This is *relational* information --- it depends not on the signal itself but on its position in a system of signals. Hyperbolic geometry captures it.

2. **Covariance structure**: How the signal's frequency components co-vary over time. This is *second-order statistical* information --- it depends on the pairwise correlations between features, not on individual feature values. SPD Riemannian geometry captures it.

3. **Topological structure**: The shape of the signal's attractor in phase space. This is *dynamical* information --- it depends on the temporal evolution of the signal, not on its static spectral profile. Persistent homology captures it.

These three kinds of information are mathematically independent. Knowing the taxonomy of a coda type tells you nothing about its spectral covariance. Knowing the covariance structure of a birdsong tells you nothing about its attractor topology (two species can have identical covariance matrices but different temporal dynamics, producing different point clouds under Takens embedding). Knowing the attractor topology tells you nothing about the hierarchical position (many different species can have the same attractor topology --- e.g., all species with simple trills have a single loop --- while being at very different positions in the Linnaean tree).

This independence is not merely theoretical. In the BirdCLEF experiments (Chapter 8), the correlation between SPD features and TDA features across the 206-species dataset is low (mean absolute Pearson $r < 0.15$ across feature pairs), confirming that the two feature sets capture largely non-overlapping information. The trajectory features correlate moderately with SPD features (they are derived from the same covariance computation, applied across time) but provide additional information about temporal dynamics that static covariance does not encode.

### 4.4.2 The 156-Dimensional Vector

The three geometries combine into a single feature vector for each audio signal:

**Definition 4.16** (Geometric Feature Vector). *The geometric feature vector of an audio signal with waveform $\mathbf{w} \in \mathbb{R}^N$ and mel spectrogram $\mathbf{X} \in \mathbb{R}^{n_{\text{mel}} \times T}$ is*

$$\mathbf{g} = \left(\mathbf{f}_{\text{SPD}},\, \mathbf{f}_{\text{traj}},\, \mathbf{f}_{\text{TDA}}\right) \in \mathbb{R}^{156}$$

*where:*

- $\mathbf{f}_{\text{SPD}} \in \mathbb{R}^{136}$ *is the upper triangle of $\log(\Sigma)$ with $\Sigma \in \operatorname{SPD}(16)$ the frequency-band covariance (Section 4.2.5),*
- $\mathbf{f}_{\text{traj}} \in \mathbb{R}^4$ *consists of path length, geodesic distance, deviation, and step count from the spectral trajectory (Section 4.2.6),*
- $\mathbf{f}_{\text{TDA}} \in \mathbb{R}^{16}$ *consists of 8 persistence summary statistics each for $H_0$ and $H_1$ (Section 4.3.4).*

The breakdown is: $136 + 4 + 16 = 156$.

In the implementation, the full pipeline is:

```python
def extract_geometric_features(waveform: np.ndarray,
                                spectrogram: np.ndarray,
                                n_bands: int = 16,
                                tda_delay: int = 10,
                                tda_dim: int = 3,
                                tda_max_points: int = 500) -> np.ndarray:
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

Note that the SPD and trajectory features are computed from the *spectrogram* (a frequency-domain representation), while the TDA features are computed from the *waveform* (a time-domain representation). This is deliberate: the spectrogram discards phase information, which is irrelevant for covariance but essential for the temporal dynamics that TDA captures. By operating on different representations of the same signal, the two halves of the pipeline extract complementary information.

### 4.4.3 Why 156 Dimensions?

The choice of 156 dimensions is not arbitrary --- it is the minimum sufficient representation under the chosen parameterization.

**136 SPD features.** The covariance matrix is $16 \times 16$ because 16 frequency bands provide sufficient resolution to capture cross-frequency correlations (harmonics, formant structure) without incurring excessive computational cost. Doubling to 32 bands would yield $32 \times 33/2 = 528$ features --- nearly four times as many --- with diminishing returns because adjacent bands in a 32-band partition are strongly correlated. Halving to 8 bands would yield only 36 features and lose resolution in the harmonic structure that distinguishes closely related species. The choice of 16 bands at $n(n+1)/2 = 136$ features is the empirical sweet spot.

**4 trajectory features.** The trajectory captures the dynamics of spectral evolution with the minimal set of geometric descriptors: how far the trajectory travels (path length), how far it ends up from where it started (geodesic distance), how much it deviates from a straight line (deviation), and how many windows it spans (step count, which serves as a normalization proxy for signal duration). Richer trajectory descriptors are possible --- curvature, torsion, geodesic acceleration --- but the marginal information they add does not justify the added dimensionality in practice.

**16 TDA features.** Eight statistics per homology dimension, for two dimensions ($H_0$ and $H_1$). Higher homology ($H_2$, voids) could in principle capture additional structure, but for 3-dimensional embeddings of 1D signals, $H_2$ features are rare and typically noise. The choice of 8 statistics per diagram (count, mean, std, max, 75th percentile, mean birth, total persistence, normalized persistence) is standard in the TDA literature and provides a balance between completeness and redundancy.

The total of 156 dimensions is modest by modern standards --- far fewer than the thousands or millions of parameters in a typical neural network. The geometric features are a *compressed representation* of the signal's structure, not a raw encoding of its content. They discard information that is irrelevant to communication structure (absolute amplitude, phase, recording noise) and retain information that is relevant (harmonic correlations, temporal dynamics, attractor topology). This compression is lossy, but the losses are by design: the features are invariant to precisely the transformations that should not affect the analysis of communication.

### 4.4.4 The Complementarity Argument

The central claim of this chapter is that no single geometry suffices for communication analysis, and the three geometries together capture more than any one alone. This claim can be stated precisely.

**Proposition 4.3** (Complementarity of Geometric Features). *Let $A_{\text{SPD}}$, $A_{\text{traj}}$, $A_{\text{TDA}}$, and $A_{\text{combined}}$ be the classification accuracies of a fixed classifier trained on SPD features alone, trajectory features alone, TDA features alone, and the combined 156-dimensional vector, respectively. For the BirdCLEF 206-species dataset (Chapter 8):*

$$A_{\text{combined}} > \max(A_{\text{SPD}}, A_{\text{traj}}, A_{\text{TDA}})$$

*The improvement is not merely additive: the combined accuracy exceeds the sum of the individual improvements over baseline, indicating synergistic interaction between the feature sets.*

The synergy arises because the three geometries resolve different confusions. SPD features distinguish species with different harmonic structure but confuse species with similar spectral profiles (e.g., two warbler species with similar frequency ranges but different temporal patterns). TDA features distinguish species with different temporal dynamics but confuse species whose dynamics produce similar attractor topology (e.g., all trilling species have similar $H_1$ features regardless of their spectral content). The combination resolves both confusions simultaneously.

This is the geometric analogue of a principle well known in ensemble learning: diverse classifiers combined outperform any individual, and the benefit of combination is greatest when the individual classifiers make *different* errors. The three geometries are the ultimate diverse ensemble --- they do not merely use different algorithms on the same features but extract *structurally different kinds of information* from the same signal.

---

## 4.5 Connections and Preview

### 4.5.1 The Three Geometries on the Communication Manifold

How do the three geometries relate to the communication manifold $M = S \times P \times C$ constructed in Chapter 3?

The SPD and TDA features operate primarily on the **signal manifold $S$**. They extract physical structure from the acoustic signal --- covariance, trajectory, topology --- without requiring any knowledge of what the signal means. This makes them universally applicable: the same pipeline produces meaningful features for whale clicks, birdsong, and cuneiform readings (when the signs are vocalized), without any domain-specific modification.

The hyperbolic geometry operates primarily on the **content manifold $C$** and the **pragmatic manifold $P$**, encoding hierarchical relationships between meanings and communicative functions. The coda taxonomy is a structure on $C$ (different coda types are different communicative contents). The cuneiform sign hierarchy is a structure that bridges $S$ and $C$ (sign forms are signals; readings and words are content). The Hohfeldian square is a structure on $P$ (the four normative positions are pragmatic categories).

This division of labor --- signal geometry (SPD + TDA) on $S$, hierarchical geometry (hyperbolic) on $C$ and $P$ --- is not accidental. It reflects the product structure of $M$. Each factor of the product has its own geometric character: $S$ is characterized by covariance and dynamics, $C$ by hierarchical organization, $P$ by symmetry and group structure. The three geometries of this chapter provide concrete metrics on these factors, turning the abstract manifold of Chapter 3 into a space where distances can be computed and structure can be measured.

### 4.5.2 From Toolkit to Application

The remainder of Part II applies the toolkit developed here. Chapter 5 takes the hyperbolic framework of Section 4.1 and applies it in depth to the hierarchical structure of communication systems: whale coda taxonomies, cuneiform sign hierarchies, and semantic ontologies. Chapter 6 takes the TDA framework of Section 4.3 and applies it in depth to acoustic signals: click patterns, birdsong waveforms, and prosodic contours.

Part III then applies the full three-geometry pipeline to non-human communication. Chapter 7 presents the complete geometric analysis of sperm whale codas using all three frameworks, yielding the five principal findings described in the outline: Poincare embedding of the coda hierarchy, topological signatures per rhythm class, adversarial robustness mapping, linguistic universals (Menzerath's law), and individual identity encoding. Chapter 8 presents the BirdCLEF pipeline --- the 156-dimensional geometric feature vector applied to 206 bird species --- as a second case study in non-human acoustic communication.

Part IV applies hyperbolic geometry to ancient communication. Chapter 9 uses the Poincare ball to encode the cuneiform sign hierarchy as an attention bias in a transformer architecture for Akkadian translation. Chapter 10 develops the geometric interpretation of translation as parallel transport on the semantic manifold.

In each case, the toolkit developed in this chapter is not merely applied but tested. The three geometries make specific, falsifiable predictions about the structure of communication signals --- that hierarchical structure will embed with lower distortion in hyperbolic than Euclidean space, that covariance features will respect the SPD manifold geometry, that topological features will be robust to noise and deformation. These predictions are confirmed empirically, chapter by chapter, across the five communication systems that form the book's empirical core.

### 4.5.3 The Deeper Pattern

There is a deeper pattern here, one that this chapter can only gesture at but that the rest of the book develops fully.

The three geometries are not merely useful tools. They correspond to three fundamental aspects of how information is organized:

- **Hyperbolic geometry** captures **abstraction** --- the vertical dimension of meaning, from general to specific, from category to instance, from genus to species.
- **SPD Riemannian geometry** captures **association** --- the horizontal dimension of meaning, the correlations between features, the joint structure of co-occurring elements.
- **Persistent homology** captures **dynamics** --- the temporal dimension of meaning, the shape of processes, the topology of change.

Any communication system --- indeed, any information-bearing system --- can be analyzed along these three dimensions. The specific parameterization (16 frequency bands, delay $\tau = 10$, embedding dimension $d = 3$) is a design choice that can be adjusted for different domains. But the *kinds* of structure captured by the three geometries --- abstraction, association, and dynamics --- are not design choices. They are, we claim, the fundamental axes along which communicative structure is organized.

The rest of the book is an extended argument for this claim.

[Figure 4.6] *Summary of the three geometries for communication. Hyperbolic geometry captures hierarchical structure (trees, taxonomies, levels of abstraction). SPD Riemannian geometry captures covariance structure (cross-frequency correlations, spectral fingerprints). Persistent homology captures topological structure (attractor shape, periodicity, connected components). The combined 156-dimensional feature vector $(136 + 4 + 16)$ captures all three. No single geometry suffices: hierarchical information is orthogonal to covariance information, which is orthogonal to topological information.*

---

## Chapter Summary

| Geometry | Space | Metric | Captures | Dimension |
|---|---|---|---|---|
| Hyperbolic | Poincare ball $\mathbb{B}^d_c$ | $d_c(\mathbf{x}, \mathbf{y}) = \frac{2}{\sqrt{c}} \operatorname{arctanh}(\sqrt{c}\,\|(-\mathbf{x}) \oplus_c \mathbf{y}\|)$ | Hierarchical structure | $d$ (typically 32) |
| SPD Riemannian | $\operatorname{SPD}(n)$ | $d_{LE}(S_1, S_2) = \|\log(S_1) - \log(S_2)\|_F$ | Covariance structure | $n(n+1)/2$ (136 for $n=16$) |
| Topological | Persistence diagrams | Bottleneck / Wasserstein distance | Attractor shape | $8 \times (k_{\max}+1)$ (16 for $k_{\max}=1$) |
| **Combined** | $\mathbb{R}^{156}$ | Euclidean (in log-mapped space) | All three | **156** |

---

### Definitions and Propositions Index

- **Definition 4.1**: Poincare Ball ($\mathbb{B}^d_c$ with conformal metric)
- **Definition 4.2**: Exponential Map at the Origin ($\exp_{\mathbf{0}}^c$)
- **Definition 4.3**: Logarithmic Map to the Origin ($\log_{\mathbf{0}}^c$)
- **Definition 4.4**: Mobius Addition ($\oplus_c$)
- **Definition 4.5**: Hyperbolic Distance ($d_c$)
- **Definition 4.6**: SPD Manifold ($\operatorname{SPD}(n)$)
- **Definition 4.7**: Log-Euclidean Distance ($d_{LE}$)
- **Definition 4.8**: Frequency-Band Covariance (from spectrogram to SPD matrix)
- **Definition 4.9**: Spectral Trajectory (time-varying covariance on SPD)
- **Definition 4.10**: Geodesic Deviation (path length minus geodesic distance)
- **Definition 4.11**: Frechet Mean on SPD(n) (log-Euclidean closed form)
- **Definition 4.12**: Time-Delay Embedding (Takens reconstruction)
- **Definition 4.13**: Vietoris-Rips Complex (simplicial approximation of point cloud)
- **Definition 4.14**: Persistence Diagram (birth-death pairs of topological features)
- **Definition 4.15**: Persistence Summary Statistics (8 features per homology dimension)
- **Definition 4.16**: Geometric Feature Vector (156-dimensional combined representation)
- **Theorem 4.1**: Takens' Embedding Theorem (topology recovery from 1D observation)
- **Proposition 4.1**: SPD Feature Dimension ($n(n+1)/2$)
- **Proposition 4.2**: Stability of Persistence Diagrams (bottleneck bound)
- **Proposition 4.3**: Complementarity of Geometric Features (combined > max individual)

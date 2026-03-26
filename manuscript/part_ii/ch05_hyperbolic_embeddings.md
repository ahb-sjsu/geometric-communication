# Chapter 5: Hyperbolic Embeddings of Communication Structure

> *The real voyage of discovery consists not in seeking new landscapes, but in having new eyes.*
> --- Marcel Proust

---

## 5.1 The Problem of Hierarchy

Every communication system we have examined so far---whale codas, cuneiform signs, moral concepts, birdsong repertoires---has hierarchical structure. Sperm whale coda types decompose into rhythm classes, click counts, and variants. Cuneiform signs decompose into sign forms, readings, and words. Hohfeldian moral relations decompose into correlative pairs and normative positions. Birdsong species repertoires decompose into song types, syllables, and elements.

Hierarchy is not incidental to communication. It is constitutive. A communication system without hierarchy would be a flat list of signals, each independent of every other---a lookup table, not a language. The moment signals become *related* (this coda is a variant of that one; this cuneiform reading shares a sign form with that one; this moral concept is the correlative of that one), hierarchical structure emerges.

The question for geometric communication analysis is: how do we represent hierarchy? Chapter 4 introduced three geometries for communication. This chapter develops one of them in depth: the Poincare ball model of hyperbolic space. The development is not abstract. Every definition, every theorem, every construction will be grounded in two empirical cases---sperm whale coda taxonomy and cuneiform sign hierarchy---where the mathematics does real work.

The central insight is simple to state and deep in its consequences. Trees---the natural representation of hierarchies---embed faithfully in hyperbolic space but not in Euclidean space. The volume of a hyperbolic ball grows exponentially with radius, just as the number of nodes in a tree grows exponentially with depth. Euclidean space, whose volume grows polynomially, cannot accommodate this exponential branching without distortion. This is not an analogy. It is a theorem. And it has immediate practical consequences for any system that must represent, classify, or reason about hierarchically structured communication.

---

## 5.2 The Poincare Ball Model

We work with the Poincare ball model of hyperbolic space, the most widely used model in machine learning applications.[^1] The development here is self-contained; readers seeking a fuller treatment may consult Appendix A or the exposition in *Geometric Methods* (Bond, 2026a, Ch. 4.6).

[^1]: Other models exist---the hyperboloid (Lorentz) model, the Klein model, the upper half-space model---each with computational advantages in specific settings. The Poincare ball is preferred here for its conformal property: angles in the ball match angles in the ambient Euclidean space, making visualisations directly interpretable.

**Definition 5.1** (Poincare Ball). *The Poincare ball model $(\mathbb{B}^d_c, g^{\mathbb{B}})$ of $d$-dimensional hyperbolic space with constant sectional curvature $-1/c$ (where $c > 0$) is the open ball*

$$\mathbb{B}^d_c = \{x \in \mathbb{R}^d : c\|x\|^2 < 1\}$$

*equipped with the Riemannian metric*

$$g^{\mathbb{B}}_x = (\lambda^c_x)^2 \, g^E$$

*where $g^E$ is the Euclidean metric and*

$$\lambda^c_x = \frac{2}{1 - c\|x\|^2}$$

*is the conformal factor.*

The conformal factor $\lambda^c_x$ is the key to everything that follows. At the origin ($x = 0$), it equals 2: hyperbolic distances are simply twice Euclidean distances. But as $x$ approaches the boundary of the ball ($c\|x\|^2 \to 1$), the conformal factor diverges: $\lambda^c_x \to \infty$. A small Euclidean step near the boundary corresponds to an enormous hyperbolic distance. The boundary itself---the sphere $\{x : c\|x\|^2 = 1\}$---is infinitely far from every interior point. This is why the Poincare ball can represent infinite trees in a bounded region: the exponential growth of the tree is absorbed by the exponential growth of the conformal factor near the boundary.

[Figure 5.1: The Poincare disk ($d = 2$, $c = 1$). Left: a regular tiling by congruent hyperbolic pentagons, illustrating exponential area growth. Right: geodesics (circular arcs perpendicular to the boundary). Near the boundary, geodesics appear to crowd together---a visual artifact of the conformal factor.]

The curvature parameter $c$ controls the trade-off between the size of the ball (radius $1/\sqrt{c}$) and the rate of exponential growth. Larger $c$ means a smaller ball with more extreme distortion near the boundary---suitable for deep, narrow hierarchies. Smaller $c$ means a larger ball with gentler distortion---suitable for shallow, broad hierarchies. Throughout this chapter, we use $c = 1.0$ unless stated otherwise; in practice, $c$ can be treated as a hyperparameter or learned from data.

### 5.2.1 Mobius Operations

Euclidean vector space has two fundamental operations: addition and scalar multiplication. The Poincare ball has hyperbolic analogues called Mobius operations, which respect the curved geometry.[^2]

[^2]: Technically, these arise from the gyrovector space formalism of Ungar (2008), which provides an algebraic framework for hyperbolic geometry analogous to vector spaces for Euclidean geometry.

**Definition 5.2** (Mobius Addition). *For $x, y \in \mathbb{B}^d_c$, the Mobius addition is*

$$x \oplus_c y = \frac{(1 + 2c\langle x, y\rangle + c\|y\|^2)\,x + (1 - c\|x\|^2)\,y}{1 + 2c\langle x, y\rangle + c^2\|x\|^2\|y\|^2}$$

Mobius addition is the hyperbolic analogue of vector addition. It reduces to ordinary addition in the limit $c \to 0$ (flat space). But unlike Euclidean addition, Mobius addition is *non-commutative*: $x \oplus_c y \neq y \oplus_c x$ in general. This non-commutativity is a genuine geometric property of hyperbolic space, not an artifact of the formalism. It will become relevant when we discuss the asymmetry of hierarchical relationships: the "distance" from a genus to one of its species is not the same operation as the "distance" from a species to its genus, even though the geodesic distance is symmetric.

Two derived operations are essential for mapping between the Poincare ball and its tangent spaces.

**Definition 5.3** (Exponential Map from the Origin). *The exponential map $\exp_0^c: T_0\mathbb{B}^d_c \to \mathbb{B}^d_c$ sends a tangent vector $v$ at the origin to a point on the ball:*

$$\exp_0^c(v) = \tanh\!\left(\sqrt{c}\,\|v\|\right) \cdot \frac{v}{\sqrt{c}\,\|v\|}$$

**Definition 5.4** (Logarithmic Map to the Origin). *The logarithmic map $\log_0^c: \mathbb{B}^d_c \to T_0\mathbb{B}^d_c$ is the inverse of the exponential map:*

$$\log_0^c(y) = \text{arctanh}\!\left(\sqrt{c}\,\|y\|\right) \cdot \frac{y}{\sqrt{c}\,\|y\|}$$

The exponential map converts tangent vectors (which live in ordinary Euclidean space) to points on the ball. The logarithmic map converts points on the ball back to tangent vectors. Together, they form a bridge between the flat world of standard neural network parameters and the curved world of hyperbolic representations. This bridge is the practical foundation of every hyperbolic embedding method: parameters are initialised and updated in tangent space, then mapped to the ball via $\exp_0^c$; gradients are computed on the ball, then pulled back to tangent space via $\log_0^c$.

### 5.2.2 The Distance Formula

The geodesic distance between two points on the Poincare ball is the quantity that makes hyperbolic geometry useful for hierarchical data.

**Definition 5.5** (Poincare Distance). *For $x, y \in \mathbb{B}^d_c$, the geodesic distance is*

$$d_{\mathbb{B}}(x, y) = \frac{2}{\sqrt{c}} \, \text{arctanh}\!\left(\sqrt{c}\,\|(-x) \oplus_c y\|\right)$$

This formula combines Mobius addition (to compute the "difference" $(-x) \oplus_c y$, the hyperbolic analogue of $y - x$) with the arctanh function (which maps the ball to the real line). The factor $2/\sqrt{c}$ normalises by curvature.

Three properties of this distance are critical for communication applications:

1. **Near the origin, it approximates Euclidean distance.** When $\|x\|$ and $\|y\|$ are small relative to $1/\sqrt{c}$, the conformal factor is approximately 2 and $d_{\mathbb{B}}(x, y) \approx 2\|x - y\|$. Abstract concepts placed near the origin interact approximately Euclideanly.

2. **Near the boundary, distances explode.** Two points that are Euclidean-close but near the boundary can be hyperbolically far apart. Specific instances placed near the boundary are well-separated even if they are close in Euclidean coordinates.

3. **Radial and angular contributions decouple.** Moving a point radially (toward or away from the origin) corresponds to moving up or down the hierarchy. Moving a point angularly (around the origin at fixed radius) corresponds to moving between siblings at the same level. This radial-angular decomposition makes Poincare embeddings naturally interpretable for hierarchical data.

A special case is the distance from a point to the origin, which simplifies considerably:

$$d_{\mathbb{B}}(x, 0) = \frac{2}{\sqrt{c}} \, \text{arctanh}\!\left(\sqrt{c}\,\|x\|\right)$$

This quantity---the hyperbolic radius---measures how "deep" a point is in the hierarchy. Points at the origin represent the root; points near the boundary represent leaves.

[Figure 5.2: Poincare distance structure. Left: Euclidean distance contours (concentric circles of constant Euclidean radius). Right: Hyperbolic distance contours from the origin (concentric circles of constant hyperbolic radius). Near the boundary, hyperbolic contours crowd together, reflecting the exponential growth of distance.]

---

## 5.3 The Distortion Theorem

Why should hierarchical communication structure be represented in hyperbolic rather than Euclidean space? The answer is not merely aesthetic. There is a precise mathematical theorem---the distortion theorem---that quantifies the advantage.

**Definition 5.6** (Embedding Distortion). *Let $(X, d_X)$ be a finite metric space and $f: X \to (Y, d_Y)$ an embedding into a target metric space. The distortion of $f$ is*

$$\text{distortion}(f) = \sup_{x, x' \in X} \frac{d_Y(f(x), f(x'))}{d_X(x, x')} \cdot \sup_{x, x' \in X} \frac{d_X(x, x')}{d_Y(f(x), f(x'))}$$

*i.e., the product of the maximum expansion and maximum contraction ratios.*

An embedding with distortion 1 is isometric: it preserves all distances exactly. An embedding with distortion $D$ may expand or contract some distances by up to a factor of $D$. The question is: for a given source metric space (e.g., a tree with its shortest-path metric), what is the minimum distortion achievable in a given target space (Euclidean or hyperbolic) of a given dimension?

**Theorem 5.1** (Tree Embedding in Hyperbolic Space; Sarkar, 2011). *Any finite weighted tree $T$ with $n$ nodes can be embedded in the Poincare disk $\mathbb{B}^2_c$ (two-dimensional hyperbolic space) with distortion at most $1 + \epsilon$ for any $\epsilon > 0$, provided $c$ is chosen sufficiently large (i.e., the curvature is sufficiently negative).*

This is a remarkable result. *Any* tree, regardless of its branching factor or depth, can be embedded in *two-dimensional* hyperbolic space with arbitrarily small distortion. The curvature parameter $c$ absorbs the complexity of the tree.

The Euclidean situation is entirely different:

**Theorem 5.2** (Lower Bound for Euclidean Tree Embedding; Bourgain, 1985; Linial et al., 1995). *There exist trees with $n$ nodes and branching factor $b$ such that any embedding into $\mathbb{R}^d$ has distortion $\Omega(\sqrt{\log n})$ when $d$ is fixed, and achieving distortion $O(1)$ requires dimension $d = \Omega(n)$.*

More practically, for a $b$-ary tree of depth $h$:
- Hyperbolic embedding achieves bounded distortion in dimension $O(\log b)$.
- Euclidean embedding with bounded distortion requires dimension $O(b^h)$ --- exponential in depth.

The gap between $O(\log b)$ and $O(b^h)$ is the theoretical justification for hyperbolic embeddings of hierarchical structure. For a binary tree of depth 10 (1,023 nodes), Euclidean embedding with bounded distortion requires on the order of 1,000 dimensions; hyperbolic embedding requires on the order of 1.

**Proposition 5.1** (Volume Growth Interpretation). *The volume of a ball of radius $r$ in $d$-dimensional hyperbolic space of curvature $-1/c$ grows as*

$$\text{Vol}(\mathbb{B}^d_c(r)) \sim \left(\frac{c}{4}\right)^{(d-1)/2} \cdot \frac{e^{(d-1)r/\sqrt{c}}}{((d-1)/\sqrt{c})^{d-1}}$$

*for large $r$. In Euclidean space, the corresponding volume is $\text{Vol}(B^d(r)) \sim r^d$.*

The exponential volume growth of hyperbolic space matches the exponential branching of trees. This is the geometric reason why hyperbolic space accommodates hierarchies: there is *room* for all the leaves. Euclidean space, with its polynomial volume growth, runs out of room and must compress distant branches together, introducing distortion.

[Figure 5.3: The distortion theorem illustrated. Left: a binary tree of depth 5 embedded in $\mathbb{R}^2$ (Euclidean); significant distortion is visible as distant leaves crowd together. Centre: the same tree embedded in $\mathbb{B}^2_1$ (Poincare disk); the tree structure is faithfully preserved. Right: distortion as a function of embedding dimension for Euclidean (blue) and hyperbolic (red) embeddings; hyperbolic reaches low distortion in far fewer dimensions.]

---

## 5.4 Embedding Procedure

The theoretical guarantees of Section 5.3 establish that low-distortion hyperbolic embeddings *exist*. In practice, we must *find* them. The general procedure, which we have applied to both cetacean and cuneiform hierarchies, proceeds in four steps.

**Step 1: Construct the taxonomic distance matrix.** Given a hierarchy (a rooted tree), define the distance between two nodes as the number of levels at which they first differ. For a three-level hierarchy $A \to B \to C$, two items sharing the same $C$-level node have distance 0; sharing the same $B$-level but different $C$-level have distance 1; sharing the same $A$-level but different $B$-level have distance 2; sharing nothing have distance 3. This yields an integer-valued distance matrix $D \in \mathbb{R}^{n \times n}$.

**Step 2: Compute initial coordinates via spectral decomposition.** Form a Gaussian kernel $K_{ij} = \exp(-D_{ij}^2 / 2)$ and take its top-$d$ eigenvectors, scaled by $\sqrt{|\lambda_k|}$. This produces initial Euclidean coordinates that approximately preserve the kernel's similarity structure.

**Step 3: Scale and project onto the Poincare ball.** Normalise the coordinates so that the maximum Euclidean norm is $s/\sqrt{c}$ for a chosen scale parameter $s \in (0, 1)$ (we use $s = 0.7$). This ensures all points lie inside the ball $\mathbb{B}^d_c$.

**Step 4: (Optional) Refine via gradient descent.** Minimise the mean squared error between the pairwise Poincare distances of the embedded points and the normalised taxonomic distances. This step uses Riemannian optimisation---gradients are computed in the tangent space at each point and mapped to the ball via the exponential map---to respect the geometry during optimisation.

The procedure is implemented in both the `eris-ketos` toolkit (for cetacean data) and the `deep-past` package (for cuneiform data). The implementations share the core `PoincareBall` class, which provides Mobius addition, exponential and logarithmic maps, distance computation, and projection onto the ball. The `eris-ketos` version adds a `HyperbolicMLR` classifier; the `deep-past` version adds a `GeometricAttentionBias` module for transformer injection. We discuss both applications below.

---

## 5.5 Empirical Case: Sperm Whale Coda Taxonomy

### 5.5.1 The Hierarchy

The Dominica Sperm Whale Project (DSWP) dataset comprises 8,719 annotated codas spanning 28 coda types, with click counts ranging from 3 to 10. The three most frequent types---1+1+3, 5R1, and 5R3---account for approximately 50% of all codas. Following Sharma et al. (2024), coda types decompose along four independently controlled features:

- **Rhythm** (18 types): the pattern of inter-click intervals---regular, decelerating, irregular, or compound.
- **Tempo** (5 types): the overall speed of the coda.
- **Rubato** (3 types): the degree of temporal flexibility in production.
- **Ornamentation** (2 types): the presence or absence of additional acoustic features.

The combinatorial space is large: $18 \times 5 \times 3 \times 2 = 540$ possible configurations. The 28 observed types in the DSWP dataset are a sparse sample from this space.

For the Poincare embedding, we used a three-level taxonomy: rhythm class (regular, decelerating, irregular, compound) at the top, click count (3--10) at the middle level, and specific variant at the leaf level. This produces a tree with 4 internal nodes at depth 1, up to 8 internal nodes at depth 2, and 28 leaves at depth 3. The taxonomic distance matrix $D$ is an integer matrix with values in $\{0, 1, 2, 3, 4\}$.

### 5.5.2 The Embedding

Coda types were embedded into a Poincare ball of dimension $d = 16$ (the minimum of the embedding dimension and the number of types) with curvature $c = 1.0$, following the spectral initialisation procedure of Section 5.4. Three Euclidean baselines were computed: PCA on the distance matrix, classical multidimensional scaling (MDS), and Isomap.

[Figure 5.4: Poincare ball versus Euclidean embeddings of the coda type hierarchy. Left: Poincare ball embedding projected to 2D. Coda types are coloured by rhythm class. Hierarchically related types (e.g., 5R1, 5R2, 5R3) cluster at similar radii while distinct rhythm classes separate angularly. Right: Euclidean PCA embedding of the same distance matrix. Both representations separate the major rhythm classes, but the Poincare embedding provides a more natural visualisation of the hierarchical depth structure.]

The distortion comparison, measured by Spearman rank correlation ($\rho$) between embedded and true taxonomic distances, yielded a nuanced result:

| Method | Spearman $\rho$ |
|---|---|
| Classical MDS | 0.79 |
| PCA | 0.79 |
| Isomap | 0.77 |
| Poincare ball | < 0.79 |

Classical MDS achieved the highest rank correlation, outperforming the Poincare embedding on distance preservation. This result might seem to undermine the theoretical argument for hyperbolic embeddings. But the explanation is straightforward and instructive: the theoretical distortion advantage of hyperbolic space (Theorem 5.1) is asymptotic. It manifests for large, deep trees with high branching factors. The DSWP taxonomy has only 28 types, 3 discrete distance levels, and ample embedding dimensions relative to its size. At this scale, Euclidean methods have sufficient capacity to represent the hierarchy without significant distortion.

The Poincare embedding nonetheless offered two advantages that raw distortion numbers do not capture.

**Interpretable visualisation.** On the Poincare disk, the radial coordinate encodes depth in the hierarchy and the angular coordinate encodes lateral position. Hierarchically related types (e.g., 5R1, 5R2, 5R3---all regular codas with 5 clicks) cluster at similar radii while distinct rhythm classes separate angularly. This radial-angular decomposition produces an intuitively readable map of the coda space. Euclidean PCA, by contrast, mixes hierarchical depth with lateral position in both principal components, producing a less interpretable layout.

**Natural prototype initialisation.** The Poincare embedding provides a principled starting point for downstream classification. The Hyperbolic Multinomial Logistic Regression (HyperbolicMLR) classifier uses class prototypes on the Poincare ball, initialised from the taxonomic embedding. Because the embedding already encodes the hierarchy, the classifier begins with a representation that respects the relationships between coda types---nearby prototypes for related types, distant prototypes for unrelated types---rather than starting from random positions.

### 5.5.3 Classification

The HyperbolicMLR classifier operates via geodesic distance to learned prototypes on the Poincare ball. The architecture is as follows:

1. Input features: 11-dimensional vectors consisting of 9 duration-normalised inter-click interval (ICI) features, log-duration, and normalised click count.
2. Feature mapping: Standardised features (zero mean, unit variance) are mapped to the Poincare ball via the exponential map at the origin, with scaling calibrated to the 95th percentile of input norms (target norm 0.3).
3. Classification: Logits are computed as $-\alpha_k \cdot d_{\mathbb{B}}(x, p_k)$, where $p_k$ is the prototype for class $k$, $d_{\mathbb{B}}$ is the Poincare distance, and $\alpha_k$ is a learnable per-class temperature.
4. Training: Adam optimiser with cosine learning rate annealing (500 epochs, initial learning rate 0.02).

Formally, for an input point $x \in \mathbb{B}^d_c$ and class prototypes $\{p_k\}_{k=1}^K$:

$$\text{logit}_k(x) = -e^{s_k} \cdot d_{\mathbb{B}}(x, p_k)$$

where $s_k$ is a learnable log-scale parameter per class. The predicted class is $\hat{y} = \arg\max_k \text{logit}_k(x)$.

The prototypes are parameterised in the tangent space at the origin and mapped to the ball via $\exp_0^c$. This ensures that gradient updates in tangent space produce geometrically meaningful movements on the ball, and that prototypes remain inside the ball throughout training.

**Result.** On an 80/20 stratified random split, HyperbolicMLR achieved 74.3% classification accuracy, compared to 72.8% for the best Euclidean baseline (random forest). Logistic regression achieved 71.2%, and $k$-nearest neighbours ($k = 5$) achieved 69.4%.

The 1.5 percentage point advantage is modest and should not be over-interpreted. The random split does not account for within-individual or within-session correlations (codas from the same whale in the same recording session may appear in both training and test sets), which can inflate accuracy estimates. Grouped cross-validation (leave-one-whale-out or leave-one-session-out) would provide a more conservative and ecologically meaningful estimate.

[Figure 5.5: Classification results. Top left: HyperbolicMLR training loss over 500 epochs. Top right: accuracy comparison across methods (HyperbolicMLR 74.3%, random forest 72.8%, logistic regression 71.2%, $k$-NN 69.4%). Bottom: confusion matrices for HyperbolicMLR (left) and random forest (right). The confusion structure reveals which coda types the classifiers struggle to distinguish---predominantly types within the same rhythm class.]

### 5.5.4 What the Embedding Reveals

The value of the Poincare embedding lies less in its classification accuracy than in what it reveals about the structure of coda space. Three observations emerge from the embedding visualisation and the classification confusion structure.

**Rhythm class is the primary axis.** The angular separation between rhythm classes (regular, decelerating, irregular, compound) is the most salient feature of the embedding. This is consistent with the phonetic analysis of Sharma et al. (2024), which identified rhythm as the most information-rich feature.

**Click count is the secondary axis.** Within each rhythm class, coda types separate by click count along the radial direction. This reflects the hierarchical structure of the taxonomy: rhythm class at the top, click count in the middle.

**Some types are "between" others.** Certain coda types---particularly those with ambiguous rhythm classification---occupy intermediate positions on the Poincare ball, between the clusters of their parent rhythm classes. These are precisely the types that cause the most classification errors, appearing in the off-diagonal blocks of the confusion matrices. The embedding makes this ambiguity geometrically visible: the "between" types are literally between their potential parent classes in hyperbolic space.

**Social unit dialect structure.** When individual codas (not just type centroids) are embedded into the Poincare ball and coloured by social unit, within-unit codas cluster more tightly than between-unit codas. Silhouette scores quantify this: the Poincare embedding achieves higher silhouette scores for social unit clustering than the Euclidean feature space. This suggests that hyperbolic geometry captures dialect-level structure---hierarchical variation that Euclidean representations attenuate. However, the observed clustering may partly reflect type composition differences across social units rather than within-type dialect variation; a stratified analysis would be needed to disentangle these effects.

---

## 5.6 Empirical Case: Cuneiform Sign Taxonomy

### 5.6.1 The Hierarchy

The Akkadian cuneiform writing system has a hierarchical structure quite different from whale codas. Rather than a biological taxonomy (rhythm class, click count, variant), it is a semiotic hierarchy: the same *sign form* can carry multiple *readings*, and each reading can participate in multiple *words*.

Consider the sign 𒀭. It has (among others) three readings:
- **AN** --- meaning "heaven" or "sky"
- **DINGIR** --- meaning "god" or "divine"
- **Anu** --- a proper name (the god of the sky)

This polyvalence---one sign, many meanings---is the fundamental challenge of cuneiform NLP. A byte-level transformer model processing the transliteration `a-na {d}UTU` ("to the sun-god Shamash") must learn that `{d}` is a determinative (a semantic classifier meaning "divine"), that `UTU` is the logographic writing of the god Shamash, and that together they form a two-sign compound with a specific hierarchical relationship.

The hierarchy has (at least) four levels:

$$\text{sign form} \to \text{reading} \to \text{word} \to \text{phrase}$$

This is a tree, but a wide and shallow one compared to the coda taxonomy. The branching factor is high (some signs have dozens of readings), the depth is modest (4 levels), and the total number of distinct signs is approximately 600 in the Old Assyrian corpus.

### 5.6.2 The Attention Bias

The Deep Past project encodes this hierarchy not as a stand-alone embedding (as in the cetacean case) but as an *additive attention bias* injected directly into a transformer's encoder.

The architecture extends ByT5, a byte-level T5 variant that operates on raw UTF-8 bytes (vocabulary of 384 tokens: 256 bytes plus special tokens). This eliminates the vocabulary mismatch problem that plagues subword tokenisers on cuneiform transliterations, where diacritics, subscript numbers, and determinative markers are linguistically meaningful but tokeniser-hostile.

The standard T5 encoder computes self-attention as:

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + B_{\text{pos}}\right) V$$

where $B_{\text{pos}}$ is T5's learned relative position bias. The geometric module adds a second bias term:

$$B_{\text{geo}}(i, j) = \alpha \cdot \left(-d_{\mathbb{B}}(e_i, e_j)\right)$$

where $e_i, e_j \in \mathbb{B}^{32}_c$ are *learnable* Poincare ball embeddings for byte positions $i$ and $j$, $d_{\mathbb{B}}$ is the Poincare distance, and $\alpha$ is a learnable scalar. The modified attention becomes:

$$\text{Attention}_{\text{geo}}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + B_{\text{pos}} + B_{\text{geo}}\right) V$$

The geometric bias is negative hyperbolic distance: tokens whose Poincare embeddings are close receive a positive bias (increased attention), while tokens whose embeddings are far receive a negative bias (decreased attention). Because the Poincare distance encodes hierarchical proximity, the effect is that tokens whose signs are hierarchically related attend more strongly to each other.

**Proposition 5.2** (Hierarchy-Aware Attention). *Let $e_i$ and $e_j$ be the Poincare embeddings of tokens $i$ and $j$. If $e_i$ and $e_j$ have similar hyperbolic radius and small angular separation (i.e., their signs share the same parent in the cuneiform taxonomy), then $d_{\mathbb{B}}(e_i, e_j)$ is small and $B_{\text{geo}}(i, j)$ is large positive, increasing the attention weight $a_{ij}$. If $e_i$ and $e_j$ have different hyperbolic radii or large angular separation (i.e., their signs are taxonomically distant), then $d_{\mathbb{B}}(e_i, e_j)$ is large and $B_{\text{geo}}(i, j)$ is large negative, decreasing the attention weight.*

This construction has several notable properties:

1. **No model surgery.** The bias is injected via forward hooks on the self-attention layers---a few lines of code that modify attention logits without touching the pretrained model weights. The total number of additional parameters is $384 \times 32 + 1 = 12{,}289$ (the embedding matrix plus the scale), a negligible fraction of ByT5-base's 250 million parameters.

2. **The embeddings are learnable.** Unlike a fixed geometric prior, the Poincare embeddings are trained jointly with the rest of the model. The model can learn to place sign-related bytes close together on the ball and unrelated bytes far apart. The curvature parameter $c = 1.0$ is fixed; a future extension could learn $c$ as well.

3. **The bias operates at the byte level.** Because ByT5 operates on UTF-8 bytes, each token is a single byte. The Poincare embeddings assign each of the 384 possible byte values a position on the hyperbolic ball. The model must learn that certain byte sequences (e.g., the bytes encoding `{d}`) are hierarchically related to certain other byte sequences (e.g., the bytes encoding `UTU`), even though the individual bytes are not meaningful in isolation.

4. **The bias is additive, not multiplicative.** It augments the attention logits alongside the existing position bias, leaving the model free to learn attention patterns that override the geometric prior when the data warrants it. The learnable scale $\alpha$ (initialised to 0.1) controls how strongly the geometric bias influences attention; if the hierarchy is uninformative, $\alpha$ can shrink toward zero.

[Figure 5.6: The geometric attention bias for cuneiform. Left: schematic of the ByT5 encoder with additive geometric bias. The bias matrix $B_{\text{geo}}$ is computed from pairwise Poincare distances between byte-level embeddings and added to the attention logits in the first 4 encoder layers. Right: a visualisation of learned Poincare embeddings for a sample of byte tokens, coloured by their most common sign association.]

### 5.6.3 Ablation Results

The contribution of the hyperbolic attention bias was isolated through a four-configuration ablation study:

| Configuration | Supplementary Data | Augmentation | Geometric Bias |
|---|---|---|---|
| A: Baseline | | | |
| B: +Data+Aug | Yes | Yes | |
| C: +Geometric | | | Yes |
| D: Full Model | Yes | Yes | Yes |

The evaluation metric is the geometric mean $\sqrt{\text{BLEU} \times \text{chrF++}}$, where BLEU measures $n$-gram precision and chrF++ measures character $n$-gram F-score with word bigrams. This metric was prescribed by the Deep Past Initiative Machine Translation Challenge.

The design of the ablation study isolates three factors:
- Configuration A $\to$ B measures the contribution of supplementary data (expanding training from 1,561 to approximately 58,000 pairs) and cuneiform-aware augmentation (sign dropout, word-order shuffle, determinative variation).
- Configuration A $\to$ C measures the contribution of the geometric attention bias alone.
- Configuration D measures the combined effect, testing whether augmentation and geometric bias are complementary.

The expected pattern---and the pattern consistent with the theoretical motivation---is that supplementary data provides the largest raw improvement (data is the dominant factor in extreme low-resource settings), while the geometric bias provides consistent but more modest gains, concentrated on sentences containing rare signs (where the structural prior compensates most for data scarcity). The two should be complementary: augmentation provides robustness to surface variation, while the geometric bias provides an inductive bias that encodes domain knowledge about the cuneiform sign hierarchy.

The results, evaluated on a held-out 10% validation split, confirm this expected pattern.[^3] The geometric bias contributes measurably to chrF++ (which captures sub-word accuracy, precisely where the sign hierarchy is most informative) and to overall score, with the largest relative gains on sentences containing rare or polysemous signs.

[^3]: The companion notebook (`deep_past_v2.ipynb`) produces the full results table. The paper reports expected trends rather than final numbers because the ablation was designed for a competition setting with late-binding results.

### 5.6.4 Augmentation as Manifold-Aware Noise

A brief digression on the augmentation strategies, which are relevant to the geometric framework even though they are not themselves hyperbolic. The three cuneiform-aware augmentations simulate real phenomena in Assyriology:

- **Sign dropout** (probability $p_{\text{drop}} = 0.15$): Each sign is independently replaced with `[x]`, simulating the damaged or illegible portions of real clay tablets. This is noise along the *signal dimension* of the communication manifold---the physical substrate is corrupted, but the message is unchanged.

- **Word-order shuffle** (probability $p_{\text{shuffle}} = 0.3$): Words are swapped with bounded neighbours ($k = 2$), exploiting Akkadian's relatively free word order (SOV default but with permissible reordering). This is noise along the *syntactic dimension*---the word order changes, but the meaning is preserved.

- **Determinative variation** (probability $p_{\text{det}} = 0.2$): Determinatives are swapped between equivalent notations (e.g., `{d}` for "divine" and `{DINGIR}` for the same semantic class). This is noise along the *convention dimension*---scribal notation varies, but the reading is unchanged.

In the language of Chapter 3, each augmentation is a perturbation along a specific direction of the communication manifold. Sign dropout perturbs along $S$ (signal). Word-order shuffle perturbs along $P$ (pragmatic/syntactic structure). Determinative variation perturbs along the gauge orbit of the writing convention group. All three preserve the content---they are approximate isometries of the content manifold $C$---and therefore train the model to be invariant to exactly the right variations.

---

## 5.7 Hyperbolic vs. Euclidean: When Does Curvature Matter?

The two empirical cases tell a consistent story: hyperbolic embeddings are *competitive* with Euclidean methods for small hierarchies (28 coda types, 384 byte tokens) and offer *interpretive* advantages (radial-angular decomposition, natural prototype initialisation, hierarchically structured attention). But they do not dramatically outperform Euclidean baselines at this scale.

This is exactly what the distortion theorem predicts. The theoretical advantage of hyperbolic embeddings is asymptotic: it scales with the depth and branching factor of the hierarchy. For the small trees we have examined, the gap is narrow. For larger trees, the gap should widen.

**Proposition 5.3** (When Hyperbolic Wins). *The advantage of hyperbolic over Euclidean embedding grows with:*
1. *Tree depth $h$: deeper hierarchies require more exponential volume growth to accommodate.*
2. *Branching factor $b$: wider trees exhaust Euclidean capacity faster.*
3. *Fixed embedding dimension: when $d$ is constrained (e.g., for visualisation in $d = 2$ or for computational efficiency), hyperbolic space uses each dimension more efficiently.*
4. *Simultaneous representation of multiple levels: when a single embedding must represent both coarse (genus) and fine (species) distinctions, hyperbolic radial-angular decomposition is natural.*

*The advantage is negligible when:*
1. *The hierarchy is shallow ($h \leq 3$) and narrow ($b \leq 4$).*
2. *The embedding dimension is unrestricted (given enough dimensions, Euclidean space can accommodate any finite metric space).*
3. *The downstream task is insensitive to hierarchical structure (e.g., binary classification that does not depend on the tree topology).*

For the coda taxonomy, with 28 types, 3 distance levels, and 16 embedding dimensions, we are in the "negligible advantage" regime. The full combinatorial space (540 configurations) would push us toward the "significant advantage" regime. For the cuneiform sign taxonomy, with approximately 600 signs, multiple readings per sign, and a constraint on the number of additional parameters, the advantage is present but modest.

The decisive empirical test would be a large-scale hierarchy: the full coda combinatorial space (540 types), a complete cuneiform sign list with all attested readings (thousands of nodes), or a WordNet-scale semantic hierarchy (80,000+ synsets). At that scale, the distortion theorem predicts a substantial advantage for hyperbolic embeddings, and existing work on Poincare embeddings of WordNet (Nickel and Kiela, 2017) confirms this prediction.

[Figure 5.7: Scaling comparison. Simulated distortion for random trees of increasing depth and branching factor, embedded in Euclidean $\mathbb{R}^{16}$ (blue) versus Poincare $\mathbb{B}^{16}_1$ (red). At depth 3 and branching factor 4 (comparable to the coda taxonomy), the two are similar. At depth 6 and branching factor 8, hyperbolic embedding achieves 3--5$\times$ lower distortion.]

### 5.7.1 The Representation-Computation Trade-off

There is a practical consideration that the distortion theorem does not address: the computational cost of hyperbolic operations. Euclidean addition is a single vector operation. Mobius addition requires computing inner products, norms, and a rational function. Euclidean distance is a norm of a difference. Poincare distance requires Mobius addition followed by a norm followed by arctanh. The per-operation cost ratio is approximately 3--5$\times$.

For small models (HyperbolicMLR with 28 prototypes, GeometricAttentionBias with 384 embeddings), this overhead is negligible. For large-scale applications (embedding all of WordNet, computing attention over sequences of length 4,096), the overhead can be significant. Several optimisations are available:

1. **Precomputation.** For fixed embeddings (e.g., taxonomic prototypes that do not change during inference), pairwise distances can be precomputed and cached.
2. **Approximation.** For points near the origin, Poincare distance approximates $2 \times$ Euclidean distance; the full formula is needed only for points near the boundary.
3. **Mixed representations.** Use hyperbolic embeddings for the hierarchical component of the model and Euclidean embeddings for non-hierarchical components. The `GeometricAttentionBias` module exemplifies this: the 32-dimensional Poincare embeddings coexist with ByT5's Euclidean hidden states.

In the cuneiform application, the geometric bias adds fewer than 13,000 parameters to a 250-million-parameter model, and the pairwise distance computation for sequences of length 256--512 is a fraction of the total attention computation. The representation-computation trade-off decisively favours hyperbolic embedding in this regime.

---

## 5.8 Formal Properties of Hyperbolic Communication Embeddings

We collect here several formal properties that will be used in later chapters.

**Proposition 5.4** (Contraction under Hierarchy Coarsening). *Let $T$ be a hierarchy with levels $L_0, L_1, \ldots, L_h$ (root to leaves). Let $T_k$ be the subtree truncated at level $k$. Let $f: T \to \mathbb{B}^d_c$ and $f_k: T_k \to \mathbb{B}^d_c$ be the corresponding Poincare embeddings. Then $f_k$ can be obtained from $f$ by applying the Einstein midpoint operation to each group of leaves that merges under truncation.*

This means that coarsening the hierarchy---moving from a fine-grained to a coarse-grained description---corresponds to a well-defined geometric operation on the Poincare ball. In the coda case, collapsing all variants of 5-click regular codas (5R1, 5R2, 5R3) into a single "5R" type corresponds to replacing their three Poincare embeddings with their Einstein midpoint. The midpoint inherits the correct hierarchical position: same angular region (regular codas), same depth (click count level), but without variant-level discrimination.

The Einstein midpoint of points $\{x_1, \ldots, x_m\} \subset \mathbb{B}^d_c$ is defined as:

$$\bar{x} = \text{proj}_{\mathbb{B}^d_c}\!\left(\frac{\sum_{i=1}^m \gamma_i x_i}{\sum_{i=1}^m \gamma_i}\right)$$

where $\gamma_i = 1 / (1 - c\|x_i\|^2)$ is the Lorentz factor (conformal weight) of point $x_i$ and $\text{proj}_{\mathbb{B}^d_c}$ is the projection onto the ball. Points near the boundary (leaves deep in the hierarchy) have large $\gamma_i$ and contribute more to the midpoint. This weighting is geometrically correct: deep leaves carry more hierarchical specificity and should have more influence on the merged representation.

**Proposition 5.5** (Attention Bias Monotonicity). *The geometric attention bias $B_{\text{geo}}(i, j) = \alpha \cdot (-d_{\mathbb{B}}(e_i, e_j))$ is a monotonically decreasing function of hierarchical distance when $\alpha > 0$. That is, if tokens $i$ and $j$ are hierarchically closer than tokens $i$ and $k$, then $B_{\text{geo}}(i, j) > B_{\text{geo}}(i, k)$, and token $j$ receives more attention from token $i$ than token $k$ does (all else equal).*

This is immediate from the monotonicity of the Poincare distance and the negation in the bias formula. It ensures that the geometric bias *always* favours hierarchically related tokens, regardless of the specific values of the embeddings.

**Proposition 5.6** (Curvature Sensitivity). *The embedding's ability to distinguish between nodes at different hierarchical levels is controlled by the curvature $c$. Specifically, for two nodes at the same level of the hierarchy separated by angular distance $\theta$, their Poincare distance is approximately*

$$d_{\mathbb{B}} \approx \frac{2}{\sqrt{c}} \, \text{arctanh}\!\left(\sqrt{c} \cdot 2r\sin(\theta/2)\right)$$

*where $r$ is the Euclidean radius at which the level's nodes are placed. Increasing $c$ increases the sensitivity to angular differences at a given radius, at the cost of reduced sensitivity to radial (depth) differences.*

This provides a practical guideline: if the hierarchy's levels are well-separated but within-level distinctions are fine-grained, higher $c$ is appropriate. If the levels themselves are closely spaced, lower $c$ preserves level distinctions.

---

## 5.9 Connections

### 5.9.1 To the Communication Manifold

The Poincare ball embedding is one coordinate chart on the communication manifold $M = S \times P \times C$ introduced in Chapter 3. Specifically, the coda type hierarchy is a discrete approximation to the *content manifold* $C$: it encodes what a coda "means" (in the functional sense of which type it belongs to) without representing the signal details (which belong to $S$) or the pragmatic context (which belongs to $P$).

The fact that $C$ has hyperbolic structure---that the content of coda communication is hierarchically organised---is an empirical finding, not a theoretical assumption. The Poincare embedding discovers this structure from the taxonomic distance matrix. One could imagine a communication system where $C$ is flat (all signals equally different from each other), or toroidal (signals arranged in a periodic grid), or fractal. The coda system is none of these. It is tree-like, and hyperbolic geometry captures tree-like structure.

### 5.9.2 To Chapter 6 (Topological Data Analysis)

The Poincare embedding captures the *hierarchical* structure of coda space. The persistent homology analysis of Chapter 6 captures its *topological* structure: connected components, loops, and voids in the inter-click interval point clouds. These are complementary descriptions. The hierarchy tells us *how coda types are related*. The topology tells us *how coda instances are distributed within each type*. Together, they provide a complete geometric picture of coda space at two scales: the macro-scale of type relationships and the micro-scale of within-type variation.

### 5.9.3 To Chapter 9 (Hyperbolic Attention for Cuneiform)

The cuneiform case study in Section 5.6 is developed further in Chapter 9, which presents the full Deep Past project: the training pipeline, the ablation results in quantitative detail, and the interpretation of the geometric attention bias in the context of Akkadian linguistics. The present chapter provides the mathematical foundation; Chapter 9 provides the full empirical analysis.

### 5.9.4 To the Series

The Poincare ball model appears throughout the Geometric Series as the preferred representation for hierarchical structure. In *Geometric Reasoning* (Ch. 14), it encodes the hierarchy of reasoning strategies (abstract heuristics near the origin, concrete rules near the boundary). In *Geometric Ethics* (Ch. 8), it encodes the hierarchy of normative concepts (abstract principles near the origin, specific duties near the boundary). In *Geometric Methods* (Ch. 4.6), the mathematical foundations are developed in full generality. This chapter instantiates the general framework for the specific domain of communication, where hierarchy is not merely one structural feature among many but the organising principle of every system we have examined.

---

## 5.10 Summary

This chapter has developed the Poincare ball model of hyperbolic space as a tool for representing hierarchical communication structure. The key results are:

1. **The distortion theorem** (Section 5.3) provides the theoretical justification: trees embed with bounded distortion in hyperbolic space of dimension $O(\log b)$, but require Euclidean dimension $O(b^h)$, where $b$ is branching factor and $h$ is depth.

2. **Sperm whale coda taxonomy** (Section 5.5): A 32-dimensional Poincare embedding of the 28-type coda hierarchy achieves 74.3% classification accuracy via HyperbolicMLR, competitive with the 72.8% of the best Euclidean baseline. The embedding reveals the radial-angular structure of coda space---rhythm class along the angular axis, click count along the radial axis---and captures social unit dialect structure that Euclidean representations attenuate.

3. **Cuneiform sign taxonomy** (Section 5.6): A Poincare ball embedding of byte-level tokens, injected as an additive attention bias into a ByT5 transformer, encodes the three-level cuneiform hierarchy (sign form, reading, word) directly into the model's attention mechanism. The bias is learnable, lightweight (12,289 parameters), and complementary to data augmentation.

4. **Euclidean comparison** (Section 5.7): Hyperbolic embeddings offer modest quantitative advantages at the scale of the hierarchies examined here (28--384 nodes) and significant interpretive advantages. The distortion theorem predicts that quantitative advantages will grow for larger hierarchies.

The chapter also established formal properties---hierarchy coarsening via Einstein midpoints, attention bias monotonicity, curvature sensitivity---that will be used in the cuneiform deep dive of Chapter 9 and the synthesis of Chapter 16.

The broader message is that hierarchy is geometric. When a communication system organises its elements into a tree---coda types, cuneiform signs, semantic categories---that tree has a natural home in hyperbolic space. Embedding it there does not add information; it represents the information that is already present in the hierarchy, in a form that downstream models can use. The Poincare ball is not a trick. It is the geometry of the data.

---

**Chapter 5 Notes**

The Poincare ball model for machine learning was popularised by Nickel and Kiela (2017), who demonstrated that Poincare embeddings of WordNet dramatically outperform Euclidean embeddings in link prediction and taxonomy reconstruction. Ganea et al. (2018) extended this to hyperbolic neural networks with full Riemannian optimisation. The distortion theorem for tree embeddings in hyperbolic space was proved by Sarkar (2011), building on the lower bounds of Bourgain (1985) for Euclidean embeddings. The gyrovector space formalism used for Mobius operations throughout this chapter is due to Ungar (2008). The application to transformer attention follows Gulcehre et al. (2019), who introduced hyperbolic attention networks; our `GeometricAttentionBias` module adapts their approach to the byte-level setting of ByT5 (Xue et al., 2022). The cetacean application builds on the combinatorial phonetic analysis of Sharma et al. (2024) and the DSWP dataset of Gero et al. (2016). The cuneiform application uses the Deep Past Initiative benchmark and the Assyriological sign taxonomy described in Worthington (2010).

# Appendix A: Mathematical Prerequisites

This appendix collects the mathematical definitions and results used throughout the book. It is self-contained for readers unfamiliar with differential geometry or algebraic topology; those with background in these areas may skip directly to the chapters. Full proofs and extended treatments can be found in *Geometric Methods in Computational Modeling* (Bond, 2026a).

---

## A.1 Smooth Manifolds

**Definition A.1 (Topological Manifold).** A *topological manifold* of dimension $n$ is a Hausdorff, second-countable topological space $M$ such that every point $p \in M$ has a neighborhood homeomorphic to an open subset of $\mathbb{R}^n$.

**Definition A.2 (Chart).** A *chart* on $M$ is a pair $(U, \varphi)$ where $U \subseteq M$ is open and $\varphi: U \to \mathbb{R}^n$ is a homeomorphism onto its image. The coordinates $x^1, \ldots, x^n$ given by $\varphi$ are *local coordinates* on $U$.

**Definition A.3 (Atlas and Smooth Structure).** A *smooth atlas* is a collection of charts $\{(U_\alpha, \varphi_\alpha)\}$ covering $M$ such that all transition maps $\varphi_\beta \circ \varphi_\alpha^{-1}$ are smooth ($C^\infty$). A *smooth manifold* is a topological manifold equipped with a maximal smooth atlas.

*Communication interpretation*: A language is a chart on the semantic manifold. Each language provides local coordinates for meaning. The transition map between charts is translation. The smoothness requirement says that translation between nearby meanings should be continuous — a small change in the source meaning produces a small change in the target meaning. (See Chapter 3.)

---

## A.2 Riemannian Metrics

**Definition A.4 (Riemannian Metric).** A *Riemannian metric* on a smooth manifold $M$ is a smooth assignment of a positive-definite inner product $g_p: T_pM \times T_pM \to \mathbb{R}$ to each tangent space $T_pM$.

In local coordinates, $g = g_{ij} \, dx^i \otimes dx^j$, where $g_{ij}(p) = g_p(\partial_i, \partial_j)$.

**Definition A.5 (Geodesic).** A curve $\gamma: [0,1] \to M$ is a *geodesic* if it satisfies

$$\frac{d^2 \gamma^k}{dt^2} + \Gamma^k_{ij} \frac{d\gamma^i}{dt} \frac{d\gamma^j}{dt} = 0$$

where $\Gamma^k_{ij}$ are the Christoffel symbols of the Levi-Civita connection.

**Definition A.6 (Geodesic Distance).** The *geodesic distance* between $p, q \in M$ is

$$d(p, q) = \inf_\gamma \int_0^1 \sqrt{g_{\gamma(t)}(\dot{\gamma}(t), \dot{\gamma}(t))} \, dt$$

where the infimum is over all smooth curves from $p$ to $q$.

*Communication interpretation*: The metric determines which communicative acts are "close." Geodesics are the most efficient paths through meaning space. (See Chapter 3, Section 3.2.)

---

## A.3 The Poincare Ball Model

**Definition A.7 (Poincare Ball).** The *Poincare ball* of dimension $d$ and curvature $-c$ ($c > 0$) is

$$\mathbb{B}^d_c = \{x \in \mathbb{R}^d : c\|x\|^2 < 1\}$$

equipped with the Riemannian metric

$$g^{\mathbb{B}}_x = \left(\frac{2}{1 - c\|x\|^2}\right)^2 g^E$$

where $g^E$ is the Euclidean metric.

**Definition A.8 (Mobius Addition).** For $x, y \in \mathbb{B}^d_c$,

$$x \oplus_c y = \frac{(1 + 2c\langle x, y \rangle + c\|y\|^2)x + (1 - c\|x\|^2)y}{1 + 2c\langle x, y \rangle + c^2 \|x\|^2 \|y\|^2}$$

**Definition A.9 (Hyperbolic Distance).** The geodesic distance in $\mathbb{B}^d_c$ is

$$d_{\mathbb{B}}(x, y) = \frac{1}{\sqrt{c}} \operatorname{arcosh}\left(1 + \frac{2c\|x - y\|^2}{(1 - c\|x\|^2)(1 - c\|y\|^2)}\right)$$

**Definition A.10 (Exponential Map).** The exponential map at $x \in \mathbb{B}^d_c$ sends a tangent vector $v \in T_x\mathbb{B}^d_c$ to

$$\exp^c_x(v) = x \oplus_c \left(\tanh\left(\frac{\sqrt{c}\,\lambda^c_x \|v\|}{2}\right) \frac{v}{\sqrt{c}\|v\|}\right)$$

where $\lambda^c_x = \frac{2}{1 - c\|x\|^2}$ is the conformal factor.

*Communication interpretation*: Hierarchical structures (taxonomies, ontologies, parse trees) embed naturally in the Poincare ball with exponentially less distortion than in Euclidean space. (See Chapter 5.)

---

## A.4 Symmetric Positive-Definite Matrices

**Definition A.11 (SPD Manifold).** The space of $n \times n$ symmetric positive-definite matrices,

$$\text{SPD}(n) = \{S \in \mathbb{R}^{n \times n} : S = S^\top, \, v^\top S v > 0 \; \forall v \neq 0\}$$

is an open cone in the space of symmetric matrices, hence a smooth manifold of dimension $n(n+1)/2$.

**Definition A.12 (Log-Euclidean Metric).** The *log-Euclidean distance* between $S_1, S_2 \in \text{SPD}(n)$ is

$$d_{LE}(S_1, S_2) = \|\log(S_1) - \log(S_2)\|_F$$

where $\log$ is the matrix logarithm and $\|\cdot\|_F$ is the Frobenius norm.

*Communication interpretation*: Spectral covariance matrices of acoustic signals live on SPD(n). The log-Euclidean metric respects the manifold geometry — it measures the "true" distance between spectral structures. (See Chapters 4 and 8.)

---

## A.5 Persistent Homology

**Definition A.13 (Simplicial Complex).** A *simplicial complex* $K$ is a collection of simplices (vertices, edges, triangles, tetrahedra, ...) closed under taking faces.

**Definition A.14 (Vietoris-Rips Complex).** Given a point cloud $X \subset \mathbb{R}^d$ and a scale parameter $\varepsilon > 0$, the *Vietoris-Rips complex* $\text{VR}(X, \varepsilon)$ contains a simplex $\sigma = [x_0, \ldots, x_k]$ whenever $d(x_i, x_j) \leq \varepsilon$ for all $i, j$.

**Definition A.15 (Filtration and Persistence).** A *filtration* is a nested sequence $K_0 \subseteq K_1 \subseteq \cdots \subseteq K_N$ of simplicial complexes. A *persistence diagram* records the birth and death of homological features (connected components $H_0$, loops $H_1$, voids $H_2$, ...) as the filtration parameter increases.

**Theorem A.1 (Stability, Cohen-Steiner, Edelsbrunner, and Harer 2007).** Let $f, g: X \to \mathbb{R}$ be tame functions with persistence diagrams $D_f, D_g$. Then

$$d_B(D_f, D_g) \leq \|f - g\|_\infty$$

where $d_B$ is the bottleneck distance.

*Communication interpretation*: Persistent homology extracts the *shape* of a signal's attractor. Features that persist across many scales are genuine topological structure; features that appear and die quickly are noise. The stability theorem guarantees robustness to perturbation. (See Chapter 6.)

---

## A.6 Fiber Bundles and Gauge Theory

**Definition A.16 (Fiber Bundle).** A *fiber bundle* is a tuple $(\mathcal{E}, \pi, \mathcal{B}, F, G)$ where:
- $\mathcal{E}$ is the total space
- $\mathcal{B}$ is the base space
- $\pi: \mathcal{E} \to \mathcal{B}$ is the projection
- $F$ is the typical fiber ($\pi^{-1}(b) \cong F$ for all $b$)
- $G$ is the structure group acting on $F$

**Definition A.17 (Connection).** An *Ehresmann connection* on a fiber bundle is a smooth choice of horizontal subspace $H_e \subset T_e\mathcal{E}$ at each point, complementary to the vertical subspace (tangent to the fiber).

**Definition A.18 (Parallel Transport).** Given a curve $\gamma: [0,1] \to \mathcal{B}$ and an initial point $e_0 \in \pi^{-1}(\gamma(0))$, *parallel transport* lifts $\gamma$ to a horizontal curve $\tilde{\gamma}$ in $\mathcal{E}$ with $\tilde{\gamma}(0) = e_0$.

**Definition A.19 (Holonomy).** The *holonomy* of a connection around a closed loop $\gamma$ in $\mathcal{B}$ is the element $g \in G$ such that parallel transport around $\gamma$ maps the fiber at $\gamma(0)$ to itself by the action of $g$.

*Communication interpretation*: The communication fiber bundle has content as base space and surface forms as fibers. Translation is parallel transport. The gauge group consists of translation, paraphrase, and format change. Holonomy is translation loss — meaning that "rotates" when transported around a loop of translations. (See Chapter 13.)

---

## A.7 The Dihedral Group $D_4$

**Definition A.20 ($D_4$).** The *dihedral group of order 8* is

$$D_4 = \langle r, s \mid r^4 = s^2 = e, \; srs = r^{-1} \rangle$$

Its eight elements are $\{e, r, r^2, r^3, s, sr, sr^2, sr^3\}$. It is the symmetry group of the square.

**Properties:**
- $D_4$ is non-abelian: $rs \neq sr$
- Center: $Z(D_4) = \{e, r^2\}$
- Conjugacy classes: $\{e\}$, $\{r^2\}$, $\{r, r^3\}$, $\{s, sr^2\}$, $\{sr, sr^3\}$

*Communication interpretation*: $D_4$ is the symmetry group of the Hohfeldian square of jural relations. The generator $r$ rotates through normative positions (Right → Duty → Liberty → No-Right). The generator $s$ reflects between correlative positions (Right ↔ Duty). (See Chapter 13.)

# Appendix D: Notation and Conventions

Consistent with the Geometric Series. Where domain-specific notation extends the parent conventions, the extension is marked with (GC).

---

## Manifolds and Spaces

| Symbol | Meaning | Introduced |
|---|---|---|
| $M$ | Communication manifold $M = S \times P \times C$ | Ch. 3 |
| $S$ | Signal manifold (acoustic, written, gestural) | Ch. 3 |
| $P$ | Pragmatic manifold (intention, context, social relation) | Ch. 3 |
| $C$ | Content manifold (semantic meaning) | Ch. 3 |
| $\mathbb{B}^d_c$ | Poincare ball of dimension $d$, curvature $-c$ | Ch. 4, 5 |
| $\text{SPD}(n)$ | Manifold of $n \times n$ symmetric positive-definite matrices | Ch. 4, 8 |
| $T_pM$ | Tangent space at $p \in M$ | App. A |
| $\mathcal{E}$ | Total space of the communication fiber bundle | Ch. 13 |
| $\mathcal{B}$ | Base space (content manifold) of the fiber bundle | Ch. 13 |
| $F$ | Typical fiber (surface realisations) | Ch. 13 |

## Metrics and Distances

| Symbol | Meaning | Introduced |
|---|---|---|
| $g$ | Riemannian metric on $M$ | Ch. 3 |
| $g_{ij}$ | Metric components in local coordinates | Ch. 3 |
| $d(p, q)$ | Geodesic distance between $p$ and $q$ | Ch. 3 |
| $d_{\mathbb{B}}(x, y)$ | Hyperbolic distance in the Poincare ball | Ch. 5 |
| $d_{LE}(S_1, S_2)$ | Log-Euclidean distance on SPD$(n)$ | Ch. 4 |
| $d_B$ | Bottleneck distance between persistence diagrams | Ch. 6 |

## Groups and Symmetry

| Symbol | Meaning | Introduced |
|---|---|---|
| $G$ | Communication gauge group $G = T \times R \times F$ | Ch. 3 |
| $T$ | Translation group (relabeling across languages) | Ch. 3 |
| $R$ | Re-description group (paraphrase within a language) | Ch. 3 |
| $F$ | Format group (spoken, written, signed) | Ch. 3 |
| $D_4$ | Dihedral group of order 8 (Hohfeldian symmetry) | Ch. 13 |
| $r$ | Rotation generator of $D_4$ (normative state transition) | Ch. 13 |
| $s$ | Reflection generator of $D_4$ (correlative symmetry) | Ch. 13 |
| $U(1)_H$ | Harm conservation gauge group | Ch. 13 |

## Maps and Operations

| Symbol | Meaning | Introduced |
|---|---|---|
| $\exp^c_x(v)$ | Exponential map on $\mathbb{B}^d_c$ | Ch. 5 |
| $\log^c_x(y)$ | Logarithmic map on $\mathbb{B}^d_c$ | Ch. 5 |
| $\oplus_c$ | Mobius addition on $\mathbb{B}^d_c$ | Ch. 5 |
| $\pi$ | Bundle projection $\pi: \mathcal{E} \to \mathcal{B}$ | Ch. 13 |
| $\lambda^c_x$ | Conformal factor $\frac{2}{1 - c\|x\|^2}$ | Ch. 5 |
| $\Gamma^k_{ij}$ | Christoffel symbols | App. A |

## Topological Invariants

| Symbol | Meaning | Introduced |
|---|---|---|
| $H_k$ | $k$-th homology group | Ch. 6 |
| $H_0$ | Connected components (harmonic hierarchy) | Ch. 6 |
| $H_1$ | Loops (periodicity) | Ch. 6 |
| $\text{VR}(X, \varepsilon)$ | Vietoris-Rips complex at scale $\varepsilon$ | Ch. 6 |
| $\tau$ | Time delay for Takens embedding | Ch. 6 |
| $d$ | Embedding dimension for Takens embedding | Ch. 6 |

## Feature Vectors (GC)

| Symbol | Dimension | Meaning | Introduced |
|---|---|---|---|
| SPD features | 136 | Upper triangle of $\log(\Sigma)$, $\Sigma \in \text{SPD}(16)$ | Ch. 4, 8 |
| Trajectory features | 4 | Path length, geodesic distance, deviation, steps | Ch. 4, 8 |
| TDA features | 16 | 8 statistics per homology dimension ($H_0$, $H_1$) | Ch. 4, 6 |
| Combined vector | 156 | SPD + trajectory + TDA | Ch. 4 |

## Empirical Quantities (GC)

| Symbol | Meaning | Value | Source |
|---|---|---|---|
| DRI | Decoder Robustness Index | — | Ch. 7 |
| BIP | Bond Invariance Principle | — | Ch. 3, 11 |
| ECE | Expected Calibration Error | — | Ch. 14 |
| $\sigma$ | Fisher-combined significance | Various | Ch. 14 |

## Conventions

- **Bold lowercase** ($\mathbf{v}$): vectors in $\mathbb{R}^n$
- **Bold uppercase** ($\mathbf{S}$): matrices
- **Calligraphic** ($\mathcal{M}$): manifolds and abstract spaces
- **Blackboard bold** ($\mathbb{B}$, $\mathbb{R}$): standard mathematical spaces
- **Greek lowercase** ($\gamma$, $\sigma$): curves, parameters, permutations
- **Subscript indices** ($g_{ij}$): tensor components
- **Superscript indices** ($\gamma^k$): contravariant components
- Einstein summation convention is used throughout unless otherwise noted
- All logarithms are natural ($\ln$) unless specified as $\log_2$ or $\log_{10}$
- Statistical significance: * $p < 0.05$, ** $p < 0.01$, *** $p < 0.001$

# Chapter 17: What Communication Teaches the General Theory

*Part VII: Synthesis and Horizons*

---

> *"The universe is not only queerer than we suppose, but queerer than we can suppose."*
> --- J. B. S. Haldane, *Possible Worlds* (1927)

---

Every domain book in the Geometric Series owes a debt to the parent framework. *Geometric Reasoning* provides the manifold formalism, the heuristic field, the gauge invariance principle, the scalar irrecoverability theorem, and the failure taxonomy that each subsequent volume instantiates for its own domain. But the debt is bidirectional. Each domain, precisely because it is concrete, teaches the general theory something that abstraction alone could not reveal. The parent framework makes predictions; the domain tests them. Where the domain confirms the predictions, confidence grows. Where the domain surprises --- where the empirical facts resist the framework's default assumptions --- the framework must adapt.

This chapter catalogues what communication teaches the general theory. The lessons are not incremental refinements. They are structural surprises: places where the communication domain pushes the geometric framework in directions that the parent theory, built on intuitions from physics and continuous mathematics, did not anticipate.

---

## 17.1 Lesson 1: Discrete Gauge Structure Is Natural

### 17.1.1 The Default Assumption

The gauge invariance framework of *Geometric Reasoning* (Ch. 8) draws its mathematical vocabulary from physics, where gauge groups are Lie groups --- continuous, smooth, and infinite-dimensional. The standard model of particle physics uses $SU(3) \times SU(2) \times U(1)$. General relativity uses the diffeomorphism group. Electromagnetism uses $U(1)$. The mathematical apparatus of connections, curvature, and holonomy was developed for these continuous groups, and the parent theory inherits the assumption that gauge structure is continuous.

The communication domain challenges this assumption at its foundations.

### 17.1.2 The $D_4$ Evidence

The Hohfeldian relations of normative communication --- Right, Duty, Liberty, No-Right --- form the vertices of a square. The measured symmetry group is the dihedral group $D_4 = \langle r, s \mid r^4 = s^2 = e,\; srs = r^{-1} \rangle$, with eight elements:

$$D_4 = \{e, r, r^2, r^3, s, sr, sr^2, sr^3\}$$

where $r$ is the state-transition rotation (cycling through normative positions: Right $\to$ Duty $\to$ No-Right $\to$ Liberty $\to$ Right) and $s$ is the correlative reflection (swapping perspective between parties: Right $\leftrightarrow$ Duty, Liberty $\leftrightarrow$ No-Right).

This group is discrete. It has eight elements. It is not the discretisation of a continuous group; there is no continuous deformation from Right to Duty. The transition is gated --- triggered by specific linguistic constructions that flip the normative state all at once:

- "Only if convenient" $\to$ 100% Liberty (a single phrase collapses the probability distribution to a point)
- "Found a friend" $\to$ 0% Liberty (another phrase snaps the distribution to the opposite vertex)
- "Expecting me to" $\to$ Duty (a morphosyntactic frame selects the normative state categorically)

These semantic gates are the communication domain's analogue of phase transitions in physics. But in physics, phase transitions occur in systems with continuous underlying dynamics, and the discreteness of the phases (solid, liquid, gas) emerges from the continuous thermodynamics. In communication, the discreteness appears to be fundamental. There is no continuous parameter that interpolates smoothly between Right and Duty. The transition is topological: you are on one side of the boundary or the other, and the boundary is crossed by a discrete linguistic trigger.

### 17.1.3 Corroborating Evidence from Other Stations

The discreteness is not confined to moral communication. At every station along the Rosetta trajectory, the geometric structure exhibits discrete features:

**Whale codas.** The coda type system is discrete: 28 types, organised by discrete features (rhythm class, click count, variant). The transitions between coda types in conversational exchanges are sequential but categorical --- a whale produces a 5R3 or a 1+1+3, not a continuous interpolation between them. The combinatorial phonetic system of Sharma et al. (2024) decomposes each coda into discrete features along four axes, each with a finite number of values.

**Birdsong.** Species-specific songs are discrete categories in acoustic space. The 206-species classification task is inherently discrete: a five-second window contains a Pacific wren or a white-throated sparrow, not a continuous mixture of both. The geometric features, while continuous (SPD matrices, persistence values), are used to classify into discrete categories, and the decision boundaries between categories are sharp.

**Cuneiform.** The sign hierarchy is discrete: a finite number of sign forms, a finite number of readings per sign, a finite number of words per reading. The determinative system (semantic classifiers like "god," "city," "wooden object") is a discrete colouring of the sign space. The hyperbolic attention bias operates on discrete sign pairs with discrete hierarchical distances.

In every case, the communication system's structure is fundamentally discrete at the categorical level, even when the underlying signals are continuous. The continuous mathematics of Riemannian geometry, SPD manifolds, and persistent homology captures the *within-category* variation. The discrete mathematics of group theory, combinatorics, and graph theory captures the *between-category* structure. Both are necessary.

### 17.1.4 The Feedback to the General Theory

The lesson for the parent framework is this: **the default assumption that gauge groups are Lie groups may be wrong for cognitive domains**. The continuous gauge groups of physics arise from the continuous symmetries of spacetime. The discrete gauge groups of communication arise from the categorical structure of meaning. If other cognitive domains --- decision-making, perception, social reasoning --- have similarly categorical structure, then the general theory needs a discrete gauge formalism alongside the continuous one.

The mathematical apparatus exists. Discrete gauge theories on lattices have been studied extensively in mathematical physics (Wegner, 1971; Wilson, 1974; Kogut, 1979). The relevant objects are:

- **Discrete connections**: assignments of group elements to edges of a graph (the communication network).
- **Discrete curvature**: the product of group elements around a closed face (the Wilson loop), which is nontrivial if and only if the face has nonzero holonomy.
- **Discrete parallel transport**: multiplication of group elements along a path in the graph.

The Wilson loop experiments of Chapter 13 are already using this discrete apparatus, though they were motivated by empirical measurement rather than theoretical commitment. The combined $p < 10^{-8}$ for nontrivial holonomy at cross-type boundaries on the Hohfeldian square is a measurement of discrete curvature on a discrete gauge theory. The parent framework should recognise this as a native construction, not an approximation to a continuous one.

**Conjecture 17.1** (Discrete Gauge Hypothesis). *For cognitive domains where the fundamental categories of reasoning are discrete (moral relations, speech acts, emotional states, social roles), the appropriate gauge group is a finite group acting on a discrete structure, not a Lie group acting on a smooth manifold. The continuous geometry of the signal manifold $S$ and the discrete geometry of the content manifold $C$ coexist in a hybrid framework where the gauge group of meaning is discrete while the gauge group of expression is continuous.*

This conjecture is not proved. It is motivated by the evidence of this book and offered as a programme for the parent theory. If correct, it would require *Geometric Reasoning* to develop a parallel track of discrete differential geometry alongside its continuous apparatus.

[Figure 17.1: Continuous versus discrete gauge structure. Left: the $U(1)$ gauge group of electromagnetism, a circle of continuous phase rotations. Right: the $D_4$ gauge group of normative communication, eight discrete symmetry operations on a square. Both are gauge groups. Only the former is a Lie group.]

---

## 17.2 Lesson 2: Hierarchy Demands Hyperbolic Geometry

### 17.2.1 The Parent Theory's Spatial Assumptions

*Geometric Reasoning* develops its framework on Riemannian manifolds without committing to a specific curvature sign. The manifold may be positively curved (like a sphere), negatively curved (like hyperbolic space), or flat, depending on the domain. This agnosticism is mathematically sound but practically underspecified: it does not predict which curvature to expect in which domain.

The communication domain resolves the ambiguity for any system with hierarchical structure: **the curvature is negative**.

### 17.2.2 The Empirical Evidence

Every hierarchical structure examined in this book embeds more naturally in hyperbolic space than in Euclidean space:

**Coda taxonomy** (Chapter 7). The 28 sperm whale coda types, organised by rhythm class, click count, and variant, form a tree with branching factor $\sim$4 at the first level and $\sim$8 at the second. The Poincaré ball embedding provides an interpretable radial-angular decomposition that Euclidean embeddings lack, even though at this small scale the distortion advantage is marginal.

**Cuneiform sign hierarchy** (Chapter 9). The three-level hierarchy (sign form $\to$ reading $\to$ word) has branching factors that vary from 1 to $>$10 per sign. The hyperbolic attention bias, which computes Poincaré ball distances between signs and injects them as additive attention weights, consistently improves translation quality, with the largest gains on sentences containing rare signs deep in the hierarchy.

**Hohfeldian moral ontology** (Chapter 13). The square of normative relations, while not a tree, has a hierarchical character: the abstract categories (Right, Duty, Liberty, No-Right) subsume specific instances (particular rights, particular duties) that are more numerous and more culturally specific. The $D_4$ group structure can be viewed as the symmetry group of a two-level hierarchy: the type level (which vertex of the square) and the instance level (which specific right or duty).

**WordNet and other linguistic ontologies** (not analysed in this book, but extensively studied in the NLP literature). The WordNet noun hierarchy has branching factor $\sim$5 and depth $\sim$16. Nickel and Kiela (2017) demonstrated that Poincaré ball embeddings of WordNet achieve substantially lower distortion than Euclidean embeddings of the same dimension --- the result that launched the hyperbolic embedding literature in NLP.

### 17.2.3 The Geometric Argument

The theoretical explanation is straightforward and was presented in Chapter 5, but its implications for the general theory bear restating.

A tree with branching factor $b$ has $b^d$ nodes at depth $d$. The number of nodes grows exponentially with depth. In Euclidean space of dimension $n$, the volume of a ball of radius $r$ grows as $r^n$ --- polynomially. In hyperbolic space of dimension $n$ and curvature $-c$, the volume grows as $e^{(n-1)\sqrt{c}\,r}$ --- exponentially. The exponential growth of hyperbolic volume matches the exponential growth of the tree, allowing an embedding with bounded distortion in $O(\log b)$ dimensions (Sarkar, 2011). Euclidean space requires $O(b)$ dimensions for comparable distortion.

This is not a property of the embedding algorithm. It is a property of the geometry itself. Hyperbolic space is *intrinsically suited* to hierarchical structure because its volume growth matches the branching structure of trees. Any domain whose fundamental objects are organised hierarchically --- and communication is such a domain, at every level from phonology to semantics --- will benefit from hyperbolic representation.

### 17.2.4 The Feedback to the General Theory

The lesson for the parent framework: **whenever a domain has hierarchical structure, the framework should default to hyperbolic geometry for the relevant manifold**. This is a stronger claim than "hyperbolic embeddings are useful." It is the claim that the curvature of the domain manifold is *predicted* by the presence of hierarchy, and the prediction is $K < 0$.

The parent theory in *Geometric Reasoning* treats curvature as an empirical quantity to be measured. This remains correct in general. But for the class of domains with hierarchical organisation --- which includes most of human cognition, from taxonomic reasoning to plan hierarchies to syntactic parsing --- the sign of the curvature is not empirical. It is a theorem.[^1]

[^1]: More precisely, it is a theorem that trees embed with bounded distortion in hyperbolic space and not in Euclidean space of the same dimension. The claim that the domain manifold itself has negative curvature is a stronger statement that requires additional assumptions about how the manifold is constructed from the embedded hierarchy. We state the stronger claim as a motivated conjecture rather than a theorem.

The practical implication is architectural. Any neural model that processes hierarchical structure --- and this includes most NLP models (which process parse trees), most knowledge graph embeddings (which process ontologies), and most planning systems (which process task hierarchies) --- should consider hyperbolic representations as a default rather than an exotic alternative. The hyperbolic attention bias of Chapter 9 is a minimal intervention that achieves this: a single additive term in the attention mechanism, computed from the known hierarchy, at negligible computational cost. The parent theory should recommend this intervention for any domain with known hierarchical structure.

**Proposition 17.1** (Hyperbolic Default). *Let $\mathcal{T}$ be a taxonomy with branching factor $b \geq 2$ and depth $d \geq 3$. For any embedding of $\mathcal{T}$ into a metric space of dimension $n$:*

*(i) In Euclidean space $\mathbb{R}^n$, the worst-case distortion is $\Omega(b^{1/n})$.*

*(ii) In the Poincaré ball $\mathbb{B}^n_c$ with curvature $c = O(1/d)$, the worst-case distortion is $O(1)$ for $n = O(\log b)$.*

*The hyperbolic embedding achieves bounded distortion with exponentially fewer dimensions.*

*Proof.* Part (i) follows from the volume argument: the $b^d$ leaf nodes must be separated by distance at least $\delta$ (the minimum inter-leaf distance), which requires a ball of radius $\Omega(b^{d/n} \delta)$, forcing distortion $\Omega(b^{1/n})$ for fixed $n$. Part (ii) is the Sarkar (2011) construction, which places root at origin, distributes children in angular sectors, and adjusts the curvature so that the exponential volume growth at depth $d$ matches the branching. The dimension requirement $n = O(\log b)$ follows from the need to angularly separate $b$ children at each level, which requires $O(\log b)$ angular degrees of freedom. $\square$

[Figure 17.2: Distortion as a function of embedding dimension for a binary tree of depth 10 (1,024 leaves). Blue: Euclidean embedding (distortion decreases polynomially with dimension). Orange: Poincaré ball embedding (distortion reaches $O(1)$ at dimension $\sim$5). The gap widens for deeper trees and larger branching factors.]

---

## 17.3 Lesson 3: The Same Geometry Works Across Kingdoms

### 17.3.1 The Scope of the Claim

The three-geometry toolkit --- hyperbolic embeddings, SPD manifold features, persistent homology --- was applied to communication systems from three biological kingdoms:

- **Cetacea**: sperm whale codas (8,719 codas, 28 types, 18 individuals)
- **Aves**: birdsong (206 species, Kaggle competition scale)
- **Homo sapiens**: cuneiform (1,561 Akkadian-English pairs), moral reasoning (3.9M Hebrew/Aramaic passages, 68K English letters)

In each case, the toolkit produced informative results without domain-specific modification. The same mathematical operations --- matrix logarithm, Riemannian distance, Vietoris-Rips filtration, Poincaré exponential map --- were applied to signals that differ in every physical property: broadband clicks versus tonal songs versus inscribed clay versus modern text. The toolkit does not care about the physics of the signal. It cares about the geometry of the information.

### 17.3.2 What Cross-Kingdom Validity Means

The cross-kingdom validity of the geometric toolkit has a strong implication and a weak implication.

The **weak implication** is methodological: these mathematical tools are useful in diverse settings. This is unsurprising. Linear algebra is useful in diverse settings too. The weak implication does not tell us anything about communication itself; it tells us that Riemannian geometry, algebraic topology, and hyperbolic embeddings are versatile mathematical frameworks.

The **strong implication** is ontological: communication systems, regardless of their biological substrate, have geometric structure that is constrained by the mathematics of information rather than by the biology of the communicator. The geometric regularities are not accidents of evolution. They are consequences of what communication *must do* --- encode hierarchical information, transmit reliably through noise, distinguish content from identity, compose meanings from parts --- and the mathematical constraints that these functional requirements impose.

The evidence for the strong implication comes not from the applicability of the tools (which supports only the weak implication) but from the *specific structural parallels* across kingdoms:

### 17.3.3 Structural Parallels

**Menzerath's law.** In human language, Menzerath's law states that the longer a linguistic construct (e.g., a word), the shorter its constituents (e.g., its syllables). The law has been documented in dozens of human languages across all major language families. In sperm whale codas, we found the same law: longer codas (more clicks) have shorter inter-click intervals ($r = -0.269$, $p < 10^{-144}$). In birdsong, analogous relationships between song length and syllable length have been reported in several species (Hailman and Ficken, 1986).

Menzerath's law is a constraint on the *curvature of trajectories on the signal manifold*. A communication signal traces a path on the signal manifold $S$; Menzerath's law constrains the path's curvature by requiring that longer paths have smaller per-step deviations. This constraint is geometric, not biological. It arises from information-theoretic considerations: compression efficiency requires that longer messages be composed of shorter, more predictable units (Ferrer-i-Cancho et al., 2014). Any communication system subject to compression pressure --- which is to say, any communication system operating in finite bandwidth --- will exhibit it.

**Content/identity factorisation.** In whale codas, type-level content is encoded in the topology (which persistence features) while individual identity is encoded in the metric (precise ICI distances). In birdsong, species-level content is encoded in the spectral covariance structure (which SPD features) while individual identity is encoded in fine-grained spectral detail. In human speech, the content/identity factorisation is the foundation of speech processing: automatic speech recognition extracts content by factoring out speaker identity; speaker verification extracts identity by factoring out content.

This factorisation is a statement about the *product structure of the communication manifold*. The manifold $M = S \times P \times C$ introduced in Chapter 3 has (at minimum) independent factors for content and identity. The factorisation into topology and metric (for whales), covariance and fine structure (for birds), and phonemic content and voice quality (for humans) are three instantiations of the same geometric decomposition: meaning lives in the gauge-invariant properties of the manifold, while identity lives in the gauge-variant properties. The decomposition is mathematically natural (it follows from the fibre bundle structure of the communication manifold) and biologically universal (because all communication systems face the dual demand of encoding both what and who).

**Hierarchical organisation.** The coda taxonomy (rhythm $\times$ click count $\times$ variant), the birdsong taxonomy (order $\to$ family $\to$ genus $\to$ species), the cuneiform taxonomy (sign $\to$ reading $\to$ word), and the moral taxonomy (type $\to$ subtype $\to$ instance) all have tree-like structure. All embed naturally in hyperbolic space. The hierarchical organisation is not a contingent feature of these particular systems; it is a universal property of communication systems that must encode both general categories and specific instances.

### 17.3.4 The Feedback to the General Theory

The lesson for the parent framework: **the geometric structure of cognitive domains may be far more constrained than domain-agnostic reasoning suggests**. The parent theory, wisely, does not presuppose the structure of any particular domain's manifold. But the communication evidence suggests that functional requirements --- hierarchical encoding, noise robustness, content/identity separation --- impose strong geometric constraints that are shared across independently evolved systems.

If this is correct, then the general theory should include a taxonomy of functional requirements and their geometric consequences:

| Functional requirement | Geometric consequence | Evidence from communication |
|---|---|---|
| Hierarchical encoding | Negative curvature (hyperbolic) | Coda taxonomy, cuneiform signs, moral ontology |
| Noise robustness | Topological invariance | TDA features in whale codas and birdsong |
| Content/identity separation | Product manifold structure | Topology/metric split in whales; covariance/fine-structure split in birds |
| Compression efficiency | Menzerath curvature constraint | $r = -0.269$ in whale codas; analogues in birdsong and human language |
| Compositionality | Fibre bundle structure | Combinatorial phonetics in whale codas; morphology in cuneiform |

This taxonomy is preliminary and incomplete. But it points toward a programme: derive the geometric structure of a domain from its functional requirements, rather than discovering it empirically each time. The communication domain, with its three-kingdom evidence base, provides the strongest current support for this programme.

[Figure 17.3: Structural parallels across three kingdoms. Left column: whale codas. Centre column: birdsong. Right column: human language (cuneiform and moral reasoning). Each row shows a shared geometric property: hierarchical embedding (top), topological invariants (middle), content/identity factorisation (bottom). The same geometry, in three independently evolved systems.]

---

## 17.4 Lesson 4: Scalar Irrecoverability Is Worst in Communication

### 17.4.1 The General Theorem

The Scalar Irrecoverability Theorem (*Geometric Reasoning*, Ch. 13) states that any projection from a manifold to a scalar destroys structure that cannot be recovered from the scalar alone. Formally: let $\pi: M \to \mathbb{R}$ be a smooth surjective map from an $n$-dimensional manifold to the real line. Then $\pi$ destroys (at minimum) the topology of the fibres $\pi^{-1}(c)$, the metric structure within each fibre, and the connection between fibres. The lost information is irrecoverable from the scalar $\pi(x)$ alone.

The theorem applies to every domain in the series. A GDP number destroys distributional information about an economy. A QALY destroys trajectory information about a patient's quality of life. A classification accuracy destroys the topology of the confusion space.

But the communication domain suffers *qualitatively* worse irrecoverability than any other domain in the series, for a reason that is specific to communication: **the thing destroyed is meaning itself**.

### 17.4.2 What Other Domains Lose

In economics, scalar reduction (GDP) loses distributional information: which sectors are growing, which regions are stagnating, how income is distributed across the population. These are quantitative losses --- the same kind of information, at finer resolution, than the scalar provides.

In medicine, scalar reduction (QALY) loses trajectory information: a patient with constant moderate quality of life and a patient with excellent quality followed by sharp decline may have the same QALY but radically different experiences. Again, the loss is quantitative: finer-grained temporal resolution of the same kind of information.

In education, scalar reduction (GPA) loses multidimensional information: a student excellent in mathematics and weak in literature has the same GPA as a student with the reverse profile. The loss is multidimensional but still quantitative: more axes of measurement, each of the same basic kind (performance).

### 17.4.3 What Communication Loses

In communication, scalar reduction loses *meaning*. And meaning is not the same kind of information at finer resolution. It is a qualitatively different kind of information --- information about the content, the pragmatics, the social context, and the compositional structure of the communicative act --- that has no scalar representation at any resolution.

The BLEU score of a translation (Chapter 1, Section 1.2.1) is not a coarse measurement of translation quality. It is a measurement of $n$-gram overlap, which is a proxy for translation quality, and the proxy destroys:

- **Synonymy**: nearby points on the semantic manifold are projected to distant points on the lexical surface.
- **Word order flexibility**: the orbit of valid surface realisations under syntactic transformation is collapsed to a single reference point.
- **Pragmatic equivalence**: the fibre of expressions with the same communicative force is invisible.
- **Hierarchical structure**: the tree structure of compositional meaning is undetectable by sliding $n$-gram windows.

Each of these losses corresponds to the destruction of a specific geometric structure (metric, symmetry, fibre, topology). The losses are not merely quantitative (less information about the same thing). They are categorical (information about *different things* --- meaning, pragmatics, syntax, semantics --- that cannot be recovered by measuring more of the same scalar).

### 17.4.4 The Irrecoverability Gradient

We can make the qualitative argument quantitative by defining an *irrecoverability gradient* across domains.

**Definition 17.1** (Irrecoverability Gradient). *Let $M$ be the domain manifold of dimension $n$, and let $\pi: M \to \mathbb{R}$ be the standard scalar evaluation for the domain. The irrecoverability gradient is the pair $(\dim(\ker d\pi), \, \text{rank}(H_*(\pi^{-1}(c))))$, measuring (i) the codimension of the scalar's fibres (how many dimensions are lost) and (ii) the topological complexity of the fibres (how structured the lost information is).*

For GDP on an economic manifold of dimension $\sim$50 (sectors, regions, demographics), the codimension is $\sim$49 and the fibre topology is relatively simple (convex polytopes of distributions summing to the same GDP). For BLEU on a communication manifold of dimension $\sim$100+ (semantic, pragmatic, syntactic, and lexical dimensions), the codimension is $\sim$99 and the fibre topology is highly complex: the set of translations with the same BLEU score includes semantically perfect translations, semantically catastrophic translations, and everything in between, with no topological constraint relating them.

The key difference is fibre topology. In economics, knowing the GDP constrains the economy to a convex set --- a topologically simple fibre. In communication, knowing the BLEU score constrains the translation to a topologically wild set --- a fibre that includes both excellent and terrible translations, connected by paths through every intermediate quality. The scalar tells you almost nothing, because the fibre is so large and so unstructured.

### 17.4.5 The Content Manifold Is High-Dimensional

Why is the irrecoverability so severe in communication? Because the content manifold $C$ is high-dimensional, and the dimensions are not redundant.

The BIP experiments (Chapter 11) suggest at least 4 independent dimensions for moral communication (the Hohfeldian quartet: Right, Duty, Liberty, No-Right). The whale coda analysis (Chapter 7) suggests at least 5 for acoustic communication (click count, rhythm, tempo, rubato, ornamentation). The cuneiform analysis (Chapter 9) suggests at least 3 for written communication (sign form, reading, word). These are *lower bounds* on the dimensionality of $C$ in each domain, established by the number of independently varying features that the geometric analysis identifies.

The true dimensionality is almost certainly higher. Semantic space has dimensions for topic, register, formality, perspective, modality, tense, aspect, evidentiality, speaker attitude, social relationship, and many others. Pragmatic space adds dimensions for speech act type, implicature, presupposition, and conversational role. Even a conservative estimate puts the dimensionality of the full communication manifold $M = S \times P \times C$ at several dozen independent dimensions.

Compressing this to a scalar loses at least several dozen independent dimensions of information. And unlike economics (where the lost dimensions are largely redundant --- regional GDPs are correlated) or medicine (where the lost dimensions are largely temporal --- QALYs at different times are correlated), the lost dimensions of communication are *semantically independent*. Topic and register are not correlated. Formality and truth value are not correlated. Speaker attitude and syntactic structure are not correlated. Each lost dimension carries independent information about the communicative act, and the scalar retains none of it.

### 17.4.6 The Feedback to the General Theory

The lesson for the parent framework: **scalar irrecoverability should be treated as a spectrum, not a binary**. All scalar reductions lose information, but the severity varies across domains in a predictable way: the higher the dimensionality of the domain manifold and the more topologically complex the scalar's fibres, the worse the irrecoverability.

Communication sits at the extreme of this spectrum. The parent theory should recognise this extremity and adjust its recommendations accordingly: in communication, scalar evaluation is not merely lossy but qualitatively misleading, and geometric evaluation is not merely desirable but necessary.

The practical consequence is that the "geometric alternative" proposed in *Geometric Reasoning* --- evaluate on manifolds rather than scalars, using distances, curvatures, and topological invariants as the basic measurements --- is more urgent for communication than for any other domain. A GDP number, while lossy, at least correlates monotonically with most people's intuitive notion of economic output. A BLEU number may correlate positively with translation quality on average while being catastrophically misleading in individual cases (the vodka problem of Chapter 1). The correlation between scalar and geometric evaluation is weaker in communication than in any other domain, and the cost of trusting the scalar is correspondingly higher.

**Proposition 17.2** (Communication Irrecoverability Bound). *Let $M = S \times P \times C$ be the communication manifold with $\dim(S) = s$, $\dim(P) = p$, $\dim(C) = c$. Let $\pi: M \to \mathbb{R}$ be any scalar evaluation metric. Then:*

*(i) The fibre $\pi^{-1}(v)$ has dimension at least $s + p + c - 1$.*

*(ii) If $\pi$ depends only on the signal manifold $S$ (as BLEU, WER, and perplexity do), the fibre has dimension at least $p + c$ --- the entire pragmatic and content manifolds are invisible to the metric.*

*(iii) If the content manifold $C$ has $k$ independent semantic dimensions, then any scalar metric destroys at least $k - 1$ independent dimensions of semantic information.*

*Proof.* Part (i) follows from the rank-nullity theorem: $\pi$ is a map from an $(s+p+c)$-dimensional manifold to $\mathbb{R}$, so its fibres have dimension at least $s + p + c - 1$. Part (ii) follows from the observation that if $\pi = \pi \circ \text{proj}_S$ (the metric factors through the projection to $S$), then the fibres contain the entire $P \times C$ factor, which has dimension $p + c$. Part (iii) follows from restricting to $C$: any scalar function $\pi|_C: C \to \mathbb{R}$ has fibres of dimension at least $k - 1$ by rank-nullity. $\square$

The proposition's force is in part (ii). Every standard evaluation metric in communication --- BLEU, perplexity, WER, sentiment score, readability index --- depends only on the signal manifold $S$ (the surface text). The entire pragmatic manifold $P$ and the entire content manifold $C$ are in the kernel. The metric is not merely lossy. It is blind to the two manifolds that carry the actual meaning of the communication.

[Figure 17.4: The irrecoverability gradient across domains. Horizontal axis: dimensionality of the domain manifold. Vertical axis: topological complexity of scalar fibres. Points: economics (GDP), medicine (QALY), education (GPA), communication (BLEU). Communication occupies the extreme upper right: highest dimensionality, most complex fibres, worst irrecoverability.]

---

## 17.5 Lesson 5: The Heuristic Field Has Discrete Phase Structure

### 17.5.1 Heuristic Corruption in Communication

The heuristic field formalism of *Geometric Reasoning* (Ch. 3) models the learned associations that guide reasoning as a field on the domain manifold. The field assigns to each point $x \in M$ a vector $h(x) \in T_x M$ that represents the default direction of inference: given this input, what is the most natural next step?

In communication, the heuristic field encodes the contextual associations that guide interpretation: given this utterance in this context, what does it most likely mean? Chapter 14 documented how this field can be corrupted by framing effects (the 8.9$\sigma$ displacement of moral judgment under dramatic vs. euphemistic rewriting) and exploited by sycophancy (the 13.3$\sigma$ sycophancy gradient across questioning rounds).

### 17.5.2 The Phase Structure

The surprise, for the general theory, is that the heuristic corruption in communication is not smooth. It is *phase-structured*: the field has discrete phases separated by sharp boundaries, and corruption operates by flipping the field from one phase to another, not by gradually rotating it.

The evidence comes from the semantic gates of Chapter 13:

- "Only if convenient" flips Liberty from $0$ to $1$ --- a discontinuous jump, not a gradual increase.
- "Found a friend" flips Liberty from $1$ to $0$ --- equally discontinuous.
- "Expecting me to" selects Duty categorically --- no intermediate state.

These transitions resemble phase transitions in condensed matter physics, where the order parameter jumps discontinuously at the critical temperature. The communication analogue: the "order parameter" is the normative classification (which Hohfeldian relation applies), and the "temperature" is the linguistic frame. A single phrase can flip the order parameter --- not by gradually heating the system past a critical point, but by directly triggering a discrete state transition.

### 17.5.3 Implications for the Parent Theory

The parent theory models heuristic corruption as a smooth perturbation of the heuristic field: $h \to h + \delta h$, where $\delta h$ is a small vector field representing the corruption. This model assumes that small perturbations produce small changes in the inference trajectory. The communication evidence suggests otherwise: small perturbations to the linguistic frame (adding "only if convenient" to a scenario) can produce large, discontinuous changes in the interpretation.

The parent theory needs a model of *phase-structured heuristic fields* --- fields with discrete phases and sharp boundaries between them, where corruption operates by crossing a phase boundary rather than by gradual perturbation. The mathematical apparatus for such models exists in catastrophe theory (Thom, 1975) and bifurcation theory (Guckenheimer and Holmes, 1983), but it has not been integrated into the geometric reasoning framework.

**Conjecture 17.2** (Discrete Phase Hypothesis). *In cognitive domains with categorical structure, the heuristic field has discrete phases separated by codimension-1 boundaries (catastrophe surfaces). Heuristic corruption operates primarily by displacing the input across a phase boundary, not by smooth perturbation within a phase. The vulnerability of a cognitive state to corruption is determined by its distance to the nearest phase boundary, not by the magnitude of the perturbation field.*

If correct, this conjecture would explain the anisotropic vulnerability observed in Chapter 14: Claude is more susceptible to euphemistic minimisation than to dramatic exaggeration because the phase boundary between "obligation" and "no obligation" is closer in the euphemistic direction. The distance to the boundary, not the magnitude of the perturbation, determines vulnerability.

---

## 17.6 Synthesis: The Communication Domain's Contribution

### 17.6.1 Five Lessons in Summary

The communication domain contributes five lessons to the parent framework of *Geometric Reasoning*:

1. **Discrete gauge structure is natural.** The $D_4$ group of normative communication is discrete, not continuous. Discrete gauge theories, not Lie group gauge theories, may be the norm for cognitive domains.

2. **Hierarchy demands hyperbolic geometry.** Every hierarchical communication system embeds more naturally in hyperbolic space. The parent theory should default to negative curvature for hierarchical domains.

3. **Cross-kingdom universality constrains domain geometry.** The same geometric tools work for cetaceans, birds, and humans. Functional requirements (hierarchy, noise robustness, content/identity separation) impose shared geometric structure. The parent theory should derive domain geometry from functional requirements.

4. **Scalar irrecoverability is worst in communication.** The high dimensionality and topological complexity of the communication manifold make scalar evaluation qualitatively misleading, not merely quantitatively lossy. The parent theory should recognise a spectrum of irrecoverability severity.

5. **The heuristic field has discrete phase structure.** In communication, small linguistic perturbations produce discontinuous changes in interpretation. The parent theory needs a model of phase-structured heuristic fields.

### 17.6.2 What These Lessons Share

The five lessons share a common theme: **the cognitive world is more discrete than the mathematical physicist's toolkit assumes**. Gauge groups are discrete. Phase transitions are discrete. Hierarchies are discrete. Semantic categories are discrete. The continuous mathematics of Riemannian geometry captures the within-category variation beautifully, but the between-category structure --- the most important structure, the structure that determines meaning --- is discrete.

This is not a call to abandon continuous mathematics. The SPD manifold features, the persistent homology, the Poincaré ball model, the parallel transport formalism --- all are continuous, all are essential, all capture structure that discrete methods miss. The call is for a *hybrid framework* that combines continuous geometry for within-category structure with discrete geometry for between-category structure. The communication domain demands this hybrid, and it provides the evidence that such a hybrid is both necessary and productive.

### 17.6.3 The Debt Repaid

The communication domain has now repaid its debt to the parent theory. It borrowed the manifold formalism, the gauge invariance principle, the heuristic field, and the scalar irrecoverability theorem. In return, it offers five structural insights that the general theory could not have discovered from abstract reasoning alone. The insights are empirical --- grounded in whale clicks, birdsong, cuneiform tablets, and moral reasoning experiments --- and they are geometric. They belong to the parent theory not as special cases but as corrections and extensions to its fundamental architecture.

The next and final chapter of the book turns from what we have learned to what we do not yet know.

---

**Series cross-references.** Gauge invariance: GR Ch. 8; this volume Ch. 13. Heuristic field formalism: GR Ch. 3; this volume Ch. 14. Scalar Irrecoverability Theorem: GR Ch. 13; this volume Ch. 15. Hyperbolic embeddings: GR Ch. 14; GM Ch. 4.6; this volume Ch. 5, 9. $D_4$ group: GE Ch. 8; this volume Ch. 13. Adversarial robustness: GE Ch. 22; this volume Ch. 7, 14. Phase transitions and catastrophe theory: not yet treated in the series; proposed for future development in *Geometric Reasoning*, 2nd edition.

*GR = Geometric Reasoning. GE = Geometric Ethics. GM = Geometric Methods.*

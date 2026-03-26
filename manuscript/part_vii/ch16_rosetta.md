# Chapter 16: The Rosetta Trajectory, Complete

*Part VII: Synthesis and Horizons*

---

> *"The real voyage of discovery consists not in seeking new landscapes, but in having new eyes."*
> --- Marcel Proust, *In Search of Lost Time*

> **THE ROSETTA TRAJECTORY --- ARRIVAL**
>
> *We began in the Caribbean, listening to clicks.*
>
> *A sperm whale off the coast of Dominica produced a sequence of five broadband pulses --- 0.35, 0.35, 0.22, 0.22 seconds apart --- and a hydrophone recorded them as a one-dimensional pressure signal, buried in shipping noise, multipath echoes, and the clicks of three other whales. We had the signal. We did not have the meaning.*
>
> *We built tools. Hyperbolic embeddings placed the 28 coda types on a Poincaré disk where hierarchy was readable in the radial coordinate and kinship among types was readable in the angular coordinate. Persistent homology extracted topological signatures --- tight clusters for regular codas, loop structures for irregular codas, multi-component structures for compound codas --- that were invariant to recording conditions. SPD manifold features captured spectral covariance structure that distinguished individuals even within the same coda type. Structure emerged from the geometry. Meaning did not.*
>
> *We moved to birdsong. The same three-geometry pipeline --- SPD, TDA, hyperbolic --- produced a 156-dimensional feature vector that classified 206 bird species on CPU, complementing neural classifiers and capturing what spectrograms missed. Here we could validate: species identity was the known meaning, and the geometric features recovered it. The tools worked on a system we understood.*
>
> *We moved to cuneiform. The Poincaré ball model encoded the three-level sign hierarchy (sign form → reading → word) directly into a transformer's attention mechanism, improving translation of 4,000-year-old Akkadian business records with only 1,561 training pairs. Translation became parallel transport on the content manifold. Translation loss became holonomy. The tools worked on a system we had partially decoded.*
>
> *We moved to moral reasoning. Cross-lingual transfer from 3.9 million Hebrew and Aramaic passages to 68,000 American English letters recovered Hohfeldian moral structure at 44.5% F1 --- nearly double chance --- with 100% transfer on the most fundamental correlative symmetries. Meaning survived translation across 2,500 years and two language families. The tools had found the gauge-invariant core.*
>
> *This chapter completes the trajectory. Not by revealing the meaning of whale codas --- we still do not know it --- but by showing that the four stations along the route are connected by a single geometric thread, and that the thread reveals a hierarchy of communicative structure that was invisible from any single station alone.*

---

## 16.1 The Trajectory Reviewed

The Rosetta trajectory was introduced in Chapter 1 as an organising metaphor: the problem of decoding an unknown communication system, approached by developing tools on progressively more transparent systems. The metaphor was borrowed, with full awareness of the analogy's limits, from the Rosetta Stone --- the bilingual inscription that allowed Champollion to decode Egyptian hieroglyphs in 1822 by exploiting the parallel Greek text. Our trajectory has no parallel text. Instead, it has a progression of geometric transparency: from a system whose meaning is entirely opaque (whale codas) through systems of increasing semantic accessibility (birdsong with known species labels, cuneiform with partial translations, moral reasoning with aligned corpora) to the gauge-invariant structure of meaning itself.

At each station, we applied the same three-geometry toolkit:

1. **Hyperbolic geometry** (Poincaré ball model): for hierarchical structure --- the tree-like organisation of communication categories, from coda types to cuneiform signs to moral concepts.
2. **Riemannian geometry** (SPD manifold): for covariance structure --- the cross-frequency correlations, spectral trajectories, and distributional signatures that characterise communication signals.
3. **Algebraic topology** (persistent homology): for shape --- the topological invariants of signal attractors, production variability, and the boundaries between communicative categories.

The claim of this chapter is that the toolkit was not merely *applied* at each station. It *revealed* something at each station that could not have been seen without the previous stations' lessons. The trajectory is not four independent case studies. It is a single argument, developed cumulatively, and the argument has a conclusion: communicative structure is stratified into three levels, each with its own geometry, each subsuming the previous.

---

## 16.2 Station 1: Whale Communication --- Structure Without Meaning

### 16.2.1 What the Geometry Found

Chapter 7 presented five findings about sperm whale codas, all geometric:

- The 28 coda types embed naturally in hyperbolic space, with the radial-angular decomposition providing an interpretable map of the taxonomic hierarchy (Finding I).
- Rhythm classes have distinct topological signatures --- persistent homology on ICI point clouds distinguishes regular, irregular, and compound codas through their $H_0$ and $H_1$ persistence profiles (Finding II).
- Adversarial perturbation analysis reveals asymmetric classification boundaries, with mean asymmetry of 0.87 (Finding III).
- The coda system satisfies Menzerath's law ($r = -0.269$, $p < 10^{-144}$), exhibits higher-order Markov sequential structure, and supports active turn-taking (Finding IV).
- Individual identity is encoded in the metric (precise ICI distances), while type-level content is encoded in the topology (which connected components, which persistence features) --- a clean separation into orthogonal geometric factors of the signal manifold (Finding V).

### 16.2.2 What the Geometry Did Not Find

Meaning. The geometric analysis extracts structure from the communication system --- hierarchy, topology, boundary geometry, statistical regularities, factorial encoding --- but it does not tell us what any of it *means*. We know that 5R3 is close to 5R1 in hyperbolic space and distant from 4i1. We do not know what 5R3 *communicates* to another whale. We know that irregular codas have loop topology. We do not know what the loops signify.

This is not a failure. It is a principled limitation, and recognising it is essential to the trajectory's logic. At Station 1, we have access only to the signal manifold $S$ and the hierarchical organisation of the signal. The content manifold $C$ --- the space of meanings --- is entirely dark. The geometric tools illuminate $S$ and its internal structure. They do not illuminate $C$ because they have no access to it: there are no parallel texts, no behavioural assays that link specific codas to specific meanings, no Rosetta Stone.

### 16.2.3 The Lesson

The whale station teaches us what geometry can extract from signal alone. The answer is: more than any scalar summary, but less than meaning. The topological signatures, the hyperbolic embedding, the adversarial boundary map, the linguistic universals, and the content/identity factorisation are all properties of the signal manifold $S$, not of the content manifold $C$. They are *necessary conditions* for a communication system --- any system with this much structure is doing something more than making noise --- but they are not *sufficient conditions* for decoding.

The lesson, stated precisely: **signal geometry is domain-independent**. The three-geometry toolkit extracts signal structure from any acoustic communication system, regardless of whether we understand the semantics. It requires only the raw signal. It assumes nothing about what the signal means.

[Figure 16.1: Station 1 on the Rosetta trajectory. The signal manifold $S$ is illuminated by three geometries. The content manifold $C$ remains dark. The arrow from $S$ to $C$ represents the decoding problem --- the mapping from signal structure to meaning --- which remains unsolved for cetacean communication.]

---

## 16.3 Station 2: Birdsong --- Validation on Known Meaning

### 16.3.1 What Changed

At the birdsong station (Chapter 8), we applied the identical three-geometry toolkit to a communication system where the "meaning" is known: species identity. A Pacific wren's song means, at minimum, "I am a Pacific wren." A white-throated sparrow's descending whistle means "I am a white-throated sparrow." This is a drastic simplification of the full communicative content of birdsong --- which also encodes territory, fitness, individual identity, and alarm --- but it provides something the whale station lacked: a ground truth against which geometric features can be validated.

The 156-dimensional geometric feature vector --- 136 SPD features (spectral covariance on SPD(16)), 4 trajectory features (geodesic deviation on the spectral manifold), 16 TDA features (topological persistence of waveform attractors) --- was deployed on 206 species under Kaggle's CPU-only inference constraint. The geometric features carried 30% of the ensemble weight in the final submission, a substantial contribution from a model with no learned convolutional features, no pretraining, and no deep architecture.

### 16.3.2 The Validation Argument

The birdsong station validates the toolkit in a precise sense. At the whale station, we demonstrated that the three geometries extract *structure*. At the birdsong station, we demonstrate that the structure they extract is *informative about meaning*. The SPD covariance matrix captures cross-frequency correlations that distinguish species; the geodesic deviation captures song complexity that varies across species; the topological persistence captures attractor shape that is species-specific. In each case, the geometric feature correlates with the known semantic label.

This is not circular. The geometric features were not designed to classify bird species. They were designed to capture the signal manifold's intrinsic structure: covariance, trajectory, and topology. The fact that this intrinsic structure correlates with species identity is an empirical finding, not a design choice. It confirms the central hypothesis of the book: that communicative structure is geometric, and that geometric tools recover it.

### 16.3.3 The Lesson

The birdsong station teaches us that **signal geometry, when validated against known meaning, is informative**. The geometric features are not arbitrary coordinates on the signal manifold. They are coordinates that align with the manifold's meaningful structure --- the axes along which different communicative acts actually differ. The SPD features capture the "vowel space" of birdsong; the trajectory features capture song complexity; the TDA features capture rhythmic and harmonic shape. Each geometry contributes information that the others miss, and the combination outperforms any single geometry.

The transition from Station 1 to Station 2 is the transition from *structure extraction* to *structure validation*. The tools are the same. What changes is the availability of ground truth.

[Figure 16.2: Station 2 on the Rosetta trajectory. The signal manifold $S$ is illuminated (as at Station 1). The arrow from $S$ to $C$ is now partially resolved: the geometric features on $S$ correlate with the known meaning (species identity) on $C$. The connection between signal geometry and semantic content is empirically confirmed.]

---

## 16.4 Station 3: Cuneiform --- Hierarchy as Geometric Prior

### 16.4.1 The New Element

At the cuneiform station (Chapters 9--10), a new geometric element entered the analysis: explicit hierarchical structure. The Akkadian writing system has a three-level hierarchy --- sign form, reading, word --- that is known from Assyriology. This hierarchy is not inferred from the signal. It is given by the structure of the writing system itself, compiled over two centuries of scholarly decipherment.

The Poincaré ball embedding of this hierarchy, injected into a transformer's attention mechanism as an additive bias, improved translation of 4,000-year-old business records. The improvement was largest for sentences containing rare signs, where the structural prior compensated most for data scarcity. The geometric prior --- the hyperbolic distance between cuneiform signs --- constrained the translation path to lie near structural geodesics, reducing holonomy (Chapter 10, Proposition 10.2).

### 16.4.2 What Hierarchy Adds

At the whale and birdsong stations, the hyperbolic embedding was a representation of the *discovered* taxonomy --- the coda types or species labels that the signal data organised into tree-like structures. At the cuneiform station, the hyperbolic embedding is a representation of a *given* taxonomy --- the sign hierarchy that Assyriologists have established through decades of philological work.

The distinction matters for the Rosetta trajectory's logic. When we embed the coda taxonomy in hyperbolic space, we are *discovering* hierarchy in the signal. When we embed the cuneiform sign taxonomy, we are *exploiting* known hierarchy as a prior. The first is an act of analysis; the second is an act of engineering. But both use the same mathematical machinery --- the Poincaré ball model, the exponential and logarithmic maps, the hyperbolic distance formula --- because both are instances of the same geometric phenomenon: hierarchical structure embeds more naturally in hyperbolic than Euclidean space.

The cuneiform station also introduced the interpretation of translation as parallel transport (Chapter 10). This interpretation depends on having two coordinate charts --- source and target language --- and a path between them. The whale station had only one chart (the signal). The birdsong station had one chart and one label set. The cuneiform station has two full linguistic systems (Akkadian and English) and the apparatus of differential geometry to describe the transport between them.

### 16.4.3 The Lesson

The cuneiform station teaches us that **hierarchical geometry requires domain knowledge**. Signal geometry (Station 1) requires only the raw signal. Hierarchical geometry (Station 3) requires knowledge of the hierarchy --- the taxonomic tree, the sign system's internal organisation, the ontological structure of the domain. This knowledge may come from the data (as in the whale coda taxonomy, where the tree is discovered by clustering) or from external sources (as in the cuneiform sign hierarchy, where the tree is given by scholarship). Either way, it goes beyond the signal itself.

The gain from hierarchical geometry is substantial. The hyperbolic attention bias improved translation quality on the hardest cases --- rare signs, unusual constructions --- precisely where the model most needed structural guidance. The hierarchy constrains the space of admissible interpretations, reducing $\epsilon_{\text{path}}$ in the translation error decomposition of Proposition 10.3. Without the hierarchy, the model is free to wander through high-curvature regions of the content manifold. With the hierarchy, the model's path is guided by the structural geodesics that the taxonomy defines.

[Figure 16.3: Station 3 on the Rosetta trajectory. The signal manifold $S$ is illuminated (as before). The hierarchical structure $H$ --- the taxonomic tree of the communication system --- is now explicitly represented as a Poincaré ball embedding, and it constrains the mapping from $S$ to $C$. The translation process is parallel transport, and the hierarchy reduces holonomy.]

---

## 16.5 Station 4: Cross-Lingual Moral Reasoning --- The Invariant Core

### 16.5.1 The Final Element

At the moral reasoning station (Chapters 11--13), the final geometric element entered the analysis: gauge invariance. The Bond Invariance Principle (BIP) asserts that meaning is invariant under the communication gauge group $G = T \times R \times F$ --- invariant under translation ($T$), re-description ($R$), and change of format ($F$). The BIP experiment tested this assertion directly by training on Hebrew/Aramaic moral texts and testing on American English moral texts, with an adversarial head forcing the encoder to discard temporal-stylistic features and retain only the invariant content.

The result: 44.5% F1 on cross-lingual moral classification (chance = 25%, $p < 10^{-50}$). Bidirectional transfer confirmed. And the most striking result: 100% transfer on Hohfeldian correlative symmetry (Right $\leftrightarrow$ Duty, Liberty $\leftrightarrow$ No-Right) across all tested scenarios.

### 16.5.2 What Gauge Invariance Adds

Gauge invariance is not a property of the signal. It is not a property of the hierarchy. It is a property of the *meaning* --- the content manifold $C$ itself. The claim is that certain structures on $C$ are invariant under coordinate change (translation between languages), and the BIP experiment measures whether this invariance holds empirically.

The $D_4$ group structure of normative communication (Chapter 13) --- the dihedral symmetry of the Hohfeldian square, with correlative reflection $s$ and state-transition rotation $r$ satisfying $r^4 = s^2 = e$, $srs = r^{-1}$ --- is the measured symmetry group of this invariant core. It is not imposed by the analysis. It is discovered by the experiment and confirmed by the Wilson loop measurements (combined $p < 10^{-8}$).

The moral reasoning station closes the loop that the whale station opened. At Station 1, we extracted signal structure without semantic access. At Station 4, we have full semantic access --- aligned corpora across languages, known moral categories, testable invariance predictions --- and we confirm that the deepest structure (the gauge-invariant core) is geometric. The $D_4$ symmetry of moral communication is as much a geometric object as the Poincaré embedding of coda types. Both live on manifolds. Both have measurable curvature. Both are invisible to scalar evaluation.

### 16.5.3 The Lesson

The moral reasoning station teaches us that **semantic geometry requires aligned corpora**. Signal geometry (Station 1) requires only the raw signal. Hierarchical geometry (Station 3) requires a taxonomy. Semantic geometry (Station 4) requires parallel data --- the same meaning expressed in two or more coordinate systems --- so that the invariant content can be extracted by factoring out the coordinate-dependent surface.

This is the most demanding requirement. It is why we cannot yet decode whale communication: we lack parallel whale-human data. The BIP experiment succeeds because the Hebrew/Aramaic and English traditions discuss the same moral problems --- the obligation to help, the right to refuse, the duty of hospitality, the liberty of personal choice --- in different linguistic coordinates. The invariant moral structure survives the coordinate change because it is a property of the content manifold $C$, not of the particular chart used to describe it.

[Figure 16.4: Station 4 on the Rosetta trajectory, complete. All three geometric layers are illuminated: signal geometry ($S$), hierarchical geometry ($H$), and semantic geometry ($C$). The gauge group $G = T \times R \times F$ acts on the surface forms; the invariant content --- the Hohfeldian $D_4$ structure --- is the fixed point of this action.]

---

## 16.6 The Hierarchy of Communicative Structure

### 16.6.1 Three Levels

The four stations reveal a hierarchy with three levels. Each level has its own geometry, its own data requirements, and its own scope.

**Level 1: Signal geometry.** The geometry of the raw communication signal, extracted without semantic access. Tools: SPD manifold features (spectral covariance), persistent homology (topological invariants of signal attractors), Takens embedding (phase-space reconstruction). Data requirement: the signal itself --- audio recordings, written texts, gesture captures. No labels, no taxonomy, no parallel texts. Scope: domain-independent. Applies equally to whale clicks, birdsong, cuneiform readings, modern speech, and any other physical signal. Stations where validated: all four.

**Level 2: Hierarchical geometry.** The geometry of the organisational structure of the communication system. Tools: Poincaré ball embeddings (hyperbolic representation of taxonomies), hyperbolic attention bias (structural prior for neural models), radial-angular decomposition (interpretable hierarchy maps). Data requirement: a taxonomic tree or ontological hierarchy, either discovered from the data (clustering) or given by domain expertise (philology, biology). Scope: requires minimal domain knowledge --- the tree structure --- but not semantic access. Applies whenever the communication system has hierarchical organisation, which appears to be universal. Stations where validated: Stations 1, 3, and 4.

**Level 3: Semantic geometry.** The geometry of meaning itself --- the invariant content that survives gauge transformations (translation, paraphrase, re-description). Tools: adversarial training with gradient reversal (factoring out surface features), gauge group identification ($D_4$ for normative communication), Wilson loop measurements (holonomy at cross-type boundaries), parallel transport analysis (translation as holonomy-minimising transport). Data requirement: aligned corpora or parallel texts --- the same meaning expressed in multiple coordinate systems. Scope: applies only when parallel data exists, which restricts current applicability to human languages with substantial multilingual corpora. Stations where validated: Stations 3 and 4.

### 16.6.2 Subsumption

The three levels form a strict hierarchy of subsumption:

**Signal geometry subsumes nothing.** It is the foundation. It requires only the physical signal and outputs structural features --- covariance, topology, trajectory --- that characterise the signal manifold $S$ without reference to meaning.

**Hierarchical geometry subsumes signal geometry.** To embed a taxonomy in hyperbolic space, you must first have identified the categories that the taxonomy organises. Those categories are discovered by applying signal geometry: clustering in ICI space reveals coda types; spectral analysis reveals species-specific signatures; character recognition reveals cuneiform signs. The hierarchical geometry operates on the output of signal geometry, organising the categories into a tree. Formally, the hierarchical embedding $\phi: \mathcal{T} \to \mathbb{B}^d_c$ maps a taxonomy $\mathcal{T}$ into the Poincaré ball, and $\mathcal{T}$ is itself a structure discovered or confirmed by signal-level analysis.

**Semantic geometry subsumes hierarchical geometry.** To identify gauge-invariant meaning, you must first have the hierarchical structure that organises the meaning space. The Hohfeldian $D_4$ group acts on the square of normative relations, which is itself a hierarchical structure (two axes: claim-privilege and correlative-state-transition). The hyperbolic attention bias that improves cuneiform translation relies on the sign hierarchy, and the translation it enables is an instance of parallel transport on the content manifold. Formally, the gauge group $G$ acts on the fibre bundle $\pi: E \to C$, where $C$ is the content manifold and $E$ is the total space of surface expressions. The base space $C$ has hierarchical structure that the Poincaré ball represents, and the fibre above each point in $C$ is the set of surface expressions that all express the same meaning. Semantic geometry identifies the base space $C$ by factoring out the fibre; hierarchical geometry maps the base space's internal structure; signal geometry provides the raw features from which the whole construction begins.

$$\text{Signal geometry} \subset \text{Hierarchical geometry} \subset \text{Semantic geometry}$$

where $\subset$ denotes "is subsumed by" --- each higher level requires and extends the lower.

[Figure 16.5: The hierarchy of communicative structure. Three concentric regions: signal geometry (outer, domain-independent), hierarchical geometry (middle, taxonomy-dependent), semantic geometry (inner, corpus-dependent). Each level subsumes the previous. The four stations of the Rosetta trajectory ascend through these levels.]

### 16.6.3 The Subsumption Is Not Merely Logical

The subsumption relation is not merely a logical implication (hierarchical geometry uses signal geometry, therefore it "subsumes" it in a trivial sense). It is a geometric subsumption: the structures at each level are geometrically richer than those at the level below, in a precise sense.

Signal geometry produces features that live in a vector space or on a Riemannian manifold (SPD$(n)$). These features have a metric (the log-Euclidean distance, the bottleneck distance for persistence diagrams) but no hierarchy and no gauge structure.

Hierarchical geometry produces features that live in a hyperbolic space (the Poincaré ball $\mathbb{B}^d_c$). Hyperbolic space is strictly richer than Euclidean space for hierarchical data: it can embed trees with bounded distortion in $O(\log b)$ dimensions where Euclidean space requires $O(b)$ (Sarkar, 2011). The curvature parameter $c$ controls the trade-off between precision at different levels of abstraction --- a degree of freedom that flat spaces do not possess.

Semantic geometry produces features that live on a fibre bundle with a connection and a gauge group. A fibre bundle is strictly richer than a Riemannian manifold: it has all the metric and topological structure of the base manifold, plus the additional structure of the fibre and the connection. The gauge group $G$ encodes the symmetries of meaning under re-description, and the holonomy of the connection measures translation loss. These structures have no analogue at the signal or hierarchical levels.

The subsumption is therefore a progression of geometric enrichment:

$$\text{Riemannian manifold} \to \text{hyperbolic space} \to \text{fibre bundle with connection}$$

Each step adds structure. Each step requires more data (signal $\to$ taxonomy $\to$ parallel corpus). Each step reveals more about the communication system. And each step is necessary for the next.

---

## 16.7 Threading the Stations

### 16.7.1 Whale Clicks to Birdsong

The transition from whale clicks to birdsong (Stations 1 to 2) is a transition within signal geometry. The same three tools --- SPD, TDA, and (in a limited form) hyperbolic embedding --- are applied to both systems. What changes is the availability of ground truth.

This transition tests the toolkit's **domain generality**. The whale and birdsong signals differ in nearly every acoustic property: broadband clicks versus tonal songs, millisecond versus multi-second durations, temporal pattern encoding versus spectral structure encoding. If the geometric toolkit were tuned to one of these signal types, it would fail on the other. The fact that it succeeds on both --- producing meaningful features in both cases, without domain-specific modification --- is evidence that the toolkit captures properties of *communication* that transcend the properties of any particular *signal type*.

The specific evidence for domain generality is the complementarity of the geometric features. In the whale analysis, TDA features captured rhythm class (the shape of the ICI point cloud). In the birdsong analysis, TDA features captured harmonic structure (the shape of the waveform attractor). Different physical properties, same mathematical tool, informative in both cases. The SPD features captured individual identity in whales (covariance structure of click timing) and species identity in birds (cross-frequency spectral correlations). Different biological properties, same manifold, informative in both cases.

### 16.7.2 Birdsong to Cuneiform

The transition from birdsong to cuneiform (Stations 2 to 3) is a transition from signal geometry to hierarchical geometry. The birdsong analysis used the three-geometry toolkit at the signal level: features extracted from raw audio, classified by a gradient-boosted tree. The cuneiform analysis used the Poincaré ball at the hierarchical level: a known taxonomy embedded in hyperbolic space and injected as a prior into a neural translation model.

This transition tests the toolkit's **level generality**. The same mathematical object --- the Poincaré ball --- serves two different functions at the two stations. At Station 2, a hyperbolic embedding of species labels organises the classification targets. At Station 3, a hyperbolic embedding of cuneiform signs constrains the translation process. The embedding is the same. The level at which it operates has shifted from the signal manifold to the content manifold's organisational structure.

The transition also introduces the concept of parallel transport, which requires two coordinate charts (source and target language) and a path between them. Birdsong classification is a single-chart problem: one signal space, one label space, no translation. Cuneiform translation is a two-chart problem: the Akkadian chart and the English chart overlap in the commercial-transaction region, and translation is the transition map between them. The geometric toolkit scales from one chart to two without modification --- the same hyperbolic distance formula that organises coda types in one chart organises cuneiform signs in a two-chart translation.

### 16.7.3 Cuneiform to Moral Reasoning

The transition from cuneiform to moral reasoning (Stations 3 to 4) is a transition from hierarchical geometry to semantic geometry. The cuneiform analysis used hierarchy as a prior, but the meaning of the translation was assessed by conventional metrics (BLEU, chrF++). The moral reasoning analysis uses gauge invariance as the object of study: the meaning itself is the thing being tested for geometric structure.

This transition tests the toolkit's **depth generality**. At Station 3, geometry aids translation. At Station 4, geometry *is* the content. The $D_4$ symmetry of the Hohfeldian square is not a tool applied to meaning; it is the measured symmetry of meaning. The Wilson loop experiments do not use geometry to improve a downstream task; they measure the geometry of the moral communication manifold directly.

The transition also introduces discreteness. The cuneiform sign hierarchy is discrete (it is a finite tree), but the translation process is continuous (the attention weights vary smoothly). The Hohfeldian $D_4$ group is discrete in a stronger sense: the transitions between normative states are gated by specific linguistic triggers ("only if convenient" $\to$ 100% Liberty), and the gauge group itself is finite ($|D_4| = 8$). This discreteness is not an approximation to a continuous symmetry. It is the measured structure of moral communication, and it has consequences for the general theory (Chapter 17).

[Figure 16.6: The three transitions along the Rosetta trajectory. Station 1 → 2: domain generality (whale → bird). Station 2 → 3: level generality (signal → hierarchy). Station 3 → 4: depth generality (hierarchy → semantics). Each transition tests a different dimension of the toolkit's scope.]

---

## 16.8 The Return to the Whales

### 16.8.1 What the Trajectory Tells Us About Cetacean Communication

The Rosetta trajectory was designed to develop tools on progressively more transparent systems and then bring those tools back to the opaque one. What have we learned that bears on the question we opened with: can we decode whale communication?

The trajectory tells us three things.

**First, the signal geometry of whale codas is richer than any scalar summary suggests.** The five findings of Chapter 7 --- hyperbolic hierarchy, topological signatures, adversarial boundaries, linguistic universals, dual encoding of content and identity --- establish that the coda system has geometric structure comparable in complexity to the signal-level structure of birdsong and cuneiform. The structure is not noise. It is a communication system with hierarchical organisation, topological differentiation, and information-theoretic regularities shared with human language.

**Second, the same tools that extract meaning-relevant structure from birdsong and cuneiform extract comparable structure from whale codas.** The SPD features that classify bird species classify coda types. The Poincaré embedding that organises cuneiform signs organises coda types. The TDA features that distinguish species-specific harmonic structure distinguish rhythm-class-specific temporal structure. If the tools are informative about meaning in the systems where we can verify, there is reason --- not proof, but reason --- to believe they are capturing meaning-relevant structure in the whale system as well.

**Third, the gap is at Level 3 --- semantic geometry --- and it is a data gap, not a tools gap.** We have the mathematical apparatus for identifying gauge-invariant meaning: adversarial training, gauge group identification, Wilson loop measurements, holonomy quantification. We lack the parallel data to apply it. No one has a corpus of whale codas aligned with behavioural meanings, let alone a cross-species parallel text. The BIP experiment worked because Hebrew/Aramaic and English share a moral discourse tradition. No comparable shared tradition links whale communication to any human language.

### 16.8.2 The Gap Between Structure and Meaning

The Rosetta trajectory makes the gap precise. It is not a vague "we don't know what they're saying." It is: we have Levels 1 and 2 (signal geometry and hierarchical geometry) for the whale system, but not Level 3 (semantic geometry), and Level 3 requires data that does not exist.

What would close the gap? Two possibilities:

**A Rosetta Stone.** Parallel whale-human data: specific codas reliably associated with specific behaviours, contexts, or meanings. The closest existing work is the observation that certain coda types (notably 1+1+3) function as identity codas --- produced preferentially during social interactions and shared within social units (Gero et al., 2016). If the identity function of 1+1+3 could be confirmed experimentally (by manipulating playback and observing responses), it would provide a single point of parallel data: coda type $\to$ social function. From that single point, the hierarchical geometry could propagate: types near 1+1+3 in the Poincaré embedding would be predicted to have related social functions, and this prediction could be tested.

**A formal semantics.** A compositional theory of coda meaning that predicts the semantic content of a coda sequence from its geometric features --- click count, rhythm class, tempo, rubato, ornamentation, and the spectral patterns discovered by Begus et al. (2024, 2025). This is a far more ambitious programme. It would require not just correlation between features and meanings but a compositional rule: the meaning of a sequence is a function of the meanings of its parts and the geometry of their combination. The combinatorial phonetic system of Sharma et al. (2024) --- rhythm $\times$ tempo $\times$ rubato $\times$ ornamentation --- provides the combinatorial structure, but the semantics of each factor remains unknown.

Neither possibility is close to realisation. The trajectory has brought us as far as geometry alone can go. The rest requires data, experiment, and --- perhaps --- a breakthrough in how we think about non-human meaning.

---

## 16.9 The Universality Argument

### 16.9.1 The Same Geometry Works Across Kingdoms

The Rosetta trajectory spans three biological kingdoms: cetacean (whales), avian (birds), and human (cuneiform, moral reasoning). The same three-geometry toolkit produces meaningful results in all three. This is either a deep fact about the geometry of communication or a coincidence of mathematical versatility.

The evidence favours the former. The coincidence hypothesis would require that three independently evolved communication systems happen to have structure that the same mathematical tools can extract, for unrelated reasons. The deep-fact hypothesis explains the same evidence parsimoniously: all communication systems, regardless of biological substrate, must solve the same geometric problems --- encoding hierarchy, preserving information under noise, separating content from identity --- and the solutions to these problems have the same mathematical structure.

The specific parallels are instructive:

| Property | Whale codas | Birdsong | Cuneiform | Moral reasoning |
|---|---|---|---|---|
| Hierarchical structure | Coda taxonomy | Phylogenetic tree | Sign hierarchy | Hohfeldian square |
| Natural embedding | Poincaré ball | (implicit) | Poincaré ball | $D_4$ group |
| Topological invariants | ICI persistence | Waveform persistence | (not tested) | Wilson loops |
| Covariance structure | ICI SPD | Spectral SPD | (not tested) | Bond space |
| Linguistic universals | Menzerath's law | Zipf's law[^1] | Zipf's law | Correlative symmetry |

[^1]: Zipf's law in birdsong syllable frequencies has been reported by several authors, though the interpretation is debated. See Suzuki et al. (2006) for evidence and Ferrer-i-Cancho and McCowan (2012) for caveats.

The table is not complete --- several cells are marked "not tested" because the corresponding analysis was not performed, not because the geometry would not apply. The SPD analysis was not applied to cuneiform because cuneiform is a written system with no acoustic signal; the TDA analysis was not applied to cuneiform or moral reasoning because the relevant signals are textual, not temporal. But where the analysis was performed, the geometry produced informative results across all three kingdoms.

### 16.9.2 Convergent Evolution of Communicative Geometry

The universality admits a biological interpretation: **convergent evolution of communicative geometry**. Just as flight evolved independently in insects, birds, bats, and pterosaurs --- because the physics of aerodynamics constrains the solution space --- so communicative structure may evolve independently in cetaceans, birds, and humans because the mathematics of information transmission constrains the solution space.

The constraints are identifiable:

- **Hierarchical organisation** arises because communication systems must encode both general categories and specific instances, and tree-like structures are the most efficient way to do so in finite bandwidth (Shannon, 1948).
- **Topological robustness** arises because communication must function in noisy environments, and topological features are by definition invariant to continuous deformation (the noise model for most acoustic environments).
- **Covariance structure** arises because multiple signal features must be coordinated, and the correlations between features carry information (about identity, context, or content) that the individual features alone do not.
- **Metric duality** (content in topology, identity in metric) arises because communication must simultaneously encode *what is being said* and *who is saying it*, and these two functions have different invariance requirements (content must be invariant across individuals; identity must vary).

These constraints are not biological. They are mathematical. Any communication system --- biological, artificial, or extraterrestrial --- that must encode hierarchical information in a noisy channel with finite bandwidth and multiple speakers will, if the arguments above are correct, converge on the same geometric structures. The convergent evolution is not of the *mechanisms* (whales, birds, and humans produce sound differently) but of the *geometry* (the mathematical structure of the information they encode).

---

## 16.10 Summary: The Trajectory as Argument

The Rosetta trajectory is not four case studies. It is a single argument with four premises and one conclusion.

**Premise 1** (Station 1): The three-geometry toolkit extracts rich structural features from an opaque communication system (whale codas), features that no scalar summary captures.

**Premise 2** (Station 2): The same toolkit, applied to a communication system with known meaning (birdsong), produces features that are informative about meaning. The toolkit is not merely extracting noise; it is extracting meaning-relevant structure.

**Premise 3** (Station 3): The toolkit, extended with hierarchical geometry, improves translation of an ancient language (cuneiform) by encoding structural knowledge as a geometric prior. The hierarchy constrains the translation path and reduces holonomy.

**Premise 4** (Station 4): The toolkit, extended with semantic geometry, reveals gauge-invariant structure in moral reasoning across languages. The deepest structure of meaning --- the $D_4$ symmetry of normative relations --- is geometric, discrete, and empirically measurable.

**Conclusion**: Communicative structure is stratified into three geometric levels --- signal, hierarchical, and semantic --- each subsuming the previous, each requiring more data, each revealing more about meaning. The same mathematical toolkit operates at all three levels, and it works across biological kingdoms.

This conclusion does not solve the problem of whale communication. It does not decode cuneiform in one pass. It does not make BLEU scores obsolete overnight. What it does is provide a framework --- rigorous, empirically grounded, and geometrically precise --- for understanding what communication *is*, what scalar evaluation *destroys*, and what geometric analysis *recovers*.

The framework is the contribution. The trajectory is the evidence.

[Figure 16.7: The complete Rosetta trajectory. Four stations, three geometric levels, one ascending path. From whale clicks (signal geometry, opaque meaning) through birdsong (signal geometry, known meaning) and cuneiform (hierarchical geometry, partial meaning) to moral reasoning (semantic geometry, gauge-invariant meaning). The arrow points from structure to meaning. The distance remaining is the distance to decoding.]

---

**Series cross-references.** Signal geometry: Ch. 4--6 of this volume; GM Ch. 4--5. Hyperbolic embeddings: Ch. 5 of this volume; GM Ch. 4.6. TDA: Ch. 6 of this volume; GM Ch. 5. SPD manifolds: Ch. 4 of this volume; GM Ch. 4.6. Parallel transport and holonomy: Ch. 10 of this volume; GR Ch. 4. Gauge invariance: Ch. 11--13 of this volume; GR Ch. 8. $D_4$ group: Ch. 13 of this volume; GE Ch. 8. The Rosetta trajectory: introduced in Ch. 1, developed through Ch. 7--12, completed here.

*GR = Geometric Reasoning. GE = Geometric Ethics. GM = Geometric Methods.*

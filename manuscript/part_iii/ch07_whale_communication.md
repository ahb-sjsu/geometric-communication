# Chapter 7: The Geometry of Whale Communication

> *"One cannot help but be in awe when he contemplates the mysteries of eternity, of life, of the marvelous structure of reality."*
> --- Albert Einstein

> **ARRIVAL**
>
> *On 18 November 2024, a hydrophone towed behind a small research vessel off the southwest coast of Dominica recorded a sequence of five broadband clicks, spaced at intervals of approximately 0.35, 0.35, 0.22, and 0.22 seconds. The pattern --- two long pauses followed by two short --- had been catalogued thousands of times by the Dominica Sperm Whale Project. It was a 5R3 coda: five clicks, regular rhythm, variant 3.*
>
> *But the catalogue entry tells us almost nothing. It tells us the name, not the geometry. It does not tell us that 5R3 occupies a specific position in hyperbolic space, close to 5R1 and 5R2 (which share its click count and rhythm class) but distant from 4i1 (which differs in both). It does not tell us that the inter-click interval point cloud for 5R3 has a characteristic topological signature --- tight clustering in $H_0$, low persistence in $H_1$ --- that distinguishes it from irregular and compound codas. It does not tell us that small perturbations to the acoustic signal can flip the decoder's classification to 4R2 but never to 1+1+3, revealing an asymmetric boundary structure in the coda space. It does not tell us that this particular whale produces 5R3 with inter-click intervals that are statistically distinguishable from every other whale in the dataset --- identity encoded in the metric, content encoded in the topology.*
>
> *This chapter tells those things. It presents the first complete geometric analysis of a non-human communication system --- all three geometries from Part II, applied to 8,719 annotated codas, producing five findings that together reveal a communication system with structure far richer than any scalar summary could suggest.*

---

## 7.1 The Dataset and the Question

The Dominica Sperm Whale Project (DSWP) has been recording sperm whale (*Physeter macrocephalus*) vocalisations off the coast of Dominica since 2005. The dataset used in this chapter --- released publicly by Sharma et al. (2024) under a CC BY 4.0 licence --- comprises 8,719 annotated codas spanning 28 coda types, with click counts ranging from 3 to 10. Each coda is annotated with up to 9 inter-click intervals (ICIs), total duration, coda type label, social unit identifier, and individual whale identifier. A companion exchange-level dialogues dataset provides 3,840 sequentially ordered entries across 11 identified whales, enabling analysis of turn-taking and sequential structure.

The coda types decompose into four rhythm classes: regular (xR), deceleration (xD), irregular (xi), and compound (x+y). The three most frequent types --- 1+1+3, 5R1, and 5R3 --- account for approximately 50% of all codas. The distribution is heavily skewed: a handful of types dominate, while many types appear only rarely.

[Figure 7.1: Dataset overview. (Left) Distribution of the 20 most frequent coda types in the DSWP dataset. The compound type 1+1+3 and regular types 5R1, 5R3 dominate. (Right) Click count histogram; the majority of codas contain 4--6 clicks.]

The landmark contribution of Sharma et al. (2024) was to show that this coda system is not a simple repertoire of fixed call types. It is a combinatorial phonetic system --- decomposable into four independently controlled features: rhythm (18 types), tempo (5 types), rubato (3 types), and ornamentation (2 types), yielding a combinatorial space of up to 540 configurations. Subsequent work by Begus et al. (2024, 2025) identified vowel-like spectral patterns within individual clicks, adding a fifth phonetic dimension. The complexity is not metaphorical. It is structural, measurable, and --- as this chapter demonstrates --- geometric.

The question this chapter addresses is not *what do the codas mean?* We do not know the answer to that question, and we will not pretend to. The question is: *what geometric structure does the coda system possess, and what does that structure tell us about the nature of cetacean communication?*

The answer comes in five parts, each grounding a mathematical tool from Part II in empirical evidence. Together, they constitute the first step on the Rosetta trajectory introduced in Chapter 1: the extraction of structure from a communication system whose semantics remain opaque.

---

## 7.2 Finding I: Hyperbolic Embedding of the Coda Hierarchy

### 7.2.1 The Taxonomic Tree

The 28 coda types in the DSWP dataset have a natural hierarchical structure. Each type is specified by a path through a three-level taxonomy:

1. **Rhythm class**: regular (R), deceleration (D), irregular (i), or compound (+).
2. **Click count**: 3, 4, 5, 6, 7, 8, 9, or 10.
3. **Variant**: within a given rhythm class and click count, multiple variants may exist (e.g., 5R1, 5R2, 5R3 are three variants of 5-click regular codas).

This taxonomy is tree-like by construction. And as Chapter 5 established, tree-like structures have a natural home: not in Euclidean space, where the polynomial growth of volume cannot accommodate exponential branching without distortion, but in hyperbolic space, where volume grows exponentially with radius to match.

The theoretical prediction is clear. The practical question is whether it matters for a taxonomy this small. With only 28 types and 3 discrete distance levels, does hyperbolic embedding offer any advantage over Euclidean methods?

### 7.2.2 The Embedding

We constructed a taxonomic distance matrix $D \in \mathbb{R}^{28 \times 28}$ by computing the number of levels at which two coda types first differ, yielding integer distances in $\{0, 1, 2, 3, 4\}$. The 28 types were then embedded into a Poincare ball of curvature $c = 1.0$ and dimension $d = 16$ via gradient descent minimising the mean squared error between embedded hyperbolic distances and normalised taxonomic distances. Three Euclidean baselines were computed for comparison: PCA on the distance matrix, classical multidimensional scaling (MDS), and Isomap.

[Figure 7.2: Poincare ball versus Euclidean embeddings of the coda type hierarchy. (Left) Poincare ball embedding: the unit disk boundary represents the ideal boundary of hyperbolic space. Coda types are coloured by rhythm class. Hierarchically related types (e.g., 5R1, 5R2, 5R3) cluster at similar radii while distinct rhythm classes separate angularly, providing an interpretable two-dimensional visualisation. (Right) Euclidean PCA embedding of the same distance matrix.]

The results were honest and instructive. In terms of pure distance preservation (Spearman $\rho$ between embedded and true taxonomic distances), classical MDS achieved the highest rank correlation ($\rho = 0.79$), with PCA comparable ($\rho = 0.79$) and Isomap close behind ($\rho = 0.77$). The Poincare embedding achieved lower $\rho$. At this scale --- 28 types, 3 distance levels, ample embedding dimensions --- Euclidean methods have sufficient capacity to preserve the hierarchy. The theoretical $O(\log n)$ distortion advantage of hyperbolic space (Sarkar, 2011) is expected to manifest more clearly for larger, deeper trees, such as the full 540-configuration combinatorial space that the rhythm $\times$ tempo $\times$ rubato $\times$ ornamentation decomposition implies.

But distortion is not the only criterion. The Poincare ball offers two advantages that matter for communication analysis.

### 7.2.3 Interpretability and the Radial-Angular Decomposition

The first advantage is interpretability. On the Poincare disk, the radial coordinate encodes depth in the hierarchy, and the angular coordinate encodes sibling relationships. This is not a post hoc interpretation; it is a mathematical consequence of the distance formula (Definition 5.5 in Chapter 5). Moving a point radially toward the boundary moves it deeper into the hierarchy. Moving it angularly at fixed radius moves it among siblings at the same hierarchical level.

In the coda embedding, this decomposition is directly visible. The four rhythm classes --- regular, deceleration, irregular, compound --- separate angularly around the disk, occupying distinct angular sectors. Within each sector, variants of the same click count cluster at similar radii. The 5R variants (5R1, 5R2, 5R3) form a tight radial cluster in the regular sector; the compound codas (1+1+3, 2+3, 3+1+3) occupy a distinct angular region with their own radial structure. The visualisation is not merely pretty. It is a direct, readable map of the taxonomy.

The Euclidean embeddings, by contrast, capture the same distances but lack a natural interpretation of the coordinate axes. PCA and MDS produce geometrically adequate layouts, but the meaning of "left versus right" or "up versus down" in these plots is arbitrary and depends on the particular eigendecomposition. In the Poincare ball, the radial and angular coordinates have intrinsic geometric meaning.

### 7.2.4 Classification: Hyperbolic Multinomial Logistic Regression

The second advantage is that the hyperbolic embedding provides a natural initialisation for downstream classification. A Hyperbolic Multinomial Logistic Regression (HyperbolicMLR) classifier was trained on 11-dimensional feature vectors: 9 duration-normalised ICI features (ICI divided by total coda duration, yielding a tempo-invariant rhythm representation), log-duration, and normalised click count. Features were standardised, mapped to the Poincare ball via the exponential map at the origin (with scaling calibrated to the 95th percentile of input norms, target norm $= 0.3$), and classified using class prototypes initialised from the taxonomic Poincare embeddings. Training used Adam optimisation with cosine learning rate annealing over 500 epochs.

The result: 74.3% classification accuracy, competitive with Euclidean baselines (logistic regression, $k$-nearest neighbours with $k = 5$, random forest with 100 trees), all trained on the same standardised features with an 80/20 stratified random split.[^1]

[^1]: We note an important caveat. This split does not account for within-individual or within-session correlations; codas from the same whale may appear in both training and test sets. Grouped cross-validation (leave-one-whale-out or leave-one-session-out) would provide a more conservative and ecologically meaningful estimate. The accuracy reported here should be interpreted as a method comparison on the same split, not as an estimate of generalisation to novel individuals.

[Figure 7.3: Classification results. (Top left) HyperbolicMLR training loss. (Top right) Classification accuracy comparison across methods. (Bottom) Confusion matrices for the HyperbolicMLR classifier (left) and the best Euclidean baseline (right). All classifiers use the same 11-dimensional feature representation with an 80/20 stratified random split.]

The headline is not that hyperbolic beats Euclidean. At this scale, it does not --- and we do not claim otherwise. The headline is that the hyperbolic classifier, initialised from a geometrically meaningful embedding of the taxonomic hierarchy, achieves competitive accuracy while producing class prototypes that have interpretable positions in the Poincare ball. Each prototype's radial position encodes its hierarchical depth; each prototype's angular position encodes its relationship to other types. The classifier is not a black box. It is a geometric map of coda space.

### 7.2.5 Connection to Chapter 5

This is the empirical payoff of the mathematical framework developed in Chapter 5. The Poincare ball model was introduced there as a theoretical tool for representing hierarchy. Here, applied to the first non-human communication system analysed in this book, it performs exactly as predicted: competitive classification accuracy with interpretable structure. The coda taxonomy --- rhythm class $\to$ click count $\to$ variant --- embeds naturally in hyperbolic space, and the embedding reveals relationships (which types are "between" others, which are peripheral, which are central) that flat representations obscure.

The deeper prediction --- that hyperbolic advantage will grow with the size of the taxonomy --- awaits testing on the full 540-configuration combinatorial space. That is a concrete target for future work, not a promissory note.

---

## 7.3 Finding II: Topological Signatures per Rhythm Class

### 7.3.1 From Inter-Click Intervals to Point Clouds

The Poincare embedding captures the hierarchical structure of coda *types*. But each type is not a single point; it is a population of individual coda productions, each with slightly different inter-click intervals. The variation within a type is where the topology lives.

For each coda type with at least 40 samples, we constructed an ICI point cloud in $\mathbb{R}^9$ --- each coda represented as a 9-dimensional vector of its inter-click intervals, zero-filled for codas with fewer than 10 clicks. This is not a Takens embedding (which reconstructs an attractor from a single time series); it is a direct embedding of the ICI feature space, where each point represents one production of a coda type, and the geometry of the point cloud reflects the variability of that type's production.

We computed Vietoris--Rips persistent homology up to dimension 1 using Ripser (Bauer, 2021; Tralie et al., 2018), with point clouds exceeding 300 points randomly subsampled for computational tractability. Eight features were extracted per homology dimension: count, maximum lifetime, total lifetime, mean birth time, mean death time, mean lifetime, lifetime standard deviation, and persistence entropy.[^2]

[^2]: Because zero-filling can introduce artificial structure in Euclidean distances (padding with zeros effectively collapses short codas onto a lower-dimensional subspace), we verified that restricting analysis to full-length vectors (codas with $\geq 10$ clicks) produced qualitatively similar persistence diagrams. The zero-filled analysis is reported because it includes more coda types, but the topological conclusions are robust to this methodological choice.

### 7.3.2 What the Persistence Diagrams Reveal

The persistence diagrams revealed systematic topological differences across rhythm classes --- exactly the kind of structural differentiation that summary statistics (means, variances) cannot capture.

**Regular codas (xR)** exhibited tight clusters with low $H_1$ persistence. This is the topological signature of a concentrated, roughly spherical point cloud: many small connected components that merge quickly ($H_0$ features are born and die at small scales), and few or no persistent loops ($H_1$ features are absent or short-lived). Geometrically, this makes sense. Regular codas have temporally uniform ICI patterns --- the clicks are evenly spaced, with minimal variation. The point cloud in ICI space is therefore tightly clustered around the centroid, and its topology is trivial: one connected component, no loops.

**Irregular codas (xi)** produced higher $H_1$ persistence --- persistent loops in the ICI point cloud. This indicates that the timing variability of irregular codas is not random noise spread uniformly around a centre. It is structured variability that creates topological features: closed paths in the ICI space through which individual productions cycle. The loop structure suggests that the timing variation has a preferred pattern --- perhaps alternating between two or more timing configurations --- rather than being isotropic.

**Compound codas (x+y)** showed elevated $H_0$ persistence --- multiple distinct connected components that persist over a wide range of scales. This is the topological hallmark of multi-modal structure. A compound coda like 1+1+3 consists of two sub-groups of clicks with a longer pause between them; the ICI pattern therefore has two natural scales (within-group and between-group), producing a point cloud with multiple clusters. Persistent homology detects this multi-component structure directly.

[Figure 7.4: Persistence diagrams by coda type. Each panel shows the $H_0$ (connected components, blue) and $H_1$ (loops, orange) persistence diagrams for one coda type. Points far from the diagonal indicate long-lived topological features. Rhythm classes exhibit systematically different topological complexity.]

[Figure 7.5: Topological feature summary. (Left) $H_1$ loop count versus maximum $H_1$ lifetime for each coda type, coloured by rhythm class. (Right) Total $H_1$ persistence ranked by coda type. Irregular and compound types show higher topological complexity.]

### 7.3.3 Invariance: Why Topology Matters for Field Recordings

These topological signatures possess a property that is not merely mathematically elegant but practically essential: they are invariant to monotone transformations of the distance metric. If every ICI is scaled by a constant factor (because the whale was recorded from a different distance, or the hydrophone has different gain, or the water temperature affects click propagation speed), the persistence diagram does not change. If noise adds a small perturbation to every ICI, the stability theorem (Chapter 6, Section 6.2) guarantees that the persistence diagram changes by at most the magnitude of the perturbation.

For field recordings of cetacean communication --- where recording conditions vary enormously from session to session, where background noise includes shipping, wave action, and the clicks of other whales, where the distance between hydrophone and animal is rarely known precisely --- this invariance is not a luxury. It is a requirement. Any feature that depends on the absolute magnitude of ICIs is confounded by recording conditions. Topological features, by construction, are not.

This is the empirical instantiation of the theoretical argument made in Chapter 6: persistent homology captures the *shape* of the signal in phase space, not its *magnitude*. For whale codas, the shape is the rhythm --- the pattern of relative timing --- and the magnitude is the absolute tempo, which varies with arousal, social context, and recording conditions. Topology separates them.

### 7.3.4 The Clean Separation of Content and Structure

The topological analysis achieves something that no scalar classifier can: a clean separation between the *type-level content* of a coda (which rhythm class, which pattern) and the *production-level variability* (how tightly clustered, how structured the variation). The persistence diagram of a coda type is a geometric object that characterises the entire population of productions, not just any single instance.

This separation will become critical in Finding V (Section 7.6), where we show that individual identity is encoded in the *metric* --- the precise distances between clicks --- while type-level content is encoded in the *topology*. The topological signatures of this section are the content channel; the metric signatures of Section 7.6 are the identity channel. The communication manifold has at least two independent factors, and geometry cleanly separates them.

---

## 7.4 Finding III: Adversarial Robustness and the Decoder Robustness Index

### 7.4.1 The Motivation: What Happens When the Signal Degrades?

A classification system tells you what a coda *is*. An adversarial analysis tells you what a coda is *not* --- and what it could become under perturbation. The distinction matters. Two coda types with identical classification accuracy may have radically different robustness profiles: one may be surrounded by a wide moat of acoustic space in which perturbation cannot change the classification, while the other may sit on a knife-edge where a small perturbation flips the decoder to a different type. The accuracy metric does not distinguish these cases. The geometry of the decision boundary does.

This is a direct application of the adversarial robustness framework introduced in *Geometric Ethics* (Bond, 2026b, Ch. 22) and adapted here for cetacean communication. The core idea: do not just ask "how accurate is the decoder?" Ask "how *fragile* is the decoder, and where are the fracture lines?"

### 7.4.2 The Decoder Robustness Index

We introduced the Decoder Robustness Index (DRI) --- the first adversarial robustness benchmark for cetacean communication decoders. The DRI works as follows.

Coda signals were synthesised from ICI data as Gaussian-enveloped 5 kHz click trains at 32 kHz sample rate.[^3] Nine parametric acoustic transforms were applied at 11 graduated intensity levels (0.0 to 1.0):

[^3]: The use of synthesised signals is a limitation. The DRI results characterise robustness-to-perturbation-of-the-synthesis-model, not robustness under real ocean acoustics. Raw DSWP audio is publicly available and a validation run on real recordings would substantially strengthen the ecological validity. We prioritise this for follow-up work.

1. Additive Gaussian noise
2. Pink noise
3. Doppler shift
4. Multipath echo
5. Amplitude scaling
6. Time stretch
7. Spectral mask
8. Click dropout
9. Circular time shift

Each transform satisfies the identity property: at intensity 0.0, the signal is unchanged. Four transforms --- amplitude scaling, time shift, additive noise, pink noise --- are designated as *invariant*: a correct decoder should tolerate them, because they do not alter the ICI structure. The remaining five are *stress transforms* that legitimately alter the signal's temporal or spectral properties.

For each perturbed signal, ICIs are re-extracted from the perturbed waveform using a peak-detection click detector (minimum inter-click gap $= 10$ ms, amplitude threshold $= 0.3 \times$ peak). The re-extracted ICIs are passed to a nearest-centroid decoder. This end-to-end pipeline --- perturb the waveform, re-extract features, classify --- ensures that waveform perturbations affect the decoder only through their impact on extractable ICI features, not through direct feature manipulation.

The graduated semantic distance between baseline and perturbed classifications is:

$$\omega(y, \hat{y}) =
\begin{cases}
0 & \text{if } y = \hat{y}, \\
\max\!\left(0.5,\; 0.5 + 0.5 \cdot \frac{\sum_{f} w_f \cdot \mathbf{1}[y_f \neq \hat{y}_f]}{\sum_{f} w_f}\right) & \text{otherwise},
\end{cases}$$

where the sum ranges over the combinatorial features $f \in \{\text{rhythm}, \text{tempo}, \text{rubato}, \text{ornamentation}\}$, with importance weights $w_{\text{rhythm}} = 1.0$, $w_{\text{tempo}} = 0.7$, $w_{\text{rubato}} = 0.4$, $w_{\text{ornamentation}} = 0.2$. The minimum penalty of 0.5 ensures that any classification flip is registered; the weighted sum captures how *semantically distant* the misclassification is. A flip within the same rhythm class is penalised less than a flip across rhythm classes.

The scalar DRI aggregates $\omega$ values across all transform--intensity--signal combinations:

$$\text{DRI} = 0.5 \cdot \bar{\omega} + 0.3 \cdot \omega_{75} + 0.2 \cdot \omega_{95}$$

The weights (0.5/0.3/0.2) follow the Bond Index convention, emphasising tail behaviour --- the worst-case perturbations are more informative than the average case, because they expose structural vulnerabilities.

[Figure 7.6: Decoder Robustness Index results. (Left) Per-transform sensitivity profile: mean $\omega$ at full intensity. Red bars indicate high vulnerability. (Centre) Adversarial flip thresholds: the minimal intensity at which each transform causes a classification change. Lower thresholds indicate greater vulnerability. (Right) DRI gauge showing the overall decoder robustness score.]

### 7.4.3 The Transform Sensitivity Spectrum

The results revealed a clear hierarchy of acoustic vulnerability.

**Click dropout** caused the highest boundary crossing rate (50% at full intensity), confirming that individual clicks are the primary information-carrying elements of the coda. Remove a click, and the decoder loses information. This is not surprising --- it would be surprising if it were otherwise --- but the quantification is useful: a 50% flip rate at full dropout intensity means that the coda system is *not* highly redundant at the level of individual clicks.

**Time shift** caused 40% crossings, despite being theoretically invariant for a correct decoder (shifting a click train in time should not change its ICI pattern). This exposed a specific vulnerability in the nearest-centroid pipeline: the peak-detection click detector is sensitive to the alignment of clicks with the analysis window, and temporal shifts that move a click outside the detection window mimic click dropout. This is a finding about the decoder, not about the whales --- but it is precisely the kind of finding that adversarial testing is designed to surface.

**Multipath echo and spectral mask** caused less than 2% crossings, indicating that these acoustic dimensions carry minimal semantic content in the ICI-based representation. The ICI features are robust to spectral corruption because they depend on timing, not on the spectral shape of individual clicks. This robustness has a geometric interpretation: the ICI feature space and the spectral feature space are approximately orthogonal, and perturbations along one dimension do not cross boundaries in the other.

### 7.4.4 Asymmetric Boundaries: The Geometry of the Decision Space

The most striking finding was the asymmetry of classification boundary crossings.

The transition matrix of decoder misclassifications revealed a mean boundary asymmetry of 0.87 on a 0--1 scale, where 0 indicates perfectly symmetric boundaries and 1 indicates purely unidirectional transitions. The asymmetry was extreme: perturbation of 5R3 codas caused misclassification as 4R2 in 223 instances, while the reverse --- 4R2 perturbed to resemble 5R3 --- occurred 0 times.

This asymmetry is a geometric statement about the structure of coda space. It means that the decision boundaries between coda types are not equidistant from their respective centroids. The boundary between 5R3 and 4R2 is close to 5R3 but far from 4R2. In the language of Chapter 3's communication manifold, the metric on coda space is anisotropic: the "distance" from type A to the boundary with type B is not equal to the distance from type B to the boundary with type A.

An asymmetry this strong ($\bar{a} = 0.87$) means that the phonetic neighbourhood structure of coda space is best represented not as an undirected graph (where adjacency is symmetric) but as a *directed* graph, where edges are weighted by adversarial vulnerability. Some types are robust neighbours (hard to perturb into each other in either direction); others are asymmetric neighbours (one can be perturbed to resemble the other, but not vice versa). The directed graph is a geometric object --- it is the adjacency structure of the decision boundary manifold --- and it carries information about the communication system that no symmetric distance metric can encode.

We emphasise the appropriate caveat: this asymmetry characterises the *decoder's decision boundaries*, not necessarily the whales' perceptual space. Replication across multiple decoder architectures (calibrated random forest, gradient-boosted classifier, deep learning models such as WhAM) would be needed to establish whether the asymmetry is a property of the signal space itself rather than an artifact of the nearest-centroid pipeline. The DRI framework is designed to be decoder-agnostic; the replication is technically straightforward.

If the asymmetry persists across decoders, it would constitute evidence that the coda combinatorial space possesses a non-trivial geometry with preferred transition directions --- potentially reflecting acoustic or perceptual constraints on coda production and reception.

### 7.4.5 Per-Type Robustness and Information Content

The per-type robustness analysis revealed an ordering consistent with the topological signatures of Finding II. Irregular codas exhibited the highest mean activation threshold (0.944 --- meaning that perturbation intensity must exceed 0.944 before classification flips), while compound codas were least robust (threshold = 0.800). This ordering makes geometric sense: irregular codas, which occupy a wide territory in ICI space (high topological complexity, spread-out point clouds), have more room to absorb perturbation before crossing a boundary. Compound codas, which have multi-component structure concentrated in specific ICI configurations, sit closer to decision boundaries.

All eight tested coda types (the most frequent in the dataset) remained well-separated under perturbation, with activation thresholds exceeding 0.5. This yields a lower bound of $\log_2(8) = 3.0$ bits of robustly decodable information per coda.[^4] This is not a channel capacity in the information-theoretic sense --- computing $I(\text{true}; \text{decoded})$ under a realistic perturbation distribution with confidence intervals remains future work. But it exceeds the unigram entropy of the rhythm distribution alone ($H(R) = 2.1$ bits), confirming that more than rhythm class is recoverable from a single coda under noisy conditions.

[^4]: The full combinatorial space --- rhythm (18) $\times$ tempo (5) $\times$ rubato (3) $\times$ ornamentation (2) $= 540$ configurations --- would yield up to $\log_2(540) \approx 9.1$ bits if all features were independently decodable. The gap between our empirical 3.0-bit lower bound and the theoretical 9.1-bit ceiling quantifies the information carried by sub-rhythm features and represents a concrete target for future decoder development.

The connection to the adversarial robustness framework from *Geometric Ethics* is direct. There, the Bond Index measured how robust an AI system's ethical judgements are to adversarial perturbation of the input. Here, the DRI measures how robust a coda decoder's classifications are to adversarial perturbation of the acoustic signal. The mathematical structure is identical: a perturbation space, a decision function, a boundary-crossing criterion, and a scalar index that aggregates vulnerability across the perturbation space. What changes is the domain. The fact that the same framework applies to AI ethics and whale communication is not a coincidence. It reflects the domain generality of the geometric approach: adversarial robustness is a property of any classification system defined on a metric space, regardless of what the space represents.

---

## 7.5 Finding IV: Linguistic Universals in Coda Communication

### 7.5.1 The Question of Universality

If sperm whale codas are a communication system, do they share statistical properties with other communication systems? The question is not about whether whales "have language" --- a question that conflates many distinct capabilities and invites fruitless definitional debates. The question is narrower and answerable: do the statistical regularities that characterise human language, and that information-theoretic arguments suggest should characterise *any* efficient communication system, also appear in coda exchanges?

We tested four specific universals, each with a clear quantitative prediction and a geometric interpretation.

### 7.5.2 Menzerath's Law

Menzerath's law (also called Menzerath-Altmann's law) states that the longer a linguistic construct, the shorter its constituents. In human language: longer words have shorter syllables; longer sentences have shorter words. The law has been documented across multiple human languages and, in recent cross-species meta-analyses (Youngblood et al., 2025), across multiple cetacean species.

For sperm whale codas, the prediction is: longer codas (more clicks) should have shorter mean inter-click intervals.

The result: Spearman $r = -0.269$, $n = 8{,}719$, $p < 10^{-144}$.

The effect is real. Longer codas compress their constituents. With a sample size of 8,719, even weak correlations achieve extreme statistical significance, and the $p$-value alone is uninformative. The relevant quantity is the effect size: $|r| = 0.269$ represents a modest but robust negative association. Clicks in longer codas are, on average, more tightly spaced than clicks in shorter codas.

[Figure 7.7: Menzerath's law in sperm whale codas. Mean ICI decreases with click count ($r = -0.269$, $p < 10^{-144}$). Each point represents one coda; the trend line shows the negative association between construct length and constituent duration.]

What does Menzerath's law mean geometrically? On the communication manifold $M = S \times P \times C$ (Chapter 3), Menzerath's law is a constraint on the signal manifold $S$: it says that the trajectory of a coda through signal space (the sequence of ICIs) is not arbitrary. Longer trajectories (more clicks) are constrained to have shorter steps (shorter ICIs). This is a curvature constraint --- it limits the set of paths that communication can trace through signal space, concentrating longer utterances in a region of $S$ characterised by compressed timing. In the language of differential geometry, Menzerath's law constrains the geodesics of the signal manifold to satisfy a length-step inverse relationship.

We note that a mixed-effects model with random intercepts for whale and recording session would provide a more rigorous test by accounting for pseudo-replication (multiple codas from the same whale in the same session are not independent). We report the simple correlation here as a first-order confirmation, consistent with the cross-species meta-analysis of Youngblood et al. (2025).

### 7.5.3 Zipf's Law and the Rank-Frequency Distribution

The rank-frequency distribution of coda types follows a Zipf-like power law with fitted exponent $\alpha = 1.44$ (nonlinear least-squares on ranks). This is steeper than the $\alpha \approx 1.0$ typical of human language, indicating a more skewed distribution dominated by a few high-frequency types (1+1+3, 5R1, 5R3).

[Figure 7.8: Rank-frequency distribution of coda types, with fitted power law ($\alpha = 1.44$). The distribution is Zipf-like but steeper than typical human language ($\alpha \approx 1.0$), indicating greater dominance by a few high-frequency types.]

We emphasise that this fit is descriptive. With only 28 distinct types, formal power-law testing (MLE with Kolmogorov--Smirnov goodness-of-fit and comparison against log-normal alternatives) lacks statistical power, and we do not claim the distribution is a true power law. The Zipf-like skew is consistent with frequency-dependent selection pressures reported across cetacean species.

Zipf's law of abbreviation --- the prediction that more frequent types should be shorter in duration --- was not statistically significant at the type level ($r = -0.129$, $p = 0.50$). This likely reflects the small number of distinct types (28) rather than an absence of the effect; with 28 data points, the test has low power to detect a moderate correlation.

### 7.5.4 Sequential Structure: Markov Chains on Coda Space

Coda exchanges are not random sequences. Consecutive codas exhibit statistical dependencies that extend beyond pairwise associations.

The mutual information between consecutive rhythm types was $I(R_t; R_{t+1}) = 0.380$ bits, representing 18.0% of the unigram entropy ($H(R) = 2.111$ bits). In other words, knowing the current coda's rhythm type reduces uncertainty about the next coda's rhythm type by 18%. This is a first-order Markov dependency --- the present predicts the future.

But the structure extends further. Trigram prediction accuracy (71.2%) exceeded bigram accuracy (66.1%), demonstrating that the sequential structure involves at least two preceding codas. This is consistent with higher-order Markov dependencies --- or, equivalently, with a hidden state that influences multiple consecutive outputs.

The geometric interpretation is immediate. A Markov chain on coda types is a random walk on a graph --- and the transition probabilities define a metric on that graph. Types that frequently follow each other are "close" in the Markov metric; types that never co-occur in sequence are "far." This Markov metric is a geometric object on the communication manifold, distinct from the ICI metric (which measures acoustic similarity) and the taxonomic metric (which measures hierarchical distance). The coda system has at least three natural metrics: acoustic, taxonomic, and sequential. Their relationship to each other --- whether types that are acoustically close are also sequentially adjacent --- is an empirical question whose answer would reveal the geometry of coda conversations, not just individual codas.

### 7.5.5 Turn-Taking: The Temporal Structure of Dialogue

The most suggestive finding among the linguistic universals concerns turn-taking. If whales are engaged in communicative exchange --- as opposed to broadcasting independently --- we would expect the latency between one whale's coda and another whale's response to differ from the latency between successive codas from the same whale.

It does. Cross-whale response latency ($\bar{x} = 2.25$ s, $n = 2{,}225$) was approximately half that of same-whale continuation latency ($\bar{x} = 4.68$ s, $n = 1{,}379$). The distributional difference was large: Kolmogorov--Smirnov $D = 0.560$, $p < 10^{-247}$. The $p$-value, as with all tests on this dataset, reflects the large sample size; the effect size ($D = 0.56$, $2.08\times$ latency ratio) is the informative quantity.

[Figure 7.9: Turn-taking structure. (Left) Distribution of inter-coda latencies for same-whale continuations (blue) and cross-whale responses (orange). Cross-whale responses are approximately twice as fast. (Right) Latency ratio by whale pair, showing consistency of the turn-taking pattern.]

The finding is striking. When a different whale responds, the response comes faster --- roughly half the time that the same whale takes to produce its next coda. This pattern is consistent with active turn-taking, in which whales are monitoring each other's vocalisations and initiating responses promptly, rather than vocalising independently at their own rate. The faster cross-whale latency suggests that a response is, in some sense, *prepared* before the preceding coda ends --- that the responding whale is processing the incoming signal and readying its reply while the first whale is still vocalising.

We note the appropriate caveats. The latencies are likely non-independent within recording sessions and dyads; a hierarchical model with random intercepts for session and whale pair would provide a more rigorous test. The large effect size ($D = 0.56$) is robust, but alternative explanations (e.g., arousal-dependent call rate, where cross-whale transitions occur during periods of higher social excitement and hence faster calling) cannot be ruled out from timing data alone.

### 7.5.6 The Geometric Interpretation of Universals

Why should a non-human communication system satisfy the same statistical regularities as human language? The information-theoretic explanation is that these regularities are not properties of *language* per se. They are properties of *any efficient communication system operating under constraints*. Menzerath's law reflects compression: longer messages compress their constituents to stay within temporal or energetic budgets. Zipf's law reflects the trade-off between vocabulary size and utterance frequency. Markov structure reflects context-dependent production. Turn-taking reflects the timing requirements of interactive dialogue.

These regularities are constraints on the communication manifold --- they limit the region of $M = S \times P \times C$ that a communication system can inhabit. A system that violates Menzerath's law is spending more energy than necessary on long utterances. A system that violates Markov structure is not exploiting context to reduce redundancy. A system without turn-taking structure is broadcasting, not conversing.

The fact that sperm whale codas satisfy all four universals does not prove that codas are "language." It proves something more precise: that the coda system occupies a region of the communication manifold that is also occupied by human language. The geometric neighbourhood is shared. The specific content may be entirely different.

---

## 7.6 Finding V: Individual Identity Encoding

### 7.6.1 The Same Type, Different Whale

The four findings above concern the structure of coda types --- categories that are shared across a social unit or clan. But communication is not only about *what is said*. It is also about *who is speaking*. Does the coda system encode individual identity, and if so, how?

The DSWP dataset includes individual whale identifiers, enabling a direct test. For the most common coda type (1+1+3), we selected four identified whales with at least 10 productions each and compared their ICI distributions pairwise.

The result: all six pairwise Kolmogorov--Smirnov tests yielded $p < 0.001$, and all remained significant after Bonferroni correction for 6 comparisons at $\alpha = 0.05$.

Individual whales produce the same coda type with statistically distinguishable inter-click interval patterns. The same "word" (1+1+3), produced by different whales, has measurably different timing --- not different enough to change the type classification (the rhythm pattern is the same), but different enough that the individual is identifiable from the timing alone.

[Figure 7.10: Individual accents in the 1+1+3 coda type. ICI distributions for four identified whales, showing statistically distinguishable timing patterns within the same coda type. All pairwise KS tests: $p < 0.001$.]

### 7.6.2 Identity in the Metric, Content in the Topology

This finding has a clean geometric interpretation that ties together the five findings of this chapter.

The *coda type* --- what is being communicated at the group or clan level --- is encoded in the topology of the ICI point cloud (Finding II). Regular codas have one topological signature; irregular codas have another; compound codas have a third. This topology is invariant to the individual whale: all whales producing 5R3 produce a point cloud with similar topological features, because the rhythm pattern is shared.

The *individual identity* --- who is communicating --- is encoded in the metric of the ICI point cloud. The precise distances between clicks, the exact timing, the subtle accelerations and decelerations that one whale produces but another does not. This metric structure is *within* the topological class: it does not change the type, but it distinguishes the individual.

In the language of the communication manifold:

$$M = S \times P \times C$$

Content (coda type) lives on the content manifold $C$. It is captured by the topology of the signal: which connected components, which loops, which persistence features. Identity lives on the signal manifold $S$. It is captured by the metric: the precise distances between points in ICI space.

This is a separation of content and identity into orthogonal geometric factors --- topology and metric, respectively. It is not a theoretical postulate; it is an empirical finding. The topology classifies; the metric identifies. The same mathematical framework that gives us persistent homology for content gives us Kolmogorov--Smirnov tests for identity, because the two are operating on different geometric structures of the same underlying space.

### 7.6.3 Dual Function and Hierarchical Encoding

This dual encoding --- type-level content at the group scale, individual-level identity within each type --- extends the identity-encoding hierarchy documented by Gero et al. (2016) and Hersh et al. (2022). Previous work established that social units within vocal clans share coda repertoires but exhibit unit-level and individual-level variation in production. Our geometric analysis provides a precise mathematical characterisation of how this hierarchical encoding works: the hierarchy maps cleanly onto the topology/metric distinction.

The dual function also suggests a possible resolution to a long-standing question in cetacean communication: why do codas have both type-level structure (the rhythm pattern) and within-type variation (the individual timing)? If type-level structure carries content (social identity, group membership, contextual signalling) and within-type variation carries individual identity (who is speaking), then the variation is not noise. It is a second communication channel operating within the first --- and the two channels are geometrically orthogonal.

---

## 7.7 The Five Findings as a Geometric Whole

The five findings of this chapter are not independent results that happen to share a dataset. They are five facets of a single geometric structure --- the communication manifold of the sperm whale coda system.

**Finding I** (Poincare embedding) characterises the hierarchical structure of the coda type space: how types relate to each other in a taxonomy of rhythm, click count, and variant. The geometry is hyperbolic; the representation is the Poincare ball.

**Finding II** (topological signatures) characterises the shape of the production space within each type: how individual productions vary around the type centroid. The geometry is topological; the representation is the persistence diagram.

**Finding III** (adversarial robustness) characterises the boundary structure of the classification space: how close each type is to being confused with its neighbours, and in which direction. The geometry is that of the decision boundary manifold; the representation is the directed adversarial graph with mean asymmetry 0.87.

**Finding IV** (linguistic universals) characterises the constraints on the communication space: which regions of the manifold are accessible and which are excluded by information-theoretic pressures. Menzerath's law constrains trajectory curvature ($r = -0.269$). Markov structure constrains sequential transitions ($I = 0.380$ bits). Turn-taking constrains temporal dynamics ($2.08\times$ latency ratio).

**Finding V** (individual identity) characterises the factorisation of the signal: content in the topology, identity in the metric. The two channels are geometrically orthogonal, enabling simultaneous encoding of *what* and *who*.

Together, these findings reveal a communication system that is:

- **Hierarchical** (the type taxonomy has tree-like structure that embeds naturally in hyperbolic space);
- **Topologically structured** (rhythm classes have distinct persistence signatures that are invariant to recording conditions);
- **Asymmetrically bounded** (decision boundaries between types are directional, not symmetric);
- **Statistically universal** (the system satisfies the same information-theoretic regularities as human language); and
- **Dually encoded** (content and identity occupy orthogonal geometric factors of the signal).

No scalar summary --- no classification accuracy, no mutual information, no single correlation coefficient --- captures this structure. The structure is *geometric*. It lives on a manifold. And recovering it requires the tools of differential geometry, algebraic topology, and adversarial analysis that Part II developed.

---

## 7.8 What We Do Not Know

Intellectual honesty demands that we state clearly what the geometric analysis does *not* tell us.

**We do not know what the codas mean.** The geometric tools extract structure from the signal, not semantics from the structure. We know that 5R3 and 5R1 are hierarchically close, that irregular codas have loop topology, that cross-whale responses are fast, and that individuals have distinctive timing. But we do not know what 5R3 *communicates* to another whale, or why 1+1+3 is the most frequent type, or what the Markov structure encodes about conversational context. Structure is a necessary condition for meaning, not a sufficient one.

**We do not know whether the boundary asymmetry is a property of the signal or the decoder.** The mean asymmetry of 0.87 is measured on a single nearest-centroid decoder. If the asymmetry is an artifact of the centroid positions rather than a property of the acoustic space, it will not replicate across decoder architectures. The DRI framework is designed for exactly this replication, and the experiment is a priority for follow-up work.

**We do not know whether the topological signatures reflect perceptual categories.** The persistence diagrams distinguish rhythm classes in the ICI feature space, but the ICI feature space may not correspond to the whales' perceptual space. Sperm whales may attend to spectral features, amplitude patterns, or directional cues that the ICI representation discards. The recent discovery of vowel-like spectral patterns (Begus et al., 2024, 2025) suggests that the ICI representation is incomplete.

**We do not know the dimensionality of the communication manifold.** The five findings suggest at least five independent structural features --- click count, rhythm, tempo, rubato, ornamentation --- but the effective dimensionality of the coda system may be higher (if spectral features constitute additional dimensions) or lower (if some features are correlated and do not vary independently).

These unknowns are not failures of the geometric approach. They are the agenda for the next phase of research. The geometric tools have done what they were designed to do: extract structure from a system we cannot yet translate. Bridging the gap from structure to meaning requires either a Rosetta stone --- parallel whale-human data, which does not exist --- or a formal semantics of coda sequences, which no one has yet proposed. The geometry is the foundation; the semantics is the building that remains to be constructed.

---

## 7.9 From Whales to the Rosetta Trajectory

This chapter is the first major empirical chapter in Part III, and it sets the template for what follows. The three-geometry toolkit --- hyperbolic embeddings for hierarchy, persistent homology for topology, adversarial analysis for boundaries --- was developed in Part II as abstract mathematical machinery. Here, applied to 8,719 sperm whale codas, it produces concrete findings about a concrete communication system: interpretable embeddings, topological invariants, directed boundary graphs, statistical universals, and a clean separation of content and identity.

The next chapter applies the same toolkit to a second non-human communication system: birdsong. The 156-dimensional geometric feature vector --- 136 SPD features, 4 trajectory features, 16 TDA features --- will be deployed on 206 bird species, in a setting where the "meaning" (species identity) is known and the geometric features can be directly validated against it. The whale analysis extracts structure from an opaque system; the birdsong analysis validates the same tools on a transparent one. Together, they constitute the non-human communication evidence for the book's central claim: that communication, across species and across millions of years of evolutionary divergence, has geometric structure that scalar evaluation destroys.

The Rosetta trajectory begins here, with clicks in the Caribbean. It will pass through birdsong in the temperate forest (Chapter 8), cuneiform on Mesopotamian clay tablets (Chapters 9--10), and cross-lingual moral reasoning spanning 2,500 years of human thought (Chapters 11--12). At each station, the same geometric tools apply. The communication systems are as different as biology can make them. The geometry is the same.

---

**Notes on data and reproducibility.** All analyses in this chapter are implemented in the `eris-ketos` Python package (v0.2.0; [PyPI](https://pypi.org/project/eris-ketos/), [GitHub](https://github.com/ahb-sjsu/eris-ketos)). The DSWP coda annotation dataset is available at the [Sharma et al. GitHub repository](https://github.com/pratyushasharma/sw-combinatoriality) under CC BY 4.0 licence. A self-contained Jupyter notebook reproducing all figures and statistical results is included in the eris-ketos repository (`notebooks/cetacean_geometric_analysis.py`, Jupytext percent format). The code is real, the data is public, and the results are reproducible.

**Series cross-references.** Poincare ball model and distortion theorem: Ch. 5 of this volume; GM Ch. 4.6. Persistent homology and stability theorem: Ch. 6 of this volume; GM Ch. 5. Adversarial robustness framework: GE Ch. 22. Communication manifold $M = S \times P \times C$: Ch. 3 of this volume. The Rosetta trajectory: Ch. 1 and Ch. 16 of this volume.

*GR = Geometric Reasoning. GE = Geometric Ethics. GM = Geometric Methods.*

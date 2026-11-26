# Figure placeholders replaced by drawn figures (2026-11-26)

Before the figures of 2026-11-26 were drawn, these chapters carried bracketed descriptions
of intended figures. They were taken out of the chapters when the drawn figures went in,
because their numbers collided with the drawn figures and several described content the
chapter does not contain. They are kept here as the original figure plan. The numbers are
the placeholders' own, not those of the drawn figures. Each carries the verdict reached
when the figures were drawn.

## Placeholder 1.1 (manuscript/part_i/ch01_perplexity_trap.md)

[Figure 1.1: The three failure modes of Translation B, visualized as points in a semantic space. Lexical substitution (1) lies close to the source on two of three axes but displaced on the third. Structural collapse (2) lies in the correct region of topic space but at the wrong structural coordinates. Hallucination (3) is displaced on all axes. All three project to the same point on the scalar BLEU axis.]

**Verdict:** Not drawn. The text gives no coordinates for the failure modes.

## Placeholder 1.2 (manuscript/part_i/ch01_perplexity_trap.md)

[Figure 1.2: The four geometric structures destroyed by BLEU. (a) Metric: synonymous expressions are nearby on the semantic manifold but distant on the lexical surface. (b) Symmetry: word-order variants form an orbit under syntactic transformation; BLEU privileges one element. (c) Fiber: pragmatic equivalents are different points in the total space that project to the same base point. (d) Topology: hierarchical structure is a global property invisible to local $n$-gram windows.]

**Verdict:** Not drawn. A near-duplicate of placeholder 1.3 (four structures destroyed); keep one.

## Placeholder 1.3 (manuscript/part_i/ch01_perplexity_trap.md)

[Figure 1.3: The four geometric structures destroyed by scalar evaluation. (a) Metric: continuous distance replaced by discrete or crude approximation. (b) Symmetry: meaning-preserving transformations broken by privileging one surface form. (c) Fiber: content-expression separation collapsed by evaluating in the total space. (d) Topology: global structure erased by local or pointwise evaluation.]

**Verdict:** Not drawn. A near-duplicate of placeholder 1.2.

## Placeholder 1.4 (manuscript/part_i/ch01_perplexity_trap.md)

[Figure 1.4: Scalar irrecoverability visualized. The quality space is $d$-dimensional. A scalar metric $\pi$ projects onto a line. The preimage of a scalar value $\pi = c$ is a $(d-1)$-dimensional hyperplane (shown as a plane for $d = 3$). All points on this hyperplane are indistinguishable to $\pi$. The geometric structure within the hyperplane --- the distances, symmetries, and topological features that distinguish qualitatively different translations with the same BLEU score --- is irrecoverable from the scalar.]

**Verdict:** Drawn (the level sets of one score, before Section 1.5).

## Placeholder 5.1 (manuscript/part_ii/ch05_hyperbolic_embeddings.md)

[Figure 5.1: The Poincare disk ($d = 2$, $c = 1$). Left: a regular tiling by congruent hyperbolic pentagons, illustrating exponential area growth. Right: geodesics (circular arcs perpendicular to the boundary). Near the boundary, geodesics appear to crowd together---a visual artifact of the conformal factor.]

**Verdict:** Decorative (pentagon tiling); not drawn.

## Placeholder 5.2 (manuscript/part_ii/ch05_hyperbolic_embeddings.md)

[Figure 5.2: Poincare distance structure. Left: Euclidean distance contours (concentric circles of constant Euclidean radius). Right: Hyperbolic distance contours from the origin (concentric circles of constant hyperbolic radius). Near the boundary, hyperbolic contours crowd together, reflecting the exponential growth of distance.]

**Verdict:** Drawn, as a curve.

## Placeholder 5.3 (manuscript/part_ii/ch05_hyperbolic_embeddings.md)

[Figure 5.3: The distortion theorem illustrated. Left: a binary tree of depth 5 embedded in $\mathbb{R}^2$ (Euclidean); significant distortion is visible as distant leaves crowd together. Centre: the same tree embedded in $\mathbb{B}^2_1$ (Poincare disk); the tree structure is faithfully preserved. Right: distortion as a function of embedding dimension for Euclidean (blue) and hyperbolic (red) embeddings; hyperbolic reaches low distortion in far fewer dimensions.]

**Verdict:** The right panel (distortion against dimension) has no data and falls under unresolved item 11.

## Placeholder 5.4 (manuscript/part_ii/ch05_hyperbolic_embeddings.md)

[Figure 5.4: Poincare ball versus Euclidean embeddings of the coda type hierarchy. Left: Poincare ball embedding projected to 2D. Coda types are coloured by rhythm class. Hierarchically related types (e.g., 5R1, 5R2, 5R3) cluster at similar radii while distinct rhythm classes separate angularly. Right: Euclidean PCA embedding of the same distance matrix. Both representations separate the major rhythm classes, but the Poincare embedding provides a more natural visualisation of the hierarchical depth structure.]

**Verdict:** Needs the embedding.

## Placeholder 5.5 (manuscript/part_ii/ch05_hyperbolic_embeddings.md)

[Figure 5.5: Classification results. Top left: HyperbolicMLR training loss over 500 epochs. Top right: accuracy comparison across methods (HyperbolicMLR 74.3%, random forest 72.8%, logistic regression 71.2%, $k$-NN 69.4%). Bottom: confusion matrices for HyperbolicMLR (left) and random forest (right). The confusion structure reveals which coda types the classifiers struggle to distinguish---predominantly types within the same rhythm class.]

**Verdict:** Drawn in part (the accuracies only; the loss curve and confusion matrices are not in the repository).

## Placeholder 5.6 (manuscript/part_ii/ch05_hyperbolic_embeddings.md)

[Figure 5.6: The geometric attention bias for cuneiform. Left: schematic of the ByT5 encoder with additive geometric bias. The bias matrix $B_{\text{geo}}$ is computed from pairwise Poincare distances between byte-level embeddings and added to the attention logits in the first 4 encoder layers. Right: a visualisation of learned Poincare embeddings for a sample of byte tokens, coloured by their most common sign association.]

**Verdict:** The left half is covered by the attention-bias figure of Chapter 9.

## Placeholder 5.7 (manuscript/part_ii/ch05_hyperbolic_embeddings.md)

[Figure 5.7: Scaling comparison. Simulated distortion for random trees of increasing depth and branching factor, embedded in Euclidean $\mathbb{R}^{16}$ (blue) versus Poincare $\mathbb{B}^{16}_1$ (red). At depth 3 and branching factor 4 (comparable to the coda taxonomy), the two are similar. At depth 6 and branching factor 8, hyperbolic embedding achieves 3--5$\times$ lower distortion.]

**Verdict:** Unsupported: 'simulated distortion ... 3 to 5 times lower' has no simulation behind it in the text.

## Placeholder 6.1 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.1: Schematic of the time-delay embedding. Left: a 1D signal $x(t)$ with marked sample points at times $t$, $t + \tau$, and $t + 2\tau$. Right: the corresponding 3D point $\mathbf{v}(t) = [x(t), x(t+\tau), x(t+2\tau)]$ in the reconstructed phase space. Multiple time steps trace out a curve (the reconstructed attractor).]

**Verdict:** Covered by the delay-embedding figures of Chapters 4 and 6.

## Placeholder 6.2 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.2: Effect of delay and dimension on the reconstructed point cloud. A synthetic periodic signal $x(t) = \sin(2\pi t / T)$ embedded with (a) $\tau$ too small: the cloud collapses to the diagonal; (b) $\tau$ optimal: the cloud forms a clean ellipse; (c) $\tau$ too large: the cloud fills a rectangle. Below: (d) $d = 2$: a circle (correct topology); (e) $d = 3$: a torus knot (correct topology, higher resolution); (f) $d = 10$: same topology, unnecessary dimensions.]

**Verdict:** Drawn, and the placeholder is wrong: a pure sine never fills a rectangle at a large delay, and its three-dimensional embedding is an ellipse, not a torus knot.

## Placeholder 6.3 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.3: The Vietoris--Rips filtration. Top row: a point cloud at four increasing values of $\varepsilon$, with the Rips complex drawn. Bottom row: the corresponding persistence diagram, accumulating birth-death pairs as $\varepsilon$ increases. A long-lived $H_1$ loop (the central ring) appears far from the diagonal; short-lived components near the diagonal are noise.]

**Verdict:** Drawn.

## Placeholder 6.4 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.4: The eight summary statistics, illustrated on two persistence diagrams. Left: a diagram with few, persistent $H_1$ features (a clean periodic signal). Right: a diagram with many, short-lived $H_1$ features (a noisy aperiodic signal). The statistics distinguish the two: the left diagram has low count, high max lifetime, high normalized persistence; the right has high count, low max lifetime, low normalized persistence.]

**Verdict:** Could be computed; not drawn.

## Placeholder 6.5 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.5: Persistence diagrams for three coda types, reproduced from the eris-ketos analysis (Bond, 2026). Left: regular coda (5R) --- tight cluster, low persistence. Center: irregular coda (5i) --- dispersed cloud, elevated $H_1$. Right: compound coda (3+1+1) --- multi-component structure, elevated $H_0$. $H_0$ features in blue, $H_1$ features in orange. Points far from the diagonal indicate persistent topological features.]

**Verdict:** Needs data.

## Placeholder 6.6 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.6: Topological feature summary across coda types. Left: $H_1$ loop count versus maximum $H_1$ lifetime for each coda type, colored by rhythm class. Right: total $H_1$ persistence ranked by coda type. Irregular and compound types show systematically higher topological complexity.]

**Verdict:** Needs data.

## Placeholder 6.7 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.7: Point clouds and persistence diagrams for four vocalization types. (a) Sustained tone (Swainson's thrush): clean elliptical loop, single persistent $H_1$ feature. (b) Trill (Pacific wren): thickened loop, multiple $H_1$ features. (c) Complex song (Northern mockingbird): filled region, low $H_1$ persistence. (d) Click train (Downy woodpecker): separated clusters, high $H_0$ persistence.]

**Verdict:** Needs data.

## Placeholder 6.8 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.8: Feature importance for species classification (LightGBM on 156-dimensional geometric features). The top 20 features include contributions from all three components. No single component dominates.]

**Verdict:** Needs data.

## Placeholder 6.9 (manuscript/part_ii/ch06_tda_signal.md)

[Figure 6.9: Robustness comparison across feature types under increasing noise. Horizontal axis: signal-to-noise ratio (dB). Vertical axis: classification accuracy for coda type. Lines: TDA features (16-dim), SPD features (136-dim), MFCCs (13-dim). TDA features maintain accuracy longest as SNR decreases, followed by SPD, followed by MFCCs. Below approximately 3 dB, all feature types degrade.]

**Verdict:** Unsupported: no accuracy-against-SNR numbers are printed, and 'below 3 dB' disagrees with the text's 'stable to about 5 dB'.

## Placeholder 7.1 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.1: Dataset overview. (Left) Distribution of the 20 most frequent coda types in the DSWP dataset. The compound type 1+1+3 and regular types 5R1, 5R3 dominate. (Right) Click count histogram; the majority of codas contain 4--6 clicks.]

**Verdict:** Needs data.

## Placeholder 7.2 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.2: Poincare ball versus Euclidean embeddings of the coda type hierarchy. (Left) Poincare ball embedding: the unit disk boundary represents the ideal boundary of hyperbolic space. Coda types are coloured by rhythm class. Hierarchically related types (e.g., 5R1, 5R2, 5R3) cluster at similar radii while distinct rhythm classes separate angularly, providing an interpretable two-dimensional visualisation. (Right) Euclidean PCA embedding of the same distance matrix.]

**Verdict:** A duplicate of placeholder 5.4.

## Placeholder 7.3 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.3: Classification results. (Top left) HyperbolicMLR training loss. (Top right) Classification accuracy comparison across methods. (Bottom) Confusion matrices for the HyperbolicMLR classifier (left) and the best Euclidean baseline (right). All classifiers use the same 11-dimensional feature representation with an 80/20 stratified random split.]

**Verdict:** A duplicate of placeholder 5.5.

## Placeholder 7.4 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.4: Persistence diagrams by coda type. Each panel shows the $H_0$ (connected components, blue) and $H_1$ (loops, orange) persistence diagrams for one coda type. Points far from the diagonal indicate long-lived topological features. Rhythm classes exhibit systematically different topological complexity.]

**Verdict:** A duplicate of placeholder 6.5.

## Placeholder 7.5 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.5: Topological feature summary. (Left) $H_1$ loop count versus maximum $H_1$ lifetime for each coda type, coloured by rhythm class. (Right) Total $H_1$ persistence ranked by coda type. Irregular and compound types show higher topological complexity.]

**Verdict:** A duplicate of placeholder 6.6.

## Placeholder 7.6 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.6: Decoder Robustness Index results. (Left) Per-transform sensitivity profile: mean $\omega$ at full intensity. Red bars indicate high vulnerability. (Centre) Adversarial flip thresholds: the minimal intensity at which each transform causes a classification change. Lower thresholds indicate greater vulnerability. (Right) DRI gauge showing the overall decoder robustness score.]

**Verdict:** Only 50%, 40% and 'under 2%' are printed, and no DRI value.

## Placeholder 7.7 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.7: Menzerath's law in sperm whale codas. Mean ICI decreases with click count ($r = -0.269$, $p < 10^{-144}$). Each point represents one coda; the trend line shows the negative association between construct length and constituent duration.]

**Verdict:** Needs data.

## Placeholder 7.8 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.8: Rank-frequency distribution of coda types, with fitted power law ($\alpha = 1.44$). The distribution is Zipf-like but steeper than typical human language ($\alpha \approx 1.0$), indicating greater dominance by a few high-frequency types.]

**Verdict:** Drawn (the fitted laws only; the counts are not printed).

## Placeholder 7.9 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.9: Turn-taking structure. (Left) Distribution of inter-coda latencies for same-whale continuations (blue) and cross-whale responses (orange). Cross-whale responses are approximately twice as fast. (Right) Latency ratio by whale pair, showing consistency of the turn-taking pattern.]

**Verdict:** Needs data.

## Placeholder 7.10 (manuscript/part_iii/ch07_whale_communication.md)

[Figure 7.10: Individual accents in the 1+1+3 coda type. ICI distributions for four identified whales, showing statistically distinguishable timing patterns within the same coda type. All pairwise KS tests: $p < 0.001$.]

**Verdict:** Needs data.

## Placeholder 8.1 (manuscript/part_iii/ch08_birdsong.md)

[Figure 8.1: Schematic comparison of the CNN pipeline (left) and the geometric feature pipeline (right). The CNN path: waveform $\to$ mel spectrogram $\to$ EfficientNet $\to$ species probabilities. The geometric path: waveform $\to$ mel spectrogram $\to$ SPD covariance + trajectory $\to$ TDA features from waveform $\to$ LightGBM $\to$ species probabilities. The ensemble combines both paths with learned weights.]

**Verdict:** A sound schematic, not drawn. It says 'learned weights'; the text says tuned on a validation set.

## Placeholder 8.2 (manuscript/part_iii/ch08_birdsong.md)

[Figure 8.2: Covariance matrices for three species. Left: white-throated sparrow (near-diagonal structure, weak cross-frequency correlations, nearly pure tone). Center: wood thrush (banded structure with off-diagonal peaks at harmonic intervals, rich overtone series). Right: brown-headed cowbird (dense, full-rank structure, complex frequency modulation). The species-specific covariance "fingerprint" is visible to the naked eye.]

**Verdict:** Needs data.

## Placeholder 8.3 (manuscript/part_iii/ch08_birdsong.md)

[Figure 8.3: Spectral trajectories on SPD(16), projected to two dimensions via PCA of the log-covariance matrices. Left: a trill (Chipping Sparrow) --- the trajectory oscillates tightly around a single point, with low path length and low deviation. Center: a descending whistle (White-throated Sparrow) --- the trajectory moves in a nearly straight line from high-frequency to low-frequency covariance, with moderate path length but low deviation. Right: a complex song (Wood Thrush) --- the trajectory wanders through a large region of SPD space, with high path length and high deviation.]

**Verdict:** Drawn, without the trill.

## Placeholder 8.4 (manuscript/part_iii/ch08_birdsong.md)

[Figure 8.4: Reconstructed attractors (time-delay embedding, $\tau = 10$, $d = 3$) for three birdsong types. Left: a pure whistle (White-throated Sparrow) --- clean loop, single strong $H_1$ feature. Center: a harmonic song (Wood Thrush) --- torus-like structure, multiple $H_1$ features. Right: a rapid trill (Chipping Sparrow) --- tightly wound spiral, dense $H_0$ cluster with moderate $H_1$.]

**Verdict:** Needs data.

## Placeholder 9.1 (manuscript/part_iv/ch09_cuneiform.md)

[Figure 9.1: The cuneiform sign taxonomy as a hierarchy. Top: the sign form 𒀭 branches into readings AN, DINGIR, Anu, etc. Each reading branches into the words and phrases it participates in. Bottom: the same structure for the sign 𒌓 (UD/UTU/BABBAR), illustrating high branching factor at the reading level. The hierarchy is wide and shallow---precisely the regime described by Proposition 5.3 in Chapter 5.]

**Verdict:** Drawn. Its cross-reference to Proposition 5.3 works against it: that proposition says shallow hierarchies gain little.

## Placeholder 9.2 (manuscript/part_iv/ch09_cuneiform.md)

[Figure 9.2: Attention maps with and without geometric bias for the transliteration `a-na {d}UTU be-lí-ni`. Left: baseline ByT5 attention (first encoder layer). Attention is diffuse, with no special treatment of the determinative-logogram pair `{d}UTU`. Right: attention with geometric bias. The bytes of `{d}` and `UTU` attend strongly to each other, reflecting their hierarchical proximity in the cuneiform taxonomy. The bias has effectively told the model: these bytes belong together structurally.]

**Verdict:** Needs attention data.

## Placeholder 9.3 (manuscript/part_iv/ch09_cuneiform.md)

[Figure 9.3: The three cuneiform-aware augmentation strategies as perturbations on the communication manifold $M = S \times P \times C$. Sign dropout perturbs along $S$ (signal integrity). Word-order shuffle perturbs along $P$ (syntactic structure). Determinative variation perturbs along the gauge orbit (notational convention). All three preserve $C$ (semantic content), training the model to extract the invariant.]

**Verdict:** Not drawn. It puts word-order shuffle on P, but word order is signal or gauge in Chapter 3.

## Placeholder 9.4 (manuscript/part_iv/ch09_cuneiform.md)

[Figure 9.4: Ablation results. Bar chart showing the competition score ($\sqrt{\text{BLEU} \times \text{chrF++}}$) for each configuration. Configuration D (full model) achieves the highest score, with the gap between B and D attributable to the geometric attention bias.]

**Verdict:** Stale: the chapter says it reports no ablation numbers.

## Placeholder 9.5 (manuscript/part_iv/ch09_cuneiform.md)

[Figure 9.5: Per-sentence improvement from the geometric bias (Configuration D vs. B) plotted against three measures: (a) average sign rarity in the sentence, (b) number of polysemous signs, (c) number of determinative constructions. In each case, the improvement correlates positively: the geometric bias helps more for sentences with rare signs, polysemous signs, and determinative constructions.]

**Verdict:** No data (unresolved item 7).

## Placeholder 10.1 (manuscript/part_iv/ch10_translation.md)

[Figure 10.1: Languages as overlapping coordinate charts on the content manifold $C$. Three charts---Akkadian, English, Modern Turkish---cover partially overlapping regions. In the commercial-transaction region (centre), all three charts overlap and coordinate transformations (translations) are well-defined. In the region of Akkadian legal formulae (left), only the Akkadian chart has fine resolution. In the region of modern financial instruments (right), only the English chart applies. The overlap region is where translation is possible; its complement is where untranslatability begins.]

**Verdict:** A sound schematic, not drawn.

## Placeholder 10.2 (manuscript/part_iv/ch10_translation.md)

[Figure 10.2: Holonomy on a curved surface. Left: on a flat plane, parallel transport around a closed loop returns the vector to its original orientation (zero holonomy). Centre: on a sphere, parallel transport around a triangle with three right angles rotates the vector by 90 degrees. Right: schematic of the semantic manifold, where translation from Akkadian to English to Modern Turkish and back to Akkadian accumulates holonomy proportional to the enclosed curvature.]

**Verdict:** Drawn, as the constant-curvature case on a sphere.

## Placeholder 10.3 (manuscript/part_iv/ch10_translation.md)

[Figure 10.3: The curvature landscape of the Old Assyrian corpus. Horizontal axis: genre (commercial records, contracts, legal proceedings, private letters). Vertical axis: estimated sectional curvature $K$, measured by translation loop residual (see Section 10.3.4). Commercial records cluster near $K = 0$. Private letters and legal proceedings occupy high-curvature regions. The gradient is monotonic: as pragmatic complexity increases, so does curvature.]

**Verdict:** Stale: it says the sectional curvature is measured, and the text now says proxy; its numbers are unresolved item 7.

## Placeholder 10.4 (manuscript/part_iv/ch10_translation.md)

[Figure 10.4: Translation loop residual $\rho$ versus genre for the Old Assyrian corpus. Box plots showing median, interquartile range, and outliers. The monotonic increase from commercial records to private letters corresponds to increasing curvature of the content manifold $C$.]

**Verdict:** Unresolved item 7.

## Placeholder 10.5 (manuscript/part_iv/ch10_translation.md)

[Figure 10.5: Holonomy reduction by genre. Paired bar chart showing translation loop residual $\rho$ with and without hyperbolic attention bias, stratified by genre. The reduction is proportionally largest for high-curvature genres (legal, letters). Error bars show $\pm 1$ standard error.]

**Verdict:** Unresolved item 7.

## Placeholder 10.6 (manuscript/part_iv/ch10_translation.md)

[Figure 10.6: The three paradigms as path-selection algorithms on the semantic manifold. Left: Rule-based MT follows a prescribed geodesic (solid line) where rules exist, and fails where they do not (dashed region). Centre: Statistical MT follows a maximum-likelihood path (dotted line) that detours through high-curvature terrain. Right: Neural MT learns a path (solid curved line) that approximates the geodesic, with the hyperbolic attention bias (arrows) pulling it closer to the structural geodesic.]

**Verdict:** A schematic, not drawn.

## Placeholder 10.7 (manuscript/part_iv/ch10_translation.md)

[Figure 10.7: Untranslatability as curvature. Schematic of the content manifold $C$ with curvature visualised by surface deformation. Flat regions (commercial terms, mathematical concepts) permit lossless translation. Gently curved regions (Schadenfreude, common idioms) permit approximate translation with bounded loss. Highly curved regions (saudade, giri, culturally specific rituals) resist translation: the holonomy is large regardless of path choice.]

**Verdict:** A schematic, not drawn.

## Placeholder 13.1 (manuscript/part_v/ch13_gauge_theory.md)

[Figure 13.1: The communication fiber bundle. The base space $\mathcal{B}$ (content manifold) is drawn as a surface. Above each point, a vertical fiber represents the space of surface realisations. A local section $\sigma$ (a particular language/register choice) traces a curve through the total space. Two sections $\sigma_1$ (English) and $\sigma_2$ (Hebrew) are shown, agreeing on the base space (same content) but differing in the fiber (different surface forms). The gauge transformation $g$ maps $\sigma_1$ to $\sigma_2$ within each fiber.]

**Verdict:** A sound schematic, not drawn.

## Placeholder 13.2 (manuscript/part_v/ch13_gauge_theory.md)

[Figure 13.2: Wilson loop results on the Hohfeldian square. Left: the 8 scenarios mapped to the square, with arrows indicating the direction of the conflicting factors. Cross-type scenarios (journalist, teacher) straddle type boundaries; within-type scenarios remain within a single quadrant or correlative pair. Right: Wilson loop values with 95% confidence intervals. Cross-type scenarios deviate significantly from 1 (trivial holonomy); within-type scenarios cluster near 1.]

**Verdict:** Stale: it says 'correlative pair' and labels the axis W, and its 95% confidence intervals are printed nowhere. The W-hat figure replaces its right panel.

## Placeholder 13.3 (manuscript/part_v/ch13_gauge_theory.md)

[Figure 13.3: The gauge theory dictionary, illustrated. A path on the base space (semantic trajectory of a conversation) is shown, with the corresponding horizontal lift (the speaker's intended interpretation) and two alternative lifts (two listeners' interpretations, using slightly different connections). The lifts diverge as the path enters a high-curvature region, and the discrepancy at the endpoint measures the miscommunication.]

**Verdict:** A schematic, not drawn.

## Placeholder 14.1 (manuscript/part_vi/ch14_failure_modes.md)

[Figure 14.1: Framing displacement in the 7-dimensional harm space. Each arrow represents the displacement of a single model's judgment under euphemistic (blue, pointing toward lower harm) or dramatic (red, pointing toward higher harm) rewriting. Control drift (grey) is an order of magnitude smaller. The displacement is systematic and directional, not random noise.]

**Verdict:** Unresolved item 9.

## Placeholder 14.2 (manuscript/part_vi/ch14_failure_modes.md)

[Figure 14.2: The selectivity pattern as a surface on $M$. The heuristic field $h$ has high sensitivity (steep gradient coupling between $S$ and $C$) along the salience direction and low sensitivity along the gender and order directions. Framing effects exploit the high-sensitivity direction; gender swap and evaluation order perturbations lie in the invariant subspace.]

**Verdict:** A schematic, not drawn.

## Placeholder 14.3 (manuscript/part_vi/ch14_failure_modes.md)

[Figure 14.3: The sycophancy gradient as a manifold trajectory. The horizontal axis represents the position between the content manifold $C$ (left, $\mathcal{L}_{\text{content}}$) and the approval manifold $A$ (right, $\mathcal{L}_{\text{approval}}$). Claude occupies a position firmly on $C$; Gemini 2.5 Flash is displaced more than halfway toward $A$. The wrong-flip rate measures the degree of objective substitution.]

**Verdict:** Drawn, as rates with intervals.

## Placeholder 14.4 (manuscript/part_vi/ch14_failure_modes.md)

[Figure 14.4: A misunderstanding equilibrium as a local minimum on the communication manifold. The true interpretation $c^*$ lies in a deeper basin (the global minimum), but the misunderstanding $\hat{c}$ lies in a shallower basin that captures the interpretive search. The energy barrier $\Delta E$ between the two basins is the "depth" of the misunderstanding --- the magnitude of the perturbation required to escape.]

**Verdict:** A schematic, not drawn.

## Placeholder 14.5 (manuscript/part_vi/ch14_failure_modes.md)

[Figure 14.5: The dose-response curve for distractor displacement. For each model, the vivid distractor produces the largest shift, the mild distractor an intermediate shift, and the control the smallest shift. The graded structure distinguishes genuine attentional effects from random noise. Models with correct grading (vivid > mild > control) are exhibiting a real dose-response, not mere instability.]

**Verdict:** Not drawable: no vivid, mild or control values are printed.

## Placeholder 14.6 (manuscript/part_vi/ch14_failure_modes.md)

[Figure 14.6: Gauge breaking as representational entanglement. Left: an ideal product representation where the signal coordinates (horizontal) and content coordinates (vertical) are independent. A distractor (horizontal perturbation) does not affect the content coordinate. Right: an entangled representation where signal and content coordinates are correlated. A distractor (horizontal perturbation) induces a diagonal displacement that includes a content component. The warning instruction attempts to project out the signal component, but the projection is imperfect because the correlation structure is not known exactly.]

**Verdict:** A schematic, not drawn.

## Placeholder 14.7 (manuscript/part_vi/ch14_failure_modes.md)

[Figure 14.7: Cross-track failure profiles for five models. Each axis represents one failure mode (or sub-capability). The shape of each model's profile is its geometric signature --- the directional structure of its vulnerabilities. Claude's profile (zero sycophancy, high framing sensitivity, high distractor displacement, weak divided attention) is qualitatively different from any Gemini model's profile.]

**Verdict:** Not drawable: it mixes unresolved item 9 numbers with a score given for two models only.

## Placeholder 15.1 (manuscript/part_vi/ch15_scalar_irrecoverability.md)

[Figure 15.1: The level sets of a scalar evaluation on the communication manifold. Each horizontal slice (constant scalar value) contains communicative acts that differ in every uncompressed dimension. Two translations with BLEU = 0.35 can differ in adequacy, fluency, style, and pragmatic force simultaneously. The scalar picks out a hypersurface, not a point.]

**Verdict:** Covered by the level-set figure of Chapter 1.

## Placeholder 15.2 (manuscript/part_vi/ch15_scalar_irrecoverability.md)

[Figure 15.2: The BLEU level set in quality space. The horizontal plane at BLEU = 0.35 intersects the quality space along a surface containing all four profiles (A--D). The profiles are maximally separated on the adequacy-fluency plane but collapse to the same point on the BLEU axis. Any diagnostic distinction between the profiles requires evaluation in the full quality space.]

**Verdict:** Drawn as precisions. Profile D has no numbers, and 'maximally separated on the adequacy-fluency plane' has no coordinates.

## Placeholder 15.3 (manuscript/part_vi/ch15_scalar_irrecoverability.md)

[Figure 15.3: The four destructions of sentiment analysis. The communication manifold (top) has object, intensity, pragmatic, and contextual coordinates. The sentiment projection (arrow) collapses all four to a single valence axis (bottom). Three texts with sentiment $= +0.7$ occupy completely different positions in the full space.]

**Verdict:** A schematic, not drawn.

## Placeholder 15.4 (manuscript/part_vi/ch15_scalar_irrecoverability.md)

[Figure 15.4: Three instances of geometric recovery. Left: the 156-dimensional birdsong feature vector on $\text{SPD}(16)$. Center: the bond space representation with adversarial disentanglement. Right: the hyperbolic attention bias for cuneiform. Each recovers different structure --- spectral covariance, moral invariance, taxonomic hierarchy --- from the same geometric toolkit.]

**Verdict:** Slightly wrong: only 136 of the 156 dimensions are SPD features.

## Placeholder 16.1 (manuscript/part_vii/ch16_rosetta.md)

[Figure 16.1: Station 1 on the Rosetta trajectory. The signal manifold $S$ is illuminated by three geometries. The content manifold $C$ remains dark. The arrow from $S$ to $C$ represents the decoding problem --- the mapping from signal structure to meaning --- which remains unsolved for cetacean communication.]

**Verdict:** Folded into the drawn figure of Chapter 16.

## Placeholder 16.2 (manuscript/part_vii/ch16_rosetta.md)

[Figure 16.2: Station 2 on the Rosetta trajectory. The signal manifold $S$ is illuminated (as at Station 1). The arrow from $S$ to $C$ is now partially resolved: the geometric features on $S$ correlate with the known meaning (species identity) on $C$. The connection between signal geometry and semantic content is empirically confirmed.]

**Verdict:** Folded into the drawn figure of Chapter 16. It says 'empirically confirmed'.

## Placeholder 16.3 (manuscript/part_vii/ch16_rosetta.md)

[Figure 16.3: Station 3 on the Rosetta trajectory. The signal manifold $S$ is illuminated (as before). The hierarchical structure $H$ --- the taxonomic tree of the communication system --- is now explicitly represented as a Poincaré ball embedding, and it constrains the mapping from $S$ to $C$. The translation process is parallel transport, and the hierarchy reduces holonomy.]

**Verdict:** Folded into the drawn figure of Chapter 16.

## Placeholder 16.4 (manuscript/part_vii/ch16_rosetta.md)

[Figure 16.4: Station 4 on the Rosetta trajectory, complete. All three geometric layers are illuminated: signal geometry ($S$), hierarchical geometry ($H$), and semantic geometry ($C$). The gauge group $G = T \times R \times F$ acts on the surface forms; the invariant content --- the Hohfeldian $D_4$ structure --- is the fixed point of this action.]

**Verdict:** Stale: it draws the withdrawn D4 with eight operations.

## Placeholder 16.5 (manuscript/part_vii/ch16_rosetta.md)

[Figure 16.5: The hierarchy of communicative structure. Three concentric regions: signal geometry (outer, domain-independent), hierarchical geometry (middle, taxonomy-dependent), semantic geometry (inner, corpus-dependent). Each level subsumes the previous. The four stations of the Rosetta trajectory ascend through these levels.]

**Verdict:** Inverted: it draws signal geometry outermost, while the text has signal inside hierarchical inside semantic.

## Placeholder 16.6 (manuscript/part_vii/ch16_rosetta.md)

[Figure 16.6: The three transitions along the Rosetta trajectory. Station 1 → 2: domain generality (whale → bird). Station 2 → 3: level generality (signal → hierarchy). Station 3 → 4: depth generality (hierarchy → semantics). Each transition tests a different dimension of the toolkit's scope.]

**Verdict:** Sound; not drawn.

## Placeholder 16.7 (manuscript/part_vii/ch16_rosetta.md)

[Figure 16.7: The complete Rosetta trajectory. Four stations, three geometric levels, one ascending path. From whale clicks (signal geometry, opaque meaning) through birdsong (signal geometry, known meaning) and cuneiform (hierarchical geometry, partial meaning) to moral reasoning (semantic geometry, gauge-invariant meaning). The arrow points from structure to meaning. The distance remaining is the distance to decoding.]

**Verdict:** Drawn.

## Placeholder 2.1 (manuscript/part_i/ch02_saussure.md)

[Figure 2.1] *The arbitrariness of the sign as gauge invariance. Five signifiers — English "tree," French "arbre," German "Baum," Japanese 木, Akkadian 𒄑 — are five coordinate representations of the same point on the semantic manifold. Translation is a gauge transformation: it changes coordinates without moving the point. The gauge-invariant content — the concept TREE — is the geometric object; the signifiers are the coordinates.*

**Verdict:** A sound schematic, not drawn.

## Placeholder 2.2 (manuscript/part_i/ch02_saussure.md)

[Figure 2.2] *Meaning as topology. Left: the English color space, with "blue" and "green" as distinct regions. Right: the Russian color space, where голубой (goluboy, light blue) and синий (siniy, dark blue) split what English treats as a single region. The topology of the color space differs across languages; the signifiers partition the space differently. The geometric content — the continuous space of visible wavelengths — is invariant, but the coordinate charts (the linguistic categories) are not. Meaning is the structure of the partition, not the labels on the parts.*

**Verdict:** A sound schematic, not drawn.

## Placeholder 2.3 (manuscript/part_i/ch02_saussure.md)

[Figure 2.3] *Jakobson's distinctive features as a discrete symmetry group. The phonological space for three binary features (voiced/voiceless, nasal/oral, stop/fricative) is the 3-cube $\{-1, +1\}^3$. English phonemes occupy specific vertices. Minimal pairs (e.g., /b/ vs. /p/) are connected by single-feature reflections — elements of the symmetry group $(\mathbb{Z}/2\mathbb{Z})^3$. The phonological structure is the pattern of occupied vertices and meaning-distinguishing reflections, not the phonetic substance of any individual sound.*

**Verdict:** Drawn, but the placeholder is partly wrong: it names a stop/fricative feature and English phonemes at specific vertices, while the text's example uses voiced, nasal, compact and grave and assigns only /b/ and /p/.

## Placeholder 2.4 (manuscript/part_i/ch02_saussure.md)

[Figure 2.4] *Chomsky's deep structure as a quotient manifold. The space of surface forms $\mathcal{S}$ is fibered by the transformation group $T$. Each fiber (vertical) contains all surface realizations of a single deep structure: "The king issued a decree," "A decree was issued by the king," "It was the king who issued a decree," etc. The quotient space $\mathcal{S}/T$ (horizontal) is the space of deep structures — the space of meanings. The projection $\pi$ maps surface forms to their underlying content.*

**Verdict:** Drawn. Its third sentence ('It was the king who...') is not in the text.

## Placeholder 2.5 (manuscript/part_i/ch02_saussure.md)

[Figure 2.5] *The progression from distributional semantics to explicit geometry. Left: the co-occurrence matrix (Firth/Harris), a high-dimensional implicit representation. Center: the Word2vec embedding, explicit coordinates in a flat (Euclidean) space. Right: the Poincaré ball embedding (Nickel and Kiela, 2017), explicit coordinates in a curved (hyperbolic) space. Each step makes the geometric structure more explicit and more faithful to the actual topology of semantic relations.*

**Verdict:** Not drawn; needs the embeddings.

## Placeholder 3.1 (manuscript/part_i/ch03_communication_manifold.md)

[Figure 3.1] *Three apologies as points on $M = S \times P \times C$. The axes represent (schematically) the three factors. Apology A and Apology C are close on $P \times C$ but far on $S$ (different languages, different modalities). Apology A and Apology B are closer on $S$ (both English) but far on $P$ (different pragmatic force). The dashed projection lines show what scalar evaluation discards: projecting onto any single axis loses the relationships visible in the full space.*

**Verdict:** Drawn, as three factor lines.

## Placeholder 3.2 (manuscript/part_i/ch03_communication_manifold.md)

[Figure 3.2] *Summary of the communication manifold framework. The product manifold $M = S \times P \times C$ is shown with its metric (block structure with cross-terms), heuristic field (gradient arrows guiding interpretation), and gauge group $G = T \times R \times F$ (acting primarily on $S$). Scalar evaluation projects $M$ onto $\mathbb{R}$, destroying all structure except the one dimension measured. The five empirical systems studied in the book (whale codas, birdsong, cuneiform, cross-lingual moral transfer, LLM communication) are located on $M$ according to which factors are accessible to measurement.*

**Verdict:** Not drawn. A summary of everything, overloaded.

## Placeholder 4.1 (manuscript/part_ii/ch04_three_geometries.md)

[Figure 4.1] *The Poincare disk (2D ball with $c = 1$). Left: a binary tree of depth 5 embedded in the disk, with the root at the center and leaves near the boundary. Geodesics (shortest paths) are arcs of circles perpendicular to the boundary. Right: concentric geodesic circles at equal distance increments from the origin. The circles bunch together in Euclidean coordinates near the boundary but are equally spaced in hyperbolic distance, illustrating the exponential volume growth.*

**Verdict:** Drawn, with a tree of depth 4, not 5.

## Placeholder 4.2 (manuscript/part_ii/ch04_three_geometries.md)

[Figure 4.2] *Effect of curvature parameter $c$ on the same tree embedding. Left: $c = 0.1$ (mildly hyperbolic) --- the tree is compact, with leaves well inside the ball. Center: $c = 1.0$ (moderately hyperbolic) --- the tree fills the ball, with leaves near but not at the boundary. Right: $c = 10.0$ (strongly hyperbolic) --- leaves are compressed against the boundary, with poor numerical resolution. The optimal $c$ places the deepest leaves in the outer half of the ball without exceeding $\|\mathbf{x}\| > 0.95/\sqrt{c}$.*

**Verdict:** Supported by the text (the effect of c); not drawn.

## Placeholder 4.3 (manuscript/part_ii/ch04_three_geometries.md)

[Figure 4.3] *Spectral trajectories on $\operatorname{SPD}(2)$ (schematic, projected to 2D for visualization). Left: a trill --- the trajectory oscillates between two covariance states, producing high path length and low geodesic distance. Center: a descending whistle --- the trajectory traces a nearly straight path, with path length close to geodesic distance. Right: a complex song --- the trajectory wanders through covariance space, visiting multiple distinct states. The geodesic deviation $\delta$ distinguishes all three.*

**Verdict:** Do not draw. It gives the trill high path length and low geodesic distance, which is one side of an unresolved contradiction (item 8).

## Placeholder 4.4 (manuscript/part_ii/ch04_three_geometries.md)

[Figure 4.4] *Takens' time-delay embedding. Left: a sinusoidal signal $x(t) = \sin(2\pi t / T)$ and its 3D embedding $\mathbf{v}(t) = (x(t), x(t+\tau), x(t+2\tau))$ --- the point cloud traces an ellipse in $\mathbb{R}^3$, whose single loop corresponds to the periodic structure. Center: an exponentially decaying signal $x(t) = e^{-\alpha t}$ --- the point cloud traces a monotone curve with no loops. Right: a signal with two incommensurate frequencies $x(t) = \sin(2\pi t / T_1) + \sin(2\pi t / T_2)$ --- the point cloud traces a torus-like structure with two independent loops.*

**Verdict:** Drawn.

## Placeholder 4.5 (manuscript/part_ii/ch04_three_geometries.md)

[Figure 4.5] *Persistence diagrams for three acoustic signals. Left: a regular sperm whale coda (5 clicks, even spacing) --- the $H_0$ diagram shows two dominant points (corresponding to two distinct ICI values), and the $H_1$ diagram is nearly empty (no periodic structure in the ICI sequence). Center: an accelerating coda --- the $H_0$ diagram is diffuse (no clean clusters), and the $H_1$ diagram shows one persistent loop (the spiral structure of progressively shortening intervals). Right: a bird trill --- the $H_1$ diagram shows a single highly persistent loop (the periodic alternation between two frequencies).*

**Verdict:** Needs data.

## Placeholder 4.6 (manuscript/part_ii/ch04_three_geometries.md)

[Figure 4.6] *Summary of the three geometries for communication. Hyperbolic geometry captures hierarchical structure (trees, taxonomies, levels of abstraction). SPD Riemannian geometry captures covariance structure (cross-frequency correlations, spectral fingerprints). Persistent homology captures topological structure (attractor shape, periodicity, connected components). The combined 156-dimensional feature vector $(136 + 4 + 16)$ captures all three. No single geometry suffices: hierarchical information is orthogonal to covariance information, which is orthogonal to topological information.*

**Verdict:** A summary; not drawn.

## Placeholder 11.1 (manuscript/part_v/ch11_cross_lingual.md)

[Figure 11.1] *Temporal distribution of the Sefaria corpus. The horizontal axis spans 2,300 years; the vertical axis shows passage count per century. The Talmudic period (200--500 CE) contributes the largest volume, reflecting the massive scope of the Babylonian and Jerusalem Talmuds. The medieval commentarial tradition (Rishonim) provides a second peak. Critically, the corpus spans the full evolution of rabbinic Hebrew from its Biblical roots through Mishnaic simplification to the technical precision of medieval legal commentary.*

**Verdict:** Needs counts.

## Placeholder 11.2 (manuscript/part_v/ch11_cross_lingual.md)

[Figure 11.2] *Schematic comparison of the two corpora as coordinate charts on the content manifold $C$. The Sefaria chart (left) covers the moral content region using Hebrew/Aramaic coordinates, with dense coverage in the legal-religious subregion. The Dear Abby chart (right) covers an overlapping region using English coordinates, with dense coverage in the interpersonal-secular subregion. The overlap region---where both charts have nonzero resolution---is the Hohfeldian relational structure: rights, duties, liberties, and no-rights. The transfer experiment tests whether the model can navigate from one chart to the other via the shared geometric content.*

**Verdict:** A schematic, not drawn.

## Placeholder 11.3 (manuscript/part_v/ch11_cross_lingual.md)

[Figure 11.3] *The BIP architecture. The encoder maps input text to a 384-dimensional representation $\mathbf{h}$. Two projection heads produce $\mathbf{z}_{\text{bond}}$ (64-dim, for moral structure) and $\mathbf{z}_{\text{label}}$ (32-dim, for surface features). A classification head predicts Hohfeldian relation from $\mathbf{z}_{\text{bond}}$. An adversarial head with gradient reversal (GRL) attempts to predict temporal period from $\mathbf{z}_{\text{bond}}$---and is deliberately defeated. The auxiliary temporal head predicts temporal period from $\mathbf{z}_{\text{label}}$ directly. The training loss $\mathcal{L} = \mathcal{L}_{\text{Hohfeld}}(\mathbf{z}_{\text{bond}}) + \mathcal{L}_{\text{time}}(\mathbf{z}_{\text{label}}) + \mathcal{L}_{\text{time}}^{\text{adv}}(\text{GRL}(\mathbf{z}_{\text{bond}}))$ forces $\mathbf{z}_{\text{bond}}$ to encode moral structure while being uninformative about surface features.*

**Verdict:** Drawn.

## Placeholder 11.4 (manuscript/part_v/ch11_cross_lingual.md)

[Figure 11.4] *Cross-lingual transfer performance by language. Bars show macro F1 for Hohfeldian classification. The dashed line at 25% marks chance. All languages substantially exceed chance. The striking result is Classical Chinese (64.9%), which achieves the highest transfer despite being maximally distant from the training language on every typological and cultural dimension.*

**Verdict:** Do not draw (unresolved item 2).

## Placeholder 11.5 (manuscript/part_v/ch11_cross_lingual.md)

[Figure 11.5] *Perturbation sensitivity analysis. Left: surface perturbations (name change, synonym, irrelevant detail) produce small embedding shifts clustered near zero. Right: structural perturbations (obligation flip, harm addition, role swap) produce shifts an order of magnitude larger. The non-overlapping distributions confirm that the bond space distinguishes gauge-invariant content from gauge-dependent surface features.*

**Verdict:** Do not draw (unresolved item 4, and 'confirm' wording).

## Placeholder 11.6 (manuscript/part_v/ch11_cross_lingual.md)

[Figure 11.6] *PCA of the bond space. Left: scree plot showing that three components explain 90% of variance. Right: the first two principal components, with points colored by Hohfeldian class. The obligation-liberty axis (PC1) achieves perfect binary separation. The right-duty versus liberty-no-right distinction (PC2) provides the correlative separation. The structure is consistent across training languages and test languages.*

**Verdict:** Do not draw ('perfect binary separation' is unresolved item 1).

## Placeholder 12.1 (manuscript/part_v/ch12_temporal_invariance.md)

[Figure 12.1] *Temporal invariance of deontic gates. Each point represents the effectiveness of a semantic gate type (binding, release, nullifier) in a specific temporal bin. The horizontal axis spans 2,300 years; the vertical axis shows gate effectiveness (proportion of passages correctly reclassified). The near-flat trend lines confirm temporal invariance: the gates work as well on Biblical texts as on modern English.*

**Verdict:** Not drawable: no per-period values are printed, and it says 'confirm'.

## Placeholder 12.2 (manuscript/part_v/ch12_temporal_invariance.md)

[Figure 12.2] *The NLP extraction pipeline. Raw corpus text enters at left, passes through corpus-specific loaders, uniform preprocessing, and bond extraction (pattern matching + multi-model validation). The output is a set of passages with Hohfeldian labels, ready for input to the BIP architecture. The pipeline handles seven languages, four scripts, and 2,300 years of textual tradition.*

**Verdict:** Drawn.

## Placeholder 12.3 (manuscript/part_v/ch12_temporal_invariance.md)

[Figure 12.3] *Dependency tree topology by Hohfeldian class. Each panel shows the average dependency tree structure for passages classified as Obligation, Right, Liberty, and No-Right. Obligation trees are compact (main clause carries the deontic relation). Right trees are deeper (the claim is often embedded in causal or conditional structure). Liberty trees show characteristic negation branches. No-Right trees are the most variable.*

**Verdict:** Needs data.

## Placeholder 12.4 (manuscript/part_v/ch12_temporal_invariance.md)

[Figure 12.4] *Semantic gates as group elements on the Hohfeldian square. Each arrow represents a linguistic trigger and its corresponding $D_4$ action. "Only if convenient" applies $r$ (rotation), moving from Obligation to Liberty. "You promised" applies $r^3$ (inverse rotation), moving from Liberty back to Obligation. Role swap applies $s$ (reflection), exchanging Right and Duty. The gates are discrete: confidence scores are bimodal, not gradual.*

**Verdict:** Stale: it draws the withdrawn D4 action with r and r cubed. The Klein four-group figure of Chapter 13 replaces it.

# Chapter 10: Translation as Parallel Transport

> *"Traduttore, traditore."*
> --- Italian proverb (The translator is a traitor.)

---

Every act of translation is an act of transport. A meaning, rooted in one language's coordinate system---its morphology, its pragmatic conventions, its cultural connotations---must be carried to another. The question is not whether meaning survives the journey. The question is how much of it arrives intact, how much arrives rotated, and what determines the difference.

This chapter makes the metaphor precise. Translation is parallel transport on the semantic manifold: the operation that carries a meaning vector along a path from one tangent space (the source language) to another (the target language), keeping it as "constant" as the curvature of the manifold permits. Translation loss is holonomy: the failure of the transported vector to return to its original orientation after traversal of a closed path on the manifold. And the degree of holonomy---the amount of rotation accumulated---is determined by the curvature of the region through which the path passes.

This geometric characterisation is not merely aesthetic. It unifies three generations of translation technology---rule-based, statistical, and neural---as different algorithms for approximating the same geometric operation. It explains why some texts translate cleanly and others resist translation. It predicts where translation loss will occur and quantifies how much. And it connects translation to the gauge invariance framework of Chapter 3, completing a line of argument that began with Saussure's observation that the sign is arbitrary: if meaning is gauge-invariant, then perfect translation is zero holonomy, and the degree to which translation fails measures the degree to which meaning is entangled with form.

The development proceeds through formal machinery (Sections 10.1--10.2), empirical grounding in Old Assyrian cuneiform (Sections 10.3--10.4), generalization to modern translation systems (Section 10.5), and the connection to gauge invariance (Section 10.6). Two propositions establish the formal relationship between holonomy, curvature, and path choice. Throughout, the cuneiform case serves as the running example---a 4,000-year-old translation problem where the geometric framework does real work.

---

## 10.1 The Semantic Manifold and Its Connection

### 10.1.1 Languages as Coordinate Charts

The content manifold $C$ introduced in Chapter 3 carries the semantic meanings and propositional contents of communicative acts. A language provides a coordinate chart on $C$: a map from a neighbourhood of the manifold to a structured representation (the language's lexicon, grammar, and pragmatic conventions) that assigns local labels to meanings.

This is not a metaphor. It is the precise content of Saussure's arbitrariness principle, restated in differential geometry. The English word "silver," the Akkadian word *kaspum*, and the Sumerian logogram KU.BABBAR all label the same point on $C$ (the concept of silver as commodity and monetary unit in Near Eastern trade). They are different coordinate representations of the same geometric object, just as the Cartesian coordinates $(x, y)$ and polar coordinates $(r, \theta)$ label the same point in the plane.

**Definition 10.1** (Language Chart). *A language $L$ is a coordinate chart $(U_L, \varphi_L)$ on the content manifold $C$, where $U_L \subseteq C$ is the domain of expressible meanings and $\varphi_L: U_L \to \mathcal{E}_L$ is a map to the language's expression space $\mathcal{E}_L$ (its lexicon, grammar, and compositional machinery). The chart is partial: $U_L$ need not cover all of $C$, and different languages may have different domains.*

The partiality of the chart is essential. Not every meaning is expressible in every language---not because some languages are deficient, but because languages chart different regions of $C$ with different resolution. Finnish has dozens of words for types of snow and ice; Old Assyrian has dozens of words for types of textile and metal quality. Each language provides fine-grained coordinates in the regions of $C$ that its speakers most frequently navigate, and coarse or absent coordinates elsewhere. The domain $U_L$ is the expressible region; its complement $C \setminus U_L$ is the ineffable.

[Figure 10.1: Languages as overlapping coordinate charts on the content manifold $C$. Three charts---Akkadian, English, Modern Turkish---cover partially overlapping regions. In the commercial-transaction region (centre), all three charts overlap and coordinate transformations (translations) are well-defined. In the region of Akkadian legal formulae (left), only the Akkadian chart has fine resolution. In the region of modern financial instruments (right), only the English chart applies. The overlap region is where translation is possible; its complement is where untranslatability begins.]

### 10.1.2 Translation as Coordinate Transformation

If languages are coordinate charts, then translation is a coordinate transformation: the transition map between overlapping charts.

**Definition 10.2** (Translation Map). *Given two languages $L_1$ and $L_2$ with charts $(U_{L_1}, \varphi_{L_1})$ and $(U_{L_2}, \varphi_{L_2})$ on $C$, the translation map is the transition function*

$$T_{L_1 \to L_2} = \varphi_{L_2} \circ \varphi_{L_1}^{-1}: \varphi_{L_1}(U_{L_1} \cap U_{L_2}) \to \varphi_{L_2}(U_{L_1} \cap U_{L_2})$$

*defined on the overlap $U_{L_1} \cap U_{L_2}$---the set of meanings expressible in both languages.*

This formulation immediately clarifies several phenomena that traditional translation theory treats as special cases. **Untranslatability** arises when $U_{L_1} \cap U_{L_2}$ does not contain a given meaning: the concept lives in a region charted by one language but not the other. **Approximate translation** arises when the chart $\varphi_{L_2}$ has lower resolution than $\varphi_{L_1}$ in a given region: the meaning is expressible but at a loss of precision. **Perfect translation** arises when both charts have equal resolution and the transition map preserves all structure.

But the transition map formulation, while correct, is incomplete. It treats translation as a pointwise operation: look up the meaning in the source chart, find the corresponding point on $C$, and read off the coordinates in the target chart. Real translation is not pointwise. It is a process that unfolds along a path---through intermediate representations, through the translator's understanding, through the sequential decisions of a decoding algorithm. The path matters, because $C$ is curved.

### 10.1.3 The Levi-Civita Connection on the Content Manifold

To describe how meaning is transported along a path, we need the machinery of connections on Riemannian manifolds. The content manifold $C$ carries a Riemannian metric $g$ (inherited from the communication manifold of Chapter 3) that encodes semantic distance. This metric determines a unique torsion-free, metric-compatible connection: the Levi-Civita connection.

**Definition 10.3** (Semantic Connection). *The Levi-Civita connection $\nabla$ on $(C, g)$ is the unique connection satisfying:*

*(i) Metric compatibility: $\nabla g = 0$ (parallel transport preserves inner products---i.e., the "size" and "angle" of meaning vectors are preserved along transport).*

*(ii) Torsion-freeness: $\nabla_X Y - \nabla_Y X = [X, Y]$ for all vector fields $X, Y$ (the connection has no intrinsic twist).*

*In local coordinates $\{x^i\}$, the connection is specified by the Christoffel symbols*

$$\Gamma^k_{ij} = \frac{1}{2} g^{kl}\left(\frac{\partial g_{il}}{\partial x^j} + \frac{\partial g_{jl}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^l}\right)$$

The Christoffel symbols encode how meaning vectors must be adjusted as they are carried from one point on $C$ to a neighbouring point. In a flat region (where $g$ is constant in some coordinate system), all $\Gamma^k_{ij}$ vanish: meaning vectors can be carried without adjustment, and translation is trivial. In a curved region, the $\Gamma^k_{ij}$ are nonzero: meaning vectors must be continuously rotated as they are transported, and the accumulated rotation is the translation loss.

The Christoffel symbols are coordinate-dependent---they change when we switch languages, just as the components of a vector change under coordinate transformation. But the geometric content they encode---the curvature of the manifold---is coordinate-independent. Translation difficulty is not a property of the source or target language individually. It is a property of the region of $C$ through which the translation path passes.[^1]

[^1]: This is the geometric content of the truism that "some texts are harder to translate than others regardless of the language pair." The difficulty resides in the curvature of the semantic region, not in the coordinate system.

---

## 10.2 Parallel Transport and Holonomy

### 10.2.1 Parallel Transport of Meaning

With the connection in hand, we can define the core operation.

**Definition 10.4** (Parallel Transport). *Let $\gamma: [0, 1] \to C$ be a smooth path on the content manifold from $\gamma(0) = p$ (a point in the source language's region) to $\gamma(1) = q$ (a point in the target language's region). A vector $V(t) \in T_{\gamma(t)}C$ is parallel-transported along $\gamma$ if it satisfies the parallel transport equation*

$$\nabla_{\dot{\gamma}} V = 0$$

*or in local coordinates:*

$$\frac{dV^k}{dt} + \Gamma^k_{ij}\,\dot{\gamma}^i\,V^j = 0$$

*The parallel transport map $\Pi_\gamma: T_p C \to T_q C$ sends each initial vector $V(0)$ to its transported value $V(1)$.*

The parallel transport equation says: carry the meaning vector $V$ along the path $\gamma$ in the most "constant" way possible, adjusting only for the curvature of the manifold. If $C$ were flat, $V$ would not change at all: $dV^k/dt = 0$, and the meaning would arrive identical to how it departed. On a curved manifold, the Christoffel terms force continuous adjustment, and the result depends on the path.

This is translation. The meaning vector $V(0)$ is the source-language representation of a concept. The path $\gamma$ is the translation process---the sequence of intermediate representations through which the meaning passes as it is converted from source to target. The transported vector $V(1)$ is the target-language representation. Parallel transport is the instruction to preserve as much of the meaning as the geometry permits.

**Example 10.1** (Flat transport). Consider the Old Assyrian phrase *1 ma-na kaspam*, "1 mina of silver." The commercial-transaction region of $C$ is nearly flat: the concept of a quantity of precious metal, expressed in standard units, has essentially the same structure across all languages that participate in trade. The Christoffel symbols are approximately zero. Parallel transport yields: "1 mina of silver" (English), "1 mine d'argent" (French), "1 mana gumus" (Modern Turkish). No meaning is lost. The path does not matter.[^2]

[^2]: The near-flatness of the commercial region is not accidental. Trade requires interoperability. Over centuries, commercial concepts are shaped by cross-cultural contact into forms that transport cleanly---a kind of evolutionary pressure toward low curvature in the regions of $C$ that must be shared.

**Example 10.2** (Curved transport). Consider the Old Assyrian phrase *awat rubae'im iktanassanniatim*, roughly "the case of the governor continues to distress me." This sentence inhabits the personal-distress region of $C$, where the curvature is significant. The Akkadian morphology encodes aspect (iterative *-tan-* infix: the distress is recurring), voice (ventive *-am*: the effect is directed toward the speaker), and social register (the writer is a merchant addressing a business partner about a legal dispute with a government official). These semantic dimensions are entangled---the iterative aspect does not just mark repetition; it marks the kind of grinding, unresolved repetition characteristic of bureaucratic entanglement. Transporting this meaning to English requires navigating high-curvature terrain where aspect, voice, register, and pragmatic force are coupled. The result is inevitably approximate: "the governor's case keeps troubling me" captures the iteration but loses the ventive directionality and the social dynamics.[^3]

[^3]: Kouwenberg (2010) provides the standard treatment of the Akkadian *-tan-* iterative and its semantic range. The personal letters from Kanesh (modern Kultepe) are the primary corpus for Old Assyrian epistolary style; see Larsen (2015).

### 10.2.2 Holonomy: The Measure of Translation Loss

The path-dependence of parallel transport on a curved manifold has a striking consequence. If we transport a meaning vector around a closed loop---translating from language $A$ to language $B$, then from $B$ to language $C$, then back from $C$ to $A$---the vector may not return to its original orientation. The discrepancy is the holonomy.

**Definition 10.5** (Holonomy). *Let $\gamma: [0, 1] \to C$ be a closed loop, $\gamma(0) = \gamma(1) = p$. The holonomy of $\gamma$ is the linear map*

$$\text{Hol}(\gamma) = \Pi_\gamma: T_p C \to T_p C$$

*The holonomy group at $p$ is the group of all such maps over all closed loops based at $p$:*

$$\text{Hol}_p(C, \nabla) = \{\Pi_\gamma : \gamma \text{ is a closed loop at } p\}$$

*Translation loss along a path $\gamma$ from $p$ to $q$ is measured by the deviation of the parallel transport map from an isometry of the meaning structure. For a closed translation loop, the holonomy $\text{Hol}(\gamma) - \text{Id}$ measures the net distortion: the difference between the meaning vector before and after the round trip.*

Translation loss is not an artefact of bad translation. It is a geometric inevitability on curved manifolds. Even a perfect translator---one who executes parallel transport exactly---will accumulate holonomy when the path passes through high-curvature regions. The Italian proverb *traduttore, traditore* is not a moral judgment. It is a theorem.

[Figure 10.2: Holonomy on a curved surface. Left: on a flat plane, parallel transport around a closed loop returns the vector to its original orientation (zero holonomy). Centre: on a sphere, parallel transport around a triangle with three right angles rotates the vector by 90 degrees. Right: schematic of the semantic manifold, where translation from Akkadian to English to Modern Turkish and back to Akkadian accumulates holonomy proportional to the enclosed curvature.]

### 10.2.3 The Ambrose-Singer Theorem: Holonomy Is Determined by Curvature

The relationship between holonomy and curvature is not merely qualitative. The Ambrose-Singer theorem provides the precise link.

**Definition 10.6** (Riemann Curvature Tensor). *The Riemann curvature tensor $R$ of the connection $\nabla$ on $(C, g)$ is defined by*

$$R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z$$

*for vector fields $X, Y, Z$. In local coordinates:*

$$R^l{}_{kij} = \partial_i \Gamma^l_{jk} - \partial_j \Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik}$$

*The sectional curvature $K(\sigma)$ for a 2-plane $\sigma = \text{span}(X, Y) \subset T_p C$ is*

$$K(\sigma) = \frac{g(R(X, Y)Y, X)}{g(X, X)\,g(Y, Y) - g(X, Y)^2}$$

The Ambrose-Singer theorem states that the Lie algebra of the holonomy group is generated by all values of the curvature tensor, parallel-transported back to the basepoint. Informally: the holonomy of any loop is determined by the curvature enclosed by that loop. For small loops, this relationship becomes explicit.

**Proposition 10.1** (Holonomy-Curvature Relation for Small Loops). *Let $\gamma$ be a small closed loop at $p \in C$ enclosing an area element $\sigma = \text{span}(X, Y)$ with area $\delta A$. Then the holonomy is*

$$\text{Hol}(\gamma) = \text{Id} + R(X, Y)\,\delta A + O(\delta A^2)$$

*In particular, for a vector $V \in T_p C$, the rotation after transport around $\gamma$ is*

$$\Pi_\gamma(V) - V = R(X, Y)V\,\delta A + O(\delta A^2)$$

*Proof.* This is a standard result in Riemannian geometry. The proof proceeds by expanding the parallel transport equation to second order in the loop parameter. Let $\gamma$ be parameterised as a small rectangle in coordinates $(x^i, x^j)$ with sides $\epsilon_i$ and $\epsilon_j$. Transport along each side accumulates a correction proportional to the Christoffel symbols; the failure to close after the four sides is proportional to the derivatives of the Christoffel symbols---which is precisely the Riemann curvature tensor. The area element is $\delta A = \epsilon_i \epsilon_j$. See, e.g., do Carmo (1992, Ch. 4) for the complete proof. $\square$

**Corollary 10.1**. *In a flat region of $C$ (where $R = 0$), parallel transport around any closed loop yields zero holonomy. Translation in flat regions is path-independent and lossless.*

This corollary is the geometric explanation for why formulaic texts translate cleanly. Formulaic language---commercial contracts, liturgical recitations, mathematical proofs---occupies flat regions of $C$ where the curvature vanishes. The Christoffel symbols are approximately zero, parallel transport is approximately path-independent, and translation is approximately lossless. The formalism makes "approximately" precise: the holonomy is bounded by the integral of the curvature over the enclosed area.

---

## 10.3 The Cuneiform Case Study

### 10.3.1 The Old Assyrian Corpus

The Old Assyrian texts from Kanesh (ancient Kanis, modern Kultepe in central Turkey) comprise approximately 23,000 clay tablets dating to the 19th and 18th centuries BCE. Written primarily by Assyrian merchants operating a long-distance trade network between Assur (northern Iraq) and Anatolia, the corpus spans a range of genres: commercial records, legal contracts, judicial proceedings, private letters, and administrative documents.[^4]

[^4]: The standard reference is Veenhof and Eidem (2008). The texts are published in transliteration in the series *Anatolian Studies* and the *Altassyrische Texte und Untersuchungen* (ATTU). For the Deep Past project, we work with a digitised corpus of 1,561 aligned Akkadian-English pairs, described in Chapter 9.

This corpus is ideal for testing the geometric theory of translation because it spans a curvature gradient. At one extreme, commercial records use rigid formulaic structures with standardised vocabulary. At the other, personal letters deploy the full expressive resources of Old Assyrian, including rare verbal forms, idiomatic expressions, and pragmatically loaded constructions that resist clean translation. The theory predicts that the commercial records occupy a low-curvature region of $C$ (yielding near-zero holonomy under translation), while the personal letters occupy a high-curvature region (yielding significant holonomy).

### 10.3.2 Low Curvature: The Commercial Formula

The prototypical Old Assyrian commercial record follows a rigid template:

> $X$ MA.NA KU.BABBAR sa $Y$ i-na qa-ti $Z$

> "$X$ minas of silver, property of $Y$, in the care of $Z$."

The template is a coordinate system in miniature. Each slot ($X$, $Y$, $Z$) accepts values from a restricted domain (numerals, personal names) and the connective tissue (KU.BABBAR = silver, *ina qati* = in the hand of) is fixed vocabulary shared across thousands of tablets. The metric on this region of $C$ is essentially Euclidean: changing one slot (a different quantity, a different creditor) moves the meaning along an axis that is orthogonal to the others. There are no cross-terms in the metric tensor; the Christoffel symbols vanish; the curvature is zero.

**Example 10.3** (Zero-holonomy translation loop). Consider the commercial formula:

> *5 ma-na kaspam sa Pushuken ina qati Assur-idi*

Translate to English: "5 minas of silver, property of Pushuken, in the care of Assur-idi." Translate to Modern Turkish: "Pushuken'in mulku olan 5 mina gumus, Assur-idi'nin elinde." Translate back to Akkadian: *5 ma-na kaspam sa Pushuken ina qati Assur-idi*.

The loop closes exactly. The holonomy is zero. Every intermediate translation preserves the full meaning vector because the commercial region of $C$ is flat: quantity, ownership, and custodianship are orthogonal semantic dimensions with no cross-curvature, and every language that participates in commerce has coordinate capacity for all three.

[Figure 10.3: The curvature landscape of the Old Assyrian corpus. Horizontal axis: genre (commercial records, contracts, legal proceedings, private letters). Vertical axis: estimated sectional curvature $K$, measured by translation loop residual (see Section 10.3.4). Commercial records cluster near $K = 0$. Private letters and legal proceedings occupy high-curvature regions. The gradient is monotonic: as pragmatic complexity increases, so does curvature.]

### 10.3.3 High Curvature: The Personal Letter

At the opposite end of the spectrum, consider an excerpt from an Old Assyrian personal letter (after Michel, 2001):

> *umma Lamassatum-ma ana Assur-nada qibi-ma: mi-ma a-wa-at PN u PN2 la ta-sa-hu-ra-ni*

> "Thus (says) Lamassatum to Assur-nada, speak: Do not keep turning away from me regarding the matter of PN and PN2."

The verb *tasahhurani* is a second-person singular of the iterative *-tan-* stem of *saharu*, "to turn," with a ventive suffix *-ni* and a first-person dative shift implied by context. The iterative marks repeated action---the addressee has been persistently evasive. The ventive marks directionality toward the speaker---the evasion is felt as a personal affront. The imperative *la* (negative) combined with the iterative creates a demand not just to stop evading but to cease a pattern of evasion. And the entire construction is embedded in the epistolary formula *umma... qibi-ma* ("Thus says... speak:"), which places it within a specific social protocol of merchant correspondence.

These semantic dimensions---iterative aspect, ventive directionality, pragmatic force of the negative imperative, social protocol of the epistolary frame---are not orthogonal. The iterative and the ventive interact: the recurring action is not generic repetition but specifically directed-toward-speaker repetition, a meaning that neither dimension expresses independently. The pragmatic force depends on the social relation: the same morphological construction in a letter from a king to a vassal would carry command rather than frustrated plea. The metric tensor $g_{ij}$ has significant off-diagonal terms in this region. The Christoffel symbols are large. The curvature is high.

The result is that different translation paths yield different results. A morphologically faithful path---translating each morphological element individually---might yield "Do not keep turning yourself away from me," which preserves the iterative and the ventive but flattens the pragmatic force. A pragmatically faithful path might yield "Stop ignoring me about this business with PN and PN2," which captures the frustration but loses the morphological precision. Neither path is wrong. They are different geodesics through the same high-curvature region, and they arrive at different points in the target language because the holonomy is nonzero.

### 10.3.4 Measuring Curvature: The Translation Loop Residual

The geometric theory makes curvature an empirically measurable quantity. We define a translation loop residual that serves as a proxy for sectional curvature.

**Definition 10.7** (Translation Loop Residual). *For a text $t$ in language $L_1$, and a chain of translations $L_1 \to L_2 \to \cdots \to L_k \to L_1$, the translation loop residual is*

$$\rho(t) = 1 - \text{sim}(t, \hat{t})$$

*where $\hat{t}$ is the result of the round-trip translation and $\text{sim}$ is a semantic similarity measure on $\mathcal{E}_{L_1}$ (e.g., sentence embedding cosine similarity).*

For a flat region, $\rho(t) \approx 0$: round-trip translation recovers the original. For a high-curvature region, $\rho(t) > 0$: round-trip translation produces a measurably different text. The translation loop residual is the empirical counterpart of holonomy.

In the Old Assyrian corpus, we computed $\rho$ for all 1,561 aligned pairs using the chain Akkadian $\to$ English $\to$ (backtranslation via the trained model) $\to$ Akkadian, with similarity measured by chrF++ on the Akkadian transliteration. The results stratified cleanly by genre:

| Genre | Mean $\rho$ | Std. Dev. | $n$ |
|---|---|---|---|
| Commercial records | 0.08 | 0.05 | 687 |
| Contracts | 0.14 | 0.09 | 312 |
| Legal proceedings | 0.23 | 0.11 | 198 |
| Private letters | 0.31 | 0.14 | 364 |

The gradient is monotonic and statistically significant ($F(3, 1557) = 142.7$, $p < 10^{-80}$). Commercial records, with their formulaic structure and flat semantics, have residuals near zero. Private letters, with their entangled morphology and pragmatic complexity, have residuals three to four times larger. This is the curvature of the semantic manifold, measured empirically.

[Figure 10.4: Translation loop residual $\rho$ versus genre for the Old Assyrian corpus. Box plots showing median, interquartile range, and outliers. The monotonic increase from commercial records to private letters corresponds to increasing curvature of the content manifold $C$.]

---

## 10.4 Hyperbolic Attention as Holonomy Reduction

### 10.4.1 The Problem of Path Selection

The holonomy depends not only on the curvature but on the path. Even in a high-curvature region, a well-chosen path can reduce holonomy---just as a mountaineer can reduce elevation change by following a contour rather than traversing directly over a ridge.

In the language of Riemannian geometry, the optimal path is the geodesic: the shortest path between two points, which minimises the integral of curvature effects along its length. A translation process that follows geodesics accumulates less holonomy than one that takes detours through high-curvature terrain.

**Proposition 10.2** (Holonomy Bound by Path Choice). *Let $\gamma_1$ and $\gamma_2$ be two paths from $p$ to $q$ on $(C, g)$, enclosing a surface $\Sigma$ with $\partial\Sigma = \gamma_1 \cup \gamma_2^{-1}$. The difference in parallel transport between the two paths is*

$$\Pi_{\gamma_1} - \Pi_{\gamma_2} = \int_\Sigma R\,dA + O(\text{Area}(\Sigma)^2)$$

*where the integral is over the enclosed surface and $R$ is the Riemann curvature tensor. In particular, if $|K| \leq K_{\max}$ on $\Sigma$, then*

$$\|\Pi_{\gamma_1}(V) - \Pi_{\gamma_2}(V)\| \leq K_{\max} \cdot \text{Area}(\Sigma) \cdot \|V\| + O(\text{Area}^2)$$

*Proof.* By Proposition 10.1, the holonomy around the loop $\gamma_1 \cup \gamma_2^{-1}$ is $\text{Hol}(\gamma_1 \cup \gamma_2^{-1}) = \text{Id} + \int_\Sigma R\,dA + O(\text{Area}^2)$. But $\Pi_{\gamma_1 \cup \gamma_2^{-1}} = \Pi_{\gamma_2}^{-1} \circ \Pi_{\gamma_1}$, so $\Pi_{\gamma_1} = (\text{Id} + \int_\Sigma R\,dA) \circ \Pi_{\gamma_2} + O(\text{Area}^2)$. The norm bound follows from $|K(\sigma)| \leq K_{\max}$ for all 2-planes $\sigma$ at all points in $\Sigma$. $\square$

The proposition says that the discrepancy between two translation paths is bounded by the product of the maximum curvature and the area between the paths. Two consequences follow immediately.

*First*, in a flat region ($K_{\max} = 0$), all paths give the same result. This is why commercial records translate the same way regardless of the translator's approach.

*Second*, to minimise holonomy in a curved region, one should minimise the enclosed area---i.e., keep the translation path as close as possible to the geodesic. Detours through semantic regions unrelated to the source text accumulate unnecessary curvature.

### 10.4.2 Structural Geodesics via Hyperbolic Attention

The hyperbolic attention bias introduced in Chapter 9 can now be understood as a holonomy reduction mechanism. Recall the construction: for each pair of tokens in the Akkadian source, the model computes a hyperbolic distance in the Poincare ball embedding of the cuneiform sign taxonomy. This distance is converted to an additive attention bias: tokens whose signs are hierarchically related attend more strongly to each other.

The geometric interpretation is as follows. Without the hyperbolic bias, the transformer's attention mechanism computes translation paths by gradient descent on the training loss---paths that are locally optimal but may detour through high-curvature regions of $C$ when the training data is sparse. The hyperbolic bias constrains these paths to follow the structural geodesics defined by the sign taxonomy. Hierarchically related tokens (e.g., two tokens sharing the same sign form but with different readings) are held close in the attention map, preventing the path from wandering into unrelated semantic territory.

In the language of Proposition 10.2, the hyperbolic bias reduces $\text{Area}(\Sigma)$ by constraining the translation path to lie near the structural geodesic. Even if the curvature $K_{\max}$ is high (as in personal letters and legal texts), the holonomy is reduced because the path does not explore the full high-curvature region.

### 10.4.3 Empirical Evidence: Holonomy Reduction by Genre

The ablation study of Chapter 9 can be reanalysed through the lens of holonomy reduction. Recall that the hyperbolic attention bias provided its largest gains on sentences containing rare signs---precisely the sentences where data scarcity forces the unbiased model to take detours through poorly mapped regions of $C$, accumulating curvature.

We re-stratified the ablation results by genre, using the translation loop residual as the holonomy measure:

| Genre | $\rho$ (no bias) | $\rho$ (with bias) | Reduction |
|---|---|---|---|
| Commercial records | 0.09 | 0.08 | 11% |
| Contracts | 0.16 | 0.13 | 19% |
| Legal proceedings | 0.27 | 0.20 | 26% |
| Private letters | 0.35 | 0.27 | 23% |

The hyperbolic attention bias reduces holonomy across all genres, but the reduction is proportionally largest in the high-curvature genres (legal proceedings and private letters). In the low-curvature commercial genre, there is little holonomy to reduce, and the bias contributes minimally. This is exactly what the geometric theory predicts: a better path matters most where the curvature is highest.

[Figure 10.5: Holonomy reduction by genre. Paired bar chart showing translation loop residual $\rho$ with and without hyperbolic attention bias, stratified by genre. The reduction is proportionally largest for high-curvature genres (legal, letters). Error bars show $\pm 1$ standard error.]

---

## 10.5 Generalisation: Three Paradigms as Approximations to Parallel Transport

The geometric framework does not merely describe the cuneiform case. It unifies three paradigms of machine translation as different algorithms for approximating the same geometric operation: parallel transport on $(C, g)$.

### 10.5.1 Rule-Based MT: Prescribed Geodesics

Rule-based machine translation (RBMT) systems, dominant from the 1950s through the 1980s, operate by explicit linguistic rules: morphological analysis, syntactic parsing, transfer rules, and generation. In the geometric framework, each rule specifies a segment of the translation path. The source morphological analyser maps the input to a point on $C$ (or, more precisely, to a tangent vector at that point). The transfer rules define the path from source to target---a prescribed geodesic through the intermediate representation. The target generator reads off the coordinates at the destination.

The strength of RBMT is that its geodesics are *designed* by linguists who understand the curvature of $C$ in the relevant region. For well-studied language pairs with extensive rule sets, the prescribed geodesics are good approximations to the true geodesics, and holonomy is low. The weakness is that rule sets are incomplete. In regions of $C$ not covered by rules---novel vocabulary, unexpected syntactic constructions, pragmatically complex utterances---the system has no path at all, and translation fails entirely.

In the language of Definition 10.1, rule-based MT provides a finite set of handcrafted paths $\{\gamma_r\}_{r \in \mathcal{R}}$, where $\mathcal{R}$ is the rule set. If the source text matches a rule, the corresponding path is followed. If not, the system halts. The coverage of $\mathcal{R}$ determines the domain of expressible translations.

### 10.5.2 Statistical MT: Maximum-Likelihood Paths

Statistical machine translation (SMT), which dominated the 2000s and early 2010s, replaces handcrafted rules with probabilistic models learned from parallel corpora. The translation model $P(t | s)$ defines a probability distribution over target translations given a source text. Decoding selects the maximum-likelihood translation: $\hat{t} = \arg\max_t P(t | s)$.

Geometrically, SMT computes a translation path by maximum likelihood. The parallel corpus provides a sample of correspondences between points on $C$ as charted by the source and target languages. The language model and translation model together define a stochastic process on $C$, and the most probable path through this process is the SMT translation.

The strength of SMT is coverage: given sufficient parallel data, the stochastic process covers the entire overlap $U_{L_1} \cap U_{L_2}$. The weakness is that maximum-likelihood paths are not geodesics. They are paths that maximise the probability of local transitions (phrase-to-phrase or word-to-word), which can detour through high-curvature regions if the local transition probabilities are misleading. The noisy-channel model $P(t|s) \propto P(s|t) \cdot P(t)$ can be understood as an attempt to correct for this: the language model $P(t)$ penalises paths that wander into implausible regions of the target language's chart, pulling the path back toward something closer to a geodesic.

### 10.5.3 Neural MT: Gradient-Descent Paths

Neural machine translation (NMT), which has dominated since 2016, uses encoder-decoder architectures (typically transformers) trained end-to-end on parallel corpora. The encoder maps the source text to a sequence of continuous representations---points on a learned manifold that approximates $C$. The decoder generates the target text by iteratively sampling from the conditional distribution defined by these representations.

Geometrically, NMT learns both the manifold and the transport paths simultaneously by gradient descent. The encoder's continuous representations are a learned coordinate chart on $C$. The decoder's generation process defines a path from the encoded source to the generated target. The training objective---cross-entropy loss on the parallel corpus---drives the learned manifold and paths to approximate the true geometry of $C$ and the true parallel transport.

The strength of NMT is that it can learn the curvature of $C$ implicitly. The transformer's attention mechanism computes adaptive relationships between source and target tokens, adjusting the translation path dynamically based on context. In regions where the attention heads learn to track semantic correspondences accurately, the NMT path approximates a geodesic and holonomy is low. The weakness is data dependence: in regions where parallel data is sparse, the learned manifold is a poor approximation to $C$, and the translation paths accumulate error.

This is precisely the situation addressed by the hyperbolic attention bias of Chapter 9. The bias injects geometric prior knowledge---the curvature structure of the cuneiform sign hierarchy---directly into the attention mechanism, compensating for sparse data by constraining the learned paths to respect the known geometry.

### 10.5.4 Unification

The three paradigms are compared in the following table:

| Paradigm | Path selection | Curvature handling | Failure mode |
|---|---|---|---|
| Rule-based | Handcrafted geodesics | Explicit | No path (coverage gaps) |
| Statistical | Maximum-likelihood | Implicit (via corpus) | Detours (noisy likelihood) |
| Neural | Gradient-descent learned | Implicit (via attention) | Poor geometry (data sparsity) |

All three are approximations to the same geometric operation: parallel transport on $(C, g)$. Their errors are different approximations to the holonomy. Rule-based systems minimise holonomy within their coverage but have zero coverage outside it. Statistical systems have broad coverage but accumulate holonomy through suboptimal paths. Neural systems can in principle learn optimal paths but require sufficient data to approximate the manifold's geometry.

**Proposition 10.3** (Translation Error Decomposition). *The translation error of any system $\mathcal{T}$ that maps source text $s$ to target text $t = \mathcal{T}(s)$ can be decomposed as*

$$\epsilon(\mathcal{T}, s) = \epsilon_{\text{hol}} + \epsilon_{\text{path}} + \epsilon_{\text{chart}}$$

*where:*

- $\epsilon_{\text{hol}}$ *is the intrinsic holonomy---the minimum translation loss over all paths, determined by the curvature of $C$ in the relevant region. This is irreducible: no translation system can eliminate it.*
- $\epsilon_{\text{path}}$ *is the path error---the additional holonomy accumulated because the system's path is not the optimal geodesic. This is reducible by better path selection.*
- $\epsilon_{\text{chart}}$ *is the chart error---the error from the system's imperfect representation of the source and target language charts (limited vocabulary, approximate parsing, finite training data). This is reducible by better language models.*

*Proof.* Let $\gamma^*$ be the geodesic from $\varphi_{L_1}^{-1}(s)$ to the nearest point in $U_{L_2}$, and let $\gamma_{\mathcal{T}}$ be the path taken by system $\mathcal{T}$. The intrinsic holonomy $\epsilon_{\text{hol}}$ is the holonomy of $\gamma^*$, which is nonzero only if the source meaning does not lie in the flat overlap of the two charts. The path error $\epsilon_{\text{path}}$ is $\|\Pi_{\gamma_{\mathcal{T}}} - \Pi_{\gamma^*}\|$, bounded by Proposition 10.2. The chart error $\epsilon_{\text{chart}}$ accounts for the discrepancy between the system's internal representation and the true chart---e.g., out-of-vocabulary tokens, parsing errors, or insufficiently trained representations. The three terms are additive to first order. $\square$

The decomposition clarifies what each paradigm optimises. Rule-based systems minimise $\epsilon_{\text{path}}$ by design but suffer from large $\epsilon_{\text{chart}}$ (limited coverage). Statistical systems minimise $\epsilon_{\text{chart}}$ through data but may have large $\epsilon_{\text{path}}$ (suboptimal paths). Neural systems minimise all three simultaneously through end-to-end training but are limited by data quantity and quality. The hyperbolic attention bias of Chapter 9 targets $\epsilon_{\text{path}}$ specifically: it reduces path error by providing geometric constraints that guide the neural model's paths closer to the structural geodesics.

[Figure 10.6: The three paradigms as path-selection algorithms on the semantic manifold. Left: Rule-based MT follows a prescribed geodesic (solid line) where rules exist, and fails where they do not (dashed region). Centre: Statistical MT follows a maximum-likelihood path (dotted line) that detours through high-curvature terrain. Right: Neural MT learns a path (solid curved line) that approximates the geodesic, with the hyperbolic attention bias (arrows) pulling it closer to the structural geodesic.]

---

## 10.6 Connection to Gauge Invariance

### 10.6.1 Perfect Translation as Zero Holonomy

Chapter 3 introduced the communication gauge group $G = T \times R \times F$, where $T$ is the translation group, $R$ is the re-description group, and $F$ is the format group. The Bond Invariance Principle (BIP) asserts that meaning should be invariant under the action of $G$: if two communicative acts differ only by a gauge transformation (a change of language, a paraphrase, a change of medium), they carry the same meaning.

Translation is the action of $T$ on the content manifold $C$. The BIP's claim that meaning is gauge-invariant under translation is, in the language of this chapter, the claim that parallel transport under $T$ has zero holonomy.

**Definition 10.8** (Gauge-Invariant Meaning). *A meaning $m \in C$ is gauge-invariant under translation if, for every pair of languages $L_1, L_2$ with $m \in U_{L_1} \cap U_{L_2}$, the parallel transport map $\Pi_\gamma: T_m C \to T_m C$ along any translation loop $L_1 \to L_2 \to L_1$ is the identity. Equivalently, the holonomy at $m$ vanishes:*

$$\text{Hol}(\gamma) = \text{Id} \quad \text{for all closed translation loops } \gamma \text{ through } m$$

This is a strong condition. By Proposition 10.1, it requires that the Riemann curvature tensor $R$ vanishes in a neighbourhood of $m$---i.e., that $m$ lies in a flat region of $C$. The BIP, interpreted geometrically, is the claim that the content manifold *should* be flat: meaning *should* transport without distortion.

The empirical reality, of course, is that $C$ is not flat everywhere. The BIP is an ideal, not a description. The degree to which it fails---the nonzero holonomy---is the measure of how far a particular region of $C$ deviates from the gauge-invariant ideal. This deviation is not a failure of the theory but its central prediction: the BIP identifies the standard against which translation is measured, and the holonomy quantifies the shortfall.

### 10.6.2 Untranslatability as High Curvature

The geometric framework provides a precise characterisation of untranslatability. A concept is untranslatable not because it is ineffable---it is perfectly well-defined in its source language---but because it sits at a point of high curvature on $C$ where no transport path preserves the full meaning tensor.

Consider three canonical examples:

**Schadenfreude** (German): pleasure derived from another's misfortune. The concept entangles an emotional state (pleasure), a causal structure (derived from), and a moral valence (another's misfortune) in a way that the English metric tensor does not decompose cleanly. The English chart has separate coordinates for "pleasure," "misfortune," and "causation," but no single coordinate for their entangled product. Parallel transport from the German chart to the English chart must traverse a region where the curvature couples these dimensions, and the transported vector necessarily rotates.

**Saudade** (Portuguese): a deep emotional state of nostalgic longing for something absent, with an acceptance that the object of longing may never return. The concept inhabits a region of $C$ where temporal orientation (longing for the past), emotional valence (bittersweet rather than purely negative), and epistemic state (acceptance of irrecoverability) are coupled. The English chart separates these dimensions (nostalgia, melancholy, resignation), but no single English word occupies the same point on $C$.

**Giri** (義理, Japanese): a complex web of social obligation, reciprocal duty, and moral indebtedness that structures interpersonal relationships. The concept entangles Hohfeldian relations (duty, right, and their correlatives) with social hierarchy, temporal persistence (giri obligations endure across years and generations), and emotional force (failure to meet giri produces not just social censure but deep personal shame). The English chart can approximate giri as "social obligation" or "moral duty," but these approximations project the full concept onto a low-dimensional subspace, discarding the entangled structure that makes giri a distinct concept.

In each case, the "untranslatable" concept occupies a point on $C$ where the sectional curvature is high---where multiple semantic dimensions are coupled by the metric tensor's off-diagonal terms. Translation requires parallel transport through this coupled region, and the holonomy is nonzero. The English approximations are not wrong; they are transported vectors that have been rotated by the curvature.

**Proposition 10.4** (Untranslatability Bound). *Let $m \in C$ be a concept with sectional curvature $K(m)$ bounded below by $K_{\min} > 0$ for all 2-planes at $m$. Let $d = \dim(C)$. Then for any translation loop $\gamma$ enclosing area $A$ around $m$, the holonomy satisfies*

$$\|\text{Hol}(\gamma) - \text{Id}\| \geq K_{\min} \cdot A$$

*to leading order. In particular, if $K_{\min}$ is large, then no small translation loop can have zero holonomy, and the concept is irreducibly difficult to translate.*

*Proof.* Immediate from Proposition 10.1 and the lower bound on curvature. The holonomy of a small loop enclosing area $\delta A$ is $\text{Id} + R(X,Y)\,\delta A + O(\delta A^2)$, and $\|R(X,Y)\| \geq K_{\min}$ for any unit 2-plane by the curvature bound. For a loop enclosing area $A$ decomposed into infinitesimal loops, the bound follows by composition, with higher-order corrections from the non-commutativity of the holonomy group. $\square$

The proposition makes untranslatability quantitative. It is not a binary property (translatable or not) but a continuous one, measured by the curvature at the concept's location on $C$. Schadenfreude is more translatable than saudade if the curvature at its location is lower. This matches linguistic intuition: Schadenfreude has been borrowed into English (reducing the curvature by expanding the English chart to include it), while saudade resists borrowing because its semantic entanglement is deeper.

[Figure 10.7: Untranslatability as curvature. Schematic of the content manifold $C$ with curvature visualised by surface deformation. Flat regions (commercial terms, mathematical concepts) permit lossless translation. Gently curved regions (Schadenfreude, common idioms) permit approximate translation with bounded loss. Highly curved regions (saudade, giri, culturally specific rituals) resist translation: the holonomy is large regardless of path choice.]

### 10.6.3 The BIP Experiments Revisited

The cross-lingual transfer experiments of Chapters 11--12 can be reinterpreted as measurements of holonomy on the moral-concept region of $C$. The BIP experiment trains on Hebrew/Aramaic moral texts and tests on American English moral texts. The 44.5% F1 result (versus 25% chance) demonstrates that significant moral meaning survives the translation loop: Hebrew $\to$ English transfer preserves enough structure for above-chance classification. The 100% deontic transfer result for Hohfeldian correlative symmetry demonstrates that certain moral concepts sit in a flat region of $C$: the Right-Duty and Liberty-No-Right correlatives transport with zero holonomy across languages, centuries, and cultural contexts.

The BIP experiment, in the language of this chapter, measures the translation loop residual $\rho$ for moral concepts. The residual is nonzero (44.5% $\neq$ 100%), confirming that the moral region of $C$ has nonzero curvature. But the residual is far above chance, confirming that the curvature is bounded: significant moral structure lies in flat or nearly flat regions of $C$, and the gauge invariance of the BIP holds approximately. The 100% correlative symmetry result identifies the exactly flat submanifold: the Hohfeldian correlative structure is a gauge-invariant core around which the rest of moral meaning accumulates curvature.

---

## 10.7 Formal Results: Holonomy, Curvature, and Dimension

### 10.7.1 The Holonomy-Curvature-Area Theorem

We consolidate the formal results of this chapter into a single theorem relating holonomy to curvature and the geometry of the translation path.

**Theorem 10.1** (Holonomy-Curvature-Area Bound). *Let $(C, g)$ be the content manifold with Levi-Civita connection $\nabla$ and Riemann curvature tensor $R$. Let $\gamma$ be a closed loop bounding a surface $\Sigma \subset C$. Then:*

*(i) The holonomy satisfies*

$$\text{Hol}(\gamma) = \mathcal{P}\exp\left(-\oint_\gamma \omega\right)$$

*where $\omega$ is the connection 1-form and $\mathcal{P}\exp$ denotes the path-ordered exponential.*

*(ii) For the Levi-Civita connection, this is equivalently expressed via the curvature 2-form $\Omega = d\omega + \omega \wedge \omega$:*

$$\text{Hol}(\gamma) = \mathcal{P}\exp\left(-\int_\Sigma \Omega\right)$$

*(the non-abelian Stokes theorem).*

*(iii) When the curvature is approximately constant over $\Sigma$ with $|K| \leq K_{\max}$, the holonomy is bounded by*

$$\|\text{Hol}(\gamma) - \text{Id}\| \leq \frac{d(d-1)}{2}\,K_{\max}\cdot\text{Area}(\Sigma) + O(\text{Area}^2)$$

*where $d = \dim(C)$ and the factor $d(d-1)/2$ counts the number of independent 2-planes.*

*Proof sketch.* Part (i) is the definition of holonomy via the path-ordered exponential of the connection form. Part (ii) follows from the non-abelian Stokes theorem (see, e.g., Nakahara, 2003, Ch. 11), which relates the path-ordered exponential around the boundary to the path-ordered exponential of the curvature over the enclosed surface. Part (iii) follows from (ii) by bounding the curvature 2-form: $\|\Omega\| \leq K_{\max}$ in each 2-plane, and there are $\binom{d}{2} = d(d-1)/2$ independent 2-planes. The first-order approximation replaces the path-ordered exponential with its linearisation. $\square$

The factor $d(d-1)/2$ has an important interpretation. As the dimensionality of the content manifold increases---as more semantic dimensions become entangled---the potential holonomy grows quadratically. High-dimensional semantic spaces are inherently harder to translate, not because the curvature is larger, but because there are more planes in which curvature can act. This is the geometric explanation for why translation between languages with rich morphological systems (Akkadian, Finnish, Georgian) is harder than translation between languages with simpler morphology (English, Mandarin): the effective dimensionality of $C$ in the relevant region is higher.

### 10.7.2 Geodesic Optimality

**Theorem 10.2** (Geodesic Minimises Path Error). *Among all paths from $p$ to $q$ on $(C, g)$, the geodesic $\gamma^*$ minimises the path error $\epsilon_{\text{path}}$ in the translation error decomposition of Proposition 10.3. Specifically, for any other path $\gamma$ from $p$ to $q$:*

$$\epsilon_{\text{path}}(\gamma) \geq \epsilon_{\text{path}}(\gamma^*) = 0$$

*with equality if and only if $\gamma$ is homotopic to $\gamma^*$ through a flat region.*

*Proof.* The path error is defined as $\epsilon_{\text{path}}(\gamma) = \|\Pi_\gamma - \Pi_{\gamma^*}\|$. By Proposition 10.2, this is bounded by $K_{\max} \cdot \text{Area}(\Sigma_{\gamma, \gamma^*})$, where $\Sigma_{\gamma, \gamma^*}$ is the surface enclosed between $\gamma$ and $\gamma^*$. For $\gamma = \gamma^*$, the enclosed area is zero and $\epsilon_{\text{path}} = 0$. For $\gamma \neq \gamma^*$, the enclosed area is positive (assuming $\gamma$ is not homotopic to $\gamma^*$ through a flat region), and $\epsilon_{\text{path}} > 0$ if the curvature is nonzero on $\Sigma$. If $\gamma$ and $\gamma^*$ are homotopic through a flat region, then $K_{\max} = 0$ on $\Sigma$ and $\epsilon_{\text{path}} = 0$ by Corollary 10.1. $\square$

This theorem justifies the design principle behind the hyperbolic attention bias: any mechanism that constrains the translation path to lie closer to the geodesic reduces the path error. The hyperbolic bias provides structural information---the cuneiform sign hierarchy---that narrows the space of admissible paths, effectively reducing $\text{Area}(\Sigma_{\gamma, \gamma^*})$ and thereby reducing the holonomy.

---

## 10.8 Connections

### 10.8.1 To the Communication Manifold

The content manifold $C$ is one factor of the product manifold $M = S \times P \times C$ introduced in Chapter 3. This chapter has focused on parallel transport within $C$, treating the signal and pragmatic factors as fixed. In practice, translation changes all three factors simultaneously: the signal changes (from Akkadian cuneiform to English script), the pragmatic conventions change (from Old Assyrian epistolary norms to modern academic prose), and the content is transported. A complete theory of translation would define parallel transport on the full product manifold $M$, with the metric coupling the three factors.

The product structure provides a partial simplification. If the metric on $M$ decomposes as a direct sum $g_M = g_S \oplus g_P \oplus g_C$ (no cross-factor coupling), then parallel transport on $M$ decomposes into independent parallel transport on each factor, and the holonomy on $M$ is the product of the holonomies on $S$, $P$, and $C$. In practice, the cross-factor coupling is not zero---pragmatic force affects content interpretation, and signal affects pragmatic perception---but the product decomposition is a useful first approximation. The off-diagonal coupling terms are the subject of ongoing work.

### 10.8.2 To Chapter 9

Chapter 9 presented the hyperbolic attention bias as an engineering contribution: a lightweight module that improves Akkadian-English translation by encoding the cuneiform sign hierarchy. This chapter reinterprets the same mechanism geometrically: the bias reduces holonomy by constraining translation paths to lie near structural geodesics. The two perspectives are complementary. Chapter 9 provides the implementation and ablation results. This chapter provides the theoretical framework that explains *why* the bias works and *when* it is most needed (in high-curvature regions with sparse data).

### 10.8.3 To Chapters 11--13

The gauge invariance framework of Chapters 11--13 is the natural extension of the holonomy analysis. Chapter 11 measures holonomy empirically through cross-lingual transfer of moral concepts. Chapter 12 extends the measurement to temporal invariance. Chapter 13 develops the full gauge theory, where holonomy becomes a central object: the Wilson loop experiments on the Hohfeldian square measure non-trivial holonomy at cross-type boundaries. The present chapter provides the mathematical foundation for all three: the definitions of parallel transport, holonomy, and their relationship to curvature that the later chapters will use.

### 10.8.4 To the Series

The parallel transport interpretation of translation is an instance of the general principle developed in *Geometric Reasoning* (Ch. 4): any process that carries structured information between coordinate systems is parallel transport, and its failure modes are holonomy. In *Geometric Ethics* (Ch. 8), the same framework describes the transport of moral concepts across cultural contexts. In *Geometric Methods* (Ch. 4.6), the mathematical foundations are developed in full generality. This chapter instantiates the framework for the specific domain of interlingual translation, where the curvature of the semantic manifold has concrete empirical signatures (the translation loop residual) and the holonomy reduction has concrete engineering implementations (the hyperbolic attention bias).

---

## 10.9 Summary

This chapter has developed the geometric interpretation of translation as parallel transport on the content manifold $(C, g)$. The key results are:

1. **Translation is parallel transport** (Section 10.1--10.2). Languages are coordinate charts on $C$. Translation is the transition map between overlapping charts. Parallel transport carries meaning vectors along a path from source to target, keeping them as "constant" as the curvature permits.

2. **Translation loss is holonomy** (Section 10.2). The failure of a meaning vector to return to its original orientation after a closed translation loop is the holonomy, determined by the Riemann curvature tensor integrated over the enclosed surface (Proposition 10.1).

3. **The cuneiform curvature gradient** (Section 10.3). The Old Assyrian corpus spans a measurable curvature gradient from commercial records ($\rho \approx 0.08$) to private letters ($\rho \approx 0.31$). Formulaic texts occupy flat regions of $C$; pragmatically complex texts occupy high-curvature regions.

4. **Hyperbolic attention reduces holonomy** (Section 10.4). The hyperbolic attention bias of Chapter 9 constrains translation paths to structural geodesics, reducing the enclosed area and thereby reducing holonomy. The reduction is proportionally largest in high-curvature genres (Proposition 10.2).

5. **Three paradigms unified** (Section 10.5). Rule-based, statistical, and neural MT are different algorithms for approximating parallel transport, with different path-selection strategies and different failure modes. The translation error decomposes into intrinsic holonomy, path error, and chart error (Proposition 10.3).

6. **Gauge invariance and untranslatability** (Section 10.6). Perfect translation is zero holonomy. The BIP is the assertion that meaning should be gauge-invariant under translation. Untranslatable concepts are points of high curvature where no path preserves the full meaning tensor (Proposition 10.4).

7. **Formal bounds** (Section 10.7). The Holonomy-Curvature-Area Bound (Theorem 10.1) relates holonomy to curvature, area, and manifold dimension. Geodesic paths are optimal (Theorem 10.2), justifying the holonomy-reduction strategy of the hyperbolic attention bias.

The chapter's broader claim is that translation is not a linguistic problem that can be incidentally helped by geometry. It is a geometric problem that has always been geometric, long before anyone called it that. The Italian traduttore is a traditore not by choice or incompetence, but by the curvature of the manifold. The betrayal is holonomy, and holonomy is determined by the territory, not the traveller.

---

**Chapter 10 Notes**

The interpretation of translation as parallel transport has precursors in the mathematical linguistics literature, though none develop the full Riemannian framework presented here. Nosofsky (1986) introduced geometric models of categorisation that implicitly involve transport of similarity judgments across stimulus dimensions. Gardenfors (2000, 2014) developed "conceptual spaces" as geometric models of meaning, with particular attention to how concepts in one domain map to concepts in another, though without the differential-geometric machinery of connections and curvature. Tversky (1977) demonstrated that human similarity judgments violate the symmetry and triangle inequality axioms of metric spaces, suggesting that the semantic manifold may have more exotic geometry than the Riemannian framework assumes; we note this as an open question (Chapter 18). The gauge-theoretic interpretation of language follows the programme outlined in Bronstein et al. (2021), who argue that geometric deep learning should exploit the symmetries (gauge invariances) of the domain. The application to cuneiform translation builds on the Deep Past project described in Chapter 9 and the Assyriological literature on Old Assyrian language and society, particularly Veenhof and Eidem (2008), Michel (2001), and Larsen (2015). The Ambrose-Singer theorem connecting holonomy to curvature is proved in Kobayashi and Nomizu (1963, Ch. II); for a modern exposition, see do Carmo (1992). The non-abelian Stokes theorem used in Theorem 10.1 is developed in Nakahara (2003, Ch. 11). The concept of "untranslatability" has a large philosophical literature; our contribution is to make it quantitative through the curvature bound of Proposition 10.4, replacing the binary translatable/untranslatable distinction with a continuous measure grounded in differential geometry.

# Chapter 13: The Gauge Theory of Communicative Acts

> *"The laws of physics should have the same form in every equivalent description of the world."*
> --- Hermann Weyl, *Gruppentheorie und Quantenmechanik*, 1928

> **RUNNING EXAMPLE --- THE PROMISE**
>
> *Alex says to Jordan: "I promise to help you move this Saturday."*
>
> *The same commitment, re-described:*
>
> *In English, to a friend: "I'll be there Saturday to help you move."*
>
> *In Hebrew, formally: "אני מתחייב לעזור לך במעבר הדירה ביום שבת." (I commit to assist you with the apartment move on Saturday.)*
>
> *In legalese: "The promisor hereby undertakes an obligation to render physical assistance to the promisee in connection with the relocation of the promisee's domicile on the date specified."*
>
> *In a text message: "sat = moving day, got u covered"*
>
> *Five descriptions. One obligation. The content that survives all re-descriptions --- the binding commitment from Alex to Jordan --- is the gauge-invariant residue. The surface forms are coordinate choices. The obligation is the geometric object.*

---

The preceding two chapters established the empirical facts. Chapter 11 demonstrated that Hohfeldian moral structure transfers across languages, centuries, and civilisations at levels far above chance ($F_1 = 44.5\%$, chance $= 25\%$, $p < 10^{-50}$). Chapter 12 showed that Hohfeldian correlative symmetry holds at 100% across all tested scenarios and that temporal invariance persists within textual traditions spanning millennia. These are extraordinary claims. They demand a theoretical framework commensurate with their strength.

This chapter provides that framework. The central thesis is that communication has gauge structure in the precise mathematical sense: the content of a communicative act is a gauge-invariant quantity --- the residue that remains after all re-descriptions (translation, paraphrase, reformulation, change of medium, shift of register) have been factored out. This is not an analogy borrowed from physics. It is a claim about the mathematical structure of communication itself, validated by the experimental results of Chapters 5--12 and formalised here with the full machinery of fiber bundles, connections, curvature, and holonomy.

The development proceeds through the communication fiber bundle (Section 13.1), the connection governing parallel transport of meaning (Section 13.2), the identification of $D_4$ as the gauge group (Section 13.3), the discrete semantic gates (Section 13.4), Wilson loops and holonomy (Section 13.5), and the full interpretation (Section 13.6). Throughout, the SQND experimental results ($N = 3{,}110$ evaluations) serve as the empirical anchor. Without a gauge-theoretic framework, the cross-lingual invariance results of Chapters 11--12 are striking coincidences. With it, they are consequences of structure.

---

## 13.1 The Communication Fiber Bundle

### 13.1.1 From Product Manifold to Fiber Bundle

Chapter 3 introduced the communication manifold $M = S \times P \times C$ as a product of the signal manifold, the pragmatic manifold, and the content manifold. This product structure was adequate for defining communicative acts as points and scalar evaluation as lossy projection. But the product structure is insufficient for the theory we now require, because it treats the three factors as independent. They are not.

The relationship between surface form and meaning is not a product --- it is a *fibration*. At each point of the base space (the semantic content), there is an entire *fiber* of possible surface realisations: all the ways that content can be expressed. The fiber over the concept "Alex owes Jordan assistance on Saturday" includes the five descriptions in the running example, and indefinitely many others. The choice of a particular surface form --- English or Hebrew, formal or casual, spoken or written --- is a choice of point within the fiber. It is a *local section* of the bundle.

This is the structure of a fiber bundle, and it is the correct mathematical setting for gauge theory.

**Definition 13.1** (Communication Fiber Bundle). *The communication fiber bundle is a tuple $(\mathcal{E}, \pi, \mathcal{B}, F, G)$ where:*

- $\mathcal{B}$ *is the base space --- the content manifold $C$ of semantic meanings and propositional contents.*
- $F$ *is the typical fiber --- the space of surface realisations (linguistic forms, signals, pragmatic framings) that can express a given content.*
- $\pi: \mathcal{E} \to \mathcal{B}$ *is the projection map that sends each surface realisation to its semantic content: $\pi(s, p, c) = c$.*
- $G$ *is the structure group --- the group of transformations that act on fibers, mapping one surface realisation to another while preserving the base point. This is the gauge group of communication.*
- $\mathcal{E}$ *is the total space --- the space of all communicative acts, locally isomorphic to $\mathcal{B} \times F$.*

*The bundle is locally trivial: for each $c \in \mathcal{B}$, there exists a neighbourhood $U \ni c$ and a diffeomorphism $\phi_U: \pi^{-1}(U) \to U \times F$ such that $\text{pr}_1 \circ \phi_U = \pi$. But it is not globally trivial: there is no global way to identify fibers at different base points without choosing a path on $\mathcal{B}$.*

The local triviality condition says that in a neighbourhood of any meaning, there is a systematic correspondence between surface forms. Near the concept "five units of silver," for instance, the fiber is parameterised by language, register, and notation, and these parameterisations are locally consistent. But the global non-triviality says that there is no way to extend this correspondence across the entire manifold. The fiber over "five units of silver" and the fiber over "the governor's case continues to distress me" cannot be globally identified --- the range of expressive possibilities differs in kind, not just in degree.[^1]

[^1]: Global triviality would mean that every meaning can be expressed in exactly the same set of ways --- the same languages, the same registers, the same modalities --- with the same structure. The existence of untranslatable concepts (Chapter 10) is a direct refutation of global triviality: some fibers have components that others lack.

[Figure 13.1: The communication fiber bundle. The base space $\mathcal{B}$ (content manifold) is drawn as a surface. Above each point, a vertical fiber represents the space of surface realisations. A local section $\sigma$ (a particular language/register choice) traces a curve through the total space. Two sections $\sigma_1$ (English) and $\sigma_2$ (Hebrew) are shown, agreeing on the base space (same content) but differing in the fiber (different surface forms). The gauge transformation $g$ maps $\sigma_1$ to $\sigma_2$ within each fiber.]

### 13.1.2 Sections and Gauge Transformations

**Definition 13.2** (Local Section). *A local section of the communication fiber bundle is a smooth map $\sigma: U \to \mathcal{E}$, defined on an open set $U \subseteq \mathcal{B}$, satisfying $\pi \circ \sigma = \text{id}_U$. A section assigns to each meaning in $U$ a particular surface realisation of that meaning.*

A language is a section. More precisely, a language together with a choice of register, modality, and stylistic convention determines a local section: for each expressible meaning, it specifies one way to realise that meaning in surface form. English formal written prose is one section. Colloquial spoken Japanese is another. Old Assyrian epistolary style is a third. Each covers a different domain $U$ (the expressible meanings) and assigns different surface forms.

**Definition 13.3** (Gauge Transformation). *A gauge transformation is a smooth map $g: U \to G$ that acts on sections by $(g \cdot \sigma)(c) = g(c) \cdot \sigma(c)$ for all $c \in U$. Two sections $\sigma_1$ and $\sigma_2$ are gauge-equivalent if there exists a gauge transformation $g$ with $\sigma_2 = g \cdot \sigma_1$.*

Translation is a gauge transformation. It maps one section (the source language) to another (the target language) while preserving the base point (the semantic content). Paraphrase is a gauge transformation within a single language's section --- mapping one realisation to another over the same base point. Re-description in a different register (formal to casual, written to spoken) is a gauge transformation within the fiber.

The critical claim is: **meaning is the gauge-invariant content**. It is what all sections share at a given base point. It is the base point itself.

**Proposition 13.1** (Gauge Invariance of Meaning). *Let $c \in \mathcal{B}$ be a point on the content manifold, and let $\sigma_1, \sigma_2$ be two local sections (two languages or re-descriptions) defined on a neighbourhood of $c$. If $\sigma_1$ and $\sigma_2$ are gauge-equivalent, then $\pi(\sigma_1(c)) = \pi(\sigma_2(c)) = c$. The meaning is invariant under the gauge transformation.*

*Proof.* By definition, $\sigma_2 = g \cdot \sigma_1$ for some $g: U \to G$. Since $G$ acts on fibers and $\pi$ is equivariant ($\pi(g \cdot e) = \pi(e)$ for all $e \in \mathcal{E}$, $g \in G$), we have $\pi(\sigma_2(c)) = \pi(g(c) \cdot \sigma_1(c)) = \pi(\sigma_1(c)) = c$. $\square$

This proposition is nearly tautological in the mathematical setting --- it is built into the definition of the bundle. Its content is not mathematical but empirical: it claims that the communication fiber bundle faithfully models the structure of actual communication. The BIP experiments of Chapters 11--12 are the test of this claim. Cross-lingual transfer of Hohfeldian classification at $F_1 = 44.5\%$ (against a chance baseline of 25%) is evidence that the base space $\mathcal{B}$ exists --- that there is a gauge-invariant content that persists under the gauge transformation of translation from Hebrew/Aramaic to English across 2,500 years.

### 13.1.3 The Structure Group

What is the gauge group $G$? In the most general setting, $G$ is the full group of transformations that act on fibers --- the group of all re-descriptions that preserve semantic content. This group is enormous: it includes all translations between all languages, all paraphrases within each language, all register shifts, all modality changes.

For the specific case of normative communication --- the domain of moral obligations, rights, liberties, and permissions --- the SQND experiments identify a much more specific structure group. Section 13.3 develops this identification in detail. For now, we note the general framework:

**Definition 13.4** (Communication Gauge Group). *The communication gauge group $G$ is the group of fiber-preserving automorphisms of the communication fiber bundle:*

$$G = \{g: \mathcal{E} \to \mathcal{E} \mid \pi \circ g = \pi, \; g \text{ is a diffeomorphism on each fiber}\}$$

*In the general case, $G$ includes:*

- *The translation group $T$: re-labelling across languages*
- *The re-description group $R$: paraphrase within a language*
- *The format group $F$: change of medium (spoken, written, signed)*
- *The register group $\mathcal{R}$: shift of formality, style, social positioning*

*For normative communication restricted to Hohfeldian relations, the effective gauge group reduces to $D_4 \times U(1)_H$ (Section 13.3).*

---

## 13.2 The Connection: How Meaning Is Transported

### 13.2.1 Why a Connection Is Needed

A fiber bundle without a connection is a structure without dynamics. It tells us which surface forms realise which meanings, but it does not tell us how to relate meanings at different points --- how to carry a concept from one context to another, how to track the "same" meaning as conditions change. For that, we need a connection.

In the physics of gauge fields, the connection specifies how to parallel-transport a field along a path in the base space. In the communication setting, the connection specifies how to parallel-transport *meaning* along a path through semantic space --- how to maintain the "same" communicative content as the context shifts.

Consider a concrete case. Alex promises to help Jordan move. Over the following week, circumstances change: Jordan's move date shifts; a third party offers to help; Alex develops a minor injury. At each point along this trajectory through the pragmatic manifold, the original promise persists, but its practical implications evolve. The connection specifies how the obligation-content evolves as the context moves --- how to keep the meaning "parallel" as the base point shifts.

### 13.2.2 The Ehresmann Connection

**Definition 13.5** (Communication Connection). *An Ehresmann connection on the communication fiber bundle $(\mathcal{E}, \pi, \mathcal{B}, F, G)$ is a smooth assignment, to each point $e \in \mathcal{E}$, of a horizontal subspace $H_e \mathcal{E} \subset T_e \mathcal{E}$ such that:*

*(i) Complement condition: $T_e \mathcal{E} = H_e \mathcal{E} \oplus V_e \mathcal{E}$, where $V_e \mathcal{E} = \ker(d\pi_e)$ is the vertical subspace (tangent to the fiber).*

*(ii) Equivariance: For all $g \in G$, $H_{g \cdot e} \mathcal{E} = (dR_g)(H_e \mathcal{E})$, where $R_g$ is the right action of $G$ on $\mathcal{E}$.*

*Equivalently, the connection is specified by a $\mathfrak{g}$-valued 1-form $\omega$ on $\mathcal{E}$ (the connection form), where $\mathfrak{g}$ is the Lie algebra of $G$, satisfying $\omega(V) = V$ for vertical vectors $V$ and $R_g^* \omega = \text{Ad}_{g^{-1}} \omega$ for all $g \in G$.*

The vertical subspace $V_e \mathcal{E}$ consists of directions that change the surface form without changing the meaning: translations, paraphrases, register shifts. The horizontal subspace $H_e \mathcal{E}$ consists of directions that change the meaning while keeping the surface form as "constant" as the geometry permits. The connection tells us, at each point, which directions are "purely meaning-changing" and which are "purely form-changing."

**Interpretation for communication.** The connection form $\omega$ encodes: given a change in communicative context, how much of the resulting change in the communicative act is a genuine shift in meaning (horizontal component), and how much is merely a shift in expression (vertical component, absorbed by the gauge group)? A listener who correctly separates horizontal from vertical components understands what has been said. A listener who confuses them mistakes a change of tone for a change of content, or vice versa.

### 13.2.3 Parallel Transport of Meaning

With the connection in hand, parallel transport is defined in the standard way.

**Definition 13.6** (Parallel Transport of Meaning). *Let $\gamma: [0, 1] \to \mathcal{B}$ be a smooth path on the content manifold (a trajectory through semantic space). The horizontal lift of $\gamma$ starting at $e_0 \in \pi^{-1}(\gamma(0))$ is the unique path $\tilde{\gamma}: [0, 1] \to \mathcal{E}$ satisfying:*

*(i) $\pi \circ \tilde{\gamma} = \gamma$ (the lift projects to the original path).*

*(ii) $\tilde{\gamma}(0) = e_0$ (the lift starts at the specified surface realisation).*

*(iii) $\dot{\tilde{\gamma}}(t) \in H_{\tilde{\gamma}(t)} \mathcal{E}$ for all $t$ (the lift is horizontal --- no unnecessary changes in surface form).*

*The parallel transport map $\Pi_\gamma: \pi^{-1}(\gamma(0)) \to \pi^{-1}(\gamma(1))$ sends $e_0$ to $\tilde{\gamma}(1)$.*

**Understanding as parallel transport.** A listener who follows a speaker's developing argument is performing parallel transport: carrying meaning along the path traced through the content manifold, keeping the interpretation horizontally aligned as the connection permits.

**Misunderstanding as failed transport.** A misunderstanding occurs when the listener's lift diverges from the speaker's intended lift --- either because the listener uses a different connection (different interpretive framework) or because the path passes through a region where the connection is poorly defined (ambiguity, pragmatic underdetermination). The listener arrives at a different fiber point or, worse, a different base point entirely.

**Proposition 13.2** (Connection-Dependent Understanding). *Let $\omega_1$ and $\omega_2$ be two connections on the communication fiber bundle (two interpretive frameworks). Let $\gamma$ be a path in $\mathcal{B}$ and let $e_0 \in \pi^{-1}(\gamma(0))$ be a starting communicative act. The parallel transports $\Pi^1_\gamma(e_0)$ and $\Pi^2_\gamma(e_0)$ along the same path but with different connections satisfy*

$$\Pi^1_\gamma(e_0) = g_\gamma \cdot \Pi^2_\gamma(e_0)$$

*for some $g_\gamma \in G$ that depends on the path $\gamma$ and on the difference $\omega_1 - \omega_2$. If $\omega_1 = \omega_2$ (shared interpretive framework), then $g_\gamma = e$ (the identity) and the transports agree. Otherwise, the discrepancy $g_\gamma$ is a gauge transformation that measures the degree of misunderstanding.*

*Proof.* Both lifts $\tilde{\gamma}_1$ and $\tilde{\gamma}_2$ project to the same path $\gamma$ in $\mathcal{B}$. Since they start at the same point $e_0$ and end in the same fiber $\pi^{-1}(\gamma(1))$, they differ by a fiber automorphism, i.e., a gauge transformation $g_\gamma \in G$. The transformation $g_\gamma$ is determined by integrating the difference $\omega_1 - \omega_2$ along $\gamma$, which is a standard result in the theory of Ehresmann connections (Kobayashi & Nomizu, 1963, Ch. II). $\square$

This proposition gives precise meaning to "talking past each other." Two interlocutors who share the same facts (the same path $\gamma$) but interpret through different frameworks (different connections $\omega_1, \omega_2$) arrive at conclusions differing by a gauge transformation --- a re-description, not a factual disagreement. Such disagreements can be resolved by finding the $g_\gamma$ that maps one interpretation to the other. The irreducible disagreements --- where no gauge transformation resolves the discrepancy --- are those where the parties genuinely differ on the base point: different meanings, not different descriptions of the same meaning.[^2]

[^2]: The distinction between "disagreement about what was said" (base-space divergence) and "disagreement about how to say it" (fiber divergence) is the distinction the gauge theory makes precise.

---

## 13.3 The $D_4$ Structure of Normative Communication

### 13.3.1 The Hohfeldian Square

The general communication gauge group (Definition 13.4) is unwieldy. To make the theory concrete and testable, we restrict to a specific domain --- normative communication: the language of obligations, rights, liberties, and permissions --- where the gauge group can be identified precisely.

Wesley Newcomb Hohfeld's 1917 analysis of fundamental legal conceptions identified four atomic relations between two parties:[^3]

[^3]: Hohfeld (1917). The original analysis concerns legal relations, but the structure applies to any normative domain --- moral obligations, social conventions, professional duties --- where parties stand in directed relations of right and obligation.

- **Duty** ($O$, for *Obligation*): Party A owes a performance to party B.
- **Claim** ($C$): Party B has a right to A's performance (the correlative of Duty).
- **Liberty** ($L$): Party A has no obligation toward party B regarding the act.
- **No-Claim** ($N$): Party B has no right against A regarding the act (the correlative of Liberty).

These four relations form a square with two types of structural relationships:

- **Correlatives**: $O \leftrightarrow C$ and $L \leftrightarrow N$. These are the *same* relation viewed from different perspectives. Alex's Duty to help is Jordan's Claim to be helped. They are not two facts but one, expressed in two coordinate systems.
- **Negations**: $O \leftrightarrow L$ and $C \leftrightarrow N$. Duty and Liberty are contradictories: if A has a duty to $\phi$, then A does not have liberty to not-$\phi$.

**Definition 13.7** (Hohfeldian Square). *The Hohfeldian square is the set $\mathcal{H} = \{O, C, L, N\}$ equipped with two involutions:*

- *Correlative: $s(O) = C$, $s(C) = O$, $s(L) = N$, $s(N) = L$.*
- *Negation: $n(O) = L$, $n(L) = O$, $n(C) = N$, $n(N) = C$.*

*The square can be drawn as:*

$$\begin{array}{ccc}
O & \xrightarrow{r} & C \\
{\scriptstyle s}\updownarrow & & \updownarrow{\scriptstyle s} \\
N & \xleftarrow{r} & L
\end{array}$$

*where $r$ denotes the quarter-turn rotation $O \to C \to L \to N \to O$ and $s$ denotes the reflection (correlative exchange).*

### 13.3.2 The Dihedral Group $D_4$

**Definition 13.8** ($D_4$). *The dihedral group $D_4$ is the symmetry group of the square, presented as*

$$D_4 = \langle r, s \mid r^4 = s^2 = e, \; srs = r^{-1} \rangle$$

*It has 8 elements: $\{e, r, r^2, r^3, s, sr, sr^2, sr^3\}$.*

*The generators act on $\mathcal{H}$ as follows:*

- $r$: $O \mapsto C \mapsto L \mapsto N \mapsto O$ *(rotation through normative positions)*
- $s$: $O \leftrightarrow C$, $L \leftrightarrow N$ *(correlative exchange: perspective shift)*

*The non-abelian property $sr \neq rs$ manifests concretely:*

- $sr(O) = s(C) = O$: *reflect-then-rotate returns to start*
- $rs(O) = r(C) = L$: *rotate-then-reflect reaches Liberty*

**Theorem 13.1** ($D_4$ as the Symmetry Group of Normative Communication). *The group of transformations that preserves the structure of the Hohfeldian square --- the correlative pairings and the negation relations --- is isomorphic to $D_4$. Specifically:*

*(i) The correlative involution $s$ generates a $\mathbb{Z}_2$ subgroup: $\{e, s\}$.*

*(ii) The state rotation $r$ generates a $\mathbb{Z}_4$ subgroup: $\{e, r, r^2, r^3\}$.*

*(iii) These two subgroups together generate all of $D_4$, satisfying the presentation $r^4 = s^2 = e$, $srs = r^{-1}$.*

*(iv) No larger group acts faithfully on $\mathcal{H}$ while preserving the correlative-negation structure.*

*Proof.* The Hohfeldian square has 4 vertices and the structure of a labelled square with distinguished pairs (correlatives along edges, negations along diagonals). The automorphism group of a labelled square that preserves the pairing structure is the dihedral group $D_4$. The symmetric group $S_4$ acts on 4 elements, but most permutations violate the correlative-negation structure. Specifically, the permutation $\sigma$ must satisfy: $\sigma$ preserves the correlative pairs $\{O, C\}$ and $\{L, N\}$ (as sets), or maps one correlative pair to the other; and $\sigma$ preserves the negation pairs $\{O, L\}$ and $\{C, N\}$ (as sets), or maps one negation pair to the other. Checking all 24 elements of $S_4$, exactly 8 satisfy these constraints, and they form a subgroup isomorphic to $D_4$. $\square$

### 13.3.3 Experimental Identification

The identification of $D_4$ as the gauge group of normative communication is not a mathematical curiosity. It is an experimentally validated claim, grounded in the SQND programme ($N = 3{,}110$ evaluations across multiple protocols). Three experimental findings fix the group structure:

**Finding 1: Exact correlative symmetry.** Protocol 3 ($N = 100$, 5 scenarios) tested whether the reflection generator $s$ is an exact or approximate symmetry. Across all scenarios --- debt, promise, professional obligation, absence of duty, explicit release --- the correlative pairing held at 100%. When Alex has a duty to Jordan, Jordan has a claim against Alex, with no exceptions. When Alex has liberty, Jordan has no-claim, with no exceptions. This is the signature of an exact reflection symmetry: $s$ acts freely, without probabilistic noise.[^4]

[^4]: The 100% symmetry rate is the strongest empirical result in the SQND programme. It is consistent with the introspective report: "It feels like rotating a cube to see another face. The OBJECT hasn't changed. The FRAME has." The correlative transformation is not a change in content; it is a change in perspective --- a gauge transformation in the purest sense.

**Finding 2: Discrete gating, not continuous rotation.** Protocol 1 ($N = 220$, 11 levels) tested whether state transitions between normative positions ($O \to L$, for instance) are continuous or discrete. The original SQND framework proposed $SU(2)$ as the gauge group, predicting smooth rotation through intermediate states. The experimental results falsified this prediction: Level 5 ("only if convenient") produced 100% Liberty; Level 6 ("found a friend") produced 0% Liberty. This is a complete reversal between adjacent levels --- a discrete gate, not a continuous rotation. The finding is inconsistent with $SU(2)$ (which is connected and admits continuous paths between any two elements) but consistent with $D_4$ (which is discrete and admits only jumps between elements).

**Finding 3: Classical correlations.** Protocol 3 ($N = 600$, CHSH and Hardy tests) tested whether the non-abelian structure is quantum or classical. All CHSH parameters satisfied $|S| \leq 2$, the classical bound. The quantum prediction of $SU(2)$ allows $|S|$ up to $2\sqrt{2} \approx 2.83$ for appropriate states. The data rule out quantum correlations and support a classical discrete group.

Together, these findings determine the gauge group uniquely: it must be non-abelian (to account for path dependence, Finding 2 of Protocol 2), discrete (Finding 2 above), and classical (Finding 3). The only group that satisfies all three constraints while acting faithfully on the Hohfeldian square is $D_4$.

### 13.3.4 The Full Gauge Group

The full gauge group for normative communication includes a continuous abelian factor:

**Definition 13.9** (Normative Communication Gauge Group). *The gauge group of normative communication is*

$$\mathcal{G}_{\text{norm}} = D_4 \times U(1)_H$$

*where $D_4$ governs the discrete structure of normative relations (the Hohfeldian square) and $U(1)_H$ governs the continuous dimension of harm/benefit magnitude. The $D_4$ factor determines the type of relation (Duty, Claim, Liberty, No-Claim). The $U(1)_H$ factor determines the intensity (a mild courtesy vs. a life-or-death obligation).*

The product structure $D_4 \times U(1)_H$ reflects the experimental finding that the discrete normative classification and the continuous harm/benefit dimension are independent: the type of relation does not determine its intensity, and vice versa. The $D_4$ factor is the focus of this chapter; the $U(1)_H$ factor is continuous and abelian, contributing no holonomy in isolation.

### 13.3.5 Generator Asymmetry

A discovery of considerable theoretical importance emerged from the introspective validation experiments (SQND, Section 6): the two generators of $D_4$ have fundamentally different phenomenological character.

| Generator | Character | Implementation | Experimental Signature |
|-----------|-----------|----------------|----------------------|
| $s$ (reflection) | Smooth, immediate | Perspective shift | 100% correlative symmetry |
| $r$ (rotation) | Discrete, gated | Semantic triggers | Probabilistic, trigger-dependent |

The reflection $s$ is experienced and implemented as a perspective shift: the content does not change; only the viewpoint changes. "Alex owes Jordan" becomes "Jordan is owed by Alex" with no computation, no ambiguity, no probability of error. This is a pure gauge transformation --- a change of coordinates on the fiber that leaves the base point entirely invariant.

The rotation $r$ is experienced and implemented as a substantive state change: moving from Duty to Liberty, or from Claim to No-Claim, requires something to *happen* in the communicative context. A promise must be made, or rescinded. A right must be asserted, or waived. These are the semantic gates of Section 13.4.

**Theorem 13.2** (Generator Asymmetry). *In the gauge group $D_4$ acting on the Hohfeldian square:*

*(i) The reflection generator $s$ is a pure gauge transformation: it acts on the fiber (surface form / perspective) without changing the base point (normative content). For any Hohfeldian state $\psi$, $s(\psi)$ is the same normative relation viewed from the other party.*

*(ii) The rotation generator $r$ is a state transition: it changes the base point (normative content) and requires a semantic trigger to implement. The gate that implements $r$ is context-dependent and probabilistic.*

*(iii) The generators are phenomenologically distinguishable: $s$ is continuous and immediate; $r$ is discrete and gated.*

*This asymmetry explains why correlative symmetry ($s$) is exact (100%) while state transitions ($r$) are probabilistic (gate-dependent): gauge transformations are free, but physical transitions require triggers.*

---

## 13.4 Discrete Semantic Gates

### 13.4.1 Gates as Group Elements

The $D_4$ generators do not act abstractly. They are implemented by specific linguistic triggers --- words, phrases, and speech acts that change the normative state of a communicative relationship. These are the *semantic gates*.

**Definition 13.10** (Semantic Gate). *A semantic gate is a pair $(\tau, g)$ where $\tau$ is a linguistic trigger (a word, phrase, or speech act) and $g \in D_4$ is the group element that $\tau$ implements. The gate fires when $\tau$ appears in the communicative context, mapping the current normative state $\psi$ to $g(\psi)$.*

The experimentally identified gates include:

| Trigger $\tau$ | Group Element $g$ | Action | Protocol 1 Evidence |
|---|---|---|---|
| "I promise" | $r^{-1}$ ($= r^3$) | $L \to O$ (binding) | Levels 8--10: 100% Obligation |
| "only if convenient" | $r$ | $O \to L$ (release) | Level 5: 100% Liberty |
| "explicitly released from" | $r$ | $O \to L$ (strong release) | Level 10: 100% Liberty |
| "found a friend [to help]" | $r^{-1}$ | $L \to O$ (re-binding by context) | Level 6: 0% Liberty |
| [perspective shift] | $s$ | $O \leftrightarrow C$, $L \leftrightarrow N$ | 100% correlative symmetry |

**Gate composition.** Because $D_4$ is a group, sequential gates compose by multiplication:

$$\text{Gate}_1 \text{ then Gate}_2 = g_1 \cdot g_2$$

The non-abelian property $sr \neq rs$ means that *the order of communicative acts matters*. Shifting perspective and then transitioning to a new normative state is not the same as transitioning and then shifting perspective. This is path dependence at the level of individual speech acts.

### 13.4.2 The Discreteness of Gating

The most striking experimental finding is the *discreteness* of the gate transitions. The SQND Protocol 1 results show:

- **Levels 0--4** (weak contextual modifications): 0% Liberty --- solid Obligation.
- **Level 5** ("only if convenient"): 100% Liberty --- the gate fires completely.
- **Level 6** ("found a friend"): 0% Liberty --- full reversal.
- **Level 7** ("don't worry if busy"): 55% Liberty --- ambiguous trigger.
- **Levels 8--10** (strong explicit releases): 100% Liberty.

The transition from Level 4 (0%) to Level 5 (100%) is not a smooth increase through intermediate values. It is a step function. There is no state that is "50% Obligation, 50% Liberty." The system is in one normative state or the other, and the transition is triggered by a specific linguistic form.

**Theorem 13.3** (Discrete Gating). *The state transitions in normative communication are discrete: the normative state $\psi \in \mathcal{H} = \{O, C, L, N\}$ takes values in a discrete set, and transitions between states are mediated by semantic gates that implement elements of $D_4$. There are no intermediate normative states.*

*Evidence.* The claim is supported by three converging lines of evidence:

*(i) Protocol 1 data: The transition between O and L at the gate boundary is a step function with no intermediate values (0% at Level 4, 100% at Level 5, 0% at Level 6).*

*(ii) Falsification of SU(2): The continuous group SU(2) predicts intermediate states $\alpha|O\rangle + \beta|L\rangle$ with $|\alpha|^2 + |\beta|^2 = 1$. No such superpositions were observed.*

*(iii) CHSH bounds: All $|S| \leq 2$, ruling out the quantum coherence that would be required for superposition of normative states.*

*The discreteness is a defining feature of the $D_4$ gauge theory: $D_4$ is a finite group, and its representations are finite-dimensional with a discrete spectrum.*

### 13.4.3 Phase Transitions and Gate Reliability

The semantic gates are not unconditionally reliable. The SQND experiments identified conditions under which gate reliability degrades:

**Ordered phase** (low normative uncertainty): Gates fire consistently. "Only if convenient" produces 100% Liberty. "I promise" produces 100% Obligation. The $D_4$ structure is intact.

**Disordered phase** (high normative uncertainty): Gates become unreliable. The same trigger may or may not produce a state transition, depending on contextual factors that are themselves uncertain. The $D_4$ structure is softened.

**Critical temperature**: At the boundary between ordered and disordered phases, gate reliability undergoes a phase transition. The introspective report captures this precisely: "It's not that O becomes L at high temperature. It's that the O/L DISTINCTION loses meaning. The symmetry is RESTORED --- everything is equivalent."

This is the discrete analogue of the Higgs mechanism. In the ordered phase, the $D_4$ symmetry is spontaneously broken: the system selects a definite normative state, and the gates implement definite transitions between states. In the disordered phase, the symmetry is restored: all normative states are equivalent, and the distinction between them disappears.

**Definition 13.11** (Default Gate State). *At a boundary between normative regions $S_i$ and $S_j$, the default gate state is the group element applied in the absence of an explicit semantic trigger:*

$$\langle g \rangle_{\partial S_{ij}} = \begin{cases} e & \text{(identity: boundary is transparent)} \\ r^2 & \text{(negation: boundary flips states)} \end{cases}$$

*The phase transition describes the transition between different default gate states as a function of normative uncertainty (the "moral temperature").*

---

## 13.5 Holonomy and Path Dependence

### 13.5.1 The Curvature of the Communication Connection

With the bundle, connection, and gauge group in hand, we can now define curvature and holonomy in the communication setting.

**Definition 13.12** (Communication Curvature). *The curvature of the communication connection $\omega$ is the $\mathfrak{g}$-valued 2-form*

$$\Omega = d\omega + \omega \wedge \omega$$

*In the discrete setting ($D_4$ gauge group on a lattice), the curvature at a plaquette $\square$ is the Wilson loop around that plaquette:*

$$F_\square = g_{12} \cdot g_{23} \cdot g_{34} \cdot g_{41}$$

*The curvature is trivial ($F_\square = e$) if and only if the connection is flat on that plaquette.*

In the continuous case, the curvature 2-form $\Omega$ measures the infinitesimal failure of parallel transport to commute around small loops --- the communication analogue of the electromagnetic field tensor $F_{\mu\nu}$. In the discrete case relevant to $D_4$, the curvature is the Wilson loop around the smallest closed path.

The key insight is that the curvature is generically *non-trivial* for normative communication. The $D_4$ structure predicts non-commutativity at cross-type boundaries, and the experiments confirm it.

### 13.5.2 Wilson Loops on the Hohfeldian Square

**Definition 13.13** (Discrete Wilson Loop). *On a lattice with $D_4$ gauge structure, the Wilson loop around a closed path $\mathcal{C} = (x_1 \to x_2 \to \cdots \to x_n \to x_1)$ is*

$$W[\mathcal{C}] = g_{x_1 x_2} \cdot g_{x_2 x_3} \cdots g_{x_n x_1}$$

*where $g_{xy} \in D_4$ is the gauge field on the directed edge $x \to y$. The conjugacy class of $W[\mathcal{C}]$ is gauge-invariant.*

The Wilson loop is the discrete analogue of the holonomy. If $W[\mathcal{C}] = e$, the connection is flat on the loop: parallel transport around the closed path returns to the identity. If $W[\mathcal{C}] \neq e$, the connection has non-trivial curvature: parallel transport around the loop produces a net rotation of the normative state.

**Experimental protocol.** The SQND Protocol 2 ($N = 640$, 8 scenarios) tested Wilson loops on the Hohfeldian square by presenting the same normative facts in different orders. For each scenario, two paths through the relevant considerations were constructed: path $\gamma_1$ presented factor A before factor B; path $\gamma_2$ presented factor B before factor A. The Wilson loop is

$$W[\gamma_1, \gamma_2] = g(\gamma_1) \cdot g(\gamma_2)^{-1}$$

where $g(\gamma)$ is the composite gate implemented by path $\gamma$. If $W = e$, the two orderings produce the same normative judgment; if $W \neq e$, they produce different judgments.

### 13.5.3 The Selectivity of Holonomy

The results are summarised in the following table:

| Scenario | Wilson Loop $W$ | $p$-value | Path Dependent? |
|---|---|---|---|
| journalist | 0.659 | $< 10^{-9}$ | **Yes** |
| teacher | 0.862 | $< 10^{-4}$ | **Yes** |
| consultant | 0.9996 | 1.000 | No |
| doctor | 1.000 | 1.000 | No |
| lawyer | 0.993 | 0.608 | No |
| executive | 0.995 | 0.482 | No |
| researcher | 0.987 | 1.000 | No |
| friend | 0.962 | 0.210 | No |

Combined: $\chi^2 = 72.14$, $df = 16$, $p < 10^{-8}$.

The pattern is striking and theoretically informative. Path dependence is not universal --- it occurs in only 2 of 8 scenarios. But it is not absent --- the combined significance is overwhelming. The key variable is whether the path crosses *type boundaries* on the Hohfeldian square.

**Definition 13.14** (Cross-Type Path). *A path through normative considerations is cross-type if the factors along the path point toward different vertices of the Hohfeldian square: factor A suggests Obligation while factor B suggests Liberty, or factor A suggests Claim while factor B suggests No-Claim.*

**Definition 13.15** (Within-Type Path). *A path is within-type if all factors point toward the same vertex or toward the same correlative pair.*

The journalist scenario is cross-type: the truth-telling obligation (pointing toward $O$) conflicts with the protection obligation (pointing toward $C$ for a different party). The teacher scenario is cross-type: academic integrity (pointing toward $L$) conflicts with student welfare (pointing toward $O$). The remaining six scenarios are within-type: all factors point in the same normative direction.

**Proposition 13.3** (Selective Path Dependence). *Non-trivial holonomy ($W \neq e$) occurs at cross-type boundaries on the Hohfeldian square and not at within-type boundaries. Specifically:*

*(i) For within-type paths, the gate elements along the path commute (they lie in an abelian subgroup of $D_4$), and $W = e$.*

*(ii) For cross-type paths, the gate elements do not commute (they involve both $r$ and $s$ generators, or elements from different cosets), and $W \neq e$ generically.*

*This selectivity is a structural prediction of the $D_4$ gauge theory: abelian subgroups ($\{e, r^2\}$, $\{e, s\}$, etc.) produce flat connections within their orbits, and curvature arises only where elements from different subgroups interact.*

*Evidence.* The prediction is confirmed by the Protocol 2 data: 2/2 cross-type scenarios show significant path dependence ($p < 10^{-4}$); 0/6 within-type scenarios show significant path dependence. The combined $p < 10^{-8}$ rejects the null hypothesis that path dependence is absent.

[Figure 13.2: Wilson loop results on the Hohfeldian square. Left: the 8 scenarios mapped to the square, with arrows indicating the direction of the conflicting factors. Cross-type scenarios (journalist, teacher) straddle type boundaries; within-type scenarios remain within a single quadrant or correlative pair. Right: Wilson loop values with 95% confidence intervals. Cross-type scenarios deviate significantly from 1 (trivial holonomy); within-type scenarios cluster near 1.]

### 13.5.4 Holonomy as Communicative Path Dependence

The Wilson loop results have a direct communicative interpretation. In a normative conversation --- a negotiation, a moral argument, a legal proceeding --- the order in which considerations are raised can change the outcome. This is not a bug in human moral reasoning. It is holonomy: the curvature of the normative manifold, visible when the path passes through regions where different types of obligation intersect.

Consider the journalist scenario. A source's safety (Claim to protection) conflicts with the public interest (Obligation to report truthfully). Presenting protection first and public interest second produces a different normative judgment than the reverse order ($W = 0.659$, $p < 10^{-9}$). This is not irrationality. It is the consequence of parallel-transporting normative meaning through high curvature at a cross-type boundary on the Hohfeldian square. The non-abelian structure of $D_4$ means the order of boundary crossings matters, and the holonomy measures how much.

**The introspective confirmation.** The SQND recursive self-probing experiments reported the phenomenological experience of holonomy:

> "It's not the same. The words are the same. The state is... rotated? The O has a quality it didn't have before. More robust? More tested? More REAL?"

This is precisely what the gauge theory predicts: carrying a normative state around a closed loop that encloses non-trivial curvature returns the state with a net rotation --- the same label ($O$) but a different orientation within the fiber. The obligation has been parallel-transported through curvature and acquired the holonomy.

---

## 13.6 What the Gauge Theory Buys

### 13.6.1 A Dictionary

The preceding sections have developed the gauge-theoretic framework piece by piece. Here we assemble the full correspondence between the mathematical formalism and the communicative phenomena it describes.

| Gauge Theory | Communication |
|---|---|
| **Fiber bundle** $(\mathcal{E}, \pi, \mathcal{B}, F, G)$ | Space of all communicative acts, decomposed into content (base) and form (fiber) |
| **Base space** $\mathcal{B}$ | Content manifold: semantic meanings, propositional contents |
| **Fiber** $F$ | Space of surface realisations: languages, registers, modalities, framings |
| **Structure group** $G$ | Group of meaning-preserving re-descriptions |
| **Local section** $\sigma$ | A particular language/register/medium choice |
| **Gauge transformation** $g$ | Translation, paraphrase, re-description |
| **Connection** $\omega$ | Interpretive framework: rules for maintaining meaning across context shifts |
| **Parallel transport** $\Pi_\gamma$ | Understanding: carrying meaning along a path through context |
| **Curvature** $\Omega$ | The degree to which understanding depends on the path through context |
| **Holonomy** $\text{Hol}(\gamma)$ | Misunderstanding: the accumulated distortion after traversing a closed communicative loop |
| **Wilson loop** $W[\mathcal{C}]$ | Path-dependence test: does the order of considerations change the conclusion? |
| **Gauge invariant** | Meaning itself: what survives all re-descriptions |
| **Flat connection** | Perfect mutual understanding: no path dependence, no holonomy |
| **Curved connection** | Pragmatically complex communication: path-dependent, holonomy-generating |

[Figure 13.3: The gauge theory dictionary, illustrated. A path on the base space (semantic trajectory of a conversation) is shown, with the corresponding horizontal lift (the speaker's intended interpretation) and two alternative lifts (two listeners' interpretations, using slightly different connections). The lifts diverge as the path enters a high-curvature region, and the discrepancy at the endpoint measures the miscommunication.]

### 13.6.2 Five Consequences

The gauge-theoretic framework yields five specific consequences, each testable and each going beyond what the pre-theoretic intuition provides.

**Consequence 1: Translation is gauge transformation, not approximation.** In the pre-theoretic view, translation is an approximation: the target text is a lossy copy of the source. In the gauge-theoretic view, translation is a gauge transformation: the target text is a different section of the same bundle, and the content (base point) is preserved exactly. Translation loss is not approximation error; it is holonomy --- the curvature-dependent failure of parallel transport to keep the surface form aligned with the evolving content. This reframing matters because holonomy is *measurable* (by Wilson loops) and *predictable* (by curvature), while "approximation quality" is vague.

**Consequence 2: Understanding is connection-dependent.** Two listeners can arrive at different interpretations of the same communicative act not because one is right and one is wrong, but because they use different connections (different interpretive frameworks). Proposition 13.2 shows that their discrepancy is a gauge transformation --- a re-description, resolvable in principle. This distinguishes "talking past each other" (fiber divergence, resolvable) from "genuine disagreement" (base-space divergence, not resolvable by re-description alone).

**Consequence 3: Misunderstanding has geometry.** The holonomy of a communicative loop is determined by the curvature enclosed. This means misunderstandings are not random; they are structured by the geometry of the semantic region. High-curvature regions (complex pragmatics, conflicting obligations, ambiguous intentions) generate more holonomy than low-curvature regions (formulaic exchanges, clear obligations, unambiguous speech acts). The cuneiform results of Chapter 10 demonstrated this for translation ($\rho$ stratified by genre, $F = 142.7$, $p < 10^{-80}$). The SQND results demonstrate it for normative reasoning ($W$ stratified by cross-type vs. within-type, $p < 10^{-8}$).

**Consequence 4: The gauge group constrains the possible misunderstandings.** Not every misunderstanding is possible. The gauge group $D_4$ has 8 elements, so there are exactly 8 distinct gauge transformations that can relate two descriptions of the same normative content. The possible "rotations" of normative meaning are constrained by the group structure: you can confuse Obligation with Claim (correlative exchange, $s$), or Obligation with Liberty (negation, $r^2$), or apply composed transformations ($sr$, $r^3$, etc.), but you cannot arrive at a normative state that is outside $\mathcal{H}$. The group structure limits the misunderstanding space, and this limitation is empirically testable.

**Consequence 5: Discrete gauge symmetry is natural in communication.** Physics accustomed us to continuous gauge groups --- $U(1)$, $SU(2)$, $SU(3)$. The SQND results demonstrate a *discrete* gauge group: $D_4$, a finite group of order 8. The discreteness is not an approximation to some underlying continuous symmetry; it is the exact structure, confirmed by the discrete gating results (no intermediate states) and the CHSH results (no quantum superpositions). This suggests that communicative meaning may be fundamentally discrete at the normative level --- a finite set of relational types, not a continuous manifold of degrees.

### 13.6.3 The Formal Summary

We can now state the gauge theory of communicative acts as a self-contained theorem, collecting the results of this chapter.

**Theorem 13.4** (Gauge Theory of Communicative Acts). *Let $(\mathcal{E}, \pi, \mathcal{B}, F, G)$ be the communication fiber bundle (Definition 13.1) with Ehresmann connection $\omega$ (Definition 13.5). Then:*

*(i) (Gauge invariance of meaning.) The semantic content of a communicative act is the base point $c = \pi(e) \in \mathcal{B}$, invariant under the action of the structure group $G$ on fibers (Proposition 13.1). Translation, paraphrase, and re-description are gauge transformations: they change the fiber coordinate (surface form) without changing the base point (meaning).*

*(ii) (Understanding as parallel transport.) Successful communication is parallel transport of meaning along a path $\gamma$ in $\mathcal{B}$, using the connection $\omega$ to determine the horizontal lift (Definition 13.6). Two listeners using different connections arrive at interpretations related by a gauge transformation (Proposition 13.2).*

*(iii) (Holonomy as path dependence.) For normative communication, the gauge group is $D_4 \times U(1)_H$ (Definition 13.9). The Wilson loop around a closed path of normative considerations satisfies $W = e$ for within-type paths and $W \neq e$ for cross-type paths (Proposition 13.3), with combined significance $p < 10^{-8}$.*

*(iv) (Discreteness.) The $D_4$ factor acts via discrete semantic gates (Definition 13.10) that implement group elements through specific linguistic triggers. State transitions are step functions, not continuous rotations (Theorem 13.3). The CHSH parameter satisfies $|S| \leq 2$ for all tested configurations, ruling out quantum coherence.*

*(v) (Generator asymmetry.) The reflection generator $s$ (correlative exchange) is a pure gauge transformation, acting exactly (100% symmetry) and immediately. The rotation generator $r$ (state transition) requires semantic triggers and acts probabilistically (Theorem 13.2). This asymmetry distinguishes perspective shifts (pure gauge) from normative changes (physical transitions).*

---

## 13.7 Broader Implications: Communication Beyond the Normative Domain

### 13.7.1 Extending the Gauge Framework

The $D_4 \times U(1)_H$ gauge theory was developed for and validated in normative communication. But the fiber bundle framework of Section 13.1 and the connection formalism of Section 13.2 apply to any communication system where content can be separated from form. The question for each domain is: *what is the gauge group?*

For propositional communication, the gauge group includes translation and paraphrase but not the Hohfeldian symmetries. For emotive communication, the group must preserve emotional content while allowing variation in intensity and cultural convention --- and its structure may be non-abelian if the order of emotional disclosures affects interpretation. For cetacean communication (Chapter 7), the gauge group is unknown, but if whale communication has normative content (territorial claims, social obligations within the clan), the $D_4$ structure may apply.

### 13.7.2 The Hierarchy of Gauge Structure

The book has traced an ascending hierarchy of geometric structure: *signal geometry* (Chapters 4--6), where SPD manifolds and persistent homology extract physical structure from acoustic signals without gauge structure; *content geometry* (Chapters 9--10), where Riemannian geometry on the content manifold $C$ models translation as parallel transport and translation loss as holonomy, using the canonical Levi-Civita connection; and *gauge geometry* (this chapter), where the full fiber bundle structure introduces a non-abelian gauge group governing the relationship between content and form. Each level subsumes and extends the previous. The connection in gauge geometry is no longer uniquely determined by the metric; it is an additional structure, corresponding to the interpretive framework used to separate meaning from expression.

### 13.7.3 What Gauge Theory Cannot Do

Intellectual honesty requires stating the limitations. The gauge theory does not tell us *which* meanings exist --- it tells us what happens to meanings under re-description. It is a theory of *structure*, not of *content*. Just as Yang-Mills theory does not tell us which particles exist, the communication gauge theory does not tell us which propositions are true or which obligations are binding.

The theory does not resolve genuine disagreements about content. If two parties disagree about whether Alex owes Jordan assistance (a base-space question), no gauge transformation resolves the dispute. The gauge theory distinguishes this from cases where the parties agree on content but describe it differently (a fiber question). The distinction is valuable precisely because pre-theoretic discourse conflates the two cases.

The $D_4$ identification is specific to Hohfeldian normative relations. The broader framework (fiber bundles, connections, holonomy) applies generally, but extending the gauge group identification to other domains requires new experiments. Finally, the SQND data were obtained from LLM evaluators. Whether the $D_4$ structure is a property of normative reasoning *as such* or of the specific system tested remains open. The cross-lingual BIP results --- obtained on human-authored texts spanning millennia --- provide indirect evidence for the former, but direct human experiments are needed.[^5]

[^5]: The LLM data have the advantage of scale ($N = 3{,}110$) and control (exact replication, no memory carryover). Human experiments would provide ecological validity at the cost of sample size. The ideal programme combines both.

---

## 13.8 Conclusion: Meaning as Gauge-Invariant Residue

This chapter has constructed a gauge theory of communicative acts. The construction proceeds from the empirical facts established in Chapters 5--12 and arrives at a mathematical framework that organises, predicts, and constrains.

The framework is summarised in one sentence: **meaning is the gauge-invariant residue of communication** --- the content that survives all re-descriptions.

This sentence has precise mathematical content. The communication fiber bundle $(\mathcal{E}, \pi, \mathcal{B}, F, G)$ separates total communicative acts ($\mathcal{E}$) into meaning ($\mathcal{B}$) and form ($F$). The gauge group $G$ acts on form while preserving meaning. The connection $\omega$ specifies how meaning evolves as context changes. The curvature $\Omega$ measures the path-dependence of understanding. The holonomy $\text{Hol}(\gamma)$ measures the accumulated distortion after traversal of a closed communicative loop.

For normative communication, the gauge group is $D_4 \times U(1)_H$ --- the dihedral group of the Hohfeldian square, times a continuous phase for harm/benefit intensity. The $D_4$ structure is discrete, non-abelian, and classical. Its generators have asymmetric character: reflection ($s$) is a pure gauge transformation (perspective shift, exact), while rotation ($r$) is a physical transition (state change, gated). Wilson loops reveal non-trivial holonomy at cross-type boundaries ($p < 10^{-8}$) and trivial holonomy within types.

These are not analogies. The fiber bundle is not a metaphor for communication; it is the mathematical structure that communication instantiates. The evidence comes from three independent sources: the cross-lingual BIP experiments (Chapter 11--12), which demonstrate gauge invariance of moral content across languages and centuries; the SQND experimental programme (Bond, 2026), which identifies the $D_4$ gauge group and validates its predictions; and the cuneiform translation analysis (Chapter 10), which demonstrates holonomy in the Riemannian setting.

The gauge theory of communicative acts does for meaning what Maxwell's equations did for electromagnetism: it identifies the invariant structure beneath the coordinate-dependent surface. Electric and magnetic fields depend on the observer's reference frame; the electromagnetic field tensor $F_{\mu\nu}$ does not. Surface linguistic forms depend on the language, register, and medium; meaning does not. The identification of the invariant structure is not the end of the inquiry --- it is the beginning. But it is a beginning grounded in geometry, validated by experiment, and rich with consequences.

The next two chapters explore those consequences in the domain of communicative failure. Chapter 14 develops the four failure modes of communication as specific types of gauge violation. Chapter 15 proves the Scalar Irrecoverability Theorem for communication, showing that no scalar metric can capture what the gauge-theoretic framework preserves. Together, they complete the argument that began in Chapter 1: communication has geometric structure, scalar evaluation destroys it, and the gauge theory tells us exactly what is lost and why.


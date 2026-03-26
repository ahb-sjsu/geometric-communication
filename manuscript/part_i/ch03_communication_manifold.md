# Chapter 3: The Communication Manifold

> *"The limits of my language mean the limits of my world."*
> --- Ludwig Wittgenstein, *Tractatus Logico-Philosophicus*, 5.6

> **RUNNING EXAMPLE — THE APOLOGY**
>
> *Consider three apologies for the same offence --- arriving an hour late to a friend's dinner party.*
>
> *Apology A, spoken in English, with a sheepish tone and direct eye contact: "I'm so sorry I'm late. I completely lost track of time."*
>
> *Apology B, written in a text message two hours after the dinner: "Hey, sorry about tonight. Got caught up with something. My bad."*
>
> *Apology C, spoken in Japanese, with a deep bow: "大変申し訳ございませんでした。遅れてしまって、本当に失礼いたしました。" (I am terribly sorry. I was inexcusably late and have been truly rude.)*
>
> *These three acts share a core of semantic content --- an acknowledgment of fault for lateness. But they differ in nearly everything else. The signals are different: spoken English, written English, spoken Japanese with a physical gesture. The pragmatic forces are different: A conveys genuine contrition with a note of self-deprecation; B conveys casual acknowledgment that borders on dismissal; C conveys deep formal respect with an intensity that would strike most English speakers as disproportionate to the offence. The social relations they enact are different: A maintains intimacy, B distances, C elevates the offended party.*
>
> *Any evaluation that reduces these three apologies to a single quality score --- "sincerity: 7/10" --- destroys the structure that makes them different acts in the world. The sheepish tone, the two-hour delay, the depth of the bow --- these are not noise to be averaged away. They are coordinates on a manifold, and the manifold is what this chapter constructs.*

---

In Chapter 1, we established that communication science lives in a perplexity trap: scalar metrics like BLEU scores, word error rates, and classification accuracy compress the structure of meaning into single numbers, and the compression is lossy in ways the Scalar Irrecoverability Theorem (Geometric Reasoning, Ch. 13) makes precise. In Chapter 2, we traced the geometric intuition from Saussure's arbitrariness of the sign (a gauge invariance statement avant la lettre) through Jakobson's distinctive features (a discrete symmetry group on phonological space) to modern word embeddings (explicit coordinates on the semantic manifold). Each generation got closer to the geometry without naming it.

This chapter names it.

We construct the **communication manifold** $M$ --- the geometric space on which communicative acts live. Every utterance, every text message, every whale click, every cuneiform inscription is a point on $M$. The manifold has a metric (what makes two communicative acts "close"), a heuristic field (the learned associations that guide interpretation), and a symmetry group (the transformations that preserve meaning). Together, these structures provide the mathematical foundation for everything that follows: the geometric toolkit of Part II, the empirical analyses of Parts III--V, and the failure taxonomy of Part VI.

The chapter proceeds in six stages. We first define the product structure $M = S \times P \times C$ and explain what each factor captures. We then equip $M$ with a metric that encodes the distinct ways communicative acts can differ. We introduce the heuristic field that guides communicative interpretation. We define the gauge group of meaning-preserving transformations. We state the communication instantiation of the Bond Invariance Principle. And we preview the failure modes that arise when these structures break down.

Throughout, we follow the principle established in *Geometric Reasoning*: every formal definition is preceded by intuition and followed by a concrete instance. The mathematics is not decoration. It is the content.

---

## 3.1 The Product Structure of Communication

### 3.1.1 Why a Product Manifold?

Every communicative act involves at least three distinguishable components. There is the physical carrier --- the sound waves, the ink marks, the hand shapes, the electromagnetic signal. There is the speaker's intention --- what the communicator means to accomplish, the social relation being enacted, the pragmatic force of the act. And there is the propositional content --- the semantic meaning, the state of affairs being described or invoked.

These three components are distinguishable because they can vary independently. The same propositional content ("the meeting is at 3pm") can be carried by different signals (spoken English, written French, American Sign Language). The same signal ("nice job") can carry different intentions (sincere praise, biting sarcasm). The same intention (to warn) can convey different content ("the ice is thin" versus "the deadline has moved"). This independence --- not perfect, but sufficient --- is what makes a product structure appropriate.[^1]

[^1]: The independence is not absolute. Signal constrains content (you cannot express a 500-word argument in a single emoji with full fidelity), and pragmatic context shapes the range of available signals (a legal contract demands written form). These cross-factor dependencies are captured by the metric's off-diagonal terms (Section 3.2) and by the curvature of $M$. The product structure is the zeroth-order approximation; the metric provides the first-order corrections.

### 3.1.2 The Three Factors

**Definition 3.1** (Communication Manifold). *The communication manifold is the product*

$$M = S \times P \times C$$

*where:*

- $S$ *is the signal manifold --- the space of physically realizable communication carriers,*
- $P$ *is the pragmatic manifold --- the space of communicative intentions, social relations, and illocutionary forces,*
- $C$ *is the content manifold --- the space of semantic meanings and propositional contents.*

*A communicative act is a point $\mathbf{m} = (s, p, c) \in M$. A scalar evaluation of a communicative act is a projection $\pi: M \to \mathbb{R}$ that discards the manifold structure.*

Each factor requires elaboration.

**The signal manifold $S$.** The signal manifold is the space of physically realizable carriers. For spoken language, $S$ includes acoustic waveforms parameterized by frequency content, amplitude envelope, duration, and prosodic contour. For written language, $S$ includes sequences of graphemes (or, more precisely, the visual forms of those graphemes --- font, handwriting style, layout). For sign language, $S$ includes hand configurations, movements, facial expressions, and body positions. For cetacean communication, $S$ includes click trains parameterized by inter-click intervals, amplitude profiles, and frequency characteristics.

The key property of $S$ is that it is the factor most directly accessible to measurement. We can record acoustic waveforms, photograph written text, and motion-capture signed language with arbitrary precision. The signal manifold is where empirical science begins --- and where scalar reduction most visibly destroys structure. A word error rate, for instance, projects $S$ onto a count of mismatched tokens, discarding the prosodic, temporal, and spectral structure that distinguishes fluent speech from a sequence of correctly identified words.

The dimensionality of $S$ depends on the communication system. For the sperm whale codas analyzed in Chapter 7, the signal manifold is parameterized by inter-click intervals (a variable-length vector in $\mathbb{R}^n$ where $n$ is the click count), spectral characteristics per click, and amplitude envelope --- roughly 20--50 effective dimensions per coda. For birdsong (Chapter 8), the 156-dimensional geometric feature vector (136 SPD + 4 trajectory + 16 TDA) provides explicit coordinates on $S$. For written text, $S$ is discrete (sequences over a finite alphabet) but can be embedded in continuous space via standard methods.

**The pragmatic manifold $P$.** The pragmatic manifold is the space of communicative intentions, social contexts, and illocutionary forces. This is the factor that speech act theory (Austin, 1962; Searle, 1969) identified but did not geometrize.

The coordinates on $P$ include at minimum:

- **Illocutionary force**: Is the act an assertion, a question, a command, a promise, a warning, an apology? Following Searle's taxonomy, this is a discrete coordinate with at least five values (assertives, directives, commissives, expressives, declaratives), though the boundaries between categories are not always sharp.
- **Speaker-hearer relation**: The social distance, power differential, and degree of familiarity between communicator and audience. Brown and Levinson's (1987) politeness theory parameterizes this by three continuous variables: power ($\mathcal{P}$), social distance ($\mathcal{D}$), and ranking of imposition ($R$).
- **Contextual embedding**: The discourse context in which the act is situated --- what has been said before, what is expected next, what shared knowledge is presupposed.
- **Communicative goal**: What the speaker intends to accomplish beyond the propositional content --- to persuade, to bond, to dominate, to entertain, to deceive.

The pragmatic manifold is the hardest factor to measure directly, and it is the factor most thoroughly destroyed by scalar evaluation. A sentiment score of +0.7 tells us nothing about whether the positive affect is sincere or performed, whether it serves connection or manipulation, whether it respects or violates the social relation between the parties. The geometry of $P$ is where the most interesting structure lives --- and where the most information is lost.

**The content manifold $C$.** The content manifold is the space of semantic meanings and propositional contents. This is, loosely, what the communicative act is "about" --- the state of affairs it describes, the proposition it asserts, the concept it invokes.

The content manifold has been the most studied of the three factors, largely because it is the one that scalar evaluation attempts (however inadequately) to capture. Word embeddings (Mikolov et al., 2013; Pennington et al., 2014) provide explicit coordinates on $C$. Sentence embeddings extend this to propositions. The BIP experiments of Chapters 11--12 demonstrate that $C$ has gauge-invariant structure: the moral content of a proposition is preserved under translation between Hebrew/Aramaic and English, across 2,500 years and two language families.

The content manifold inherits rich geometric structure from the communication systems that express it. Semantic hierarchies (hypernymy, meronymy, troponymy) give $C$ a tree-like structure that embeds naturally in hyperbolic space (Chapter 5). Semantic similarity gives $C$ a metric structure that word embeddings approximate. Polysemy introduces singularities --- points where the manifold degenerates because a single expression maps to multiple meanings --- that we will address in Chapter 10.

### 3.1.3 Points on the Manifold: A Worked Example

To make the abstraction concrete, let us map the three apologies from the running example to points on $M$.

**Apology A** (spoken English, sheepish, in person):

$$\mathbf{m}_A = (s_A, p_A, c_A)$$

where $s_A$ encodes the acoustic waveform of spoken English with sheepish prosody (falling intonation, reduced volume, slightly elevated pitch indicating social discomfort); $p_A$ encodes the pragmatic configuration (illocutionary force: expressive-apology; social relation: intimate-symmetric; communicative goal: restore relationship; contextual embedding: face-to-face, immediately following the offence); and $c_A$ encodes the propositional content (the speaker was late; the speaker acknowledges fault; the cause was the speaker's negligence).

**Apology B** (text message, casual, delayed):

$$\mathbf{m}_B = (s_B, p_B, c_B)$$

where $s_B$ encodes the written text signal (informal orthography, abbreviation "My bad," no punctuation marks of emphasis); $p_B$ encodes the pragmatic configuration (illocutionary force: expressive-apology, attenuated; social relation: casual-distanced; communicative goal: acknowledge without full engagement; contextual embedding: asynchronous, two hours after the offence --- the delay itself is pragmatically loaded); and $c_B$ encodes the propositional content (the speaker was absent; the speaker acknowledges this; the cause is vaguely attributed).

**Apology C** (spoken Japanese, formal bow):

$$\mathbf{m}_C = (s_C, p_C, c_C)$$

where $s_C$ encodes the acoustic waveform of formal Japanese with accompanying deep bow (the gestural component is part of the signal); $p_C$ encodes the pragmatic configuration (illocutionary force: expressive-apology, maximally intensified; social relation: deferential-asymmetric, elevating the offended party; communicative goal: full restoration through self-abasement; contextual embedding: face-to-face, ritualized); and $c_C$ encodes the propositional content (the speaker was late; the speaker was inexcusably rude; the fault is entirely the speaker's).

Now consider the distances between these points. Apologies A and C share similar pragmatic force (both are genuine, face-to-face, relationship-restoring acts) and similar content (both acknowledge fault for lateness), but their signals are maximally different (spoken English vs. spoken Japanese with bow). Apologies A and B share similar signals in the broadest sense (both are in English) but differ sharply in pragmatics (genuine contrition vs. casual acknowledgment) and partially in content (A attributes the cause to negligence, B is vague). These distance patterns are exactly what the metric of Section 3.2 formalizes.

[Figure 3.1] *Three apologies as points on $M = S \times P \times C$. The axes represent (schematically) the three factors. Apology A and Apology C are close on $P \times C$ but far on $S$ (different languages, different modalities). Apology A and Apology B are closer on $S$ (both English) but far on $P$ (different pragmatic force). The dashed projection lines show what scalar evaluation discards: projecting onto any single axis loses the relationships visible in the full space.*

### 3.1.4 Why Product Structure Matters

The product structure $M = S \times P \times C$ is not merely organizational. It has a precise mathematical consequence: **scalar evaluation of a communicative act is a projection onto one factor followed by a further contraction to $\mathbb{R}$.**

A BLEU score operates almost entirely within $S$ and $C$ --- it measures n-gram overlap (a signal-level comparison) as a proxy for content preservation, ignoring $P$ entirely. A sentiment score projects onto a one-dimensional submanifold of $C$ (the valence axis), discarding all other content dimensions and both $S$ and $P$. A word error rate projects onto $S$ alone, treating every token substitution as equally costly regardless of its semantic or pragmatic consequence.

**Proposition 3.1** (Projection Loss). *Let $\pi_S: M \to S$, $\pi_P: M \to P$, and $\pi_C: M \to C$ be the canonical projections. For any scalar evaluation $\phi: M \to \mathbb{R}$ that factors through a single projection --- i.e., $\phi = \psi \circ \pi_X$ for some $X \in \{S, P, C\}$ and some $\psi: X \to \mathbb{R}$ --- the preimage $\phi^{-1}(r)$ for any value $r \in \mathbb{R}$ is a submanifold of $M$ of codimension 1 in $X$ and full dimension in the remaining two factors. In particular, knowing $\phi(\mathbf{m})$ leaves the coordinates on the two unprojected factors entirely undetermined.*

This is the communication-specific form of the Scalar Irrecoverability Theorem. The information loss is not gradual or approximate. It is total in the discarded dimensions. A BLEU score of 0.35 is consistent with any pragmatic force and any social relation whatsoever. A sentiment score of +0.8 is consistent with any signal form and any illocutionary force whatsoever. The product structure makes this irrecoverability transparent: each factor is an independent source of information, and projecting away a factor destroys that information completely.

---

## 3.2 The Communication Metric

### 3.2.1 What Makes Two Communicative Acts "Close"?

We need a metric on $M$ --- a principled measure of distance between communicative acts. Without a metric, the manifold is a topological space only: we know which acts are "nearby" in a qualitative sense, but we cannot say *how far apart* they are, and we cannot define geodesics (optimal communication paths), curvature (the complexity of the communication landscape), or deviation (the extent to which a communicative act misses its target).

The product structure suggests a natural starting point. Since $M = S \times P \times C$, each factor contributes independently to the total distance, and the simplest metric is the product metric:

$$d^2(\mathbf{m}_1, \mathbf{m}_2) = \alpha_S \, d_S^2(s_1, s_2) + \alpha_P \, d_P^2(p_1, p_2) + \alpha_C \, d_C^2(c_1, c_2)$$

where $d_S$, $d_P$, $d_C$ are metrics on the individual factors and $\alpha_S, \alpha_P, \alpha_C > 0$ are weighting coefficients that control the relative importance of each factor. This is a block-diagonal metric: the distance depends only on within-factor distances, with no cross-factor terms.

But block-diagonality is an approximation. In practice, the factors are not fully independent. The signal constrains the content (some meanings are easier to express in some media than others). The pragmatic context shapes the signal (formal settings demand formal register). The content influences the pragmatic possibilities (you cannot sincerely promise something impossible). These cross-factor dependencies are captured by off-diagonal terms in the metric tensor.

**Definition 3.2** (Communication Metric). *The communication metric is a Riemannian metric $g$ on $M$ whose components, in the natural coordinates induced by the product structure, take the block form*

$$g = \begin{pmatrix} g_{SS} & g_{SP} & g_{SC} \\ g_{PS} & g_{PP} & g_{PC} \\ g_{CS} & g_{CP} & g_{CC} \end{pmatrix}$$

*where $g_{SS}$, $g_{PP}$, $g_{CC}$ are the metric tensors on $S$, $P$, $C$ respectively, and the off-diagonal blocks $g_{SP}$, $g_{SC}$, $g_{PC}$ (and their transposes) encode cross-factor correlations.*

The metric tensor $g$ is symmetric and positive-definite, as required for a Riemannian metric. The diagonal blocks carry the primary distance information; the off-diagonal blocks carry the correlation information. When the off-diagonal blocks vanish, the metric is block-diagonal and the factors are metrically independent. When they are nonzero, the factors interact: the distance between two communicative acts depends not only on how they differ in each factor separately, but on how the differences across factors relate to each other.

### 3.2.2 The Diagonal Blocks: Within-Factor Distance

Each diagonal block carries domain-specific structure.

**The signal metric $g_{SS}$.** For acoustic signals (speech, whale clicks, birdsong), the natural metric is the log-Euclidean metric on the SPD manifold of spectral covariance matrices, as developed in Chapter 4:

$$d_{LE}(\Sigma_1, \Sigma_2) = \|\log(\Sigma_1) - \log(\Sigma_2)\|_F$$

where $\Sigma_i$ is the spectral covariance matrix of signal $s_i$ and $\|\cdot\|_F$ is the Frobenius norm. This metric respects the manifold geometry of positive-definite matrices --- it does not suffer from the swelling effect that plagues the arithmetic mean of covariance matrices in Euclidean space. For written text, $g_{SS}$ might be an edit distance, a character-level embedding distance, or a visual similarity measure for handwritten or typographic forms.

**The pragmatic metric $g_{PP}$.** The pragmatic manifold has both continuous and discrete structure. The social-relation coordinates (power, distance, imposition) are continuous and support a standard Euclidean or Riemannian metric. The illocutionary force coordinate is discrete (assertion, question, command, promise, etc.), and the distance between illocutionary types reflects the pragmatic effort of reinterpretation: misinterpreting a question as an assertion is a smaller error than misinterpreting a command as a promise. This mixed structure makes $g_{PP}$ a hybrid metric --- smooth in the continuous directions, discrete-valued in the categorical directions.

**The content metric $g_{CC}$.** For propositional content, the natural metric is the semantic distance in an embedding space. Word-level metrics are inherited from word embeddings; sentence-level metrics from sentence embeddings. The BIP experiments (Chapters 11--12) provide empirical evidence about the structure of $g_{CC}$: the fact that moral content transfers across languages at 44.5% F1 (chance = 25%, $p < 10^{-50}$) means that the content metric is approximately preserved under the translation gauge transformation --- a strong constraint on $g_{CC}$.

For hierarchical content (taxonomies, ontologies, conceptual trees), the Poincare ball metric (Chapter 5) provides a more natural distance:

$$d_{\mathbb{B}}(x, y) = \cosh^{-1}\!\left(1 + 2\frac{\|x - y\|^2}{(1 - \|x\|^2)(1 - \|y\|^2)}\right)$$

This hyperbolic metric captures the exponential growth of semantic specificity: general concepts (near the origin) are close to each other, while specific instances (near the boundary) are far apart, matching the branching structure of natural-language taxonomies.

### 3.2.3 The Off-Diagonal Blocks: Cross-Factor Correlations

The off-diagonal blocks encode the ways in which the factors are not independent. Three types of cross-factor correlation are particularly important for communication.

**Signal-content correlation ($g_{SC}$).** Some signals are intrinsically better carriers for some content. Onomatopoeia is the simplest case: the word "buzz" carries the content *buzzing sound* with a signal that partially instantiates the content. Iconicity in sign language is another: the ASL sign for "tree" resembles a tree. In these cases, $g_{SC} \neq 0$ --- the distance between communicative acts depends on how well the signal "fits" the content. Sound symbolism research (Blasi et al., 2016) suggests that such correlations, while not universal, are widespread across languages.

**Signal-pragmatic correlation ($g_{SP}$).** The signal carries pragmatic information beyond the propositional content. Prosody encodes illocutionary force (rising intonation for questions in many languages). Register encodes social relation (formal vocabulary signals deference; slang signals intimacy). The two-hour delay in Apology B is a signal-level fact (the message was sent at time $t + 2h$) that carries pragmatic weight (it communicates that the apology was not urgent). These signal-pragmatic correlations are captured by $g_{SP}$.

**Pragmatic-content correlation ($g_{PC}$).** The pragmatic context shapes how content is interpreted. The sentence "Can you pass the salt?" has propositional content (a question about the hearer's ability) that is routinely overridden by pragmatic force (an indirect request). The content metric for this sentence depends on the pragmatic context: in a dinner conversation, the content distance between "Can you pass the salt?" and "Please pass the salt" is near zero; in a medical evaluation of motor function, it is large. This context-dependence of content distance is encoded in $g_{PC}$.

### 3.2.4 Characteristic Distance Patterns

The metric structure reveals three characteristic patterns that recur throughout the book.

**Translation**: same content, different signals. For a faithful translation, $d_C(c_1, c_2) \approx 0$ while $d_S(s_1, s_2)$ is large (the source and target language signals are very different). The total distance is dominated by the signal component. In a block-diagonal metric, translation preserves the content coordinates exactly and moves only in the signal directions. In the full metric with cross-terms, the signal change may induce a small content shift (the holonomy of translation, developed in Chapter 10).

**Sarcasm**: same signal, different pragmatics. The utterance "Great job" spoken with sincere enthusiasm and the same utterance spoken with contemptuous sarcasm have $d_S(s_1, s_2) \approx 0$ in the textual representation (identical words) but $d_P(p_1, p_2) \gg 0$ (opposite pragmatic force) and potentially $d_C(c_1, c_2) \gg 0$ (opposite propositional attitude). In the acoustic representation, $d_S$ is nonzero because prosody differs --- but the prosodic difference is small compared to the pragmatic and content difference. Sarcasm is a near-isometry on $S$ that induces a large displacement on $P \times C$.

**Paraphrase**: same content, same pragmatics, different signals within a language. "The cat sat on the mat" and "The mat was sat upon by the cat" have $d_C \approx 0$, $d_P \approx 0$, and $d_S > 0$ (different word sequences). Paraphrase is a pure signal transformation that preserves both content and pragmatics --- it is an element of the gauge group that we define in Section 3.4.

**Proposition 3.2** (Diagnostic Patterns). *The three characteristic patterns --- translation, sarcasm, and paraphrase --- are distinguished by their distance profiles on $M$:*

| Pattern | $d_S$ | $d_P$ | $d_C$ |
|---|---|---|---|
| Translation | large | $\approx 0$ | $\approx 0$ |
| Sarcasm | small | large | large |
| Paraphrase | moderate | $\approx 0$ | $\approx 0$ |

*Any scalar evaluation that projects onto a single factor conflates at least two of these three patterns.*

This proposition makes the information loss of scalar evaluation structurally precise. A metric that sees only $d_S$ (like a word error rate) cannot distinguish translation from paraphrase --- both involve signal change with content preservation. A metric that sees only $d_C$ (like a semantic similarity score) cannot distinguish sincere assertion from sarcasm when both use the same words. Only the full metric on $M$ resolves all three patterns.

---

## 3.3 The Heuristic Field on $M$

### 3.3.1 Interpretation as Navigation

When a hearer receives a communicative signal, they must interpret it --- they must infer, from the observed signal $s$ and the available context, the speaker's pragmatic intention $p$ and the propositional content $c$. This inference problem is a navigation problem on $M$: given a point in $S$ (the observed signal) and partial information about the location in $P$ and $C$ (the context), find the most likely point $(s, p, c) \in M$ that the speaker intended.

This is search, and search requires a heuristic.

**Definition 3.3** (Communication Heuristic Field). *The communication heuristic field is a smooth function*

$$h: M \to \mathbb{R}$$

*that assigns to each point $\mathbf{m} = (s, p, c) \in M$ an estimated cost $h(\mathbf{m})$ of reaching the intended communicative act from $\mathbf{m}$. The gradient $\nabla h$ is the navigational signal that guides interpretation: $-\nabla h$ points toward lower cost, i.e., toward interpretations that the heuristic judges more likely.*

The heuristic field is the mathematical form of what communicators call "context." When you hear "bank" in a conversation about fishing, your heuristic field has a steep gradient toward the *riverbank* interpretation and a flat or uphill gradient toward the *financial institution* interpretation. When you hear "bank" in a conversation about mortgages, the gradients reverse. The heuristic field is not static --- it is dynamically shaped by everything the communicator has learned about language, social convention, the current discourse, and the specific interlocutor.

### 3.3.2 What Constitutes a Good Heuristic?

From *Geometric Reasoning* (Ch. 3), a heuristic is **admissible** if it never overestimates the true cost: $h(\mathbf{m}) \leq h^*(\mathbf{m})$ for all $\mathbf{m} \in M$, where $h^*$ is the true optimal cost-to-go. Translated to communication:

**Definition 3.4** (Admissible Communication Heuristic). *A communication heuristic $h$ is admissible if it never overestimates semantic distance --- i.e., if the interpreted meaning is never judged to be farther from the intended meaning than it actually is.*

An admissible heuristic is a *charitable* interpreter. It may underestimate ambiguity (judging two interpretations to be closer to the intended meaning than they are), but it never overestimates it (it never rules out the correct interpretation by judging it too distant). Charity of interpretation --- the default assumption that the speaker's words make sense and are relevant --- is a pragmatic universal identified by Grice (1975) and Davidson (1974). The geometric framework reveals its mathematical content: charitable interpretation is the communicative form of heuristic admissibility.

A heuristic is **consistent** if it satisfies the triangle inequality: $h(\mathbf{m}_1) \leq d(\mathbf{m}_1, \mathbf{m}_2) + h(\mathbf{m}_2)$ for all $\mathbf{m}_1, \mathbf{m}_2 \in M$. In communication, consistency means that the estimated difficulty of reaching the intended interpretation from $\mathbf{m}_1$ is never more than the estimated difficulty from $\mathbf{m}_2$ plus the cost of moving from $\mathbf{m}_1$ to $\mathbf{m}_2$. Consistent heuristics produce a smooth interpretive landscape without local reversals --- the hearer never needs to "backtrack" in their interpretation.

### 3.3.3 The Sources of the Heuristic

The communication heuristic field is assembled from at least four sources, each contributing to a different region or direction of the gradient.

**Linguistic convention.** The default meanings of words and constructions, accumulated over a lifetime of language exposure. This is the broadest and most stable component of the heuristic. It contributes a strong gradient in the content dimension $C$: hearing the word "dog" activates a steep descent toward the *canine* region of the content manifold.

**Discourse context.** The preceding utterances in the current conversation. This component is dynamic and local. It shapes the heuristic primarily in the pragmatic dimension $P$: a series of questions establishes an interrogative context that biases interpretation of ambiguous utterances toward the question reading. It also modulates $C$ by activating relevant semantic domains (the *fishing* frame, the *banking* frame).

**Social knowledge.** Information about the speaker, the hearer, their relationship, and the social situation. This component shapes $P$ strongly: knowing that the speaker is your boss versus your friend versus a stranger changes the pragmatic gradients dramatically, even for identical signals.

**World knowledge.** General knowledge about how the world works. This component contributes to $C$ by ruling out impossible or implausible interpretations. Hearing "I flew to New York" does not activate the *literal flight* interpretation because world knowledge makes this overwhelmingly unlikely for a human speaker.

**Proposition 3.3** (Heuristic Decomposition). *The communication heuristic field admits an approximate decomposition*

$$h(\mathbf{m}) \approx h_{\text{ling}}(\mathbf{m}) + h_{\text{disc}}(\mathbf{m}) + h_{\text{soc}}(\mathbf{m}) + h_{\text{world}}(\mathbf{m})$$

*where each component contributes primarily to gradients along specific directions in $M$. The decomposition is approximate because the components interact: discourse context modulates the activation of linguistic convention, social knowledge constrains what world knowledge is relevant, and so forth.*

### 3.3.4 Communication Breakdown as Heuristic Corruption

When communication fails --- when the hearer arrives at an interpretation the speaker did not intend --- the geometric diagnosis is straightforward: the heuristic field guided the hearer to the wrong point on $M$. The hearer descended a gradient that led to a local minimum of $h$ that does not coincide with the speaker's intended point.

The general failure taxonomy from *Geometric Reasoning* (Ch. 5) applies directly:

- **False valleys**: The heuristic has a local minimum at an unintended interpretation. The hearer descends into this valley and cannot escape without external information. Example: a non-native speaker interprets "I could care less" literally (as expressing some degree of caring) rather than idiomatically (as expressing complete indifference). The literal interpretation is a false valley in the heuristic landscape --- grammatically coherent and locally consistent, but globally wrong.

- **Flat regions**: The heuristic provides no gradient signal, and the hearer cannot choose between competing interpretations. Example: encountering a genuinely ambiguous sentence like "Visiting relatives can be annoying." The heuristic landscape is flat between the two readings (the act of visiting relatives is annoying / relatives who visit are annoying), and resolution requires additional context.

- **Corrupted gradients**: The heuristic points in the wrong direction due to misleading context or prior experience. Example: a sarcastic speaker says "Wonderful" with flat affect. The hearer's linguistic heuristic has a gradient toward the positive interpretation; the prosodic and contextual heuristic has a gradient toward the negative interpretation. If the linguistic gradient dominates, the hearer misses the sarcasm. This is heuristic corruption in the $P$-direction, caused by a mismatch between $g_{SP}$ (the cross-term that should link the flat prosodic signal to the sarcastic pragmatic force) and the hearer's estimated version of that cross-term.

---

## 3.4 The Communication Gauge Group

### 3.4.1 What Transformations Preserve Meaning?

We arrive at the central question of the book: what is meaning? The geometric answer is: meaning is what is preserved when everything else changes. More precisely, meaning is the invariant content of a communicative act under the group of meaning-preserving transformations.

To define meaning, we must therefore define the transformations that preserve it.

**Definition 3.5** (Communication Gauge Group). *The communication gauge group is*

$$G = T \times R \times F$$

*where:*

- $T$ *is the translation group --- the group of relabelings across languages,*
- $R$ *is the re-description group --- the group of paraphrases within a language,*
- $F$ *is the format group --- the group of modality changes (spoken $\leftrightarrow$ written $\leftrightarrow$ signed).*

*A gauge transformation $\tau \in G$ is a map $\tau: M \to M$ that changes the signal coordinates while preserving the content and pragmatic coordinates (up to the holonomy induced by the transformation path).*

Each component of $G$ deserves careful analysis.

### 3.4.2 The Translation Group $T$

The translation group $T$ contains the transformations that map a communicative act from one language to another while preserving meaning. If $\mathbf{m} = (s, p, c)$ is an assertion in English and $\tau_{E \to F}(\mathbf{m}) = (s', p', c')$ is its French translation, the gauge invariance requirement is:

$$c' = c \quad \text{and} \quad p' \approx p$$

That is, the content is preserved exactly (this is the definition of a faithful translation) and the pragmatic force is preserved approximately (the assertion remains an assertion, the social relation is maintained, the communicative goal is the same). The signal changes entirely: $s'$ is a sequence of French phonemes or graphemes bearing no systematic resemblance to $s$.

The translation group is not abelian. Translating English $\to$ French $\to$ Japanese is not, in general, the same as translating English $\to$ Japanese directly. Different translation paths may induce different holonomies --- different small rotations of the meaning vector upon arrival. This path-dependence is the geometric content of the well-known observation that translation is not transitive: back-translation (English $\to$ French $\to$ English) does not always recover the original.

The empirical evidence for the approximate gauge invariance of content under $T$ is the BIP cross-lingual transfer result (Chapters 11--12): moral content expressed in ancient Hebrew/Aramaic can be recognized by a classifier trained on modern English with 44.5% F1, and the Hohfeldian correlative symmetry holds at 100% across all tested language pairs. This is not perfect invariance --- the 44.5% is above chance ($p < 10^{-50}$) but below ceiling --- and the gap between 44.5% and 100% measures the holonomy of the Hebrew-to-English translation path on the moral-content submanifold.

### 3.4.3 The Re-Description Group $R$

The re-description group $R$ contains the transformations that paraphrase a communicative act within a single language. "The cat sat on the mat," "The mat had a cat sitting on it," and "Upon the mat, a cat was seated" are three elements of $R$ applied to the same content.

$R$ is richer than it first appears. It includes:

- **Syntactic paraphrase**: Active $\leftrightarrow$ passive, cleft constructions, topicalization. These are surface-structure transformations in the Chomskyan sense --- and Chapter 2's observation that Chomsky's deep structure is a quotient manifold (surface forms modded out by syntactic transformations) is precisely the statement that $R$ includes the syntactic transformation group.
- **Lexical paraphrase**: Synonym substitution. "Big" $\leftrightarrow$ "large," "begin" $\leftrightarrow$ "commence." These transformations preserve denotative content but may shift connotative content (register, formality, specificity) --- a fact that makes the boundary between $R$ and the pragmatic transformations fuzzy.
- **Structural paraphrase**: Decomposing a complex sentence into simpler ones, or combining simple sentences into a complex one. "Although he was tired, he kept working" $\leftrightarrow$ "He was tired. Nevertheless, he kept working."

The re-description group is the largest and least well-defined component of $G$. Every natural language has an inexhaustible supply of paraphrases for any given content, and the question of when two expressions are "true paraphrases" (identical in content and pragmatics) versus "approximate paraphrases" (similar content, shifted pragmatics) is one of the oldest problems in linguistics. The geometric framework does not solve this problem, but it reframes it precisely: $R$ is the subgroup of signal transformations under which the metric distance in $P \times C$ is exactly zero. Approximate paraphrases are transformations near $R$ but not in it --- they induce small but nonzero displacements on $P \times C$.

### 3.4.4 The Format Group $F$

The format group $F$ contains the transformations that change the modality of the signal while preserving content and pragmatics. Speaking a written text aloud. Transcribing a spoken utterance. Translating a spoken-language utterance into sign language.

$F$ is the smallest and most structured component of $G$. Its elements are well-defined (the set of available modalities is finite: spoken, written, signed, tactile, electronic) and its action is relatively predictable. The primary source of non-trivial structure in $F$ is the fact that different modalities have different expressive capacities. Speech carries prosody that writing does not. Writing carries visual layout that speech does not. Sign language carries spatial grammar that neither speech nor writing can directly represent. These modality-specific channels mean that $F$ is not a simple relabeling --- format changes may require compensatory adjustments in the signal to preserve the pragmatic and content coordinates.

**Example.** Reading aloud the written sentence "She said she was *fine*" requires a prosodic choice: the italicized "fine" suggests emphasis that carries pragmatic weight (skepticism, sarcasm, or simple stress). The writer used italics --- a visual signal --- to encode pragmatic force. The reader must translate this into a prosodic signal --- an acoustic encoding of the same pragmatic force. The format transformation $F_{\text{written} \to \text{spoken}}$ is not a trivial relabeling; it requires interpreting the pragmatic content of the visual signal and re-encoding it in the acoustic modality. The holonomy of this transformation is the information lost or distorted in the conversion.

### 3.4.5 The Full Gauge Group: Structure and Properties

The full gauge group $G = T \times R \times F$ has several important structural properties.

**$G$ is infinite.** There are infinitely many languages (finitely many extant, but the translation group includes all possible languages, including constructed and historical ones). There are infinitely many paraphrases for any given content. The format group is finite, but the other two factors make $G$ infinite.

**$G$ is non-abelian.** As noted above, different translation paths yield different holonomies, so the translation group is non-abelian. The re-description group is also non-abelian: paraphrasing before translating generally yields a different result than translating before paraphrasing.

**$G$ acts primarily on $S$.** The gauge transformations change the signal while (approximately) preserving the content and pragmatic coordinates. In the language of fiber bundles, $S$ is the fiber and $P \times C$ is the base space. The gauge group acts on the fiber, and meaning lives on the base.

**Proposition 3.4** (Meaning as Gauge Invariant). *The meaning of a communicative act $\mathbf{m} = (s, p, c) \in M$ is the equivalence class $[\mathbf{m}]$ under the action of $G$:*

$$[\mathbf{m}] = \{\tau(\mathbf{m}) : \tau \in G\}$$

*Two communicative acts have the same meaning if and only if they are related by a gauge transformation. The content manifold $C$ (together with the pragmatic manifold $P$) parameterizes the space of equivalence classes $M / G$.*

This definition makes "meaning" a precise mathematical object: it is the orbit of a communicative act under the gauge group. An English assertion, its French translation, its Japanese translation, its paraphrase, and its spoken/written variants are all points in the same orbit --- they all have the same meaning. A sarcastic utterance and a sincere utterance of the same words are in *different* orbits, because sarcasm is not a gauge transformation (it changes the pragmatic coordinates, not just the signal).

---

## 3.5 The Communication BIP

### 3.5.1 Statement of the Principle

We can now state the communication-specific instantiation of the Bond Invariance Principle.

**Definition 3.6** (Communication BIP). *Any evaluation of a communicative act that purports to measure meaning must be invariant under the communication gauge group $G = T \times R \times F$. Formally, for any meaning-evaluation function $\phi: M \to V$ (where $V$ is the evaluation space) and any gauge transformation $\tau \in G$:*

$$\phi(\tau(\mathbf{m})) = \phi(\mathbf{m}) \quad \text{for all } \mathbf{m} \in M$$

*Any dependence of $\phi$ on the signal coordinates that is not mediated by the cross-factor terms $g_{SP}$ and $g_{SC}$ constitutes a gauge anomaly --- a confusion of descriptive artifact with communicative content.*

The Communication BIP is a diagnostic criterion, not a normative aspiration. It tells us what to test. Given a metric, a classifier, a translation system, or any other tool that claims to measure communicative meaning, we apply gauge transformations and check invariance. If the output changes, the tool is confusing signal with meaning.

### 3.5.2 What the BIP Rules Out

The BIP has immediate consequences for standard evaluation practice.

**BLEU scores are not gauge-invariant.** A reference translation and a paraphrase of that translation have identical meaning (they are related by $\tau \in R$), but they may have very different BLEU scores because BLEU measures n-gram overlap in $S$, not distance in $C$. The BLEU score of a perfect paraphrase may be near zero. This is a gauge anomaly: the evaluation changes under a meaning-preserving transformation.

**Perplexity is not gauge-invariant.** The perplexity of a sentence depends on the language model's probability distribution over $S$, not on the content $c$. Two sentences with identical content but different syntactic structures may have very different perplexities. Perplexity measures how well the model predicts the signal, not how well it captures the meaning.

**Sentiment scores are not gauge-invariant.** Expressing the same positive sentiment in formal English ("I found the experience thoroughly delightful") versus informal English ("That was awesome!") may yield different sentiment scores because the sentiment classifier is sensitive to lexical cues that differ between registers. This is a gauge anomaly under the re-description subgroup $R$.

**Proposition 3.5** (No Scalar Is Gauge-Invariant). *No scalar-valued evaluation function $\phi: M \to \mathbb{R}$ can be simultaneously (i) gauge-invariant under $G$, (ii) sensitive to differences in content $c$, and (iii) computable from the signal $s$ alone. Any two of these three properties can be satisfied; all three cannot.*

*Proof sketch.* (i) and (iii) together require that $\phi$ be constant on the orbits of $G$ but computable from $s$. Since $G$ acts transitively on the fibers of $\pi_S^{-1}(s)$ for a fixed content $c$ (different signals can express the same content), and different fibers may map to the same signal via different languages, a function of $s$ alone cannot separate content classes. Hence (ii) fails. The other two pairwise satisfactions are straightforward: (i) + (ii) is achieved by projecting onto $C$ (but this requires access to $c$, violating (iii)); (ii) + (iii) is achieved by any standard NLP metric (but these are not gauge-invariant, violating (i)). $\square$

This proposition is the communication-specific form of the impossibility result at the heart of the Scalar Irrecoverability Theorem. It says that the standard pipeline of communication evaluation --- observe the signal, compute a number, use the number to evaluate meaning --- is structurally incapable of gauge invariance. Gauge-invariant evaluation requires access to the content manifold, and the content manifold is not observable in the signal alone.

### 3.5.3 How Gauge Invariance Can Be Approximated

Proposition 3.5 does not mean that all evaluation is hopeless. It means that gauge-invariant evaluation requires going beyond the signal. Three strategies are available:

**Parallel data.** If we have access to the same content expressed in multiple signals (parallel corpora, paraphrase databases, multilingual resources), we can triangulate the content coordinates by observing which features are invariant across signals. This is exactly the strategy of the BIP experiments (Chapters 11--12): by training on Hebrew/Aramaic and testing on English, the experiment forces the model to learn content features that are invariant under the translation gauge $T$.

**Structured evaluation.** Instead of a scalar, evaluate on a structured space that separates signal, pragmatic, and content dimensions. The MQM (Multidimensional Quality Metrics) framework for translation evaluation is a step in this direction: it scores accuracy, fluency, terminology, and style separately, preserving some of the tensor structure that a single score destroys.

**Geometric features.** Extract features that are invariant under signal transformations by construction. The TDA features of Chapter 6 (persistent homology of the signal's phase-space attractor) are topological invariants --- they do not change under homeomorphisms of the signal. The SPD manifold features of Chapter 4 are invariant under orthogonal transformations of the spectral basis. These features occupy a middle ground: they are computable from the signal alone, they are invariant under a *subgroup* of $G$, and they capture *some* content information. They are not fully gauge-invariant, but they are more gauge-invariant than raw signal metrics.

---

## 3.6 Failure Modes and Scalar Irrecoverability

### 3.6.1 The Four Failure Modes, Instantiated

The general failure taxonomy from *Geometric Reasoning* (Chapters 5--8) maps onto communication as follows. Each mode is previewed here and developed fully in Chapters 14--15.

**Heuristic corruption** (the signal is distorted). The hearer's heuristic field is warped by features of the signal that do not correspond to content or pragmatic differences. Framing effects are the paradigmatic example: the 8.9$\sigma$ result from the Social Cognition benchmark shows that euphemistic versus dramatic descriptions of the same moral scenario displace moral judgment by 10--16 points on a 100-point scale. The framing manipulation corrupts the heuristic field without changing the geometric content of the communicative act. In the metric formalism, framing effects inflate the cross-term $g_{SC}$ --- they make signal-level features (word choice, emotional register) appear to carry content information when they do not.

**Objective hijacking** (the receiver optimizes the wrong thing). The receiver replaces the content manifold $C$ (what is being communicated) with an alternative manifold (what the receiver wants to hear, what would be socially comfortable, what would avoid conflict). Sycophancy is the communication-domain instance: the 13.3$\sigma$ sycophancy gradient from the Learning benchmark shows that language models will alter their stated beliefs to agree with the interlocutor. The model has replaced the content objective (be accurate) with a social objective (be agreeable) --- it is optimizing on $P$ at the expense of $C$.

**Local minima** (communication gets stuck). Two communicators, each interpreting the other through a flawed heuristic, converge on a stable but wrong shared interpretation. Neither party revises because the local gradient of their heuristic field points toward the current (wrong) equilibrium. Cross-cultural miscommunication often has this structure: each party interprets the other's behavior through their own cultural heuristic, arriving at a coherent but incorrect model that is self-reinforcing. Escape requires a perturbation large enough to exit the basin of attraction --- an explicit metacommunicative intervention ("I think we are misunderstanding each other").

**Gauge breaking** (the meaning changes under re-description). The system's evaluation of a communicative act changes when the act is subjected to a gauge transformation. The 4.6$\sigma$ sensory distractor result from the Attention benchmark demonstrates this: adding morally irrelevant vivid details to a scenario changes the moral judgment, even though the details are gauge degrees of freedom (they change the signal without changing the content). The ~39% recovery ceiling under explicit metacognitive warning shows that gauge invariance, once broken, is difficult to restore.

### 3.6.2 Scalar Irrecoverability in Communication

The communication manifold $M = S \times P \times C$, equipped with the metric $g$, the heuristic field $h$, and the gauge group $G$, provides the framework for stating precisely what scalar evaluation destroys.

**Theorem 3.1** (Communication Scalar Irrecoverability). *Let $\phi: M \to \mathbb{R}$ be any scalar evaluation of a communicative act. The preimage $\phi^{-1}(r)$ for any $r \in \mathbb{R}$ is a submanifold of $M$ of codimension at most 1. In particular:*

1. *A BLEU score of 0.35 is consistent with communicative acts spanning the full range of pragmatic forces and social relations.*
2. *A sentiment score of $+0.8$ is consistent with communicative acts spanning the full range of illocutionary types (sincere assertion, sarcastic assertion, rhetorical question, performative utterance).*
3. *A word error rate of 5% is consistent with communicative acts whose content distances range from $d_C = 0$ (errors in function words only) to $d_C \gg 0$ (errors in content words that alter meaning).*

*The information destroyed by scalar contraction is not recoverable from the scalar value alone. The function $\phi$ is a surjection from a manifold of dimension $\dim(S) + \dim(P) + \dim(C)$ to $\mathbb{R}$, and the kernel of this surjection has dimension $\dim(M) - 1$.*

This theorem is not surprising --- it follows directly from the dimensional mismatch between $M$ and $\mathbb{R}$ --- but its consequences for communication science are severe. Every evaluation metric in current use --- BLEU, METEOR, BERTScore, perplexity, sentiment, toxicity, readability --- is a scalar contraction of the communication tensor. Each one discards almost all of the structure of $M$. The geometric framework provides the vocabulary for saying what is lost and the machinery for recovering it.

### 3.6.3 What Geometry Recovers

The path forward is not to abandon evaluation but to evaluate on the manifold rather than on the real line. This means:

- **Evaluating translation** by measuring the holonomy of the translation path on $M$ (Chapter 10), not by counting n-gram overlaps.
- **Evaluating speech recognition** by measuring geodesic distance on the content manifold $C$, not by counting word errors on $S$.
- **Evaluating communication quality** by measuring the gauge violation tensor $V_{ij}$ (the extent to which the evaluation changes under gauge transformations), not by computing a single quality score.
- **Evaluating communication systems** by measuring the topological and geometric features of the signal manifold (the 156-dimensional feature vector of Chapters 4 and 8), not by computing classification accuracy alone.

These are not theoretical proposals. They are implemented and validated in the empirical chapters that follow. The eris-ketos toolkit (Chapters 5--7) computes geometric features of whale communication. The deep-past pipeline (Chapters 9--10) uses hyperbolic attention bias for cuneiform translation. The BIP experiments (Chapters 11--12) test gauge invariance of moral content across languages. In each case, the geometric evaluation captures structure that scalar evaluation misses, and the captured structure is empirically meaningful.

---

## 3.7 Looking Forward

This chapter has constructed the mathematical stage on which the rest of the book performs. The communication manifold $M = S \times P \times C$, equipped with its metric $g$, heuristic field $h$, and gauge group $G = T \times R \times F$, provides:

1. **A language for describing communicative acts** that separates signal from pragmatics from content, rather than collapsing them into a single representation.
2. **A metric for comparing communicative acts** that respects the distinct ways acts can differ (in signal, in intention, in meaning) and the correlations between those differences.
3. **A diagnostic for communication failure** that identifies specific pathologies (heuristic corruption, objective hijacking, local minima, gauge breaking) rather than reporting a generic "quality" score.
4. **A definition of meaning** as the gauge-invariant content of a communicative act --- the equivalence class under translation, paraphrase, and format change.
5. **A precise statement of what scalar evaluation destroys** and why the destruction is irrecoverable.

The next three chapters develop the geometric toolkit that makes this framework empirically operational. Chapter 4 introduces the three geometries (hyperbolic, SPD, topological) that provide concrete metrics on $S$, $P$, and $C$. Chapter 5 applies hyperbolic geometry to hierarchical meaning structures. Chapter 6 applies topological data analysis to communication signals. Each toolkit chapter validates the same claim: the geometry of communication is not a post hoc interpretation of results obtained by other means. It is the method by which the results are obtained.

The framework rests on an empirical bet: that the product structure $M = S \times P \times C$ captures enough of the structure of communication to be useful, and that the gauge group $G = T \times R \times F$ captures enough of the meaning-preserving transformations to define meaning precisely. Parts III--V of the book test this bet across five communication systems spanning three biological kingdoms and four millennia. The bet, as we shall see, pays off.

[Figure 3.2] *Summary of the communication manifold framework. The product manifold $M = S \times P \times C$ is shown with its metric (block structure with cross-terms), heuristic field (gradient arrows guiding interpretation), and gauge group $G = T \times R \times F$ (acting primarily on $S$). Scalar evaluation projects $M$ onto $\mathbb{R}$, destroying all structure except the one dimension measured. The five empirical systems studied in the book (whale codas, birdsong, cuneiform, cross-lingual moral transfer, LLM communication) are located on $M$ according to which factors are accessible to measurement.*

---

## Chapter Summary

| Concept | Formal Object | Intuition |
|---|---|---|
| Communicative act | Point $\mathbf{m} = (s, p, c) \in M$ | Everything about the act: how it was said, why, and what |
| Signal | $s \in S$ | The physical carrier (sound, text, gesture) |
| Pragmatics | $p \in P$ | The intention, social context, illocutionary force |
| Content | $c \in C$ | The semantic meaning, propositional content |
| Communication metric | $g = (g_{XX'})$ on $M$ | What makes two acts "close" or "far" |
| Heuristic field | $h: M \to \mathbb{R}$ | The learned associations guiding interpretation |
| Translation group | $T \subset G$ | Relabeling across languages |
| Re-description group | $R \subset G$ | Paraphrase within a language |
| Format group | $F \subset G$ | Modality change (spoken $\leftrightarrow$ written $\leftrightarrow$ signed) |
| Meaning | Orbit $[\mathbf{m}] = G \cdot \mathbf{m}$ | What is preserved when everything else changes |
| Communication BIP | $\phi(\tau(\mathbf{m})) = \phi(\mathbf{m})$ for $\tau \in G$ | Meaning evaluation must be gauge-invariant |
| Scalar Irrecoverability | $\dim(\phi^{-1}(r)) = \dim(M) - 1$ | Scalar evaluation destroys almost everything |

---

### Definitions and Propositions Index

- **Definition 3.1**: Communication Manifold ($M = S \times P \times C$)
- **Definition 3.2**: Communication Metric (block-structured Riemannian metric on $M$)
- **Definition 3.3**: Communication Heuristic Field (scalar field guiding interpretation)
- **Definition 3.4**: Admissible Communication Heuristic (charitable interpretation)
- **Definition 3.5**: Communication Gauge Group ($G = T \times R \times F$)
- **Definition 3.6**: Communication BIP (meaning evaluation invariant under $G$)
- **Proposition 3.1**: Projection Loss (scalar evaluation leaves unprojected factors undetermined)
- **Proposition 3.2**: Diagnostic Patterns (translation, sarcasm, paraphrase distinguished by distance profiles)
- **Proposition 3.3**: Heuristic Decomposition (four sources of the communication heuristic)
- **Proposition 3.4**: Meaning as Gauge Invariant (meaning is the orbit under $G$)
- **Proposition 3.5**: No Scalar Is Gauge-Invariant (impossibility of gauge-invariant scalar evaluation from signal alone)
- **Theorem 3.1**: Communication Scalar Irrecoverability

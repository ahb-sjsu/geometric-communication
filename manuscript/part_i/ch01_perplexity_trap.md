# Chapter 1: The Perplexity Trap

*Part I: The Problem*

---

> *"Not everything that can be counted counts, and not everything that counts can be counted."*
> --- William Bruce Cameron

> **THE ROSETTA TRAJECTORY**
>
> *In 1954, researchers at Georgetown University and IBM demonstrated the first public machine translation system. It translated sixty Russian sentences into English using a vocabulary of 250 words and six grammar rules. The press was ecstatic. The New York Times predicted that machine translation would be a solved problem within five years. The researchers knew the demonstration was rigged --- the sentences were carefully selected to fall within the system's narrow competence --- but they also believed the prediction was roughly correct. Surely, expanding the vocabulary, adding grammar rules, and increasing computing power would close the gap.*
>
> *It did not. In 1966, the Automatic Language Processing Advisory Committee (ALPAC) issued a devastating report concluding that machine translation was not merely unsolved but economically unjustified. The field collapsed. Funding dried up. Researchers moved to other problems. The failure was not computational --- it was evaluative. Nobody could agree on what "good translation" meant, because nobody had a way to measure it that captured what actually mattered.*
>
> *Six decades later, the measurement problem remains. We have BLEU scores, perplexity, word error rates, sentiment scores, readability indices --- an entire apparatus of scalar evaluation. And every one of these numbers destroys the very structure it claims to measure. This chapter explains what is lost, why it cannot be recovered, and what must replace it.*

---

## 1.1 The Vodka Problem

Consider two English translations of a Russian proverb:

> **Translation A:** "The spirit is willing, but the flesh is weak."
>
> **Translation B:** "The vodka is good, but the meat is rotten."

The story that these represent an actual machine translation failure is almost certainly apocryphal --- it has circulated since the 1960s as a cautionary tale about the Georgetown-IBM demonstration and its successors, and no one has ever produced the system that generated Translation B.[^1] But apocryphal or not, the example is devastating, because it exposes a structural deficiency in how we evaluate communication that persists to this day.

Compute the BLEU score of each translation against the reference "The spirit is willing, but the flesh is weak." Translation A scores perfectly: it *is* the reference. Translation B scores poorly on unigram overlap --- "vodka," "good," "meat," and "rotten" do not appear in the reference --- and zero on any $n$-gram with $n > 2$, since no bigram except "the" plus a content word matches.

Now reverse the problem. Suppose we do not know which translation is correct. Suppose we have only the two translations and a set of scalar metrics. Can we recover, from those metrics, *what went wrong* with Translation B?

The BLEU score tells us that Translation B has low $n$-gram overlap with the reference. It does not tell us *why*. It cannot distinguish between three radically different failure modes:

1. **Lexical substitution with preserved structure.** The translator chose the wrong word from a set of homonyms or near-homonyms. "Spirit" (the animating principle) became "spirit" (distilled alcohol, hence vodka). "Flesh" (the body, frailty) became "flesh" (meat). The syntactic structure is preserved; the semantic field has shifted. The error is localized and correctable --- a better dictionary would fix it.

2. **Structural collapse with preserved topic.** The translator understood the general domain (something about willingness and weakness) but could not reconstruct the sentence structure, producing a grammatically correct but semantically unrelated sentence in the same general topic area. The error is global and structural.

3. **Complete hallucination.** The translator produced a fluent sentence that bears no systematic relationship to the source. The output is coherent English, but it is not a translation of anything.

These three failure modes have identical BLEU scores. They have completely different implications for the translation system, completely different remedies, and completely different relationships to the source text's meaning. The scalar has compressed a three-dimensional failure taxonomy into a single number, and the compression is irreversible. No amount of staring at the BLEU score will tell you which failure occurred.

[Figure 1.1: The three failure modes of Translation B, visualized as points in a semantic space. Lexical substitution (1) lies close to the source on two of three axes but displaced on the third. Structural collapse (2) lies in the correct region of topic space but at the wrong structural coordinates. Hallucination (3) is displaced on all axes. All three project to the same point on the scalar BLEU axis.]

This is not a contrived example. It is the normal operating condition of every scalar evaluation metric used in communication science. The vodka problem is not about translation. It is about the geometry of meaning and the impossibility of capturing that geometry in a single number.

## 1.2 The Scalar Menagerie

The evaluation of communication --- human and machine, spoken and written, ancient and modern --- has generated a remarkable zoo of scalar metrics. Each was invented to solve a real problem. Each captures something genuine. And each destroys geometric structure that its inventors did not know existed.

### 1.2.1 BLEU: The $n$-Gram Guillotine

BLEU (Bilingual Evaluation Understudy) was introduced by Papineni et al. in 2002 as an automatic metric for machine translation evaluation.[^2] Its design was explicitly pragmatic: human evaluation of translation quality is expensive, slow, and inconsistent, so an automatic proxy that correlates with human judgment would be enormously useful. BLEU computes a modified precision score over $n$-grams of different lengths, combining them via a geometric mean and applying a brevity penalty for translations shorter than the reference:

$$\text{BLEU} = \text{BP} \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)$$

where $p_n$ is the modified $n$-gram precision (the fraction of $n$-grams in the candidate that appear in the reference, clipped to avoid rewarding repetition), $w_n = 1/N$ is the uniform weight, and $\text{BP} = \min(1, e^{1 - r/c})$ is the brevity penalty with $r$ the reference length and $c$ the candidate length.

BLEU was a breakthrough. Before BLEU, evaluating machine translation required human judges --- expensive, slow, and difficult to calibrate across studies. BLEU made evaluation automatic, reproducible, and fast. It enabled the rapid iteration that drove statistical machine translation forward through the 2000s. Its inventors were careful to note its limitations: it measures only surface-level $n$-gram overlap, it requires one or more reference translations, and it does not capture meaning, fluency, or adequacy as separate dimensions. The field heard the first half of this message and ignored the second.

What does BLEU destroy?

**Synonymy.** "The automobile accelerated" and "The car sped up" have zero bigram overlap despite being near-synonyms. BLEU punishes every lexical choice that deviates from the reference, regardless of whether the deviation preserves meaning. On the semantic manifold, these two phrases occupy nearby points --- their meanings are close --- but BLEU measures surface distance, not semantic distance. It projects the semantic manifold onto the lexical surface and measures distance in the projection.

**Word order flexibility.** "She gave him the book" and "The book she gave to him" express the same propositional content with different syntactic structures. BLEU captures the shared unigrams ("she," "gave," "him," "the," "book") but penalizes the different bigrams and trigrams. Languages with freer word order --- German, Latin, Japanese, Akkadian --- are systematically disadvantaged, because the space of valid surface realizations is larger, making any single reference a poorer representative of the set.[^3]

**Pragmatic equivalence.** "Could you close the door?" and "Close the door" have the same pragmatic force (a request to close the door) with different levels of politeness. BLEU treats them as different strings. More broadly, BLEU has no representation of speaker intention, social context, or communicative function --- the entire pragmatic manifold is invisible to it.

**Hierarchical structure.** "The dog that bit the cat that ate the rat" has a nested clause structure that determines its meaning. Scrambling the clause order produces nonsense. BLEU's $n$-gram window sees only local fragments; the global syntactic tree --- the hierarchical structure that determines compositional meaning --- is visible only to the extent that it is reflected in local $n$-gram statistics. For deeply embedded structures, this reflection is faint.

Each of these losses corresponds to the destruction of a specific geometric structure. Synonymy is metric structure: nearby points on the semantic manifold are projected to distant points on the lexical surface. Word order flexibility is a symmetry: the set of valid surface realizations of a meaning forms the orbit of a syntactic transformation group, and BLEU breaks this symmetry by privileging one element of the orbit (the reference). Pragmatic equivalence is a fiber: the meaning "request to close the door" is the base point, and the various ways to express it (imperative, interrogative, indirect) are the fiber above that point. BLEU evaluates in the total space rather than the base space. Hierarchical structure is topology: the tree structure of the sentence is a topological object that BLEU's sliding window cannot detect.

[Figure 1.2: The four geometric structures destroyed by BLEU. (a) Metric: synonymous expressions are nearby on the semantic manifold but distant on the lexical surface. (b) Symmetry: word-order variants form an orbit under syntactic transformation; BLEU privileges one element. (c) Fiber: pragmatic equivalents are different points in the total space that project to the same base point. (d) Topology: hierarchical structure is a global property invisible to local $n$-gram windows.]

### 1.2.2 Perplexity: The Probabilistic Myopia

Perplexity is the standard evaluation metric for language models. It measures how well a probability distribution predicts a sample:

$$\text{PPL}(W) = \exp\left(-\frac{1}{N}\sum_{i=1}^{N} \log P(w_i \mid w_{<i})\right)$$

where $W = w_1, w_2, \ldots, w_N$ is a sequence of $N$ tokens and $P(w_i \mid w_{<i})$ is the model's predicted probability of token $w_i$ given the preceding context. Lower perplexity means the model assigns higher probability to the tokens that actually occurred --- it is less "surprised" by the data.

Perplexity has a clean information-theoretic interpretation: it is $2^H$ where $H$ is the cross-entropy between the model's distribution and the empirical distribution. A perfect model --- one that knows exactly which token comes next --- has perplexity 1. A model that assigns uniform probability over a vocabulary of $V$ tokens has perplexity $V$. A model with perplexity 30 is, informally, "as confused as if it were choosing uniformly among 30 equally likely next tokens."

This is useful. It is also profoundly misleading as a measure of language understanding, and the geometric reasons are precise.

**Perplexity is a pointwise metric.** It evaluates each token prediction in isolation (conditional on the context, but scoring each position independently). It has no representation of whether the model understands the *global* coherence of the text --- whether the narrative is consistent, whether the argument is valid, whether the dialogue is pragmatically appropriate. A model could achieve low perplexity by being excellent at local collocation statistics ("strong" is likely after "the spirit is") while having no representation of discourse structure.

**Perplexity is surface-locked.** It measures the probability of the *actual* surface form, not the probability of the *meaning*. Consider a model that perfectly understands the meaning of every sentence but expresses that understanding through unconventional word choices --- a model that always says "automobile" where the training data says "car." Its perplexity will be high, because its surface predictions deviate from the observed surface, even though its semantic predictions are perfect. Perplexity measures fidelity to the surface distribution, not fidelity to the semantic content.

**Perplexity destroys the distinction between easy and hard tokens.** The average in the exponent weights all positions equally. A text might contain 95% predictable function words and connectives ("the," "is," "but," "and") and 5% content-bearing tokens that carry the actual information. The model's performance on the content tokens --- the tokens that matter for meaning --- is diluted by its performance on the function tokens. A perplexity of 15 might mean "excellent on everything" or "near-perfect on function words, terrible on content words." The average destroys the distinction.

The geometric structure that perplexity destroys is the *heterogeneity of the prediction surface*. A language model's prediction at each position in a text is not a number; it is a probability distribution over the vocabulary --- a point on the probability simplex $\Delta^{V-1}$, which is a $(V-1)$-dimensional manifold. The full prediction of a model on a text of length $N$ is a trajectory on this simplex: a sequence of $N$ points, each representing the model's belief about the next token. This trajectory has structure --- curvature (how sharply the distribution shifts from position to position), topology (whether the trajectory revisits similar distributions), and symmetry (whether semantically equivalent positions produce similar distributions). Perplexity collapses the entire trajectory to a single number: the geometric mean of the probabilities along the path. It is a scalar summary of a manifold-valued trajectory, and the Scalar Irrecoverability Theorem (*Geometric Reasoning*, Ch. 13) predicts exactly what it loses.

### 1.2.3 Word Error Rate: The Edit Distance Trap

Word Error Rate (WER) is the standard metric for automatic speech recognition:

$$\text{WER} = \frac{S + D + I}{N}$$

where $S$ is the number of substitutions, $D$ the number of deletions, $I$ the number of insertions, and $N$ the total number of words in the reference. WER is an edit distance normalized by reference length: the minimum number of word-level operations needed to transform the hypothesis into the reference, expressed as a proportion.

WER treats all errors as equal. Substituting "cat" for "car" and substituting "cat" for "democracy" both count as one substitution. Deleting "the" and deleting "not" both count as one deletion. This uniform weighting destroys the *metric structure* of the error space. Some errors are catastrophic (inserting "not" reverses the meaning of a sentence); others are trivial (substituting "a" for "the" in most contexts). WER has no representation of this distinction because it operates on a flat, unweighted space where all word-level edit operations have unit cost.

The geometric structure destroyed is the semantic metric on word space. In a semantically informed evaluation, the cost of substituting word $a$ for word $b$ would be a function of their semantic distance: $c(a, b) = d_{\text{semantic}}(a, b)$. Substituting "automobile" for "car" would cost nearly zero; substituting "automobile" for "freedom" would cost the full distance across the semantic manifold. WER replaces this rich metric with the discrete metric: $c(a, b) = 0$ if $a = b$, $c(a, b) = 1$ otherwise. The entire continuous structure of semantic similarity is collapsed to a binary distinction.

Moreover, WER destroys *positional structure*. An error in a syntactically critical position (the verb, the negation, the subject) can change the meaning of the entire sentence; an error in a peripheral position (an adjective, an aside, a filler phrase) may leave the meaning nearly intact. WER weights all positions equally. The syntactic tree --- which encodes which positions are structurally critical --- is invisible.

### 1.2.4 Classification Accuracy: The Topology Eraser

In communication science, classification accuracy appears everywhere: sentiment classification (positive/negative/neutral), speaker identification (which speaker?), language identification (which language?), intent detection (which communicative intent?), species identification from vocalizations (which species?). The metric is deceptively simple:

$$\text{Accuracy} = \frac{\text{Number correct}}{\text{Total}}$$

Classification accuracy destroys the *topology of the class space*. Consider sentiment analysis. A three-class system (positive/negative/neutral) achieves 70% accuracy. But misclassifying positive as neutral (a one-step error on the valence axis) is qualitatively different from misclassifying positive as negative (a two-step error that reverses the polarity). Accuracy treats both errors as equal --- both are "wrong." The confusion matrix captures some of this structure, but it is typically contracted to a scalar (accuracy, macro-F1, or AUC) before being reported.

For species identification from vocalizations --- the task at the heart of the BirdCLEF competition and the eris-ketos cetacean analysis that we will examine in Chapters 7 and 8 --- the problem is more severe. Misclassifying a Humpback whale coda as a Sperm whale coda is not the same kind of error as misclassifying it as a Blue whale song. Humpback and Sperm whales produce clicks through different mechanisms with different spectral properties; the error likely reflects acoustic confusion at the feature level. Humpback and Blue whales are both mysticetes with some shared vocal characteristics; the error might reflect genuine taxonomic proximity. The class space has a hierarchical structure --- the phylogenetic tree of the species --- and errors that cross different levels of this hierarchy have different causes and different implications. Classification accuracy, by treating all errors as equivalent, erases this hierarchy entirely.

A whale coda classifier with 95% accuracy tells us that 95% of codas were assigned to the correct coda type. It tells us nothing about:

- Whether the errors are concentrated in acoustically similar coda types (suggesting a feature-level limitation) or scattered across the taxonomy (suggesting random noise)
- Whether the errors are systematically asymmetric (coda type A is often confused with type B, but not vice versa), which would reveal the directed structure of the perceptual boundary
- Whether the classifier has learned the *meaning* of the coda types (whatever that meaning is) or merely their acoustic signatures

These are geometric properties of the classification boundary --- its curvature, its symmetry, its relationship to the taxonomic hierarchy --- and all of them are invisible to the scalar accuracy metric.

### 1.2.5 Readability Indices: The Dimensionality Collapse

The Flesch-Kincaid readability score, the Gunning fog index, the Coleman-Liau index, the SMOG grade, and their many cousins all attempt to measure how "readable" a text is by computing a scalar from surface statistics: average sentence length, average word length, syllable count, polysyllabic word frequency. The Flesch Reading Ease formula is typical:

$$\text{FRE} = 206.835 - 1.015 \left(\frac{\text{total words}}{\text{total sentences}}\right) - 84.6 \left(\frac{\text{total syllables}}{\text{total words}}\right)$$

This is a linear projection from a two-dimensional space (average sentence length, average syllables per word) onto a scalar. The projection destroys everything about readability that is not captured by these two features: logical structure, coherence, presupposition load, domain-specific vocabulary, the reader's background knowledge, pragmatic clarity, and the interaction between all of these. A passage of Hegel and a passage of a VCR instruction manual can have identical Flesch scores while being unreadable for completely different reasons --- one because the ideas are genuinely complex and densely interrelated, the other because the writing is simply bad.

The geometric structure destroyed is the *dimensionality of the readability manifold*. Readability is not a one-dimensional quantity. It is at minimum a function of syntactic complexity, semantic density, pragmatic clarity, domain familiarity, and coherence structure. These dimensions are not reducible to each other: a text can be syntactically simple but semantically dense (a mathematics paper using short sentences), or syntactically complex but semantically transparent (a legal contract with nested clauses expressing simple conditions). Readability indices project this multi-dimensional manifold onto a line and discard the rest.

### 1.2.6 Sentiment Scores: The Affect Flattener

Sentiment analysis reduces text to a scalar (positive/negative/neutral) or, in more sophisticated systems, to a point on a one-dimensional valence axis from $-1$ to $+1$. Some systems add a second dimension --- arousal --- producing a point in the two-dimensional valence-arousal plane. Even this modest expansion is unusual; most deployed sentiment systems are scalar.

What does the scalar destroy?

**The object of the sentiment.** "I love the camera but hate the battery life" is positive about one aspect and negative about another. Scalar sentiment either averages these (producing a misleadingly neutral score) or picks one (producing a misleadingly decisive score). The aspect structure of the sentiment --- the fact that it is a *tensor* with different values along different dimensions of the product --- is collapsed.

**The pragmatic force.** "Great, another meeting" is syntactically positive and pragmatically negative (sarcastic). Scalar sentiment, operating on the surface, reads it as positive. The pragmatic inversion --- the 180-degree rotation on the meaning manifold between the literal and intended senses --- is invisible to a metric that operates on surface features alone.

**The social context.** The same words carry different sentiment when spoken by a friend (affectionate teasing) versus a stranger (hostility) versus a subordinate (deference) versus a superior (condescension). Scalar sentiment strips the social coordinates entirely. The communicative act is a point on the product manifold $M = S \times P \times C$, where $S$ is the signal, $P$ the pragmatic context, and $C$ the content. Scalar sentiment projects onto a one-dimensional subspace of $C$ and discards $S$ and $P$ entirely.

**The intensity profile across dimensions.** "I'm excited but anxious" is not captured by any point on a one-dimensional valence axis. It requires at least two dimensions (positive activation, negative activation) and arguably more (anticipation, uncertainty, arousal). The psychological evidence from Russell's circumplex model, Plutchik's wheel of emotions, and the PAD (Pleasure-Arousal-Dominance) model all agree that affect is multi-dimensional.[^4] Scalar sentiment is a lossy projection from this multi-dimensional space.

Every content moderation system built on scalar sentiment inherits these losses. Every social media analytics platform that reports "sentiment trending positive" has destroyed the aspect structure, the pragmatic force, the social context, and the intensity profile of what was actually said. The number is not wrong, exactly. It is a valid contraction of a tensor. But the contraction is lossy, and the lost information is precisely the information needed to understand what the communication *means*.

## 1.3 The Geometry That Scalars Destroy

The previous section catalogued six scalar metrics and their specific losses. A pattern emerges. Each metric destroys one or more of four fundamental geometric structures:

**Metric structure.** The continuous distance between meanings --- the fact that "car" is closer to "automobile" than to "democracy," that a half-step error is less severe than a polarity reversal. BLEU replaces semantic distance with lexical identity. WER replaces it with the discrete metric. Sentiment scores replace the multi-dimensional distance between emotional states with a one-dimensional projection. In each case, the rich metric on the semantic manifold is replaced by a cruder metric that discards gradations of similarity.

**Symmetry structure.** The invariances that preserve meaning --- the fact that "the dog bit the man" and "the man was bitten by the dog" express the same propositional content under a syntactic transformation, that "Il pleut" and "it's raining" express the same content under a lexical transformation (translation), that a request can be expressed as an imperative, an interrogative, or an indirect speech act while preserving its communicative function. These are symmetries of the communication manifold: transformations that move points on the surface (different expressions) while preserving the base point (the meaning). Scalar metrics break these symmetries by privileging one surface form (the reference) and measuring distance from it.

**Fiber structure.** The separation between content and expression --- the fact that a single meaning can be realized in many surface forms, and a single surface form can carry many meanings. This is the fiber bundle structure of communication: the base space is meaning, the fiber at each point is the set of expressions that convey that meaning, and the total space is the set of all expressed meanings. Scalar metrics operate in the total space (comparing expressions) rather than the base space (comparing meanings). They cannot distinguish between two expressions that are far apart in the total space but project to the same base point (paraphrases) and two expressions that are equally far apart but project to different base points (distinct meanings).

**Topological structure.** The global shape of meaning space --- the hierarchical nesting of categories, the connected components of discourse, the loops in argumentative structure. Classification accuracy erases the topology of the class space. Perplexity, by averaging over positions, erases the topology of the discourse trajectory. Readability indices, by projecting onto two surface statistics, erase the topological structure of coherence. Topology is inherently global --- it concerns properties that are invariant under continuous deformation --- and scalar metrics, by contracting to a point, destroy all global structure.

[Figure 1.3: The four geometric structures destroyed by scalar evaluation. (a) Metric: continuous distance replaced by discrete or crude approximation. (b) Symmetry: meaning-preserving transformations broken by privileging one surface form. (c) Fiber: content-expression separation collapsed by evaluating in the total space. (d) Topology: global structure erased by local or pointwise evaluation.]

These four structures are not independent luxuries. They are the mathematical substance of what communication *is*. Metric structure is what makes some utterances more similar than others. Symmetry structure is what makes translation, paraphrase, and reformulation possible. Fiber structure is what separates meaning from expression --- the fundamental duality that Saussure identified in 1916 and that every subsequent theory of language has grappled with. Topological structure is what gives discourse its coherence, argument its validity, and narrative its arc. A measurement apparatus that destroys all four is not measuring communication. It is measuring something else --- something correlated with communication, perhaps, but structurally impoverished in exactly the dimensions that matter.

## 1.4 The Scalar Irrecoverability Theorem

The losses catalogued above are not merely inconvenient. They are mathematically irreversible. This is the content of the Scalar Irrecoverability Theorem, proved in *Geometric Reasoning* (Ch. 13) and here stated in its communication-specific form.

**Theorem 1.1 (Scalar Irrecoverability for Communication).** *Let $\mathbf{q} \in \mathbb{R}^d$ be the quality profile of a communicative act (or a system that produces communicative acts) across $d$ independent evaluation dimensions. For any scalar projection $\pi: \mathbb{R}^d \to \mathbb{R}$, there exist communicative acts $A$ and $B$ such that $\pi(\mathbf{q}_A) = \pi(\mathbf{q}_B)$ despite $A$ being strictly superior to $B$ on a substantive subset of the $d$ dimensions. The information destroyed by $\pi$ --- namely, the identity of which dimensions $A$ dominates and which $B$ dominates --- is not recoverable from the scalar values $\pi(\mathbf{q}_A)$ and $\pi(\mathbf{q}_B)$ alone.*

The proof follows immediately from the parent theorem. The condition is that the quality profiles of communicative acts (or communication systems) are mutually Pareto-non-dominated across the evaluation dimensions --- that is, no act (or system) dominates every other on every dimension simultaneously. This condition holds empirically for every communication evaluation scenario we will examine in this book. Two translations with identical BLEU scores can differ in adequacy, fluency, terminology, and style. Two language models with identical perplexity can differ in coherence, factual accuracy, pragmatic appropriateness, and safety. Two speech recognition systems with identical WER can differ in their error distributions across phonemes, positions, and semantic criticality.

The theorem has a sharpened form that is particularly relevant to communication:

**Corollary 1.1.1.** *For any $k$ scalar metrics $\pi_1, \ldots, \pi_k$ with $k < d$, the joint evaluation $(\pi_1(\mathbf{q}), \ldots, \pi_k(\mathbf{q}))$ still fails to recover the full profile $\mathbf{q}$. The information loss is reduced but not eliminated until $k \geq d$.*

This means that the response to scalar irrecoverability is not "use two metrics instead of one" or "report BLEU and METEOR and chrF++ together." If the quality profile has $d$ independent dimensions, you need at least $d$ independent measurements to characterize it. And the critical word is *independent*: BLEU, METEOR, and chrF++ are all $n$-gram overlap metrics with different weighting schemes; they are three projections along nearly parallel directions, not three independent measurements. Adding correlated metrics does not reduce the information loss; it merely gives the illusion of thoroughness.

What is the dimensionality $d$ of communication quality? The outline in Section 1.2 suggests at least the following independent dimensions:

1. **Semantic adequacy** --- does the communication convey the intended meaning?
2. **Fluency** --- is the surface form natural and well-formed?
3. **Pragmatic appropriateness** --- does the communication achieve the intended social effect?
4. **Structural fidelity** --- is the hierarchical organization of the content preserved?
5. **Terminological precision** --- are domain-specific terms handled correctly?
6. **Stylistic register** --- is the level of formality appropriate to the context?
7. **Coherence** --- does the discourse hold together over longer spans?
8. **Robustness** --- does the quality hold under perturbation of the input?

This is likely an undercount. The BIP experiments described in Chapters 11--12 identify at least four independent dimensions within moral communication alone (the Hohfeldian quartet: Right, Duty, Liberty, No-Right). The eris-ketos analysis in Chapter 7 identifies at least five independent dimensions within whale coda communication (click count, rhythm class, tempo, rubato, ornamentation). Communication quality is not merely multi-dimensional; it is high-dimensional, and the gap between the dimensionality of the quality profile and the dimensionality of the evaluation (usually 1, occasionally 2 or 3) is vast.

The theorem does not say that scalar metrics are useless. It says they are lossy, and the loss is irrecoverable. A BLEU score of 0.35 is not meaningless --- it constrains the set of possible translations to those that share roughly 35% of their $n$-grams with the reference. But it constrains the set along *one* axis while leaving all other axes unconstrained. The set of translations consistent with BLEU = 0.35 is not a point; it is a $(d-1)$-dimensional submanifold of the quality space. Everything in that submanifold looks identical to BLEU. The information that distinguishes points within the submanifold --- the information that tells you whether the translation is adequate but disfluent, fluent but pragmatically inappropriate, or uniformly mediocre --- is gone.

[Figure 1.4: Scalar irrecoverability visualized. The quality space is $d$-dimensional. A scalar metric $\pi$ projects onto a line. The preimage of a scalar value $\pi = c$ is a $(d-1)$-dimensional hyperplane (shown as a plane for $d = 3$). All points on this hyperplane are indistinguishable to $\pi$. The geometric structure within the hyperplane --- the distances, symmetries, and topological features that distinguish qualitatively different translations with the same BLEU score --- is irrecoverable from the scalar.]

## 1.5 What This Costs

The irrecoverability theorem is a mathematical fact. But mathematics does not bleed. What bleeds is practice --- the systems built on scalar evaluation, the decisions made on scalar evidence, the understanding lost to scalar compression. The costs are concrete.

### 1.5.1 Translation Quality That Isn't

The machine translation community has spent two decades optimizing for BLEU. The results are impressive by the metric and often disappointing by the experience. Neural machine translation systems achieve BLEU scores that would have seemed miraculous in 2000, yet they routinely produce translations that are fluent, confident, and wrong --- mistranslating negation, dropping qualifiers, hallucinating content that appears nowhere in the source.[^5]

The reason is Goodhart's law, applied to a geometric situation: when BLEU becomes the optimization target, systems learn to produce $n$-gram-rich output that maximizes overlap with references, regardless of whether the $n$-grams are assembled into coherent meaning. The metric has become the territory, and the territory it describes is the lexical surface, not the semantic manifold. Systems optimized for BLEU learn to navigate the lexical surface with precision while ignoring the semantic manifold that the lexical surface is supposed to represent.

### 1.5.2 Language Models That Surprise No One

Perplexity optimization has driven the development of language models from the $n$-gram models of the 1990s through the neural language models of the 2010s to the massive transformers of the 2020s. The trajectory has been spectacular: perplexity on standard benchmarks has fallen from hundreds to tens to single digits. And yet the resulting models exhibit behaviors --- hallucination, inconsistency, susceptibility to adversarial prompts, sycophancy --- that perplexity does not predict and cannot measure.

The disconnect between perplexity and behavior is not a failure of the models. It is a failure of the metric. Perplexity measures average next-token prediction accuracy. Hallucination is a failure of *coherence* --- the model generates locally plausible tokens that globally contradict established facts. Sycophancy is a failure of *invariance* --- the model's output changes when the social context changes but the evidential content does not. These are geometric properties --- coherence is topological (global consistency), invariance is symmetric (preservation under transformation) --- and they are invisible to a metric that evaluates tokens one at a time.

### 1.5.3 Content Moderation That Moderates the Wrong Thing

Scalar sentiment scores underpin most automated content moderation systems. The pipeline is standard: classify the sentiment of each post or comment, flag posts that exceed a negativity threshold, route flagged posts to human reviewers or automated action. The problems are well-documented and geometrically predictable.

Sarcasm inversion: "What a wonderful day to be stuck in traffic for three hours" is classified as positive because the surface features are positive. The pragmatic rotation from literal to sarcastic meaning is invisible to a surface-level classifier. Aspect collapse: "I love this restaurant but the service is terrible" is classified as mixed or neutral, averaging the positive aspect (food) with the negative aspect (service). The aspect structure --- which dimension of the experience is being evaluated --- is destroyed by the scalar projection. Context erasure: "Kill it!" in a gaming context is classified as violent; the same phrase in a business context ("this presentation will kill it") is classified as positive. The social context that determines the meaning is absent from the scalar representation.

These are not edge cases. They are the normal operating condition of scalar sentiment analysis. The losses predicted by the Scalar Irrecoverability Theorem manifest as systematic errors in every system built on scalar evaluation: errors that no amount of training data, model capacity, or hyperparameter tuning can fix, because they arise not from the model's limitations but from the metric's dimensionality.

### 1.5.4 Understanding That Isn't

Perhaps the most consequential cost is epistemic. Scalar evaluation creates the illusion of understanding. When we report that a system achieves "BLEU 0.42" or "perplexity 12.3" or "95% accuracy," we have produced a number --- a definite, comparable, rankable number --- and the existence of the number creates a sense that we know something. We know how good the system is. We can compare it to other systems. We can track its improvement over time.

But what do we know? We know the value of a specific contraction of a tensor we have not measured. We know the position of a shadow on the wall of the cave. The Scalar Irrecoverability Theorem tells us precisely what we do not know: everything in the $(d-1)$-dimensional hyperplane perpendicular to the projection direction. And in communication, the hyperplane contains exactly the structure that makes communication *communication* --- the meaning, the intention, the social context, the coherence, the pragmatic force.

This is not a call to abandon quantitative evaluation. It is a call to upgrade it. The question is not "should we measure?" but "in what space should we measure?" The answer --- the answer that this book develops across seventeen subsequent chapters --- is: on the communication manifold, with its full geometric structure intact.

## 1.6 A Different Path

If scalar metrics destroy geometric structure, the remedy is geometric evaluation: measuring communication in a space that preserves the metric, the symmetry, the fiber structure, and the topology that scalars discard.

This is not a utopian proposal. It is already happening, piecemeal and without a unifying framework.

**Word embeddings** (Word2Vec, GloVe, BERT embeddings) are coordinates on the semantic manifold. They represent meanings as points in a high-dimensional space where distance corresponds (approximately) to semantic dissimilarity. The success of embedding-based metrics like BERTScore and COMET over $n$-gram metrics like BLEU is evidence that moving evaluation from the lexical surface to the semantic manifold improves measurement quality.[^6] But current embedding-based metrics still contract to scalars at the final step: BERTScore computes pairwise token similarities and then averages. The manifold structure is used internally and then discarded in the output.

**Hyperbolic embeddings** represent hierarchical meaning in the Poincare ball, where the exponential growth of volume matches the exponential branching of semantic taxonomies. We will see in Chapter 5 that cuneiform sign hierarchies, whale coda taxonomies, and moral concept ontologies all embed more naturally in hyperbolic space than in Euclidean space. The curvature of the embedding space encodes structural information --- the hierarchy of abstraction from general to specific --- that flat embeddings lose.

**Topological data analysis** extracts the *shape* of a communication signal --- its connected components, loops, and higher-dimensional voids --- using persistent homology. Applied to whale click patterns (Chapter 6) and birdsong spectral contours (Chapter 8), TDA produces topological invariants that are robust to noise, amplitude variation, and recording conditions. These invariants capture structure that is invisible to spectral analysis: the *shape* of the vocalization in phase space, not just its frequency content.

**SPD manifold features** represent the covariance structure of acoustic signals on the manifold of symmetric positive-definite matrices, equipped with a Riemannian metric that respects the manifold geometry. The 156-dimensional geometric feature vector developed for birdsong analysis in Chapter 8 --- 136 SPD features, 4 trajectory features, 16 TDA features --- captures cross-frequency correlations, spectral trajectory complexity, and topological persistence in a single representation that outperforms any single geometry alone.

These are not competing alternatives to scalar evaluation. They are complementary geometric structures, each capturing a different aspect of the communication manifold. And they already work. The empirical results presented in this book --- Menzerath's law in whale codas (Chapter 7), hyperbolic attention bias for cuneiform translation (Chapter 9), cross-lingual moral invariance at 44.5% F1 (Chapter 11) --- are all products of geometric evaluation applied where scalar evaluation fails.

The question is not whether geometric methods work. The question is whether they can be unified into a coherent framework that explains *why* they work and *what* they measure. This is the project of the book.

## 1.7 The Plan

The book proceeds in seven parts along what we call the Rosetta trajectory --- the path from raw signal to structured meaning, developed through five communication systems spanning 4,000 years and three biological kingdoms.

**Part I (Chapters 1--3)** establishes the problem and the framework. Chapter 2 recovers the geometric intuitions buried in the history of linguistics --- Saussure's arbitrariness of the sign as gauge invariance, Jakobson's distinctive features as a discrete symmetry group, Chomsky's deep structure as a quotient manifold --- and shows that the field has been reaching toward geometry for over a century without naming it. Chapter 3 constructs the communication manifold $M = S \times P \times C$, the product of signal, pragmatic, and content manifolds, and defines the metric, heuristic field, and symmetry group that give it structure.

**Part II (Chapters 4--6)** develops the geometric toolkit: hyperbolic embeddings for hierarchical structure, SPD manifolds for covariance structure, and topological data analysis for shape. These three geometries are orthogonal --- they capture hierarchy, covariance, and topology respectively --- and their combination produces a richer representation than any single geometry alone.

**Parts III--V (Chapters 7--13)** apply the toolkit to five communication systems: sperm whale codas, birdsong, Akkadian cuneiform, cross-lingual moral reasoning, and the gauge theory of communicative acts. Each application validates the geometric approach on a different system and contributes empirical evidence for the central claim.

**Part VI (Chapters 14--15)** catalogs the failure modes of communication through the geometric lens and proves the domain-specific Scalar Irrecoverability Theorem with full formal machinery.

**Part VII (Chapters 16--18)** synthesizes the Rosetta trajectory, identifies what communication teaches the general geometric framework, and poses the open questions that the next generation of research must address.

The argument, stripped to its essence, is this: communication has geometric structure. Scalar evaluation destroys that structure. The destruction is mathematically irreversible. Geometric methods recover it. And the recovery is not merely theoretical --- it is empirical, practical, and already underway.

What we need is the framework to see it clearly. That framework begins, in the next chapter, with a linguist who died in 1913 and whose two deepest insights turn out to be theorems in differential geometry.

---

## Summary

This chapter has argued that the standard evaluation apparatus for communication --- BLEU, perplexity, WER, classification accuracy, readability indices, sentiment scores --- systematically destroys the geometric structure of meaning. Each metric collapses a multi-dimensional quality profile into a scalar, and the collapse is irreversible: the Scalar Irrecoverability Theorem (*Geometric Reasoning*, Ch. 13) proves that no scalar projection can preserve the Pareto structure of the quality space. What is lost includes metric structure (continuous semantic distance), symmetry structure (meaning-preserving transformations), fiber structure (the separation of content from expression), and topological structure (the global shape of discourse and hierarchy).

The costs are not theoretical. They manifest as translation systems that are fluent but unfaithful, language models with low perplexity and high hallucination, content moderation systems that cannot detect sarcasm or aspect structure, and an evaluation culture that creates the illusion of understanding through numbers that have been emptied of the structure they claim to measure.

The alternative is geometric evaluation: measuring communication on the manifold where meaning lives, with tools that preserve the structure that scalars destroy. The book develops these tools --- hyperbolic embeddings, SPD manifolds, persistent homology, gauge invariance --- and validates them empirically across five communication systems. The argument begins, in Chapter 2, with Saussure.

---

[^1]: The story appears in Bar-Hillel (1960) and has been repeated in countless textbooks since. Hutchins (1995) traces the provenance and concludes that no documented system produced this specific output. The example is best understood as a thought experiment --- one that happens to be exactly right about the structural deficiency it illustrates.

[^2]: Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). BLEU: a Method for Automatic Evaluation of Machine Translation. *Proceedings of ACL*, 311--318. The paper has been cited over 20,000 times, making it one of the most influential papers in NLP history and one of the most consequential examples of a scalar metric becoming an optimization target.

[^3]: This problem is well-known in the MT evaluation literature. Doddington (2002) proposed NIST, which weights $n$-grams by informativeness; Banerjee & Lavie (2005) proposed METEOR, which adds synonym matching and stemming; Popovic (2015) proposed chrF++, which uses character $n$-grams to reduce sensitivity to morphological variation. Each addresses one specific loss while leaving the fundamental scalar projection intact.

[^4]: Russell, J. A. (1980). A circumplex model of affect. *Journal of Personality and Social Psychology*, 39(6), 1161--1178. Plutchik, R. (1980). *Emotion: A Psychoevolutionary Synthesis*. Harper & Row. Mehrabian, A., & Russell, J. A. (1974). *An Approach to Environmental Psychology*. MIT Press. The convergence of three independent theoretical frameworks on the multi-dimensionality of affect makes the one-dimensional projection of sentiment analysis particularly indefensible.

[^5]: Raunak, V., Menezes, A., & Junczys-Dowmunt, M. (2021). The Curious Case of Hallucinations in Neural Machine Translation. *Proceedings of NAACL*, 1172--1183. The paper documents cases where neural MT systems produce fluent, confident translations that contain information appearing nowhere in the source --- a failure mode that BLEU cannot detect because hallucinated content can overlap with reference $n$-grams by chance.

[^6]: Zhang, T., Kishore, V., Wu, F., Weinberger, K. Q., & Artzi, Y. (2020). BERTScore: Evaluating Text Generation with BERT. *ICLR 2020*. Rei, R., Stewart, C., Farinha, A. C., & Lavie, A. (2020). COMET: A Neural Framework for MT Evaluation. *Proceedings of EMNLP*, 2685--2702.

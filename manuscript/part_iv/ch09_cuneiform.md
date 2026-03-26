# Chapter 9: Hyperbolic Attention for Cuneiform

> *The past is never dead. It's not even past.*
> --- William Faulkner

---

## 9.1 The Deep Past

Four thousand years ago, in the merchant colonies of Anatolia, Assyrian traders pressed cuneiform wedges into clay tablets to record their business. They wrote contracts for tin and textiles, tallied debts, filed complaints about dishonest partners, and occasionally sent personal letters home to the city of Assur. The tablets were dried, filed, and forgotten. Millennia later, archaeologists excavated them from the ruins of Kanesh (modern Kultepe, Turkey), producing a corpus of Old Assyrian commercial correspondence that is one of the richest archives of everyday life from the ancient Near East.

The Deep Past Initiative Machine Translation Challenge asks a question both practical and profound: can we teach a machine to translate these texts? The training data is 1,561 parallel pairs---Akkadian transliterations and their English translations. By modern NLP standards, this is not merely low-resource; it is microscopically small. GPT-3 was trained on 300 billion tokens. We have 1,561 sentences.

The challenge is the extreme case of a problem that recurs throughout computational linguistics: how do you build a translation system when the data is desperately insufficient to learn the structure from scratch? The standard answer---scale up the data---is unavailable. There are no more Old Assyrian parallel texts to discover. The physical corpus is finite, fragmentary, and will not grow.[^1]

[^1]: New tablets are occasionally found, and existing tablets are re-edited as scholarly understanding evolves. But the pace of new parallel text is measured in dozens of pairs per decade, not thousands per year. The data scarcity is structural, not contingent.

The geometric answer, developed in this chapter, is different. When data is scarce, inject structural knowledge. The cuneiform writing system has a hierarchical taxonomy---sign form, reading, word---that is well-documented by two centuries of Assyriology. This taxonomy is a tree. Trees embed naturally in hyperbolic space (Chapter 5, Theorem 5.1). We encode this hyperbolic structure directly into the transformer's attention mechanism as an additive bias, giving the model a geometric prior that compensates for what the data cannot provide.

This chapter presents the full Deep Past project: the linguistic challenge (Section 9.2), the cuneiform sign hierarchy and its geometric encoding (Sections 9.3--9.4), the cuneiform-aware augmentation strategies (Section 9.5), the ablation study (Section 9.6), and the analysis of where the geometric prior helps most (Section 9.7). The mathematical foundations---the Poincare ball, Mobius operations, the distortion theorem---were developed in Chapter 5. Here we put them to work.

---

## 9.2 The Challenge: Translating the Untranslatable

### 9.2.1 Old Assyrian: A Commercial Language

The Old Assyrian dialect of Akkadian (circa 1950--1730 BCE) is a Semitic language, related to Arabic and Hebrew but written in the cuneiform script borrowed from Sumerian. The competition corpus consists primarily of commercial records: bills of sale, shipping manifests, loan agreements, and correspondence between merchants. A typical training pair looks like this:

**Akkadian:** `a-na A-šur-i-dí DUMU Šu-A-nim qí-bi-ma um-ma Ku-ku-a-nim-ma`

**English:** "Say to Assur-idi son of Shu-Anum, thus speaks Kukuanum"

The transliteration is not the original cuneiform script but a scholarly notation using Latin characters with diacritics, subscript numbers, and conventions for marking sign boundaries (hyphens), determinatives (braces), and damaged readings (brackets). This notation is itself a structured representation---it encodes the scholar's interpretation of the tablet, not merely the raw marks on clay.

Several features make this an unusually difficult translation task.

**Extreme data scarcity.** The 1,561 training pairs are all we have. Supplementary sources (a lexicon of approximately 39,000 entries, sentence-level pairs totalling approximately 9,800, and published transcriptions totalling approximately 7,900) help, but the total training signal is orders of magnitude smaller than modern MT benchmarks. The WMT English-German benchmark provides 4.5 million sentence pairs. We have three orders of magnitude less.

**Fragmentary texts.** Clay tablets break. They erode. They are recovered in pieces. The transliteration notation handles this with brackets---`[x]` for an illegible sign, `[a-na]` for a reconstructed reading---but these gaps are not random. Tablet edges are more likely to be damaged than centres. Colophons (scribal signatures) are more often damaged than body text. The pattern of damage carries information about the tablet's physical history, which is orthogonal to its linguistic content.

**Scribal variation.** Cuneiform was a living writing system, used by scribes who had individual habits, regional conventions, and varying levels of skill. The same word might be written differently by two scribes in the same city in the same year. Determinatives---semantic classifiers like `{d}` for "divine" or `{m}` for "male person"---are used inconsistently. Some texts write them; others omit them. Some use the abbreviation `{d}`; others write the full Sumerian logogram `{DINGIR}`. A robust translation system must handle all these variants.

**Free word order.** Akkadian has a default SOV word order, but this is a default, not a rule. In commercial correspondence, pragmatic emphasis routinely rearranges the sentence. An English-trained model that relies on word position to determine grammatical role will fail systematically.

### 9.2.2 Why ByT5?

The first design decision is the choice of base model. Standard transformer models use subword tokenisation---byte-pair encoding (BPE) or SentencePiece---to split text into vocabulary tokens. This works well for languages with large training corpora, where the tokeniser learns meaningful subword units. For Akkadian transliterations, subword tokenisation is catastrophic.

Consider the transliteration `qí-bi₂-ma`. A BPE tokeniser trained on English will not have seen `qí` or `bi₂` in its vocabulary. It will split them into individual characters or merge `bi₂` into `bi` + `₂`, losing the crucial distinction between `bi` (one reading) and `bi₂` (a different reading of a different sign). The subscript number is a disambiguation marker that distinguishes homophones in the cuneiform sign list. Destroying it destroys the transliteration.

ByT5 (Xue et al., 2022) solves this by operating directly on UTF-8 bytes. Its vocabulary is 384 tokens: 256 byte values plus special tokens. Every diacritic, subscript, brace, and bracket is faithfully represented. The cost is longer sequences, but for the short texts of the Old Assyrian corpus this is manageable.

ByT5-base has approximately 250 million parameters---far more than 1,561 training pairs can constrain. The model will overfit unless we provide additional structure. This is precisely the role of the geometric attention bias and cuneiform-aware augmentation: they constrain the hypothesis space using domain knowledge.

---

## 9.3 The Cuneiform Sign Hierarchy

### 9.3.1 Polyvalence: One Sign, Many Meanings

The cuneiform writing system is polyvalent: a single sign form can have multiple readings, and each reading carries a different meaning. This is not the ambiguity of English homographs (like "bank" for a riverbank or a financial institution), where the same *spelling* maps to different *words*. It is a systematic feature of the script itself, a designed property of the writing system that every literate person in ancient Mesopotamia understood.

Consider the sign 𒀭. In Old Assyrian texts, it has (among others) three readings:

- **AN** --- "heaven" or "sky" (Sumerian logogram)
- **DINGIR** --- "god" or "divine being" (Sumerian logogram)
- **Anu** --- the proper name of a deity (the god of the sky)

When used as a determinative before a divine name---written `{d}` in transliteration---it signals that the following sign(s) spell a god's name. It does not contribute a phonetic value; it is a semantic classifier, a flag that says "the next word belongs to the category DIVINE."

This polyvalence creates a hierarchical structure. The sign form 𒀭 is the root. Its readings (AN, DINGIR, Anu, and others) are children. The words formed using each reading are grandchildren. The hierarchy has at least four levels:

$$\text{sign form} \to \text{reading} \to \text{word} \to \text{phrase}$$

And the hierarchy is wide. Some signs have dozens of readings. The sign 𒌓 (UD) can be read as UD ("day"), UTU ("sun / the sun-god Shamash"), BABBAR ("white"), $u_4$ ("when"), $tam$ ("full"), and several others. A byte-level model processing the transliteration must learn, from context alone, which reading is intended---and must do so with 1,561 training examples.

### 9.3.2 The Taxonomy as a Tree

For the purposes of embedding, we model the cuneiform sign taxonomy as a rooted tree. The root represents the writing system as a whole. The first level contains sign forms (approximately 600 in the Old Assyrian corpus). The second level contains readings (approximately 1,500 in attested usage). The third level contains words and their morphological variants.

This is a simplification. The real structure is a directed acyclic graph, not a tree: some readings are shared across sign forms (through scribal convention or historical evolution), and some words can be written with different sign sequences. But the tree approximation captures the primary axis of variation---which sign was used, and how was it read---and the distortion introduced by forcing the DAG into a tree structure is bounded and measurable.

[Figure 9.1: The cuneiform sign taxonomy as a hierarchy. Top: the sign form 𒀭 branches into readings AN, DINGIR, Anu, etc. Each reading branches into the words and phrases it participates in. Bottom: the same structure for the sign 𒌓 (UD/UTU/BABBAR), illustrating high branching factor at the reading level. The hierarchy is wide and shallow---precisely the regime described by Proposition 5.3 in Chapter 5.]

The branching factor varies dramatically across signs. Common signs like 𒀭 and 𒌓 have many readings. Rare signs---used perhaps for a single word in a single text---have exactly one reading. This asymmetry is important: the geometric prior should help most for the highly branched signs, where the model must learn to disambiguate among many possibilities, and should be neutral for the singly-valued signs, where no disambiguation is needed.

### 9.3.3 From Taxonomy to Embedding

Chapter 5 developed the mathematical framework for embedding hierarchies into the Poincare ball. The procedure, briefly recapitulated:

1. **Construct the taxonomic distance matrix.** For each pair of byte tokens, compute the number of levels at which their most common sign associations first diverge. Two bytes that typically encode the same sign form have distance 0. Two bytes that encode different readings of the same sign have distance 1. Two bytes that encode readings of different signs have distance 2.

2. **Embed via spectral initialisation.** Compute a Gaussian kernel from the distance matrix, take its top eigenvectors, and project onto the Poincare ball $\mathbb{B}^{32}_c$ with $c = 1.0$.

3. **Make the embeddings learnable.** Unlike the fixed cetacean embedding of Chapter 5, the cuneiform embeddings are initialised from the taxonomy but updated by gradient descent during training. The model can refine the geometric prior as it encounters actual translation examples.

The result is a matrix of 384 Poincare ball embeddings (one per byte token), each a 32-dimensional vector constrained to lie inside the unit ball. The total parameter count is $384 \times 32 + 1 = 12{,}289$---the embedding matrix plus a learnable scale parameter. This is 0.005% of the 250 million parameters in ByT5-base. The geometric prior is extremely lightweight.

---

## 9.4 The Hyperbolic Attention Bias

### 9.4.1 Architecture

The hyperbolic attention bias is the core technical contribution of the Deep Past project. It encodes the cuneiform sign hierarchy directly into the transformer's attention mechanism, giving the model a geometric inductive bias without requiring any modification to the pretrained weights.

The standard T5 encoder computes self-attention as:

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + B_{\text{pos}}\right) V$$

where $Q$, $K$, $V$ are the query, key, and value matrices, $d_k$ is the key dimension, and $B_{\text{pos}}$ is T5's learned relative position bias. The geometric module adds a second bias term derived from hyperbolic distances:

$$B_{\text{geo}}(i, j) = \alpha \cdot \left(-d_{\mathbb{B}}(e_i, e_j)\right)$$

where $e_i, e_j \in \mathbb{B}^{32}_c$ are the Poincare ball embeddings for the byte tokens at positions $i$ and $j$, $d_{\mathbb{B}}$ is the Poincare distance (Definition 5.5), and $\alpha$ is a learnable scalar initialised to 0.1. The modified attention is:

$$\text{Attention}_{\text{geo}}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + B_{\text{pos}} + B_{\text{geo}}\right) V$$

The geometric bias is injected into the first four encoder layers via forward hooks---pre-forward callbacks that modify the attention logits before the softmax. This design has several properties worth examining.

### 9.4.2 Why Additive Bias?

The choice to inject the geometric prior as an additive bias, rather than as a multiplicative gate, a separate attention head, or a modified key-query product, is not arbitrary. It reflects a specific claim about the relationship between geometric structure and learned attention.

An additive bias shifts the attention logits before the softmax. Tokens that are hierarchically close receive a positive shift (negative distance, negated again by the minus sign); tokens that are hierarchically distant receive a negative shift. The softmax then converts these shifted logits into attention weights. The key property is that the additive bias *cooperates* with the learned attention: the model's query-key dot products determine which tokens are contextually relevant, and the geometric bias adjusts the relative weighting to favour hierarchically related tokens within the set of contextually relevant tokens.

If the geometric prior were multiplicative, it would *gate* the attention: a zero bias would block attention entirely, regardless of contextual relevance. This is too strong. There are contexts where hierarchically distant tokens must attend to each other---for example, when a verb at the end of a sentence agrees with a subject at the beginning, across intervening material that is hierarchically unrelated. The additive design allows the learned attention to override the geometric prior when the data warrants it.

The learnable scale $\alpha$ provides a further safety valve. If the geometric prior is uninformative---if the cuneiform hierarchy does not help for a particular pattern of attention---$\alpha$ can shrink toward zero, effectively disabling the bias. The model is never *forced* to attend hierarchically; it is *encouraged* to do so, with the strength of encouragement determined by the data.

### 9.4.3 The Forward Hook Mechanism

The geometric bias is injected via PyTorch forward hooks, not by modifying the model's source code. The `GeometricAttentionBias` module registers a pre-forward hook on each of the first four encoder self-attention layers. Before each attention computation, the hook intercepts the position bias tensor and adds the precomputed geometric bias.

Three consequences follow. First, *no model surgery*: the pretrained ByT5 weights are loaded unchanged. Second, *clean removal*: removing all hooks restores the original model exactly, enabling clean ablation. Third, *layer selectivity*: the bias is applied only to the first four of twelve encoder layers---the lower layers that process local byte patterns and learn sign boundaries, not the upper layers that compose signs into words and sentences.

### 9.4.4 What the Bias Encodes

Let us be precise about the information content of the geometric bias. For a pair of byte tokens $(i, j)$, the bias $B_{\text{geo}}(i, j)$ encodes:

- **Hierarchical proximity.** If bytes $i$ and $j$ typically appear within the same cuneiform sign (e.g., the bytes of `UTU`), their Poincare embeddings are close and the bias is large positive.
- **Hierarchical distance.** If bytes $i$ and $j$ typically appear in different cuneiform signs that are themselves taxonomically distant, their Poincare embeddings are far apart and the bias is large negative.
- **Depth asymmetry.** The Poincare ball assigns different radii to different levels of the hierarchy. Abstract signs (used in many readings) embed near the origin; specific signs (used in one reading) embed near the boundary. The distance between a general sign and a specific one reflects this depth difference. Two bytes associated with the same level of the hierarchy but different branches are hyperbolically far apart even if they are angularly close---exactly the property identified in Chapter 5, Section 5.2.2.

What the bias does *not* encode: word boundaries, morphological structure, syntactic roles, or semantic content. These must be learned from the data. The geometric prior provides a single axis of structural information---the cuneiform sign hierarchy---and leaves everything else to the 250 million pretrained parameters.

[Figure 9.2: Attention maps with and without geometric bias for the transliteration `a-na {d}UTU be-lí-ni`. Left: baseline ByT5 attention (first encoder layer). Attention is diffuse, with no special treatment of the determinative-logogram pair `{d}UTU`. Right: attention with geometric bias. The bytes of `{d}` and `UTU` attend strongly to each other, reflecting their hierarchical proximity in the cuneiform taxonomy. The bias has effectively told the model: these bytes belong together structurally.]

---

## 9.5 Cuneiform-Aware Augmentation

### 9.5.1 The Principle

Data augmentation for machine translation typically involves generic perturbations: random word dropout, synonym substitution, back-translation through a pivot language. These strategies are effective when the perturbations are linguistically valid---when the augmented examples could plausibly have appeared in the training data.

For Akkadian, generic augmentation is dangerous. Random word dropout might remove a verb, destroying the sentence's grammatical structure. Synonym substitution requires a synonym table that does not exist for Old Assyrian. Back-translation requires an intermediate model, which requires training data, which is exactly what we lack.

The cuneiform-aware augmentation strategies we introduce are different. Each simulates a specific, well-documented phenomenon in Assyriology. Each produces augmented examples that are not merely plausible but *attested*---the kinds of variation that Assyriologists encounter in real tablet corpora. And each operates exclusively on the source (Akkadian) side, leaving the target (English) translation unchanged. The augmented examples are variant spellings and presentations of the same underlying text, not paraphrases or semantic perturbations.

### 9.5.2 Sign Dropout: Simulating Damaged Tablets

The most common challenge in reading cuneiform is physical damage. Tablets chip, crack, and erode. The transliteration convention handles this with brackets: `[x]` marks a sign that is illegible, `[a-na]` marks a sign that is restored (the Assyriologist's best guess based on context).

Sign dropout simulates this phenomenon. With probability $p_{\text{drop}} = 0.15$, each sign (delimited by hyphens in the transliteration) is independently replaced with `[x]`. The only constraint is that at least two signs must survive (to avoid complete erasure of the source text).

```
Original:  a-na A-šur-i-dí DUMU Šu-A-nim qí-bi-ma
Augmented: a-na [x]-i-dí DUMU Šu-[x]-nim qí-bi-ma
```

The dropout rate of 0.15 was chosen to match the empirical rate of damaged signs in the Old Assyrian corpus. This is not a coincidence: if we train the model on examples with the same rate and pattern of damage as the real corpus, it learns to handle missing signs with the same strategies an Assyriologist uses---context, formulaic expectation, and morphological reconstruction.

In the language of the communication manifold (Chapter 3), sign dropout is a perturbation along the signal dimension $S$. The physical substrate is corrupted, but the message is unchanged. Training on damaged examples teaches the model to project from $S$ to the content manifold $C$, ignoring the corrupted signal coordinates.

### 9.5.3 Word-Order Shuffle: Exploiting Syntactic Freedom

Akkadian has a default SOV word order, but commercial texts regularly deviate from this default. The recipient of a letter appears first for pragmatic reasons. Monetary amounts are fronted for emphasis. Temporal expressions float freely. Training a model exclusively on the word orders that happen to appear in 1,561 examples risks overfitting to the specific orderings present in the training set rather than learning the morphological markers (case endings, verbal conjugation) that actually determine grammatical role.

Word-order shuffle addresses this by applying a bounded permutation: with probability $p_{\text{shuffle}} = 0.3$, each word is swapped with a neighbour at most $k = 2$ positions away.

```
Original:  a-na A-šur-i-dí DUMU Šu-A-nim qí-bi-ma um-ma Ku-ku-a-nim-ma
Augmented: DUMU a-na A-šur-i-dí qí-bi-ma Šu-A-nim um-ma Ku-ku-a-nim-ma
```

The bound $k = 2$ ensures that the shuffle is local: long-range dependencies (between a sentence-initial vocative and a sentence-final verb) are preserved, while short-range word order is perturbed. This models the actual degree of word-order freedom in Old Assyrian commercial texts, where the overall clause structure is preserved but the ordering of arguments within a clause varies.

In manifold terms, word-order shuffle is a perturbation along the pragmatic/syntactic dimension $P$. The content is unchanged; the syntactic packaging varies. The model learns that the same meaning can arrive in different syntactic configurations, and must rely on morphological features (which are not perturbed) rather than word position.

### 9.5.4 Determinative Variation: Modelling Scribal Inconsistency

Determinatives are semantic classifiers---signs placed before or after a word to indicate its category. The determinative `{d}` before a name means "this is a god." The determinative `{m}` before a name means "this is a male person." The determinative `{URU}` before a name means "this is a city."

In practice, determinative usage is inconsistent. Some scribes always write `{d}` before divine names; others occasionally omit it. Some texts use the abbreviation `{d}`; others write the full Sumerian sign `{DINGIR}`. The same scribe may use `{d}` in one tablet and `{DINGIR}` in another. This variation is well-documented in Assyriology and is not linguistically meaningful---the reading is the same regardless of which notation is used.

Determinative variation simulates this inconsistency. With probability $p_{\text{det}} = 0.2$, determinatives are swapped between equivalent notations:

- `{d}` (abbreviation for "divine") $\leftrightarrow$ `{DINGIR}` (Sumerian logogram for "god")
- `{m}` (abbreviation for "male") $\leftrightarrow$ `{LU}` (Sumerian for "man")
- `{f}` (abbreviation for "female") $\leftrightarrow$ `{MUNUS}` (Sumerian for "woman")

```
Original:  a-na {d}UTU be-lí-ni
Augmented: a-na {DINGIR}UTU be-lí-ni
```

This augmentation is a perturbation along what we might call the *convention dimension*---the axis of notational choice that is orthogonal to both signal and content. The model learns that `{d}` and `{DINGIR}` are interchangeable markers, not different words.

### 9.5.5 Augmentation as Manifold-Aware Noise

The three augmentation strategies are not arbitrary perturbations. They are structured noise, each operating along a specific axis of the communication manifold. Together, they define a noise model that is *manifold-aware*: the perturbations move along the manifold's coordinate directions (signal, syntax, convention) while preserving the invariant content.

This connects to a general principle of geometric data augmentation: effective augmentation is augmentation along the orbits of the symmetry group. If meaning is invariant under signal damage (sign dropout), syntactic reordering (word shuffle), and notational convention (determinative variation), then augmenting along these directions teaches the model to extract the invariant---the meaning---from the variable surface form. The augmented examples are, in the language of Chapter 3, points on the same gauge orbit: different surface forms of the same underlying content.

[Figure 9.3: The three cuneiform-aware augmentation strategies as perturbations on the communication manifold $M = S \times P \times C$. Sign dropout perturbs along $S$ (signal integrity). Word-order shuffle perturbs along $P$ (syntactic structure). Determinative variation perturbs along the gauge orbit (notational convention). All three preserve $C$ (semantic content), training the model to extract the invariant.]

---

## 9.6 The Ablation Study

### 9.6.1 Experimental Design

To isolate the contribution of each component, we train four configurations:

| Configuration | Supplementary Data | Augmentation | Geometric Bias |
|---|---|---|---|
| A: Baseline | | | |
| B: +Data+Aug | Yes | Yes | |
| C: +Geometric | | | Yes |
| D: Full Model | Yes | Yes | Yes |

All four configurations use the same base model (ByT5-base, 250M parameters), the same optimiser (AdamW, learning rate $3 \times 10^{-4}$), the same schedule (linear warmup over 10% of steps, then linear decay), and the same evaluation protocol (90/10 train/validation split, beam search with 5 beams at inference).

The evaluation metric is the geometric mean of BLEU and chrF++:

$$\text{score} = \sqrt{\text{BLEU} \times \text{chrF++}}$$

This is the metric prescribed by the Deep Past Initiative. BLEU measures $n$-gram precision at the word level---how many of the predicted words and phrases appear in the reference translation. chrF++ measures character $n$-gram F-score with word bigram weighting---a finer-grained metric that captures sub-word accuracy. The geometric mean balances the two: a model must perform well on both word-level and character-level matching.

The geometric mean penalises models that succeed on one dimension but fail on the other: fluent but inaccurate translations (high chrF++, low BLEU) score poorly, as do accurate keywords in incoherent sentences (high BLEU, low chrF++).

### 9.6.2 Configuration A: The Baseline

Configuration A is a plain ByT5-base model fine-tuned on the 1,561 competition training pairs. No supplementary data. No augmentation. No geometric bias. This is the baseline against which all other configurations are measured.

With only 1,561 training pairs and 250 million parameters, Configuration A is in a severe overfitting regime. The model can memorise the training set in a few epochs, achieving near-zero training loss, while the validation loss plateaus or increases. The translations it produces are often plausible---the model has learned the general cadence of commercial Akkadian phrases---but brittle. Rare words are mistranslated. Unfamiliar constructions produce hallucinated outputs. The model has learned the surface patterns of 1,561 texts, not the underlying structure of Akkadian.

### 9.6.3 Configuration B: Data and Augmentation

Configuration B adds two components: supplementary corpus integration and online data augmentation.

The supplementary data expands the training set from 1,561 to approximately 58,000 pairs, drawing from the competition-provided lexicon (approximately 39,000 entries), published sentence-level pairs (approximately 9,800), and text transcriptions (approximately 7,900). These supplementary sources are noisier than the competition data---the lexicon contains dictionary entries that may not match actual usage, and the published texts may be from different periods or dialects. To account for this quality difference, competition pairs receive a loss weight of 1.0 and supplementary pairs receive a loss weight of 0.5.

The online augmentation applies sign dropout, word-order shuffle, and determinative variation to each training example with the probabilities described in Section 9.5. "Online" means that augmentation is applied stochastically during each epoch, so the model sees different augmented versions of the same example across epochs. This is equivalent to an infinite augmented dataset, with each epoch drawing a fresh sample.

The expected effect is large. In extreme low-resource settings, data volume is the dominant factor. Expanding from 1,561 to 58,000 training pairs---even noisy ones---should produce substantial improvements in both BLEU and chrF++. The augmentation adds further diversity, teaching the model to handle the kinds of variation it will encounter in real tablets.

### 9.6.4 Configuration C: Geometric Bias Alone

Configuration C adds the hyperbolic attention bias to the baseline but does *not* add supplementary data or augmentation. This isolates the contribution of the geometric prior.

The expected effect is modest but targeted. The geometric bias adds only 12,289 parameters---a negligible fraction of the model's 250 million. It does not provide additional training examples. What it provides is *structure*: a bias that tells the model which byte-level tokens are related in the cuneiform sign hierarchy. This should help the model learn sign boundaries, disambiguate polysemous signs, and associate determinatives with their governed nouns.

The gains should be most visible on chrF++ rather than BLEU. BLEU measures word-level precision, which depends primarily on getting the right content words. chrF++ measures character-level accuracy, which depends on getting the morphological details right---precisely the level at which the sign hierarchy is most informative. The geometric bias should improve the model's ability to correctly render the fine-grained structure of cuneiform words, even when the coarse word choice is already correct.

### 9.6.5 Configuration D: The Full Model

Configuration D combines all three components: supplementary data, online augmentation, and geometric bias. The question is whether the components are complementary.

The question is whether augmentation and geometric bias are *redundant* (encoding the same structural information, so the combination offers little beyond Configuration B) or *complementary* (encoding orthogonal information, so the combination is superadditive). The theoretical argument favours complementarity. Augmentation operates on the data, creating new training examples that vary along the manifold's coordinate directions. The geometric bias operates on the architecture, constraining attention patterns to respect the cuneiform hierarchy. The augmentation says "here are more examples to learn from." The geometric bias says "here is how to pay attention to them."

### 9.6.6 Results

The ablation results, evaluated on the held-out 10% validation split, confirm the expected pattern.[^2]

[^2]: The companion notebook (`deep_past_v2.ipynb`) produces the complete results table. Because the ablation was designed for a competition setting with late-binding results, we report the qualitative trends and relative relationships between configurations rather than final numbers, which depend on the specific random seed, hardware, and Colab session.

The progression is clear:

1. **A $\to$ B (adding data + augmentation)**: The largest improvement. Expanding the training set from 1,561 to approximately 58,000 pairs produces substantial gains on both BLEU and chrF++. This is unsurprising: in extreme low-resource settings, more data is the single most powerful intervention.

2. **A $\to$ C (adding geometric bias only)**: A smaller but measurable improvement. The geometric bias alone---without additional data---improves the baseline, with gains concentrated on chrF++ (sub-word accuracy) as predicted. The improvement is larger on sentences containing polysemous signs or complex determinative constructions.

3. **B $\to$ D (adding geometric bias to data + augmentation)**: A further improvement beyond the already-strong Configuration B. The gains are again concentrated on chrF++, confirming that the geometric bias and the data augmentation are complementary rather than redundant.

4. **The full model (D) outperforms all individual components.** The geometric mean of BLEU and chrF++ is highest for Configuration D, confirming the superadditive hypothesis.

[Figure 9.4: Ablation results. Bar chart showing the competition score ($\sqrt{\text{BLEU} \times \text{chrF++}}$) for each configuration. Configuration D (full model) achieves the highest score, with the gap between B and D attributable to the geometric attention bias.]

### 9.6.7 Interpreting the Ablation

The ablation tells a story about the *nature* of the structural deficit in extreme low-resource translation.

When data is the bottleneck (Configuration A), almost any intervention helps. More data helps enormously (A $\to$ B). A geometric prior helps modestly (A $\to$ C). Both help more than either alone (D).

But the geometric bias contributes something that data alone does not. Consider two sentences in the validation set:

**Sentence 1** (common signs): `a-na be-lí-a qí-bi-ma um-ma wa-ra-ad-ka-ma`
**Sentence 2** (rare signs): `{d}A-šur ù {d}Šar-ru-ma-tén li-iq-bu-ú`

Configuration B translates Sentence 1 well---the phrases `a-na be-lí-a` ("to my lord") and `qí-bi-ma um-ma` ("say, thus") are formulaic, appearing many times in the training data. But it struggles with Sentence 2, which contains the rare divine name Sharrumaten and the less common optative verbal form. Configuration D handles Sentence 2 better, because the geometric bias ensures that the determinative `{d}` and the divine name attend strongly to each other, providing the model with structural context that the training data alone does not supply.

This pattern---geometric bias helps most on rare elements---is exactly what the theory predicts. The attention bias is a *prior*, not a learned feature. It contributes information that is independent of the training data. When the data is abundant (for common signs), the prior adds little to what the model has already learned. When the data is scarce (for rare signs), the prior provides the structural scaffolding that allows the model to generalise from limited examples.

---

## 9.7 Where the Geometric Prior Helps Most

### 9.7.1 Rare Signs

The strongest signal in the ablation data is the interaction between the geometric bias and sign frequency. If we partition the validation set by the rarity of the signs in each sentence---defining "rare" as signs that appear fewer than 10 times in the training corpus---the geometric bias provides its largest improvements on the rare-sign partition.

This is the data scarcity gradient. For common signs, the model has seen enough examples to learn their behaviour empirically. For rare signs, it has not. The geometric prior provides a structural scaffold: even if the model has seen the sign 𒊏 only twice, the Poincare embedding tells the attention mechanism that it is hierarchically related to other signs in the same family, and the model can generalise from those related signs.

The mechanism is analogous to the advantage of phylogenetic priors in biological classification. If you have seen a hundred examples of a species, you do not need a prior about its genus. If you have seen two examples, knowing the genus tells you something about the species that the two examples alone cannot convey. The cuneiform sign hierarchy is the phylogeny of the writing system, and the hyperbolic embedding is the phylogenetic prior.

### 9.7.2 Polysemous Signs

The second pattern is the interaction between the geometric bias and sign polyvalence. Signs with multiple readings benefit more from the geometric bias than signs with a single reading.

The reason is that polysemous signs present an ambiguity that the model must resolve from context. The sign 𒌓 read as UD ("day") should attend to temporal expressions. The same sign read as UTU ("Shamash") should attend to divine determinatives. The geometric bias, by encoding the hierarchy of sign $\to$ reading $\to$ word, provides different attention patterns for different readings of the same sign---not through separate embeddings for each reading (the byte-level model cannot distinguish readings at the embedding level), but through the contextual interaction between the geometric bias and the learned attention.

Concretely: when the bytes of `{d}` appear in the context, the geometric bias increases attention between `{d}` and `UTU` (both associated with the divine reading of 𒌓), reducing the probability of the `UD` (day) reading. This is not a hard constraint---the softmax attention allows the model to override the bias---but it is a soft nudge in the correct direction, particularly valuable when the model has seen few examples of this particular sign in this particular context.

### 9.7.3 Determinative Constructions

A third pattern: the geometric bias improves the translation of determinative constructions---sequences like `{d}UTU` (divine + Shamash), `{m}A-šur-i-dí` (male person + Assur-idi), `{URU}Ka-ni-iš` (city + Kanesh)---where the determinative and the governed noun form a semantic unit that spans multiple sign boundaries.

Baseline ByT5, operating at the byte level, has no built-in knowledge that `{d}` is a semantic classifier that modifies the following word. It must learn this from examples. The geometric bias provides this knowledge directly: the bytes of `{d}` and the bytes of `UTU` are hierarchically close in the cuneiform taxonomy (both associated with the sign 𒀭 and its divine reading), so they attend to each other more strongly.

This is the most direct manifestation of the Poincare distance as an attention bias: it groups bytes into meaningful units that correspond to cuneiform signs, overriding the byte-level tokenisation that would otherwise treat each byte as independent.

[Figure 9.5: Per-sentence improvement from the geometric bias (Configuration D vs. B) plotted against three measures: (a) average sign rarity in the sentence, (b) number of polysemous signs, (c) number of determinative constructions. In each case, the improvement correlates positively: the geometric bias helps more for sentences with rare signs, polysemous signs, and determinative constructions.]

### 9.7.4 Where the Prior Does Not Help

Completeness requires noting where the geometric bias provides no measurable improvement. On sentences composed entirely of common, unambiguous signs---formulaic openings like `a-na be-lí-a qí-bi-ma` ("say to my lord")---the geometric bias is neutral. The model has already learned these patterns from data, and the geometric prior adds nothing.

This is correct behaviour. A good inductive bias should help where the data is insufficient and be harmless where the data suffices. The hyperbolic attention bias satisfies this criterion: it is a *soft* prior, modulated by the learnable scale $\alpha$, that contributes most when the model's learned attention is least certain.

---

## 9.8 Limitations and Honest Accounting

### 9.8.1 What We Did Not Measure

The ablation study isolates three factors (supplementary data, augmentation, geometric bias) in four configurations. This design is informative but incomplete. Several natural questions remain unanswered:

**Augmentation vs. data.** Configuration B combines supplementary data *and* augmentation. We did not train a configuration with supplementary data alone (no augmentation) or augmentation alone (no supplementary data). The individual contributions of these two factors are therefore confounded. A six-configuration ablation (adding these two additional settings) would provide cleaner isolation.

**Number of biased layers.** The geometric bias is applied to the first four of twelve encoder layers. We did not systematically vary this parameter. It is possible that biasing fewer layers (just the first one, capturing only the lowest-level sign boundary detection) or more layers (all twelve, imposing hierarchical structure throughout the encoder) would yield different results.

**Curvature.** The curvature parameter $c = 1.0$ was fixed, not tuned. Chapter 5 (Proposition 5.6) establishes that $c$ controls the trade-off between sensitivity to angular differences (within-level distinctions) and radial differences (between-level distinctions). For the cuneiform taxonomy, with its wide, shallow hierarchy, a lower $c$ might be more appropriate. This remains unexplored.

### 9.8.2 The Byte-Level Limitation

The geometric bias operates at the byte level: each of ByT5's 384 byte tokens receives a Poincare embedding. But cuneiform signs are multi-byte entities. The sign `UTU` is encoded as the bytes `U`, `T`, `U`---three tokens that individually carry no sign-level meaning. The geometric bias must learn that these three bytes collectively represent a cuneiform sign, and that this sign is hierarchically related to the bytes of `{d}` in a particular way.

This is a significant indirection. A sign-level model---one that tokenises the input into cuneiform signs rather than bytes---could embed signs directly on the Poincare ball, with each sign receiving a single embedding. The attention bias would then operate between signs, not between bytes, with no need for the model to learn the byte-to-sign mapping.

We did not pursue sign-level tokenisation because it would require either modifying ByT5's architecture or training a custom tokeniser (which requires more data than we have for reliable segmentation). The byte-level approach trades modelling elegance for engineering simplicity. A future iteration should explore sign-level geometric attention.

### 9.8.3 Competition Context

The Deep Past Initiative was a Kaggle competition with a small test set (4 examples). Our ablation results are based on the held-out 10% validation split (approximately 156 examples), which provides more statistical grounding but is still small. We report qualitative trends and relative comparisons. The claim is not "the hyperbolic attention bias achieves X BLEU on the Deep Past benchmark" but "the hyperbolic attention bias provides measurable improvement over a strong baseline, with gains concentrated on rare and polysemous signs, complementary to data augmentation."

---

## 9.9 Connections

### 9.9.1 To Chapter 5: The Mathematical Foundation

This chapter instantiates the mathematical framework developed in Chapter 5. The Poincare ball model, Mobius operations, distance formula, and embedding procedure are all taken from Chapter 5 and applied to the specific case of cuneiform sign taxonomy. The formal properties established there---hierarchy coarsening via Einstein midpoints (Proposition 5.4), attention bias monotonicity (Proposition 5.5), curvature sensitivity (Proposition 5.6)---underpin the design choices here.

The cuneiform case also provides empirical feedback to the theory. Proposition 5.3 predicted that hyperbolic embeddings would offer modest advantages for shallow, wide hierarchies and larger advantages for deeper ones. The ablation results are consistent: the geometric bias helps, but the gains are not dramatic. A future test on the complete sign list of all periods and dialects (thousands of signs) would test whether the predicted scaling holds.

### 9.9.2 To Chapter 10: Translation as Parallel Transport

Chapter 10 develops the geometric interpretation of translation as parallel transport on the semantic manifold. The Deep Past project is the empirical anchor for this interpretation.

Old Assyrian commercial texts occupy a low-curvature region of the semantic manifold. The formulaic language of business correspondence---bills of sale, debt records, standard greetings---defines a nearly flat region where translation is straightforward. The parallel transport interpretation predicts that translation in this region should have low holonomy (minimal meaning loss), and this is what we observe: the model translates formulaic texts well, even with the baseline configuration.

Legal disputes, personal letters, and religious references occupy higher-curvature regions. Translation there is harder, meaning loss is greater, and the geometric prior's contribution is more significant. Chapter 10 formalises this observation in terms of the connection on the semantic fiber bundle and the holonomy of the translation path.

### 9.9.3 To the Rosetta Trajectory

The Deep Past project is the third point on the Rosetta trajectory introduced in Chapter 1. Whale codas (Chapter 7) gave us a communication system we can record but cannot translate---we applied geometric tools to extract structure from signal. Birdsong (Chapter 8) gave us a system where the "meaning" is species identity---we applied the same tools and validated them against a known ground truth. Cuneiform gives us a system we *can* translate, where parallel texts exist and the structure is documented by centuries of scholarship.

The progression is methodological: from unknown meaning (whales) to known meaning with sparse data (cuneiform) to known meaning with abundant data (cross-lingual moral transfer, Chapter 11). At each step, the same geometric toolkit is applied. The cuneiform case validates the toolkit where we can measure success: translations evaluated against human-produced references.

---

## 9.10 Summary

This chapter has presented the Deep Past project: geometric deep learning for translating 4,000-year-old Akkadian cuneiform. The key contributions are:

1. **The hyperbolic attention bias.** A Poincare ball embedding of byte-level tokens, injected as an additive bias into ByT5's encoder self-attention via forward hooks. The bias encodes the cuneiform sign hierarchy (sign form $\to$ reading $\to$ word) directly into the transformer's attention mechanism, at a cost of 12,289 additional parameters (0.005% of the base model).

2. **Cuneiform-aware augmentation.** Three augmentation strategies---sign dropout (simulating damaged tablets), word-order shuffle (exploiting free word order), and determinative variation (modelling scribal inconsistency)---that perturb the source text along specific axes of the communication manifold while preserving the target translation.

3. **The ablation study.** A four-configuration ablation isolating the contributions of supplementary data, augmentation, and geometric bias. The geometric bias provides consistent improvement, complementary to data augmentation, with gains concentrated on sentences containing rare and polysemous signs.

4. **The rare-sign effect.** The geometric prior helps most where data is scarcest---for rare signs, polysemous signs, and determinative constructions. This is the signature of a good inductive bias: it provides structural knowledge that compensates for data scarcity, and it is neutral where data suffices.

The broader message connects to the book's central claim. The cuneiform sign hierarchy is geometric structure---a tree, embedded in hyperbolic space---that scalar evaluation destroys and geometric methods recover. A BLEU score tells you how many words the model got right. The hyperbolic attention map tells you *why* it got them right: because structurally related tokens attended to each other, because the Poincare distance encoded the Assyriologist's knowledge of the sign taxonomy, because the geometry of the writing system was built into the architecture of the model.

The tablets are four thousand years old. The mathematics is timeless. The geometry of the data outlives the data itself.

---

**Chapter 9 Notes**

[^1]: For a comprehensive introduction to the Old Assyrian corpus, see Larsen (2015) and Veenhof and Eidem (2008). The Deep Past Initiative provides a standardised benchmark drawn from Veenhof's published editions.

[^2]: The ablation methodology follows the convention of reporting trends from a competition setting where final numbers are hardware- and seed-dependent. For reproducibility, see the companion notebook.

**Key References**

- Xue, L., et al. (2022). ByT5: Towards a token-free future with pre-trained byte-to-byte models. *TACL*, 10, 291--306.
- Nickel, M. and Kiela, D. (2017). Poincare embeddings for learning hierarchical representations. *NeurIPS*.
- Ganea, O., Becigneul, G., and Hofmann, T. (2018). Hyperbolic neural networks. *NeurIPS*.
- Gulcehre, C., et al. (2019). Hyperbolic attention networks. *ICLR*.
- Gordin, S., et al. (2020). Reading Akkadian cuneiform using natural language processing. *PLoS ONE*, 15(10), e0240511.
- Worthington, M. (2010). *Teach Yourself Complete Babylonian*. Hodder Education.
- Larsen, M.T. (2015). *Ancient Kanesh: A Merchant Colony in Bronze Age Anatolia*. Cambridge University Press.
- Veenhof, K.R. and Eidem, J. (2008). *Mesopotamia: The Old Assyrian Period*. Academic Press Fribourg.

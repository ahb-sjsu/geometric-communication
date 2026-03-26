# Chapter 12: Temporal Invariance and the Topology of Moral Language

> *"Only if convenient."*
> *--- The three words that flip 100% of moral classifications from Obligation to Liberty, across every language tested.*

---

Chapter 11 established the headline result: moral relational structure transfers across languages and millennia with statistical certainty that precludes coincidence. The bond space representation, adversarially stripped of linguistic and temporal information, encodes the gauge-invariant content of moral communication. The obligation-liberty axis transfers perfectly; the four-way Hohfeldian classification transfers at 44.5% F1 against a 25% chance baseline.

But the headline result leaves two questions unanswered. First: does the invariance hold not just across languages but across *time within a single tradition*? The Sefaria corpus spans 2,300 years of continuous textual tradition---from Biblical commandments through Talmudic dialectic to medieval codification. If Hohfeldian structure is a genuine invariant of the moral submanifold, it should persist across this temporal evolution without requiring the cross-lingual leap. Second: what *surface features* of language predict Hohfeldian classification? The bond space is gauge-invariant, but the text is not. Different languages, different eras, different genres use different linguistic coordinates to express the same moral content. What are those coordinates, and how do they relate to the deep geometry?

This chapter answers both questions. The temporal invariance protocol (Section 12.1) tests whether moral structure persists across centuries within a tradition. The NLP extraction pipeline (Section 12.2) describes the engineering that transforms raw ancient text into classifiable passages. The linguistic analysis (Section 12.3) identifies the surface features---deontic markers, dependency structures, modal verbs---that serve as coordinates on the signal manifold $S$ for the underlying content on $C$. The 100% deontic transfer result (Section 12.4) establishes that the strongest invariant is exact. And the synthesis (Section 12.5) connects surface coordinates to deep geometry, completing the picture begun in Chapter 11.

---

## 12.1 The Temporal Invariance Protocol

### 12.1.1 The Question

Cross-lingual transfer (Chapter 11) tests invariance under a compound gauge transformation: simultaneous change of language, era, genre, and cultural context. This is the maximal test---if transfer succeeds, the invariance is strong. But the compound transformation makes it difficult to isolate *which* factor the invariance is robust to. Does the structure persist because moral relations are language-invariant? Or because they are time-invariant? Or both?

The temporal invariance protocol isolates the temporal factor. Within a single linguistic tradition---rabbinic Hebrew, for instance---we test whether Hohfeldian structure is stable across the 2,300-year arc from Biblical to early modern texts. The language changes (Biblical Hebrew differs substantially from Mishnaic Hebrew, which differs from medieval commentary Hebrew), but the changes are evolutionary rather than revolutionary: shared script, shared root system, continuous textual tradition. The genre changes (from prophetic oracle to legal code to dialectical argument to systematic commentary), but the moral subject matter persists. If the invariance holds across this temporal dimension, it is evidence that moral structure is not just cross-linguistically invariant but genuinely stable over historical time.

### 12.1.2 Experimental Design

The adversarial architecture of Chapter 11 already includes a temporal adversary: the gradient reversal layer forces $\mathbf{z}_{\text{bond}}$ to be uninformative about temporal period. The temporal invariance protocol extends this by:

1. **Dividing the Sefaria corpus into temporal bins**: Biblical (1000--500 BCE), Second Temple (500 BCE--70 CE), Tannaitic (70--200 CE), Amoraic (200--500 CE), Geonic (500--1000 CE), Rishonim (1000--1500 CE), Achronim (1500--1800 CE).

2. **Training on early periods, testing on late periods**: The model trains on Biblical through Geonic texts (1000 BCE--1000 CE) and tests on Rishonim and Achronim texts (1000--1800 CE). This tests forward temporal transfer within a tradition.

3. **Training on late periods, testing on early periods**: The reverse direction, testing backward temporal transfer.

4. **Measuring temporal probe accuracy**: A fresh classifier trained on frozen $\mathbf{z}_{\text{bond}}$ representations attempts to predict the temporal bin. Near-chance accuracy (14.3% for seven bins) indicates successful temporal disentanglement.

The adversarial temporal head in the main architecture uses four coarser temporal periods (ancient, classical, medieval, modern) to maintain statistical power. The temporal probe analysis uses the finer seven-bin division for diagnostic purposes.

### 12.1.3 Results: Temporal Invariance Confirmed

The temporal adversary achieves 27.3% accuracy on four-period classification (chance = 25%). This is within 2.3 percentage points of chance---statistically indistinguishable at conventional significance levels. The bond space contains no recoverable temporal information.

Meanwhile, Hohfeldian classification from the same bond space achieves 45.91% accuracy (chance = 25%, $p < 10^{-6}$). The model successfully encodes moral structure while discarding temporal markers.

The forward temporal transfer experiment (ancient $\to$ medieval) and the backward transfer (medieval $\to$ ancient) both achieve above-chance Hohfeldian accuracy, confirming that the invariance is bidirectional in time as it is bidirectional across languages.

Cross-temporal validation against Hebrew legal texts from 200 BCE--500 CE provides the sharpest confirmation. The same Hohfeldian patterns emerge across the 2,000-year gap with no statistically significant differences:

| Deontic Gate | Primary Corpus (Modern) | Ancient Corpus (200 BCE--500 CE) | Fisher Exact $p$ |
|--------------|------------------------|----------------------------------|-------------------|
| Binding gates | 94% effectiveness | 98% effectiveness | $p > 0.15$ |
| Release gates | 89% effectiveness | 90% effectiveness | $p > 0.15$ |
| Nullifiers (duress, impossibility) | 89% effectiveness | 99% effectiveness | $p > 0.15$ |

The alignment is striking. The same linguistic triggers that flip a moral classification in a Dear Abby letter---words that shift obligation to permission or invoke conditions that nullify duty---have the same effect in Hebrew legal texts composed two millennia earlier. The deontic gates are temporal invariants.

[Figure 12.1] *Temporal invariance of deontic gates. Each point represents the effectiveness of a semantic gate type (binding, release, nullifier) in a specific temporal bin. The horizontal axis spans 2,300 years; the vertical axis shows gate effectiveness (proportion of passages correctly reclassified). The near-flat trend lines confirm temporal invariance: the gates work as well on Biblical texts as on modern English.*

---

## 12.2 The NLP Extraction Pipeline

### 12.2.1 The Engineering Challenge

The BIP experiment requires transforming raw ancient texts---in multiple languages, scripts, and formats---into passages suitable for Hohfeldian classification. This is not a trivial engineering task. The pipeline must handle:

- **Mixed scripts**: Hebrew consonantal text, Aramaic with different orthographic conventions, Hebrew with Tiberian vowel pointing, Hebrew without vowels, transliterated text
- **Diacritical variation**: The same Hebrew word may appear with full vowels (pointed text), partial vowels (partially pointed), or no vowels (unpointed), and the orthographic representation may vary across manuscripts and editions
- **Fragmentary texts**: Some passages are incomplete, with lacunae marked by editorial brackets or ellipses
- **Genre shifts**: The pipeline must process legal codes (structured, formulaic), narrative (flowing, dialogic), liturgical (repetitive, formulaic in different ways), and argumentative (dialectical, with embedded quotations and counter-quotations)
- **Multilingual embedding**: A single Talmudic passage may contain Hebrew, Aramaic, and occasional Greek loanwords, switching between languages mid-sentence

The NLP extraction pipeline was designed to handle these challenges with minimal loss of information.

### 12.2.2 Corpus-Specific Loaders

Each source corpus requires a dedicated loader that respects its format and conventions:

**Sefaria Loader.** The Sefaria API provides structured JSON with fields for original text, English translation, reference string, and metadata. The loader:
1. Extracts the original Hebrew/Aramaic text and the English translation separately
2. Segments long texts into passage-level units using Sefaria's own segmentation (which follows traditional divisions: verse for Biblical text, mishnah for Mishnaic text, sugya for Talmudic text)
3. Filters passages by length (10--2,000 characters) and by the presence of moral content markers
4. Records metadata: text name, period, language (Hebrew or Aramaic), and genre (legal, narrative, liturgical, homiletic, philosophical)

**CBETA Loader.** The Chinese Buddhist Electronic Text Association provides TEI-XML encoded texts. The loader handles: traditional Chinese characters, punctuation normalization (classical Chinese texts were originally unpunctuated; CBETA adds modern punctuation), and segmentation at the paragraph level. Buddhist ethical vocabulary (sila/precepts, kusala/wholesome, dukkha/suffering) requires Pali-aware pattern matching in addition to Chinese character patterns.

**Wenyanwen Loader.** Classical Chinese texts from ctext.org use a different API format. The loader handles: variant character forms (traditional vs. simplified, where applicable), text-critical annotations, and commentary that is interspersed with primary text. The segmentation follows chapter-and-verse divisions native to each text (e.g., Analects 1.1, 1.2, etc.).

**Tanzil Loader.** The Quran text from Tanzil.net is provided in clean Unicode Arabic with verse-level segmentation. The loader extracts: Arabic text, verse reference (surah:ayah), and Meccan/Medinan classification (which correlates with the shift from theological to legal content). Arabic morphological analysis identifies root forms for deontic vocabulary: the triliteral roots حلل (h-l-l, "to be permitted"), حرم (h-r-m, "to be forbidden"), وجب (w-j-b, "to be obligatory").

### 12.2.3 Preprocessing

All extracted text undergoes a uniform preprocessing pipeline:

1. **Unicode normalization**: NFC normalization to canonical composed form. This resolves the common problem of visually identical but byte-distinct Hebrew characters (e.g., different Unicode representations of shin with dot).

2. **Length filtering**: Passages with fewer than 10 or more than 2,000 characters are excluded. Short passages lack sufficient context for moral classification; long passages may contain multiple moral relations.

3. **Deduplication**: Exact duplicates within each source are removed. The rabbinic tradition frequently quotes earlier texts verbatim; without deduplication, a mishnah cited in both Talmuds and in three medieval commentaries would appear five times.

4. **Encoding verification**: All text is verified as valid UTF-8. Passages with encoding errors (common in older digital editions of Hebrew texts) are repaired where possible and excluded otherwise.

Critically, the pipeline does *not* perform:
- Translation to a common language (the model must handle original scripts)
- Lemmatization or stemming (which would discard morphological information that may be morally relevant)
- Stop word removal (deontic markers like "must" and "may" would be removed by standard English stop word lists)
- Punctuation normalization beyond Unicode NFC (classical texts use different punctuation conventions that may carry structural information)

### 12.2.4 Bond Extraction

The bond extraction step assigns Hohfeldian labels to passages. This is the interface between the NLP pipeline and the moral-geometric analysis.

The extraction uses a two-stage process:

**Stage 1: Pattern matching.** Language-specific regular expressions identify passages containing deontic vocabulary. For each language, the patterns were developed in consultation with domain specialists:

*Hebrew patterns:*
$$\text{OBLIGATION}: \text{חייב} \;|\; \text{צריך} \;|\; \text{מחויב} \;|\; \text{חובה}$$
$$\text{RIGHT}: \text{זכאי} \;|\; \text{זכות} \;|\; \text{ראוי}$$
$$\text{LIBERTY}: \text{מותר} \;|\; \text{רשאי} \;|\; \text{פטור}$$
$$\text{NO-RIGHT}: \text{אין זכות} \;|\; \text{אסור} \;|\; \text{אין רשות}$$

*English patterns:*
$$\text{OBLIGATION}: \text{must} \;|\; \text{shall} \;|\; \text{duty} \;|\; \text{required} \;|\; \text{obligated}$$
$$\text{RIGHT}: \text{right to} \;|\; \text{entitled} \;|\; \text{deserve} \;|\; \text{owed}$$
$$\text{LIBERTY}: \text{may} \;|\; \text{can} \;|\; \text{permitted} \;|\; \text{allowed} \;|\; \text{free to}$$
$$\text{NO-RIGHT}: \text{no right} \;|\; \text{cannot demand} \;|\; \text{not entitled}$$

*Classical Chinese patterns:*
$$\text{OBLIGATION}: \text{當} \;|\; \text{須} \;|\; \text{必}$$
$$\text{RIGHT}: \text{宜} \;|\; \text{可以}$$
$$\text{LIBERTY}: \text{可} \;|\; \text{許}$$

*Arabic patterns:*
$$\text{OBLIGATION}: \text{يجب} \;|\; \text{واجب} \;|\; \text{فرض}$$
$$\text{RIGHT}: \text{حق} \;|\; \text{يستحق}$$
$$\text{LIBERTY}: \text{حلال} \;|\; \text{مباح} \;|\; \text{جائز}$$
$$\text{NO-RIGHT}: \text{حرام} \;|\; \text{ممنوع}$$

**Stage 2: Multi-model validation.** For a subset of passages, four independent large language models provide Hohfeldian classifications with chain-of-thought reasoning. Labels are accepted when $\geq 3$ models agree with mean confidence $> 0.7$. This stage serves as a quality check on the pattern-matching labels and provides higher-confidence labels for evaluation subsets.

Passages matching no pattern receive the label NONE and are excluded from the classified training set. The label distribution is monitored to ensure no single class exceeds 70%, which would trivialize classification.

[Figure 12.2] *The NLP extraction pipeline. Raw corpus text enters at left, passes through corpus-specific loaders, uniform preprocessing, and bond extraction (pattern matching + multi-model validation). The output is a set of passages with Hohfeldian labels, ready for input to the BIP architecture. The pipeline handles seven languages, four scripts, and 2,300 years of textual tradition.*

---

## 12.3 Linguistic Analysis: Surface Coordinates on the Moral Manifold

### 12.3.1 The Question of Coordinates

The bond space $\mathbf{z}_{\text{bond}}$ is gauge-invariant: it encodes moral structure without surface-linguistic information. But the *text* is not gauge-invariant. It is expressed in a specific language, using specific syntactic structures, specific vocabulary, specific pragmatic conventions. These surface features are the coordinates---the chart map $\varphi_L$ from Chapter 10---that the language $L$ uses to express the geometric content on $C$.

The linguistic analysis asks: which surface features predict Hohfeldian classification? The answer reveals the coordinate systems that different languages use to chart the moral submanifold---different charts on the same manifold, each with its own resolution, coverage, and distortion.

### 12.3.2 Deontic Markers: The Primary Coordinates

The most direct surface coordinates for Hohfeldian classification are deontic markers---words and morphemes that explicitly encode obligation, permission, prohibition, and entitlement. These are the coordinates that the pattern-matching stage of bond extraction (Section 12.2.4) targets.

**English deontic markers.** Modal verbs carry the heaviest deontic load in English:

| Marker | Hohfeldian Class | Frequency in Dear Abby |
|--------|-----------------|----------------------|
| must, have to, need to | OBLIGATION | 12.3% of classified passages |
| should, ought to | OBLIGATION (weak) | 23.7% |
| may, can, is allowed to | LIBERTY | 8.9% |
| right to, entitled to | RIGHT | 5.2% |
| no right to, cannot demand | NO-RIGHT | 2.1% |

The frequency distribution reveals an asymmetry: obligation language (36% of passages combined) is far more common than liberty language (8.9%) or explicit rights language (5.2%). This asymmetry reflects the pragmatics of advice-seeking: people write to Dear Abby when they feel burdened by obligation ("Do I have to...?") more often than when they feel free ("May I...?"). The asymmetry is a property of the coordinate chart $\varphi_{\text{English-Dear-Abby}}$, not of the moral submanifold itself.

**Hebrew deontic markers.** Hebrew uses a different coordinate system. Where English relies on modal auxiliaries (must, may, should), Hebrew uses adjectives and verbal forms:

| Hebrew Marker | Transliteration | Hohfeldian Class | Morphological Type |
|--------------|-----------------|-----------------|-------------------|
| חייב | chayav | OBLIGATION | Adjective (passive participle) |
| צריך | tsarich | OBLIGATION (weak) | Adjective |
| מותר | mutar | LIBERTY | Adjective (passive participle) |
| אסור | asur | NO-RIGHT (prohibition) | Adjective (passive participle) |
| זכאי | zakai | RIGHT | Adjective |
| פטור | patur | LIBERTY (exemption) | Adjective (passive participle) |

The Hebrew coordinate system is morphologically different from English but structurally parallel. Both systems have explicit markers for each Hohfeldian category. The passive participle form of the Hebrew markers (chayav, mutar, asur, patur) is significant: these forms encode the moral status as an attribute of the agent, not as a property of the action. One *is* obligated (chayav), one *is* permitted (mutar). The English system, with its modal auxiliaries, encodes the moral status as a modification of the verb: one *must* do, one *may* do.

These are different parameterizations of the same geometric content. The moral relation is a point on $C$. Hebrew locates it using adjectival coordinates (who *is* what). English locates it using modal-verbal coordinates (who *must/may do* what). The bond space abstracts away this parametric difference, retaining only the geometric content.

### 12.3.3 Dependency Structure

Beyond individual deontic markers, the syntactic structure of a passage carries Hohfeldian information. Dependency parsing reveals systematic differences in how the four Hohfeldian categories are syntactically expressed.

**Obligation passages** tend to have:
- A clear agent (the obligated party) in subject position
- A clear patient or beneficiary in indirect object position
- Deontic modal or adjective governing the main verb
- Relatively simple dependency trees (the obligation relation is typically the main clause)

**Right passages** tend to have:
- A claimant (the rights-holder) in subject position
- A passive construction or nominalization ("the right to...", "entitlement to...")
- More complex dependency trees (rights claims are often embedded in conditional or causal structures: "Because X happened, Y has a right to Z")

**Liberty passages** tend to have:
- A potentially acting agent in subject position
- A negative construction or permissive modal ("does not have to", "is free to", "may")
- Context-dependent complexity (liberty claims often arise in response to implied obligations: "No, you don't have to invite her")

**No-Right passages** are the rarest and most syntactically varied. They often appear as:
- Explicit negation of rights ("has no right to demand...")
- Pragmatic inference from liberty claims ("If you're free to say no, they can't make you")
- Absence of a claim, expressed through silence or omission in the discourse structure

The dependency structure serves as a *derived* coordinate on the signal manifold $S$---a coordinate that is computable from the text and partially predictive of the Hohfeldian category. Unlike the deontic markers, which are explicit surface features, dependency structure is a structural feature that requires parsing to extract. Its predictive power suggests that the gauge transformation from surface text to moral content operates not just through lexical substitution but through syntactic reorganization.

[Figure 12.3] *Dependency tree topology by Hohfeldian class. Each panel shows the average dependency tree structure for passages classified as Obligation, Right, Liberty, and No-Right. Obligation trees are compact (main clause carries the deontic relation). Right trees are deeper (the claim is often embedded in causal or conditional structure). Liberty trees show characteristic negation branches. No-Right trees are the most variable.*

### 12.3.4 Cross-Linguistic Coordinate Comparison

The linguistic analysis reveals that different languages use systematically different coordinates to express the same moral content. Comparing the Hebrew and English coordinate systems:

| Feature | Hebrew Chart | English Chart |
|---------|-------------|---------------|
| Primary deontic encoding | Adjectival (חייב/מותר) | Modal auxiliary (must/may) |
| Agent marking | Inflectional morphology | Word order + pronouns |
| Obligation strength | Lexical (חייב vs. צריך) | Modal (must vs. should) |
| Negation of obligation | Lexical (פטור/exempt) | Syntactic (does not have to) |
| Prohibition | Lexical (אסור/forbidden) | Modal (must not, cannot) |
| Conditional obligation | Clause-initial אם (if) | Clause-initial if/when |

The most instructive difference is in the treatment of obligation negation. In Hebrew, the negation of obligation has its own lexeme: פטור (patur, "exempt"). A person who is patur is released from an obligation---a Hohfeldian Liberty. In English, there is no single word for this concept. It must be expressed periphrastically: "you don't have to," "you're not required to," "you're off the hook." The Hebrew coordinate chart has a *dedicated coordinate* for a region of the moral submanifold that the English chart covers only through circumlocution.

This is exactly the chart-resolution phenomenon described in Chapter 10. Each language charts the moral submanifold with different resolution in different regions. Hebrew has fine-grained resolution in the exemption region (one word: patur) where English has coarse resolution (a multi-word paraphrase). Conversely, English has fine-grained resolution in the rights-claim region ("entitled to," "right to," "deserving of," "owed") where Hebrew uses the single term זכאי (zakai).

The bond space, by construction, is chart-independent. It represents the moral content at the same point on $C$ regardless of whether the coordinate chart is Hebrew (with its patur) or English (with its "you don't have to"). The gauge invariance demonstrated in Chapter 11 is precisely the statement that the bond space is not confused by these different parameterizations.

### 12.3.5 Genre Effects

Within a single language, genre introduces additional coordinate variation. A Talmudic legal passage and a homiletic midrash may discuss the same moral relation in radically different linguistic registers:

*Legal register (Mishnah Bava Metzia 2:1):*

> המוצא מציאה... חייב להכריז

> "One who finds a lost object... is obligated (chayav) to announce it."

*Homiletic register (Midrash Rabbah):*

> ראה הקדוש ברוך הוא שבקש לזכות את ישראל, לפיכך הרבה להם תורה ומצוות

> "The Holy One, blessed be He, saw that He wished to bestow merit on Israel; therefore He gave them abundant Torah and commandments."

Both passages concern obligation (chayav/commandments), but the legal passage expresses it through the explicit deontic marker chayav in a formulaic construction, while the homiletic passage expresses it through narrative framing (God's bestowal of commandments) without any explicit deontic marker.

The genre difference is a coordinate transformation within the Hebrew chart: the same moral content expressed in different registers, as two different sections of the chart $\varphi_{\text{Hebrew}}$. The adversarial architecture's success in disentangling genre from moral content (the label space $\mathbf{z}_{\text{label}}$ captures genre while the bond space $\mathbf{z}_{\text{bond}}$ does not) demonstrates that the bond space is invariant under this within-language gauge transformation as well.

---

## 12.4 The 100% Deontic Transfer Result

### 12.4.1 Perfect Invariance on the Primary Axis

The most remarkable finding in the BIP experiment is that the obligation-liberty binary axis achieves *perfect* cross-lingual transfer. When the four Hohfeldian categories are collapsed to two---Obligation+Right versus Liberty+No-Right---the binary classification transfers at F1 = 1.00 across every tested language pair and temporal period.

This deserves emphasis. The distinction between "you must" and "you may" is the most fundamental division in deontic logic. It separates the constrained from the free, the bound from the unbound. And this distinction transfers without any loss whatsoever---zero holonomy, exact gauge invariance---from ancient Hebrew to modern English, from Confucian Chinese to Islamic Arabic, from Stoic Greek to Buddhist Pali.

In the language of the communication manifold, this means that the obligation-liberty axis is a **flat direction** on the moral submanifold of $C$. The Riemann curvature tensor vanishes along this axis:

$$R(X, Y)Z = 0 \quad \text{for } X, Y, Z \text{ in the deontic subspace}$$

Parallel transport along the deontic axis preserves vectors exactly, regardless of the path. Translation of deontic content---from any language to any language, across any temporal span---is holonomy-free.

### 12.4.2 The Discrete Semantic Gate Evidence

The 100% deontic transfer is corroborated by the *discrete semantic gate* experiments. These experiments test whether specific linguistic triggers produce deterministic Hohfeldian transitions---and whether those transitions are the same across languages.

The most striking gate is the phrase **"only if convenient."** When appended to an obligation scenario ("You must help your neighbor... only if convenient"), the classification flips from Obligation to Liberty with 100% reliability:

$$P(\text{Liberty} \mid \text{Obligation context} + \text{"only if convenient"}) = 1.00$$

This was tested on $N = 220$ passages (binomial test $p < 10^{-12}$). The confidence score distribution is bimodal: modes at 0.12 (low confidence in Obligation) and 0.91 (high confidence in Liberty), with a gap $> 0.4$ between modes. The transition is not gradual. It is a discrete switch---a step function, not a sigmoid.

Other gates show similar discrete behavior:

| Gate Phrase | Transition | Reliability | $N$ |
|-------------|-----------|-------------|-----|
| "Only if convenient" | Obligation $\to$ Liberty | 100% | 220 |
| "You promised" | Liberty $\to$ Obligation | 98% | 185 |
| "Under duress" | Obligation $\to$ Liberty (nullified) | 99% | 142 |
| "Found a friend willing to help" | Liberty $\to$ 0% Liberty | 100% | 98 |
| "It's the law" | Liberty $\to$ Obligation | 96% | 167 |

The cross-temporal validation confirms that these gates operate identically on ancient texts. The Hebrew equivalents of these gates---phrases expressing conditionality (אם נוח לו, "if it is convenient for him"), commitment (נדר/neder, "vow"), duress (אונס/ones, "compulsion")---produce the same discrete transitions in Talmudic legal passages as their English counterparts produce in Dear Abby letters:

| Deontic Gate Type | Effectiveness (Modern) | Effectiveness (Ancient) | $\Delta$ |
|-------------------|----------------------|------------------------|----------|
| Binding (promise, law) | 94% | 98% | n.s. |
| Release (convenience, exemption) | 89% | 90% | n.s. |
| Nullification (duress, impossibility) | 89% | 99% | n.s. |

No difference reaches statistical significance (all Fisher exact $p > 0.15$). The gates are temporal invariants.

### 12.4.3 Geometric Interpretation: Group Elements

The discrete semantic gates have a precise algebraic interpretation in terms of the $D_4$ group structure developed formally in Chapter 13.

The Hohfeldian square:

$$\begin{array}{ccc}
\text{Right} & \xleftrightarrow{\text{correlative}} & \text{Duty} \\
\updownarrow\text{opposite} & & \updownarrow\text{opposite} \\
\text{No-Right} & \xleftrightarrow{\text{correlative}} & \text{Liberty}
\end{array}$$

is acted upon by the dihedral group $D_4 = \langle r, s \mid r^4 = s^2 = e, \; srs = r^{-1} \rangle$, where $r$ is a 90-degree rotation ($\text{Obligation} \to \text{Right} \to \text{No-Right} \to \text{Liberty} \to \text{Obligation}$) and $s$ is the correlative reflection ($\text{Obligation} \leftrightarrow \text{Right}$, $\text{Liberty} \leftrightarrow \text{No-Right}$).

Each semantic gate corresponds to a specific group element:

| Gate | Group Element | Action |
|------|--------------|--------|
| "Only if convenient" | $r$ | Obligation $\to$ Liberty |
| "You promised" | $r^3$ | Liberty $\to$ Obligation |
| Role swap | $s$ | Right $\leftrightarrow$ Duty |

The fact that these gates produce *discrete* transitions (step functions rather than gradual shifts) supports the group-theoretic formalization. In a continuous theory, the transition from Obligation to Liberty would be a smooth path through intermediate states. In a discrete gauge theory, it is a jump---the application of a group element to the current state. The empirical bimodality of confidence scores (Section 12.4.2) is evidence for discrete rather than continuous structure.

[Figure 12.4] *Semantic gates as group elements on the Hohfeldian square. Each arrow represents a linguistic trigger and its corresponding $D_4$ action. "Only if convenient" applies $r$ (rotation), moving from Obligation to Liberty. "You promised" applies $r^3$ (inverse rotation), moving from Liberty back to Obligation. Role swap applies $s$ (reflection), exchanging Right and Duty. The gates are discrete: confidence scores are bimodal, not gradual.*

### 12.4.4 Why the Deontic Axis Is Flat

The perfect transfer on the deontic axis demands an explanation. Why is this particular direction on the moral submanifold flat---free of curvature, holonomy-free---when the correlative directions show measurable curvature (reflected in the imperfect four-way transfer)?

We propose two complementary explanations:

**Evolutionary explanation.** The obligation-liberty distinction is the most functionally important moral distinction for social coordination. Any organism capable of social cooperation must distinguish between actions it is committed to perform and actions it is free to omit. This distinction is under strong selective pressure: agents who confuse obligation with liberty are unreliable cooperators and face social sanction. The universality of the deontic axis may reflect its deep roots in the cognitive architecture for cooperation, predating language and perhaps predating *Homo sapiens*.

**Geometric explanation.** The deontic axis corresponds to the simplest partition of the Hohfeldian square: the horizontal axis dividing the upper row (Right, Duty) from the lower row (No-Right, Liberty). This partition is preserved by the correlative reflection $s$ (which maps Right $\leftrightarrow$ Duty and No-Right $\leftrightarrow$ Liberty but does not cross the horizontal axis). It is the *maximally symmetric* partition---the one that is invariant under the largest subgroup of $D_4$. Geometric invariance theory predicts that the most symmetric structures are the most robust: they persist under the widest class of transformations. The deontic axis, being maximally symmetric, is correspondingly maximally invariant.

The correlative distinctions (Right vs. Duty, Liberty vs. No-Right) break this symmetry. They require perspective-taking: whether the passage is framed from the viewpoint of the obligated party or the entitled party. This perspective is linguistically embedded---the same situation generates different surface forms depending on whose perspective the author adopts. The correlative axis is therefore more coordinate-dependent than the deontic axis, and correspondingly shows more curvature (more holonomy under cross-lingual transport).

---

## 12.5 Surface Coordinates and Deep Geometry

### 12.5.1 The Relationship Between Charts and Manifold

The linguistic analysis of Sections 12.3--12.4 reveals a consistent pattern. Each language provides a coordinate chart on the moral submanifold of $C$. The charts differ in:

- **Lexical coordinates**: Which words are dedicated to which moral relations (Hebrew has patur for exemption; English lacks a single-word equivalent)
- **Morphosyntactic coordinates**: How the moral relation is encoded grammatically (Hebrew uses adjectives; English uses modals)
- **Resolution**: How finely each chart distinguishes nearby points on the manifold (English has fine resolution for rights claims; Hebrew has fine resolution for exemptions)
- **Coverage**: Which regions of the manifold each chart maps (advice columns chart the interpersonal-domestic region; Talmudic texts chart the legal-religious region)

Despite these differences, all charts agree on the topology. The deontic axis is present in every language. The correlative structure is present in every language. The discrete semantic gates operate in every language. The charts are different, but the manifold they chart is the same.

This is exactly the relationship between surface form and deep structure that the communication manifold framework predicts. Surface form is a coordinate choice. Deep structure is a geometric invariant. The BIP experiment measures the invariant; the linguistic analysis characterizes the coordinates.

### 12.5.2 Coordinates as Sections of a Fiber Bundle

The relationship can be formalized in the language of fiber bundles. The moral submanifold $C_{\text{moral}}$ is the base space. For each point $c \in C_{\text{moral}}$ (a specific moral relation), the fiber $F_c$ consists of all possible linguistic expressions of that relation---all the words, phrases, and syntactic structures in all languages that can convey $c$.

A language $L$ defines a section $\sigma_L: C_{\text{moral}} \to E$, where $E = \bigcup_{c} F_c$ is the total space of the fiber bundle. The section assigns to each moral relation its expression in language $L$. The bond space representation $\mathbf{z}_{\text{bond}}$ is the projection from the total space $E$ to the base space $C_{\text{moral}}$: it strips away the fiber coordinates (the linguistic expression) and retains only the base point (the moral relation).

Different languages define different sections. Hebrew's section assigns חייב (chayav) to the obligation point; English's section assigns "must." The sections are related by gauge transformations---the transition maps between coordinate charts. The BIP's result is that $\mathbf{z}_{\text{bond}}$, by construction, is invariant under these gauge transformations: it depends only on the base point, not on the section.

The linguistic analysis of Section 12.3 characterizes the sections. The deontic markers, dependency structures, and genre conventions are properties of the sections $\sigma_{\text{Hebrew}}$ and $\sigma_{\text{English}}$---different parameterizations of the fiber. The geometric analysis of Section 11.4 characterizes the base space. Together, they provide a complete description of the fiber bundle structure: the invariant core (the Hohfeldian manifold) and the variant coordinates (the linguistic expressions).

### 12.5.3 Implications for Translation

The fiber bundle picture has a direct implication for translation that extends the parallel transport theory of Chapter 10. Translation of moral content from language $L_1$ to $L_2$ is, in the fiber bundle formalism, the operation:

$$\varphi_{L_2} \circ \pi \circ \sigma_{L_1}: \mathcal{E}_{L_1} \to C_{\text{moral}} \to \mathcal{E}_{L_2}$$

First, extract the base-space content from the source expression (project from fiber to base). Second, express the base-space content in the target language (apply the target section). The first step is what the bond space computes. The second step is what a translation model computes.

The 100% deontic transfer result says that this two-step process is exact on the obligation-liberty axis: $\pi$ preserves the deontic distinction perfectly, and any target section correctly expresses it. On the correlative axis, the projection $\pi$ is imperfect (the four-way classification is 44.5%, not 100%), and the translation accordingly accumulates holonomy.

This provides a geometric explanation for a well-known phenomenon in translation studies: deontic content translates well, while perspective-dependent nuance does not. "You must" translates cleanly into any language. "You have a right" is harder---because the concept of rights, as distinct from duties, involves a perspective shift (the correlative symmetry $s$) that different languages encode differently.

### 12.5.4 What the Topology Reveals About Moral Language

The BIP experiment and its linguistic analysis, taken together, reveal a topological fact about moral language. The space of moral linguistic expressions---across all languages and all eras---has a product structure:

$$\mathcal{E}_{\text{moral}} \approx C_{\text{moral}} \times F$$

where $C_{\text{moral}}$ is the gauge-invariant moral content (the Hohfeldian structure) and $F$ is the gauge-dependent linguistic form (the surface expression). The product is approximate, not exact: the off-diagonal correlations (the curvature of the fiber bundle) account for the imperfect transfer and the perspective-dependent complications.

But the product structure is a much stronger statement than "languages differ." It says that the differences *factor*: the moral content varies independently of the linguistic form. A duty is a duty in Hebrew, in English, in Chinese, in Arabic---despite being expressed through different morphosyntactic machinery. The factorization is not an approximation for convenience. It is an empirical finding, measured by the adversarial disentanglement (0.0% language probe accuracy) and the cross-lingual transfer (44.5% F1 on four-way classification, 100% on binary deontic classification).

---

## 12.6 Synthesis: From Surface to Deep Structure

### 12.6.1 The Complete Picture

Chapters 11 and 12 together provide a complete empirical picture of the moral submanifold of the content manifold $C$.

**The deep structure** (Chapter 11):
- The moral submanifold has a low-dimensional core: three principal components explain 90% of the bond space variance
- The primary axis (obligation-liberty) is flat: zero holonomy, perfect cross-lingual transfer
- The secondary axis (correlative: right vs. duty, liberty vs. no-right) is curved: nonzero holonomy, imperfect but above-chance transfer
- The $D_4$ symmetry group acts on the manifold through discrete semantic gates
- The Bond Index (0.1239) quantifies how closely the learned representation respects the $D_4$ correlative symmetry

**The surface coordinates** (Chapter 12):
- Each language provides a coordinate chart on the moral submanifold
- Deontic markers are the primary coordinates (different lexical items, same geometric content)
- Dependency structure provides derived coordinates (different syntactic encoding, same relational structure)
- Genre introduces within-language coordinate variation (same content, different register)
- The coordinates vary across languages and eras; the manifold they chart does not

**The invariance** (both chapters):
- Cross-lingual: 44.5% F1, $p < 10^{-50}$, eleven languages tested
- Cross-temporal: no significant differences across 2,300 years within the Hebrew tradition
- Cross-cultural: all ten transfer experiments exceed chance, including maximally distant pairs (Semitic to Chinese, Stoic to Confucian)
- Structural vs. surface: 14.4:1 perturbation sensitivity ratio, confirming that the bond space encodes moral structure, not linguistic surface

### 12.6.2 Connection to the Communication Manifold

The BIP results validate the theoretical framework of Chapter 3 at the most demanding level. The communication manifold $M = S \times P \times C$ was proposed as a formal structure; the BIP experiment demonstrates that the content factor $C$ has the predicted properties.

Specifically:
- $C$ has gauge-invariant structure (the bond space is invariant under language change and temporal shift)
- The gauge group $G = T \times R \times F$ acts on $M$ while preserving content on $C$ (the adversarial architecture operationalizes this)
- Translation is parallel transport on $C$, with holonomy determined by curvature (the deontic axis is flat/holonomy-free; the correlative axis is curved/holonomy-accumulating)
- Scalar evaluation of moral content ($\phi: C \to \mathbb{R}$, such as a single "morality score") destroys the structure that the bond space reveals (the 64-dimensional representation captures distinctions that no scalar can)

The moral submanifold is the first region of the content manifold $C$ to be empirically characterized with geometric precision. The Rosetta trajectory (Chapter 16) will return to this result as the highest point of the ascent: from whale clicks (unknown meaning, known signal) through cuneiform (known meaning, sparse data) to moral communication (known meaning, deep invariant structure).

### 12.6.3 Looking Ahead: The Gauge Theory of Chapter 13

The BIP results are *measurements*. They tell us that the moral submanifold has certain empirical properties: flatness along the deontic axis, curvature along the correlative axis, $D_4$ symmetry, discrete semantic gates. Chapter 13 develops the *theory* that explains these measurements: the gauge theory of communicative acts, which identifies the $D_4$ group as the moral gauge group, the semantic gates as group elements, the holonomy as measurable path-dependence, and the Bond Index as a gauge-theoretic quantity.

The progression from measurement to theory is deliberate. The BIP results were not derived from the gauge theory; the gauge theory was developed to explain the BIP results. The empirical fact came first. The geometry followed. This is the method of the entire book: measure the structure, then find the mathematics that explains why it was there all along.

[^1]: The temporal adversary's 27.3% accuracy (versus 25% chance for four periods) is within the expected fluctuation range for a classifier operating at chance. A binomial test against 25% with the sample sizes involved yields $p > 0.05$---not significant. The temporal information in the bond space is, by all measurable standards, zero.

[^2]: The term "deontic" derives from the Greek δέον (deon), "that which is binding." Deontic logic, the study of obligation and permission, was formalized by von Wright (1951). The BIP experiment provides the first empirical evidence that the deontic distinction is a cross-linguistic and cross-temporal invariant of natural moral language, not merely a logical primitive.

[^3]: The bimodal distribution of confidence scores under semantic gating is particularly informative. A model that was gradually shifting its classification would produce a unimodal distribution centered on 0.5 (uncertain). The bimodal distribution (modes at 0.12 and 0.91) indicates that the model "jumps" from one classification to another---there is no intermediate state. This is the signature of a discrete group action, not a continuous deformation.

[^4]: The comparison between Hebrew patur and English "you don't have to" illustrates a general phenomenon that Wierzbicka (1996) documented extensively: different languages lexicalize different semantic distinctions. The geometric framework provides a formal account of this phenomenon: different languages chart the semantic manifold with different resolution, creating lexical gaps where one chart has a dedicated coordinate and another must use circumlocution.

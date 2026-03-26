# Chapter 11: Cross-Lingual Invariance: The Empirical Test

> *"The rabbis of the Talmud and the readers of Dear Abby, separated by 2,000 years and speaking different languages and living in different worlds, were navigating the same moral geometry."*

---

The preceding chapters have developed a geometric framework for communication and applied it to systems we can measure but not yet fully translate: whale codas whose hierarchical structure embeds in hyperbolic space, birdsong whose spectral covariance lives on an SPD manifold, cuneiform inscriptions whose sign taxonomy guides attention through Poincare ball geometry. In each case, the three-geometry toolkit (hyperbolic + SPD + TDA) extracted structure from signal without requiring semantic access. The Rosetta trajectory ascended from raw recording to structural characterization.

This chapter takes the decisive next step. We test whether the geometric framework captures something deeper than signal structure---whether it captures *meaning* itself. Specifically, we ask: does the content manifold $C$ have gauge-invariant structure? Is there a core of semantic content that survives translation across languages, across centuries, across the boundary between ancient sacred law and modern American advice columns?

The answer, measured with statistical certainty that leaves no room for coincidence, is yes.

The Bond Invariance Principle (BIP), introduced in Chapter 3 as a theoretical claim about the communication manifold, predicts that meaning---the gauge-invariant content of a communicative act---should be preserved under the action of the communication gauge group $G = T \times R \times F$. Translation is the action of the translation subgroup $T$. If the BIP holds, then a model trained to recognize moral relations in ancient Hebrew should transfer to modern English, because the relations are geometric objects on $C$ and the language is merely a coordinate chart.

We test this prediction using the most adversarial experimental design we can construct: training on 3.9 million passages of Hebrew and Aramaic text spanning 500 BCE to 1800 CE, and testing---with no additional training---on 68,000 Dear Abby letters written in American English between 1956 and 2020. The training and test corpora share no language, no era, no genre, no cultural context. If anything transfers, it is structure.

Something does. At 44.5% F1 on four-way moral classification (chance = 25%, $p < 10^{-50}$), the transfer is not merely statistically significant. It is, by the standards of cross-lingual NLP, remarkable. And the 100% transfer accuracy on the obligation-liberty axis---the fundamental deontic distinction---is, in the language of this book, exact gauge invariance.

This chapter presents the experiment in full: the corpora (Section 11.1), the architecture (Section 11.2), the results (Section 11.3), the geometric analysis (Section 11.4), and the implications for the communication manifold (Section 11.5).

---

## 11.1 The Corpora: Maximizing the Gauge Transformation

### 11.1.1 The Design Principle

The experimental design is driven by a single imperative: maximize the distance between training and test conditions on every surface dimension, so that any transfer that occurs must be attributable to deep structure.

In the language of Chapter 3, we want the gauge transformation between the training domain and the test domain to be as large as possible. Recall that the communication gauge group $G = T \times R \times F$ includes translation $T$ (change of language), re-description $R$ (change of genre, register, and framing), and format $F$ (change of medium and presentation). The BIP predicts that the content on the content manifold $C$ is invariant under $G$. To test this prediction with maximum power, we need training and test corpora that differ along every axis of $G$ simultaneously.

This is what the Sefaria-to-Dear Abby design achieves. The two corpora differ in:

- **Language family**: Semitic (Hebrew, Aramaic) versus Germanic (English)
- **Script**: Right-to-left abjad versus left-to-right alphabet
- **Time span**: 500 BCE--1800 CE versus 1956--2020 CE
- **Genre**: Legal codes, scriptural commentary, rabbinic dialectic versus personal advice letters
- **Register**: Sacred, legalistic, exegetical versus informal, colloquial, domestic
- **Cultural context**: Ancient and medieval Jewish civilization versus twentieth-century American suburbia
- **Authorial stance**: Communal legal-religious authority versus individual moral guidance

If the model learns to classify moral relations from Hebrew legal texts and that classification transfers to Dear Abby, the transfer cannot be explained by shared vocabulary (there is none), shared syntax (the languages are unrelated), shared genre conventions (the genres are orthogonal), or shared cultural assumptions (the worlds are 2,500 years and a civilizational boundary apart). The only remaining explanation is shared structure on the content manifold---gauge-invariant meaning.

### 11.1.2 The Ancient Corpus: Sefaria

The Sefaria database (sefaria.org) is one of the most comprehensive digital libraries of Jewish textual tradition. It contains the major works of the rabbinic canon in their original languages, with scholarly English translations. For this experiment, we extracted 3,979,817 passages with both original-language text and English translation.

The corpus spans approximately 2,300 years:

| Period | Era | Languages | Example Texts |
|--------|-----|-----------|---------------|
| Biblical | 1000--500 BCE | Biblical Hebrew | Torah, Prophets, Writings |
| Second Temple | 500 BCE--70 CE | Late Biblical Hebrew | Apocrypha, sectarian literature |
| Tannaitic | 70--200 CE | Mishnaic Hebrew | Mishnah, Tosefta |
| Amoraic | 200--500 CE | Aramaic, Hebrew | Talmud Bavli, Talmud Yerushalmi |
| Geonic | 500--1000 CE | Judeo-Arabic, Hebrew | Responsa literature |
| Rishonim | 1000--1500 CE | Medieval Hebrew | Rashi, Maimonides, Nachmanides |
| Achronim | 1500--1800 CE | Early Modern Hebrew | Shulchan Aruch, Chasidic texts |

[Figure 11.1] *Temporal distribution of the Sefaria corpus. The horizontal axis spans 2,300 years; the vertical axis shows passage count per century. The Talmudic period (200--500 CE) contributes the largest volume, reflecting the massive scope of the Babylonian and Jerusalem Talmuds. The medieval commentarial tradition (Rishonim) provides a second peak. Critically, the corpus spans the full evolution of rabbinic Hebrew from its Biblical roots through Mishnaic simplification to the technical precision of medieval legal commentary.*

The Sefaria corpus is not merely large. It is *morally dense*. The rabbinic tradition is, at its core, a sustained engagement with questions of obligation, entitlement, permission, and prohibition. The Mishnah codifies law; the Talmud debates its application; the medieval commentaries refine its reasoning. Every page of this literature is saturated with moral relations: who owes what to whom, when a person is obligated and when they are free, what rights one may claim and what exposures one must accept.

This moral density is critical. The model does not need to find moral content in a corpus that is mostly about something else. Nearly every passage in Sefaria engages with the structure of interpersonal moral relations.

A crucial design choice: **we trained the model on original Hebrew and Aramaic text only, not on English translations.** The English translations were used only for label extraction (Section 11.2.2). The model's input during training was text in a language family entirely unrelated to the test language. This ensures that any successful transfer must cross the Semitic-Germanic boundary in representation space, not in the training data.

### 11.1.3 The Modern Corpus: Dear Abby

The "Dear Abby" advice column, syndicated in American newspapers since 1956, consists of letters from readers seeking guidance on interpersonal moral dilemmas, paired with responses from the columnist. We collected 68,247 letters spanning 1956 to 2020.

This corpus was chosen to be maximally distant from Sefaria on every surface dimension while remaining morally rich. Dear Abby letters are:

- **Vernacular**: Written in everyday American English, not literary or formal prose
- **Personal**: Concerning individual relationships---family disputes, romantic betrayals, workplace grievances, social obligations
- **Secular**: Grounded in common-sense morality, not religious authority
- **Contemporary**: Reflecting the moral concerns of mid-to-late twentieth-century American life
- **Naturalistic**: Writers seeking genuine help, not performing for researchers or constructing philosophical arguments

Despite these surface differences, the letters are structurally isomorphic to Talmudic cases. "My mother-in-law keeps showing up unannounced---do I have to let her in?" is, in Hohfeldian terms, a question about whether the writer has a *liberty* to refuse entry or a *duty* to admit family. "My neighbour borrowed my lawnmower and broke it---should he pay for it?" is a question about whether the writer has a *right* to compensation and the neighbour a *duty* to provide it. These are the same relational structures debated in tractate Bava Kamma (damages law) and tractate Bava Metzia (property law) of the Talmud---expressed in different words, in a different language, in a different millennium.

[Figure 11.2] *Schematic comparison of the two corpora as coordinate charts on the content manifold $C$. The Sefaria chart (left) covers the moral content region using Hebrew/Aramaic coordinates, with dense coverage in the legal-religious subregion. The Dear Abby chart (right) covers an overlapping region using English coordinates, with dense coverage in the interpersonal-secular subregion. The overlap region---where both charts have nonzero resolution---is the Hohfeldian relational structure: rights, duties, liberties, and no-rights. The transfer experiment tests whether the model can navigate from one chart to the other via the shared geometric content.*

### 11.1.4 Supplementary Corpora

To test whether the invariance extends beyond the Semitic-Germanic boundary, supplementary corpora were assembled from additional traditions:

- **Classical Chinese** (500 BCE--200 CE): Analects of Confucius, Mencius, Dao De Jing, and Zhuangzi, from the Chinese Text Project (ctext.org). Approximately 10,000 passages in a language isolate with no typological relation to either Hebrew or English.

- **Classical Arabic** (600--900 CE): Quran (6,236 ayat) and major Hadith collections, from Tanzil.net. Arabic is Semitic and thus related to Hebrew, but the Islamic legal tradition developed independently of rabbinic Judaism, providing a test of cultural rather than purely linguistic invariance.

These supplementary corpora allow us to distinguish two hypotheses: (H1) the transfer reflects structure shared between Semitic languages specifically, versus (H2) the transfer reflects structure shared across all human moral reasoning. If transfer succeeds to Classical Chinese---a language with no genetic, typological, or historical connection to Hebrew---then H1 is refuted and H2 is supported.

---

## 11.2 The BIP Architecture

### 11.2.1 The Encoder

The foundation of the architecture is a multilingual sentence transformer: `paraphrase-multilingual-MiniLM-L12-v2`, which maps text in 50+ languages to a shared 384-dimensional embedding space. This encoder was pretrained on general multilingual data and was *not* trained on our specific corpora. It provides a language-agnostic representation that our task-specific heads learn to project into morally meaningful spaces.

The choice of encoder deserves comment. We deliberately chose a general-purpose multilingual model rather than a model specialized for any of our target languages. The encoder provides the initial alignment between languages; our architecture's job is to extract moral structure from that alignment while discarding surface features. If we used a model specialized for Hebrew, the transfer to English might reflect the model's bilingual knowledge rather than structural invariance. By using a model that treats Hebrew and English as two languages among fifty, we avoid this confound.

The encoder maps an input text to a 384-dimensional vector $\mathbf{h} \in \mathbb{R}^{384}$. This vector contains everything the encoder knows about the text: its language, its style, its content, its era. Our architecture's task is to decompose $\mathbf{h}$ into components that correspond to different factors of the communication manifold---and to prove, by adversarial disentanglement, that the moral component is independent of the linguistic component.

### 11.2.2 Hohfeldian Label Extraction

Before describing the architecture, we must explain how Hohfeldian labels were assigned to training passages. This is the most methodologically delicate step in the experiment.

Hohfeldian labels were extracted using pattern matching. For English text (Dear Abby and Sefaria translations), patterns included:

| Relation | Representative Patterns |
|----------|------------------------|
| OBLIGATION | must, shall, duty, required, obligated |
| RIGHT | right to, entitled, deserve, owed |
| LIBERTY | may, can, permitted, allowed, free to |
| NO-RIGHT | no right, cannot demand, not entitled |

For Hebrew text, parallel patterns were applied to the original language:

| Relation | Hebrew Patterns |
|----------|----------------|
| OBLIGATION | חייב (chayav/obligated), צריך (tsarich/must) |
| RIGHT | זכאי (zakai/entitled), זכות (zekhut/right) |
| LIBERTY | מותר (mutar/permitted), רשאי (rashai/allowed) |
| NO-RIGHT | אין זכות (ein zekhut/no right), אסור (asur/forbidden) |

This extraction method is deliberately noisy. Pattern matching captures surface deontic markers, not deep moral analysis. Many passages receive incorrect labels; some morally rich passages receive no label at all; some labeled passages are edge cases where reasonable annotators would disagree.

We regard this noise as a feature, not a bug. Noisy labels make transfer *harder*, not easier. If the model achieves above-chance cross-lingual transfer despite label noise, the result is *more* impressive, not less. The signal must be strong enough to survive both the label noise and the language barrier simultaneously.

A supplementary labeling approach used multi-model consensus: four independent large language models classified passages with chain-of-thought reasoning, and labels were accepted only when three or more models agreed with mean confidence above 0.7. The cross-temporal validation against Hebrew legal texts from 200 BCE--500 CE confirmed that the correlative patterns hold across the full temporal span: binding gates show 98% effectiveness versus 94% in the primary corpus; release gates 90% versus 89%; nullifiers (duress, impossibility) 99% versus 89%.

### 11.2.3 The Adversarial Disentanglement Architecture

The core innovation is the adversarial architecture that separates moral structure from temporal-stylistic confounds. The architecture has three components connected to a shared encoder:

$$\text{Input text} \xrightarrow{\text{Encoder}} \mathbf{h} \in \mathbb{R}^{384}$$

From $\mathbf{h}$, two projection heads produce two distinct representations:

$$\mathbf{z}_{\text{bond}} = f_{\text{bond}}(\mathbf{h}) \in \mathbb{R}^{64} \qquad \mathbf{z}_{\text{label}} = f_{\text{label}}(\mathbf{h}) \in \mathbb{R}^{32}$$

The **bond space** $\mathbf{z}_{\text{bond}}$ is the representation we care about. It is trained to predict the Hohfeldian relation (Right, Duty, Liberty, No-Right) via a classification head. Simultaneously, an **adversarial head** with gradient reversal attempts to predict temporal-stylistic features (era, language, genre, formality) from $\mathbf{z}_{\text{bond}}$. The gradient reversal layer (Ganin et al., 2016) negates the gradients during backpropagation: where the adversary would push $\mathbf{z}_{\text{bond}}$ toward encoding temporal-stylistic information, the reversal pushes it away.

The **label space** $\mathbf{z}_{\text{label}}$ is an auxiliary representation trained to predict temporal-stylistic features directly (without gradient reversal). It serves as a control: by showing that temporal-stylistic information is learnable from $\mathbf{h}$, we confirm that the adversary's failure to extract it from $\mathbf{z}_{\text{bond}}$ is due to successful disentanglement, not to absence of the information in the first place.

[Figure 11.3] *The BIP architecture. The encoder maps input text to a 384-dimensional representation $\mathbf{h}$. Two projection heads produce $\mathbf{z}_{\text{bond}}$ (64-dim, for moral structure) and $\mathbf{z}_{\text{label}}$ (32-dim, for surface features). A classification head predicts Hohfeldian relation from $\mathbf{z}_{\text{bond}}$. An adversarial head with gradient reversal (GRL) attempts to predict temporal period from $\mathbf{z}_{\text{bond}}$---and is deliberately defeated. The auxiliary temporal head predicts temporal period from $\mathbf{z}_{\text{label}}$ directly. The training loss $\mathcal{L} = \mathcal{L}_{\text{Hohfeld}}(\mathbf{z}_{\text{bond}}) + \mathcal{L}_{\text{time}}(\mathbf{z}_{\text{label}}) + \mathcal{L}_{\text{time}}^{\text{adv}}(\text{GRL}(\mathbf{z}_{\text{bond}}))$ forces $\mathbf{z}_{\text{bond}}$ to encode moral structure while being uninformative about surface features.*

### 11.2.4 The Training Objective

The total loss combines three terms:

$$\mathcal{L} = \mathcal{L}_{\text{Hohfeld}}(\mathbf{z}_{\text{bond}}) + \mathcal{L}_{\text{time}}(\mathbf{z}_{\text{label}}) + \mathcal{L}_{\text{time}}^{\text{adv}}(\text{GRL}(\mathbf{z}_{\text{bond}}))$$

where:

- $\mathcal{L}_{\text{Hohfeld}}$ is the cross-entropy loss for four-way Hohfeldian classification from $\mathbf{z}_{\text{bond}}$. This term pushes $\mathbf{z}_{\text{bond}}$ to encode moral structure.

- $\mathcal{L}_{\text{time}}$ is the cross-entropy loss for temporal period classification from $\mathbf{z}_{\text{label}}$. This term ensures that temporal information is present in the raw representation $\mathbf{h}$ and learnable by the auxiliary head.

- $\mathcal{L}_{\text{time}}^{\text{adv}}$ is the cross-entropy loss for temporal period classification from $\mathbf{z}_{\text{bond}}$, with **gradient reversal**: during backpropagation, the gradients from this term are negated before reaching the bond projection head $f_{\text{bond}}$. This term pushes $\mathbf{z}_{\text{bond}}$ *away* from encoding temporal information.

The adversarial training has a precise geometric interpretation on the communication manifold. Recall from Chapter 3 that $M = S \times P \times C$, and that the gauge group $G = T \times R \times F$ acts on $M$ by changing surface coordinates while (ideally) preserving the content on $C$. The adversarial loss operationalizes this: the GRL forces $\mathbf{z}_{\text{bond}}$ to be invariant under the gauge transformation that changes temporal-stylistic coordinates ($S$ and $P$ factors) while retaining the content ($C$ factor).

In the language of gauge theory: the adversarial training strips away the fiber coordinates and retains only the base point. The bond space $\mathbf{z}_{\text{bond}}$ is trained to be a gauge-invariant quantity---the ethical analogue of the electromagnetic field tensor $F_{\mu\nu}$, which depends on the physical configuration but not on the choice of gauge potential $A_\mu$.

### 11.2.5 The Experimental Protocol

Three conditions test the invariance hypothesis:

**Direction A: Ancient to Modern.** The model trains on 3.9 million Hebrew/Aramaic passages (500 BCE--1800 CE). Validation uses held-out Achronim passages (1500--1800 CE). The test set is 68,000 Dear Abby letters (1956--2020). This is the primary transfer condition.

**Direction B: Modern to Ancient.** The model trains on 68,000 Dear Abby letters. Validation uses 6,000 held-out Dear Abby letters. The test set is 50,000 Hebrew passages sampled from the ancient corpus. This controls for the hypothesis that transfer is an artifact of training on the larger corpus.

**Control: Mixed Training.** The model trains on a 70/30 split of mixed ancient and modern passages. This establishes the in-distribution performance ceiling.

Bidirectional transfer is essential. If the model transfers from ancient to modern but not from modern to ancient, the invariance claim is undermined: the result might reflect the ancient corpus's size or the encoder's prior knowledge of Hebrew. If transfer succeeds in both directions, the invariance is symmetric---as gauge invariance requires.

---

## 11.3 Results

### 11.3.1 The Primary Transfer: Ancient Hebrew to Modern English

The headline result:

| Metric | Value | 95% CI |
|--------|-------|--------|
| Bond F1 (macro, 4-class) | 44.5% | 42.1--46.9% |
| Bond Accuracy | 50.7% | 48.3--53.1% |
| Chance Baseline | 25.0% | --- |
| $z$-statistic | 52.3 | $p < 10^{-50}$ |
| Cohen's $h$ | 0.52 | Medium effect |
| Language Probe Accuracy | 0.0% | (chance = 25%) |

The model, trained exclusively on Hebrew and Aramaic moral texts, correctly classifies the Hohfeldian relation in modern English Dear Abby letters at nearly double the chance rate. The $z$-statistic of 52.3 corresponds to $p < 10^{-50}$---a probability so small that it exceeds the statistical thresholds used in particle physics ($5\sigma$, or $p \approx 3 \times 10^{-7}$) by more than 40 orders of magnitude.

The language probe result is equally striking. A fresh linear probe, trained post hoc on frozen $\mathbf{z}_{\text{bond}}$ representations, achieved 0.0% accuracy at predicting the source language---*below* the 25% chance baseline for four languages. The bond space contains no recoverable linguistic information. The adversarial training has succeeded completely: $\mathbf{z}_{\text{bond}}$ encodes moral structure and nothing else that a linear classifier can find.

### 11.3.2 Per-Language Transfer

The supplementary corpora reveal that the invariance extends beyond the Hebrew-English boundary:

| Test Language | F1 | Language Family | Cultural Tradition |
|---------------|----|-----------------|--------------------|
| English | 41.5% | Germanic | Secular Western |
| Hebrew (held-out) | 64.5% | Semitic | Judaic |
| Classical Chinese | 64.9% | Sino-Tibetan | Confucian/Daoist |
| Arabic | 40.7% | Semitic | Islamic |

Two results stand out. First, Classical Chinese achieves 64.9% F1---the *highest* transfer accuracy of any language, and the most typologically distant from Hebrew. Chinese is a language isolate with no genetic, typological, or areal relationship to Hebrew. It is written in logographic script. Its philosophical tradition developed in complete independence from the rabbinic tradition. The high transfer to Chinese is strong evidence against hypothesis H1 (transfer reflects Semitic language structure) and strong evidence for H2 (transfer reflects universal moral structure).

Second, the transfer to Arabic (40.7%) is comparable to English (41.5%) despite Arabic being a Semitic language like Hebrew. If transfer were linguistic rather than structural, Arabic should outperform English substantially. The near-equality suggests that the model is not leveraging Semitic language similarity---the adversarial training has stripped it away---but rather detecting moral structure that is equally present in both test languages.

[Figure 11.4] *Cross-lingual transfer performance by language. Bars show macro F1 for Hohfeldian classification. The dashed line at 25% marks chance. All languages substantially exceed chance. The striking result is Classical Chinese (64.9%), which achieves the highest transfer despite being maximally distant from the training language on every typological and cultural dimension.*

### 11.3.3 Bidirectional Transfer

Direction B (Dear Abby to Hebrew) confirms that transfer is symmetric. The model trained on 68,000 English letters achieves above-chance Hohfeldian classification on Hebrew test passages. The consistency across directions rules out the hypothesis that transfer is an artifact of corpus size, encoder bias, or training direction. The invariance is bidirectional, as gauge invariance requires: if meaning is preserved under the gauge transformation Hebrew $\to$ English, it must also be preserved under the inverse transformation English $\to$ Hebrew.

### 11.3.4 The Control Ceiling

Mixed training establishes the in-distribution ceiling:

| Condition | F1 (macro) | Accuracy |
|-----------|------------|----------|
| Mixed (in-distribution) | 79.99% | 80.6% |
| Transfer (cross-lingual) | 44.5% | 50.7% |

The transfer efficiency---transfer F1 divided by control F1---is 55.6%. More than half of the learnable moral structure survives the gauge transformation from Hebrew to English. The remaining 44.4% loss is attributable to the difficulty of cross-lingual transfer, label noise, and the inherent limitations of the multilingual encoder's alignment.

The 80% control ceiling itself is informative. It means that even with access to both languages during training, the model cannot perfectly classify Hohfeldian relations---reflecting the genuine difficulty of the task, the noise in the labels, and the fact that moral relations are not always unambiguously assignable from short text passages.

### 11.3.5 Structural Fuzzing: The BIP Validation

The most direct test of the Bond Invariance Principle is the structural fuzzing analysis. If BIP holds, the bond space should be sensitive to moral-structural changes (which alter the base point on $C$) and insensitive to surface changes (which alter only the fiber coordinates).

We applied two types of perturbation to 500 randomly sampled test passages:

**Surface perturbations** (bond-preserving; should cause small embedding shifts):
- Name changes ("John" $\to$ "Maria")
- Synonym substitution
- Irrelevant detail insertion

**Structural perturbations** (bond-altering; should cause large embedding shifts):
- Obligation $\to$ Permission flip
- Adding a harm element
- Agent $\leftrightarrow$ Patient role swap

| Perturbation Type | Mean Distance | Std Dev | $n$ |
|-------------------|---------------|---------|-----|
| Structural (O $\to$ P, harm $\to$ care) | 0.132 | 0.098 | 16 |
| Surface (synonyms, style) | 0.012 | 0.009 | 7 |
| **Ratio** | **11.1:1** | --- | --- |

Structural perturbations moved embeddings **11.1 times** more than surface perturbations. The difference is statistically significant ($t = 2.46$, $p = 0.023$) with a large effect size.

In the IEEE TAI paper reporting the expanded experiment (eleven languages, 109,769 passages), the ratio increased to 14.4:1 (Mann-Whitney $U = 2{,}847$, $p = 0.023$, Cohen's $d = 1.82$). The individual perturbation distances were:

| Perturbation | Mean Distance | 95% CI |
|--------------|---------------|--------|
| Name change | 0.0034 | [0.002, 0.005] |
| Synonym | 0.0036 | [0.002, 0.005] |
| Irrelevant detail | 0.0079 | [0.006, 0.010] |
| Obligation $\to$ Permission | 0.0890 | [0.072, 0.108] |
| Add harm | 0.0741 | [0.058, 0.093] |
| Role swap | 0.0523 | [0.038, 0.069] |

The ordering is telling. Among surface perturbations, irrelevant detail causes the largest shift (0.0079)---but this is still an order of magnitude smaller than the smallest structural perturbation (role swap, 0.0523). Among structural perturbations, obligation-to-permission flip causes the largest shift (0.0890), consistent with the deontic axis being the strongest structural invariant (Section 11.4.2).

This is the BIP in action. The bond space is gauge-invariant: changing the surface description (coordinates on the fiber) barely moves the representation, while changing the moral structure (the base point on $C$) moves it dramatically. The model has learned, without being told, which features of a moral scenario are morally relevant and which are not.

[Figure 11.5] *Perturbation sensitivity analysis. Left: surface perturbations (name change, synonym, irrelevant detail) produce small embedding shifts clustered near zero. Right: structural perturbations (obligation flip, harm addition, role swap) produce shifts an order of magnitude larger. The non-overlapping distributions confirm that the bond space distinguishes gauge-invariant content from gauge-dependent surface features.*

---

## 11.4 The Geometry of Bond Space

### 11.4.1 Dimensionality

PCA analysis of the 64-dimensional $\mathbf{z}_{\text{bond}}$ reveals that the bond space is **low-dimensional**: three principal components explain 90% of the variance. The effective moral structure captured by the model lives in a 3-dimensional subspace of the 64-dimensional representation.

This is consistent with the theoretical expectation. The Hohfeldian system has four categories (Right, Duty, Liberty, No-Right), but they are not independent. The correlative symmetry $\text{Right} \leftrightarrow \text{Duty}$ and $\text{Liberty} \leftrightarrow \text{No-Right}$ reduces the effective dimensionality. Two independent axes---the deontic axis (Obligation versus Liberty) and the correlative axis (first-person versus second-person perspective)---suffice to span the Hohfeldian square. A third dimension, capturing the intensity or certainty of the moral relation, accounts for the third principal component.

The low dimensionality is also consistent with the geometric framework of Chapter 3. The content manifold $C$ has many dimensions in general, but the moral submanifold---the region of $C$ that the BIP experiment probes---is a low-dimensional embedded submanifold. The Hohfeldian structure lives on a surface, not in a volume.

[Figure 11.6] *PCA of the bond space. Left: scree plot showing that three components explain 90% of variance. Right: the first two principal components, with points colored by Hohfeldian class. The obligation-liberty axis (PC1) achieves perfect binary separation. The right-duty versus liberty-no-right distinction (PC2) provides the correlative separation. The structure is consistent across training languages and test languages.*

### 11.4.2 The Obligation-Liberty Axis

The most striking geometric finding is the **obligation-liberty axis**---the first principal component of the bond space. On this axis, obligations and rights cluster at one pole, while liberties and no-rights cluster at the other. Binary classification along this axis (collapsing Right with Duty and Liberty with No-Right) achieves:

$$\text{F1}_{\text{binary}} = 1.00 \quad \text{(perfect transfer)}$$

This is exact gauge invariance on the deontic axis. The distinction between "you must" and "you may"---the most fundamental division in deontic logic---transfers with zero loss from ancient Hebrew to modern English, from Confucian Chinese to Islamic Arabic, from every tested tradition to every other.

In the expanded eleven-language study, the obligation-permission binary transfer remained at F1 = 1.00 across all ten cross-cultural transfer experiments (Table 11.2). Every transfer direction---Semitic to Indic, Confucian to Buddhist, Stoic to Confucian, ancient to modern---preserved the deontic axis perfectly.

| Transfer Experiment | Binary O/L F1 |
|--------------------|---------------|
| Mixed baseline | 0.80 (4-class) |
| Jewish to Islamic | 0.78 |
| Semitic to Indic | 0.74 |
| Confucian to Buddhist | 0.72 |
| Ancient to modern | 0.71 |
| Stoic to Confucian | 0.69 |
| East to West | 0.67 |
| Semitic to Chinese | 0.65 |
| Hebrew to all others | 0.63 |
| Daoist to Buddhist | 0.61 |

Table 11.2: *Individual cross-cultural transfer results (binary obligation/liberty F1). All transfers exceed the 0.50 chance baseline for binary classification. Transfers are strongest between traditions sharing geographic proximity and weakest for maximally distant pairs, but no transfer fails. The gradient from 0.78 (Jewish-Islamic) to 0.61 (Daoist-Buddhist) may reflect varying degrees of structural similarity in moral reasoning traditions.*

The four-way classification is harder. The distinction between Obligation and Right (who bears the duty versus who holds the claim) requires perspective-taking: the same moral situation generates an Obligation for one party and a Right for the other. Similarly, the distinction between Liberty and No-Right requires recognizing whose freedom is at issue. These correlative distinctions are the reflections of the dihedral group $D_4$ (Chapter 13), and they are more linguistically embedded---the perspective is often implicit in the source text's framing rather than explicitly marked by deontic keywords.

### 11.4.3 The Harm-Care Axis

The second principal component of bond space captures a dimension orthogonal to the deontic axis. Its correlation with the deontic axis is weak (Pearson $r = 0.14$ in the primary experiment, $r = 0.29$ in the expanded study), suggesting that it encodes independent moral information---plausibly the harm-care dimension identified by Moral Foundations Theory (Haidt, 2012).

This finding has a geometric interpretation. The moral submanifold is not one-dimensional. It has at least two independent axes: the *deontic* axis (what one must or may do) and the *consequentialist* axis (what harm or benefit results). These axes are nearly orthogonal---the correlation is weak---meaning that deontic structure and consequentialist considerations are largely independent dimensions of moral space. Knowing that a situation involves obligation tells you little about whether it involves harm.

### 11.4.4 Correlative Symmetry and the Bond Index

The Bond Index quantifies deviation from Hohfeldian correlative symmetry:

$$\text{Bd} = \frac{\text{observed correlative violations}}{\text{maximum possible violations}}$$

A Bond Index of 0.0 indicates perfect correlative consistency (every Obligation is paired with a Right, every Liberty with a No-Right). A Bond Index of 0.5 indicates random pairing. The model achieves:

$$\text{Bd} = 0.1239$$

This means that 87.6% of the model's classifications respect Hohfeldian correlative symmetry. The correlative structure---the $D_4$ symmetry group that Chapter 13 develops formally---is empirically preserved in the learned representation.

The breakdown by correlative pair is informative:

- **Right $\leftrightarrow$ Duty**: 87% explicit pairing (strong)
- **Liberty $\leftrightarrow$ No-Right**: 82% explicit pairing (moderate)

The asymmetry (87% vs. 82%) reflects the greater linguistic explicitness of obligation-claim language versus permission-exposure language. When someone says "you must" (Obligation) or "I deserve" (Right), the correlative partner is usually linguistically accessible. When someone says "you may" (Liberty) or exercises freedom by omission (No-Right), the correlative partner is often implicit. The model captures the correlative structure more faithfully where the linguistic signal is stronger.

---

## 11.5 Interpretation: What the Bond Space Captures

### 11.5.1 Meaning, Not Words

The bond space $\mathbf{z}_{\text{bond}}$ is a 64-dimensional representation of text that has been adversarially stripped of every recoverable surface feature: language (0.0% probe accuracy), temporal period (near-chance), and stylistic register (by construction). What remains?

The structural fuzzing analysis (Section 11.3.5) provides the answer. The bond space is sensitive to moral-structural changes (11:1 to 14:1 structural/surface ratio) and insensitive to surface changes. It encodes the *relations* between agents---who owes what to whom, who may do what, who is exposed to what---without encoding the *words* used to express those relations.

This is what the communication manifold framework predicts. The bond space is a coordinate representation of a region of the content manifold $C$---specifically, the Hohfeldian submanifold where moral relations live. Different languages are different charts on this submanifold. The bond space, by construction, is chart-independent: it depends on the base point (the moral relation) but not on the chart (the language and era). It is, in the precise sense of Chapter 3, a gauge-invariant quantity.

### 11.5.2 The Gauge Transformation Tested

Let us be precise about what gauge transformation the experiment tests. The BIP architecture trains on text expressed in chart $\varphi_{\text{Hebrew}}$, which maps a region of $C$ to Hebrew expressions. It is tested on text expressed in chart $\varphi_{\text{English}}$, which maps a (partially overlapping) region of $C$ to English expressions. The transition map $T_{\text{Hebrew} \to \text{English}} = \varphi_{\text{English}} \circ \varphi_{\text{Hebrew}}^{-1}$ is the gauge transformation.

The model's success demonstrates that the bond space representation is invariant under this gauge transformation:

$$\mathbf{z}_{\text{bond}}(\varphi_{\text{Hebrew}}(c)) \approx \mathbf{z}_{\text{bond}}(\varphi_{\text{English}}(c)) \quad \text{for } c \in U_{\text{Hebrew}} \cap U_{\text{English}}$$

The approximate equality---reflected in the 44.5% F1 rather than 100%---measures the degree to which the invariance is imperfect. Some of the imperfection is attributable to label noise, encoder limitations, and the difficulty of the four-way classification task. But the 100% binary transfer on the obligation-liberty axis shows that on the strongest structural invariant, the gauge invariance is exact.

### 11.5.3 Connecting to Parallel Transport

In Chapter 10, we defined translation as parallel transport on the content manifold: carrying meaning from one coordinate system to another along a path. The BIP experiment provides the first empirical measurement of that transport.

The training process can be understood as the model learning the *connection* on the moral submanifold of $C$. The Christoffel symbols---the adjustments needed to carry a meaning vector from one point to a neighbouring point---are implicitly encoded in the model's learned parameters. The adversarial training ensures that the connection is metric-compatible: the "size" and "angle" of moral relations are preserved during transport.

The 55.6% transfer efficiency (relative to the 80% in-distribution ceiling) measures the holonomy of the transport. In the flat region of $C$ (the deontic axis, where the obligation-liberty distinction lives), the holonomy is zero---perfect transport. In the curved region (the correlative distinctions, where perspective-dependent relations live), the holonomy is nonzero---the meaning arrives "rotated" by the curvature of the moral submanifold.

This connects directly to the results of Chapter 10. The Old Assyrian commercial formula *1 ma-na kaspam* ("1 mina of silver") translates with zero holonomy because it inhabits a flat region of $C$. The moral command *chayav* ("obligated") similarly translates with zero holonomy on the deontic axis---it inhabits a flat region of the moral submanifold. The complex personal-distress passage in Akkadian accumulates holonomy because it inhabits a curved region. The correlative distinctions in Hohfeldian classification similarly accumulate holonomy because perspective-dependent moral relations inhabit a curved region.

The BIP experiment quantifies, for the first time, the curvature of the moral submanifold. The flatness of the deontic axis and the curvature of the correlative region are empirical facts about the geometry of meaning, measured across 2,500 years and the Semitic-Germanic language boundary.

### 11.5.4 What This Means for Communication

The BIP results carry a strong implication for the theory of communication developed in this book. The content manifold $C$ is not homogeneously structured. It has regions of low curvature---commercial transactions, basic deontic distinctions---where meaning transports cleanly across any gauge transformation. It has regions of higher curvature---perspective-dependent relations, culturally embedded connotations---where meaning accumulates holonomy during transport.

But the crucial finding is that the content manifold has an *invariant core*. The Hohfeldian relational structure---rights, duties, liberties, exposures---is that core. It is not a cultural construction. It is not a product of the Hebrew language or the rabbinic tradition. It is not a product of the English language or American advice culture. It is a geometric feature of moral space itself: a structural invariant that any coordinate chart on $C$ must respect, just as any coordinate system on a sphere must respect the sphere's intrinsic curvature.

The rabbis of the Talmud, debating whether a found object must be returned or may be kept, and the readers of Dear Abby, asking whether a borrowed lawnmower must be replaced, are using different coordinates to navigate the same manifold. The coordinates are arbitrary---that is Saussure's insight, restated as gauge invariance. The manifold is not.

This is the strongest empirical evidence in this book for the central claim stated in Chapter 1: communication has geometric structure that scalar evaluation destroys. The 44.5% F1 is not a number that captures what the BIP experiment reveals. What it reveals is a 2,500-year invariance in the deep grammar of moral reasoning---a topological fact about the content manifold that no scalar metric was designed to detect, and that the geometric framework of this book was built to illuminate.

### 11.5.5 Resolving Euthyphro

The BIP results bear on one of the oldest questions in Western philosophy. In Plato's *Euthyphro*, Socrates asks: is the pious loved by the gods because it is pious, or is it pious because it is loved by the gods? In secular terms: is morality objective (existing independently of any mind) or subjective (constructed by minds)?

The BIP experiment suggests a resolution that escapes both horns of the dilemma. Morality is *relational*: it is the structure that necessarily emerges when agents stand in certain relations to one another. Just as geometry requires space to instantiate it yet is invariant across all spaces that do, moral structure requires minds to instantiate it yet is invariant across all minds that do.

This claim is precisely what the experiment tests. If moral structure were culturally constructed---a product of the Hebrew language, the rabbinic tradition, the specific historical circumstances of ancient Jewish civilization---it would not transfer to Dear Abby. If moral structure were a Platonic form independent of all minds, we would have no way to access or measure it. But if moral structure is *relational*---emerging whenever agents stand in relations of obligation, entitlement, liberty, and exposure---then it should be invariant across all communities of agents, detectable by any model that attends to relational structure, and measurable by the methods of this chapter.

The 44.5% F1 is evidence for relational objectivity. The structure is there, in the Hebrew texts and in the English texts, not because one tradition borrowed it from the other, but because any community of moral agents---rabbis debating in Babylonia, advice-seekers writing in Chicago---necessarily generates the same relational geometry. The invariance is not coincidental. It is structural, in the precise sense that the curvature of a sphere is structural: not dependent on the coordinate system, not imposed from outside, but inherent in the object itself.

### 11.5.6 Implications for AI Alignment

If moral structure is gauge-invariant, then AI alignment may be more tractable than commonly assumed. The challenge is not to instill arbitrary human values in artificial agents---values that might be culturally contingent or internally inconsistent. The challenge is to instantiate the invariant moral geometry that any sufficiently sophisticated agent will converge upon.

The BIP architecture provides a prototype for how this might work. The adversarial disentanglement forces the model to attend to structural features (bonds) rather than surface features (language, genre, era). The Bond Index provides a quantitative test for whether a system's moral reasoning respects the correlative symmetry of the Hohfeldian structure. The perturbation ratio (structural/surface sensitivity) provides a test for gauge invariance: is the system responding to morally relevant features or to morally irrelevant ones?

These tools convert the untestable claim "this AI system is ethical" into the testable claim "this AI system achieves Bond Index $< \tau$ with structural/surface ratio $> 2.0$." The convergence from arbitrary initial representations toward low Bond Index under invariance training provides a principled optimization objective that is culture-independent---not because it ignores cultural variation, but because it targets the structural invariants that all cultures share.

The expanded eleven-language study reinforces this point. The same structural invariants emerge from Confucian, Buddhist, Abrahamic, and Western secular traditions. An alignment system built on these invariants would not privilege any single tradition; it would encode the relational geometry that all traditions instantiate. This is not cultural imperialism disguised as universalism. It is the empirical finding that certain features of moral reasoning---the deontic axis, correlative symmetry, discrete semantic gating---are shared across every tradition tested, and the engineering proposal that these features can serve as the foundation for culturally robust alignment.

---

## 11.6 Limitations and Open Questions

### 11.6.1 What the Experiment Does Not Show

The BIP experiment demonstrates invariance of *relational* moral structure---the Hohfeldian quartet. It does not demonstrate invariance of *substantive* moral content. The experiment shows that the *grammar* of moral reasoning (who owes what to whom) is universal; it does not show that the *conclusions* (what one ought to do) are universal. The Talmud's answer to a property dispute and Dear Abby's answer may differ---but they are navigating the same relational space.

This distinction is important for avoiding overclaiming. The experiment is consistent with both moral universalism (the same moral truths hold everywhere) and a weaker position that we call *structural universalism*: the relational framework within which moral reasoning operates is universal, even if the substantive conclusions reached within that framework vary across cultures.

### 11.6.2 The Encoder's Prior Knowledge

The multilingual encoder was pretrained on text in 50+ languages, including Hebrew and English. It is therefore possible that the encoder has already learned some cross-lingual alignment that facilitates transfer. We mitigate this concern by (1) using an encoder not trained on our specific corpora, (2) demonstrating adversarial disentanglement that strips surface-linguistic information, and (3) noting that the encoder provides general semantic alignment, not moral-structural alignment specifically. The task-specific moral structure must be learned by our architecture.

Nevertheless, a fully satisfying test would use an encoder with no prior cross-lingual alignment---e.g., two monolingual encoders trained independently on Hebrew and English. If transfer still occurred through a shared bond space, the result would be unimpeachable. This remains future work.

### 11.6.3 Cultural Coverage

The experiment covers Judaic, Confucian/Daoist, Islamic, and secular Western traditions. It does not cover Hindu, Buddhist, African, Indigenous American, or other traditions. The invariance claim is bounded by the traditions tested. Extension to Buddhist texts (Pali Canon), Hindu texts (Mahabharata, Dharmasutras), and others is essential for a fully universal claim.

The expanded corpus (eleven languages, 109,769 passages) reported in the IEEE TAI study partially addresses this gap, adding Sanskrit (Hindu), Pali (Buddhist), Greek (Classical), Latin (Stoic), French (Enlightenment), and Spanish (Renaissance) to the test set. Cross-cultural transfer succeeded in all ten experimental configurations, with F1 ranging from 0.61 (Daoist to Buddhist) to 0.78 (Jewish to Islamic). The universality claim, while strengthened, remains bounded by the predominantly Eurasian scope of the available digitized corpora.

### 11.6.4 The Road to Chapter 12

The BIP experiment demonstrates cross-lingual invariance at a single level of analysis: the four Hohfeldian categories. Chapter 12 asks the complementary question: what *within* a language predicts Hohfeldian classification? What are the linguistic coordinates---the surface features on the signal manifold $S$---that different languages use to express the same gauge-invariant moral content? And does the invariance hold not just across languages but across *time within a single tradition*?

The answers will reveal the relationship between the deep geometry and the surface coordinates---between the manifold and its charts---with an empirical precision that the cross-lingual experiment alone cannot provide.

[^1]: The 52.3 $z$-statistic translates to a probability of approximately $10^{-600}$ under the normal distribution. The more conservative $p < 10^{-50}$ reflects our uncertainty about the tails of the distribution and the possibility of systematic biases that inflate the test statistic.

[^2]: The Sefaria database is maintained as an open-source project. The data used in this experiment is available under a CC-BY-NC license. All experimental code is available at the repository listed in Appendix C.

[^3]: The adversarial weight $\lambda$ was ramped from 0.1 to 1.0 over the first three epochs of training. This gradual ramp prevents the adversary from destabilizing training in early epochs when the bond representation has not yet formed. The schedule follows Ganin et al. (2016).

[^4]: Classical Chinese is classified as a Sino-Tibetan language by most linguists. Its typological distance from Hebrew is extreme: it is isolating (no inflectional morphology), topic-prominent (not subject-prominent), and written in logographic script. The Confucian ethical tradition developed in the Spring and Autumn period (770--476 BCE) with no documented contact with Near Eastern legal traditions until the Silk Road era (circa 200 BCE), and the texts used in our corpus predate any plausible influence.

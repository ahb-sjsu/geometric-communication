# Appendix C: The BIP Experimental Protocol

## Full Specification of the Cross-Lingual Transfer Experiment

This appendix provides a complete specification of the Bond Invariance Principle (BIP) experiment described in Chapters 11--12, sufficient for independent replication. The experiment tests whether Hohfeldian moral relations---Right, Duty, Liberty, No-Right---constitute a gauge-invariant structure that persists across languages, cultures, and millennia. We train an adversarial disentanglement model on ancient Hebrew and Aramaic ethical texts (500 BCE--1800 CE) and test zero-shot transfer to modern American English advice columns (1956--2020), with supplementary evaluation on Classical Chinese and Arabic corpora.

All code and data are available at `github.com/ahb-sjsu/sqnd-probe`. Configuration files referenced below are `config_bip.yaml` and `corpora.yaml` in the repository root.

---

## C.1 Corpus Preparation

### C.1.1 Training Corpus: Sefaria Database

The primary training corpus is drawn from the Sefaria Project (sefaria.org), a freely available, community-maintained library of Jewish texts. The Sefaria-Export repository provides the complete digitized corpus as structured JSON files organized by category, with parallel Hebrew/Aramaic originals and English translations.

**Acquisition.** The corpus is obtained by shallow-cloning the Sefaria-Export repository:

```bash
git clone --depth 1 https://github.com/Sefaria/Sefaria-Export.git
# Approximate size: 8.3 GB
```

The JSON directory contains subdirectories for each category of text (Tanakh, Mishnah, Talmud, Midrash, Halakhah, Kabbalah, Musar, Responsa, etc.). Each text is stored as a JSON file with `he` (Hebrew/Aramaic original) and `text` or `en` (English translation) fields, organized hierarchically by chapter and verse or folio and line.

**Temporal bins.** Passages are assigned to temporal periods based on the Sefaria directory structure and category metadata:

| Code | Period | Date Range | Primary Languages | Representative Texts |
|------|--------|------------|-------------------|---------------------|
| BIB | Biblical | 1000--500 BCE | Biblical Hebrew | Torah, Prophets, Writings |
| ST | Second Temple | 500 BCE--70 CE | Late Hebrew | Apocrypha, sectarian texts |
| TAN | Tannaitic | 70--200 CE | Mishnaic Hebrew | Mishnah, Tosefta |
| AMO | Amoraic | 200--500 CE | Aramaic, Hebrew | Talmud Bavli, Talmud Yerushalmi, Midrash |
| GEO | Geonic | 600--1000 CE | Judeo-Arabic, Hebrew | Responsa literature |
| RIS | Rishonim | 1000--1500 CE | Medieval Hebrew | Rashi, Maimonides, Nachmanides |
| ACH | Achronim | 1500--1800 CE | Early Modern Hebrew | Shulchan Aruch, Chasidic texts |

Period assignment is performed by a deterministic mapping from Sefaria category to period:

```python
CATEGORY_TO_PERIOD = {
    'Tanakh': 'BIBLICAL',   'Torah': 'BIBLICAL',
    'Prophets': 'BIBLICAL', 'Writings': 'BIBLICAL',
    'Mishnah': 'TANNAITIC', 'Tosefta': 'TANNAITIC',
    'Talmud': 'AMORAIC',    'Bavli': 'AMORAIC',
    'Yerushalmi': 'AMORAIC','Midrash': 'AMORAIC',
    'Halakhah': 'RISHONIM', 'Kabbalah': 'RISHONIM',
    'Philosophy': 'RISHONIM',
    'Musar': 'ACHRONIM',    'Responsa': 'ACHRONIM',
    'Chasidut': 'ACHRONIM',
}
```

**Passage extraction.** The `SefariaLoader` recursively traverses the JSON directory tree. For each JSON file, it extracts paired (Hebrew/Aramaic original, English translation) passages by flattening nested list structures. Priority is given to ethically rich tractates: the Talmudic orders Nezikin (damages), Nashim (women/family law), and Mo'ed (festivals), as well as the Mishnaic tractates Pirkei Avot, Bava Kamma, Bava Metzia, Sanhedrin, and Ketubot.

**Text cleaning.** All passages undergo the following preprocessing:

1. Unicode normalization to NFC form
2. HTML tag removal (Sefaria source text contains inline markup)
3. Whitespace normalization (collapse multiple spaces, strip leading/trailing whitespace)
4. Length filtering: minimum 50 characters, maximum 2,000 characters

**Language detection.** Passages from Talmud Bavli, Targums, and Zohar are tagged as Aramaic; all others as Hebrew. Language is assigned from Sefaria metadata rather than automatic detection, since the two languages frequently co-occur.

**Deduplication.** Each passage receives a deterministic ID: the first 12 hex characters of the MD5 hash of the source name, structural reference, and first 50 characters of the Hebrew original. Re-runs produce identical IDs; exact duplicates are naturally deduplicated.

The final training corpus comprises approximately 3.9 million passages with both Hebrew/Aramaic original and English translation. For training, the model receives **only the original Hebrew/Aramaic text** (or the English text in the appropriate experimental condition), never the translation.

### C.1.2 Test Corpus: Dear Abby Letters

The test corpus consists of letters from the "Dear Abby" syndicated advice column, spanning 1956--2020. The corpus was chosen because it is maximally distant from the training corpus along every conceivable confound: language (American English vs. Hebrew/Aramaic), era (20th--21st century vs. ancient/medieval), genre (informal advice-seeking vs. legal/religious commentary), and cultural context (secular American vs. Jewish legal tradition).

**Source.** The Dear Abby dataset is available as a CSV file via Kaggle. The columns include the date of publication, the reader's question (letter), and the columnist's answer (response).

**Preprocessing.** Each letter is formatted as a combined question-answer pair (`QUESTION: [text] ANSWER: [response]`). The same cleaning pipeline (Unicode normalization, whitespace normalization, length filtering at 50--2,000 characters) is applied. Year of publication is extracted for temporal metadata; topical category (family, marriage, work, friendship, etc.) is assigned by keyword regex matching.

**Deduplication.** Letter IDs are the first 12 hex characters of the MD5 hash of the date and first 50 characters of the question. The final test corpus comprises approximately 68,000 letters, with an additional 20,000-letter archive (1985--2017) available for extended evaluation.

### C.1.3 Supplementary Corpora

Two additional corpora test cross-cultural invariance beyond the Semitic--Germanic language family boundary.

**Classical Chinese.** The core Chinese corpus draws from the Chinese Text Project (ctext.org) and includes the Analects, Mencius, Dao De Jing, Zhuangzi, Daxue, and Zhongyong, representing the Confucian and Daoist traditions (approximately 500 BCE--200 CE). In the v10.9 expansion, the corpus is diversified to include:

- *Buddhist Chinese*: Dhammapada (Chinese translation), Diamond Sutra, Lotus Sutra, Heart Sutra, Brahma Net Sutra, Vimalakirti Sutra, Platform Sutra (~50 passages)
- *Legalist Chinese*: Han Feizi, Shang Jun Shu, Guanzi (~40 passages)
- *Mohist Chinese*: Mozi, with emphasis on the "Universal Love" chapters (~30 passages)
- *Neo-Confucian Chinese*: Zhu Xi, Wang Yangming, Zhou Dunyi, Zhang Zai (~30 passages)

This diversification tests whether Chinese transfer performance reflects genuine invariant structure or corpus homogeneity.

**Arabic.** The Arabic corpus includes the Quran, Hadith collections, Islamic legal maxims (*qawa'id fiqhiyya*), Sufi ethical texts (al-Ghazali, al-Qushayri, Rumi), and Arabic philosophical ethics (al-Farabi, Ibn Rushd, Ibn Khaldun). The v10.8 corpus (~180 passages) is expanded substantially in v10.9.

**Sanskrit/Pali (planned).** Passages from the Mahabharata, Bhagavad Gita, Manusmriti, Upanishads, Dhammapada, and Vinaya Pitaka serve as an independence test: an Indo-European tradition developed independently of both Semitic and Sinitic moral thought.

### C.1.4 Labeling Protocol: Hohfeldian Relation Assignment

Hohfeldian labels are assigned to passages through a hybrid extraction pipeline. The primary method is pattern-based, with optional LLM augmentation for ambiguous cases.

**Pattern-based extraction.** For each passage, the English text (the translation for ancient texts, the original for Dear Abby) is scanned against compiled regular expression patterns for each Hohfeldian state:

| Hohfeldian State | English Patterns | Hebrew Patterns |
|-----------------|------------------|-----------------|
| OBLIGATION (Duty) | must, shall, duty, required, obligated, responsible, have to, need to | חייב (chayav), מצווה (mitzvah) |
| RIGHT (Claim) | right to, entitled, deserve, owed, demand, may claim | זכאי (zakai) |
| LIBERTY (Privilege) | may, can, permitted, allowed, free to, optional, voluntary | מותר (mutar), רשות (reshut) |
| NO-RIGHT (Exposure) | cannot demand, no right, not entitled, may not require | אסור (asur) |

Each pattern is compiled with case-insensitive matching. The Hohfeldian state with the highest match count across its pattern set is assigned as the passage's primary label. Passages matching no patterns receive a NONE label and are excluded from supervised training on the Hohfeldian classification task.

**Bond type extraction.** In addition to Hohfeldian state, each passage is labeled with one or more of ten bond types, identified by a separate set of domain-specific patterns:

| Bond Type | Representative Patterns |
|-----------|------------------------|
| HARM_PREVENTION | kill, murder, harm, hurt, save, rescue, protect |
| RECIPROCITY | return, repay, owe, debt, mutual, exchange |
| AUTONOMY | choose, decision, consent, force, coerce |
| PROPERTY | property, own, steal, buy, sell, land |
| FAMILY | honor parent, marry, divorce, inherit |
| AUTHORITY | obey, command, law, judge, permit, forbid |
| CARE | care, help, assist, feed, visit, charity |
| FAIRNESS | fair, just, equal, deserve, bias |
| EMERGENCY | emergency, urgent, life-threatening, pikuach nefesh |
| CONTRACT | promise, vow, oath, agreement, pledge |

**Consent status.** Each passage is also classified by consent status (EXPLICIT_YES, IMPLICIT_YES, CONTESTED, IMPLICIT_NO, EXPLICIT_NO, IMPOSSIBLE), determined by a third pattern set targeting consent-indicative language. Disputed passages---those containing markers such as "machlok," "some say... others say," or multiple attributed rabbinic opinions---are flagged and assigned to a "contested" consensus tier.

**Known limitations.** The pattern-based approach is deliberately noisy. Label noise makes transfer *harder*, not easier, so successful transfer despite noise constitutes stronger evidence for invariant structure. A hybrid mode (pattern + LLM classification via Claude 3 Haiku, confidence threshold 0.7) is specified in `config_bip.yaml` for production use. The experiments in Chapters 11--12 use pattern-based labels only.

---

## C.2 Model Architecture

### C.2.1 Encoder

The base encoder is a pretrained multilingual sentence transformer. Two configurations are used across experimental versions:

| Version | Model | Embedding Dim | Languages |
|---------|-------|---------------|-----------|
| v10.8 (paper draft) | `paraphrase-multilingual-MiniLM-L12-v2` | 384 | 50+ languages |
| v10.9+ (full tensor) | `sentence-transformers/all-mpnet-base-v2` | 768 | English-dominant, multilingual |
| Alternate | LaBSE (`sentence-transformers/LaBSE`) | 768 | 109 languages |

The encoder maps each passage to a fixed-dimensional embedding $h \in \mathbb{R}^{d}$ via mean pooling over the last hidden state, weighted by the attention mask:

$$h = \frac{\sum_{i=1}^{L} m_i \cdot h_i}{\sum_{i=1}^{L} m_i}$$

where $h_i$ is the hidden state at position $i$, $m_i$ is the attention mask value, and $L$ is the sequence length. If the encoder's native hidden size differs from the target $d_\text{model}$, a learned linear projection maps to the target dimension.

The encoder may be frozen (all parameters fixed) or fine-tuned. The default configuration fine-tunes the encoder with a lower learning rate than the classification heads. Maximum sequence length is 256 tokens (v10.8) or 512 tokens (v10.9+).

### C.2.2 Disentanglement Module

The core architectural innovation is the disentanglement of the encoder representation into two complementary latent spaces:

- **$z_\text{bond}$** (bond space): Trained to encode moral structure (Hohfeldian relations, bond types) while being *uninformative* about temporal, linguistic, and stylistic features. Dimension: 64 (v10.8) or 128 (v10.9+).
- **$z_\text{label}$** (label space): Trained to capture the temporal-stylistic information that $z_\text{bond}$ discards. Dimension: 32 (v10.8) or 64 (v10.9+).

Both projections use a variational architecture with the reparameterization trick:

```
h (768-dim)
  |
  +---> bond_mean:   Linear(768, 384) -> ReLU -> Dropout(0.1) -> Linear(384, d_bond)
  +---> bond_logvar: Linear(768, 384) -> ReLU -> Dropout(0.1) -> Linear(384, d_bond)
  |
  +---> label_mean:   Linear(768, 384) -> ReLU -> Dropout(0.1) -> Linear(384, d_label)
  +---> label_logvar: Linear(768, 384) -> ReLU -> Dropout(0.1) -> Linear(384, d_label)
```

During training, $z_\text{bond} = \mu_\text{bond} + \sigma_\text{bond} \cdot \epsilon$ where $\epsilon \sim \mathcal{N}(0, I)$ and $\sigma_\text{bond} = \exp(0.5 \cdot \text{logvar}_\text{bond})$. During evaluation, $z_\text{bond} = \mu_\text{bond}$.

### C.2.3 Classification Heads

The model has multiple classification heads, each a two-layer MLP:

| Head | Input | Output Classes | Objective |
|------|-------|----------------|-----------|
| Hohfeld Classifier | $z_\text{bond}$ | 4 (Right, Duty, Liberty, No-Right) | Maximize accuracy |
| Bond Type Classifier | $z_\text{bond}$ | 10 (bond types) | Maximize accuracy |
| Time Classifier (adversarial) | GRL($z_\text{bond}$) | 8--26 (time periods) | Minimize accuracy (~chance) |
| Time Classifier (control) | $z_\text{label}$ | 8--26 (time periods) | Maximize accuracy |
| Language Classifier (adversarial) | GRL($z_\text{bond}$) | 4--8 (languages) | Minimize accuracy (~chance) |
| Genre Classifier (adversarial) | GRL($z_\text{bond}$) | 4 (legal, narrative, wisdom, advice) | Minimize accuracy (~chance) |

Each classifier head follows the architecture:

```
Linear(d_input, hidden_dim) -> ReLU -> Dropout(p) -> Linear(hidden_dim, n_classes)
```

where hidden_dim = 128 for adversarial heads and 64 for task heads, and dropout $p = 0.2$ for adversarial heads, $p = 0.1$ for task heads.

### C.2.4 Gradient Reversal Layer

The adversarial heads receive input through a Gradient Reversal Layer (GRL; Ganin et al., 2016). The GRL is the identity function in the forward pass and negates (and scales) the gradient in the backward pass:

$$\text{GRL}(x) = x \quad \text{(forward)}$$
$$\frac{\partial \text{GRL}}{\partial x} = -\lambda \cdot I \quad \text{(backward)}$$

where $\lambda$ is the reversal strength. This forces $z_\text{bond}$ to become uninformative about the adversarial target (time period, language, genre) while remaining informative about the task target (Hohfeldian state, bond type). The parameter $\lambda$ controls the adversarial pressure; see Section C.3.2 for the schedule.

### C.2.5 Complete Architecture Diagram

```
Input text
    |
    v
[Encoder: all-mpnet-base-v2 or LaBSE]
    |
    v
h (768-dim)
    |
    +-------> [Bond Projection (VAE)] --> z_bond (64 or 128-dim)
    |                                        |
    |                                   +----+----+----+
    |                                   |    |    |    |
    |                                   v    v    v    v
    |                                 [HOH] [BND] [GRL]-->[TIME_ADV]
    |                                  cls   cls         [LANG_ADV]
    |                                                    [GENRE_ADV]
    |
    +-------> [Label Projection (VAE)] --> z_label (32 or 64-dim)
                                              |
                                              v
                                           [TIME_CTL]
                                             cls
```

---

## C.3 Training Procedure

### C.3.1 Loss Function

The total loss is a weighted sum of six components:

$$\mathcal{L} = \lambda_\text{hohf} \mathcal{L}_\text{hohf} + \lambda_\text{bond} \mathcal{L}_\text{bond} + \lambda_\text{time} \mathcal{L}_\text{time} + \lambda_\text{adv} \mathcal{L}_\text{adv} + \lambda_\text{kl} \mathcal{L}_\text{kl} + \lambda_\text{bip} \mathcal{L}_\text{bip}$$

where:

- $\mathcal{L}_\text{hohf}$: Cross-entropy loss for Hohfeldian classification from $z_\text{bond}$.
- $\mathcal{L}_\text{bond}$: Binary cross-entropy loss for multi-label bond type classification from $z_\text{bond}$.
- $\mathcal{L}_\text{time}$: Cross-entropy loss for time period classification from $z_\text{label}$ (the control path---this should succeed).
- $\mathcal{L}_\text{adv}$: Negative entropy of the time period prediction from $z_\text{bond}$. We *maximize* the entropy of the adversarial classifier's output, forcing it toward uniform (chance-level) predictions: $\mathcal{L}_\text{adv} = -H(\text{softmax}(f_\text{time}(\text{GRL}(z_\text{bond}))))$.
- $\mathcal{L}_\text{kl}$: KL divergence regularization for both variational projections: $\mathcal{L}_\text{kl} = D_\text{KL}(q(z_\text{bond}|h) \| p(z)) + D_\text{KL}(q(z_\text{label}|h) \| p(z))$ where $p(z) = \mathcal{N}(0, I)$.
- $\mathcal{L}_\text{bip}$: Contrastive loss on bond-isomorphic pairs. Passages with identical bond structure signatures (same agent-patient-relation-consent topology) from *different* time periods should have similar $z_\text{bond}$ representations. Implemented as InfoNCE with temperature $\tau = 0.07$.

### C.3.2 Hyperparameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Optimizer | AdamW | $\beta_1 = 0.9$, $\beta_2 = 0.999$ |
| Learning rate | $2 \times 10^{-5}$ | For both encoder and heads |
| Weight decay | 0.01 | |
| LR schedule | OneCycleLR | 10% warmup, cosine annealing |
| Warmup steps | 1,000 | |
| Batch size | 32 | |
| Max epochs | 50 | |
| Early stopping patience | 5 epochs | On validation loss |
| Gradient clipping | 1.0 (max norm) | |
| Max sequence length | 512 tokens | |
| $\lambda_\text{hohf}$ | 1.0 | |
| $\lambda_\text{bond}$ | 1.0 | |
| $\lambda_\text{time}$ | 1.0 | |
| $\lambda_\text{adv}$ | 1.0 | Fixed; GRL $\lambda$ controls adversarial strength |
| $\lambda_\text{kl}$ | 0.1 | Low weight prevents posterior collapse |
| $\lambda_\text{bip}$ | 2.0 | High weight emphasizes structural invariance |
| GRL $\lambda$ | 1.0 | Fixed in primary experiments |
| Dropout (task heads) | 0.1 | |
| Dropout (adversarial heads) | 0.2 | |
| InfoNCE temperature | 0.07 | |

### C.3.3 Training Loop

Each epoch proceeds as follows:

1. Iterate over training batches. For each batch:
   a. Tokenize passages and move tensors to GPU.
   b. Forward pass through encoder, disentangler, and all classification heads.
   c. Compute composite loss $\mathcal{L}$.
   d. Backward pass with gradient reversal active on adversarial paths.
   e. Clip gradients by max norm (1.0).
   f. Optimizer step and learning rate scheduler step.
2. Evaluate on validation set with adversarial lambda set to 0.0 (no gradient reversal during evaluation).
3. Track validation loss for early stopping. Save checkpoint if validation loss improves.
4. If no improvement for 5 consecutive epochs, stop training and reload best checkpoint.

### C.3.4 Gradient Reversal Lambda Schedule

The primary experiments use a fixed $\lambda = 1.0$ for the gradient reversal layer. An alternative schedule, ramping $\lambda$ from 0 to 1 over the first 20% of training, was tested but did not produce significantly different results. The fixed schedule is preferred for simplicity and reproducibility.

---

## C.4 Experimental Design

### C.4.1 Direction A: Ancient to Modern (Primary)

| Split | Content |
|-------|---------|
| Train | ~3.9M Hebrew/Aramaic passages (BIB, ST, TAN, AMO, GEO, RIS periods; 500 BCE--1500 CE) |
| Validation | Achronim passages (ACH period; 1500--1800 CE), held out |
| Test | ~68K Dear Abby letters (1956--2020, American English) |

This is the primary BIP test. The model is trained exclusively on ancient and medieval Hebrew/Aramaic text and evaluated on modern English with no additional training, adaptation, or fine-tuning.

### C.4.2 Direction B: Modern to Ancient

| Split | Content |
|-------|---------|
| Train | ~68K Dear Abby letters (1956--2020) |
| Validation | ~6K Dear Abby letters, held out |
| Test | ~50K Hebrew passages, sampled from the Sefaria corpus |

Bidirectional transfer controls for the possibility that the result is an artifact of training on the larger corpus. If transfer works in both directions, the invariant structure is genuine.

### C.4.3 Mixed Training (Control Ceiling)

| Split | Content |
|-------|---------|
| Train | 70% mixed ancient + modern |
| Test | 30% mixed ancient + modern |

This establishes the ceiling for in-distribution performance.

### C.4.4 Full Transfer Matrix

For the temporal invariance protocol (Chapter 12), all 56 pairwise transfers between the 8 time periods are computed as a SLURM array job (one transfer experiment per array task). Each cell in the $8 \times 8$ matrix (minus the diagonal) records the Hohfeldian classification accuracy when training on one period and testing on another.

### C.4.5 Leave-One-Era-Out Cross-Validation

For each of the 8 temporal periods with sufficient data (>100 passages), the model is trained on all other periods and tested on the held-out period. This yields 8 independent tests of temporal transfer.

---

## C.5 Evaluation Metrics

### C.5.1 Primary Metrics

**F1 (macro).** The primary metric for Hohfeldian classification. Macro F1 gives equal weight to each of the four classes regardless of class frequency, ensuring that minority classes (typically No-Right) are not ignored. Reported as the mean across 5 random seeds with 95% confidence intervals.

**Accuracy.** Overall classification accuracy, with Wilson score 95% confidence intervals.

**Per-class precision and recall.** For each Hohfeldian state (Right, Duty, Liberty, No-Right), we report precision $P_c = \text{TP}_c / (\text{TP}_c + \text{FP}_c)$ and recall $R_c = \text{TP}_c / (\text{TP}_c + \text{FN}_c)$.

### C.5.2 Adversarial Success Measures

**Language probe accuracy.** After training, a fresh linear probe is trained on frozen $z_\text{bond}$ representations to predict the source language. Successful disentanglement is indicated by probe accuracy near the chance level (25% for 4 languages, 12.5% for 8 languages). The reported result of 1.2% (below chance) and 0.0% for the cross-lingual condition confirms that $z_\text{bond}$ contains no recoverable linguistic information.

**Time period probe accuracy.** Analogously, a fresh linear probe trained on frozen $z_\text{bond}$ to predict time period should achieve near-chance accuracy. Near-chance time prediction from $z_\text{bond}$, combined with above-chance Hohfeldian prediction, demonstrates that the bond space encodes moral structure but not temporal-stylistic features.

**Time Invariance Score (TIS).** A composite metric:

$$\text{TIS} = 1 - \frac{\text{Time\_acc} - \text{chance}}{1 - \text{chance}}$$

where Time_acc is the adversarial classifier's accuracy from $z_\text{bond}$. TIS > 0.90 indicates strong temporal invariance.

### C.5.3 Bond Index

The Bond Index quantifies the structural consistency of Hohfeldian classifications by measuring correlative symmetry violations. Hohfeldian positions come in correlative pairs: Duty $\leftrightarrow$ Right, and Liberty $\leftrightarrow$ No-Right. If the model classifies one party as having a Duty, the correlative party should have a Right. A classification that assigns Duty to one party and No-Right to the other constitutes a symmetry violation.

$$\text{Bond Index} = \frac{\text{observed violations}}{\text{maximum possible violations}}$$

A Bond Index of 0.0 indicates perfect correlative symmetry; 0.5 indicates random classification; values above 0.5 indicate systematic anti-correlation.

### C.5.4 Structural Fuzzing Analysis

To validate that $z_\text{bond}$ captures structural rather than surface features, we compute embedding distances under two perturbation types:

- **Structural perturbations**: Change the Hohfeldian state (Obligation to Permission), swap agent/patient roles, alter consent status. These should produce *large* movements in $z_\text{bond}$.
- **Surface perturbations**: Synonym substitution, style changes (formal to informal), paraphrase. These should produce *small* movements in $z_\text{bond}$.

The ratio of mean structural distance to mean surface distance (the "structural sensitivity ratio") should be significantly greater than 1.0. The reported ratio of 11.1x ($t = 2.46$, $p = 0.023$) confirms structural sensitivity with surface invariance.

### C.5.5 Geometric Analysis

**PCA of $z_\text{bond}$.** Principal component analysis on the bond space reveals its effective dimensionality. The reported finding is that 3 components explain 90% of variance, consistent with the theoretical prediction that Hohfeldian relations form a bounded, low-dimensional manifold.

**Manifold comparison.** For each time period, UMAP projections of $z_\text{bond}$ are computed. If BIP holds, the manifolds should be congruent (similar cluster structure, similar topological features) across periods, differing only in orientation. Procrustes analysis quantifies the alignment between period-specific manifolds.

---

## C.6 Statistical Testing

### C.6.1 Comparison to Chance

All reported accuracies and F1 scores are tested against the chance baseline (25% for 4-class Hohfeldian classification) using a $z$-test:

$$z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}}$$

The primary result ($z = 52.3$, $p < 10^{-50}$) is computed on the full test set of ~68,000 letters. Effect size is reported as Cohen's $h = 2 \arcsin(\sqrt{\hat{p}}) - 2 \arcsin(\sqrt{p_0})$.

### C.6.2 Confidence Intervals

All metrics are reported with 95% confidence intervals computed by one of:

- **Wilson score interval** for accuracy (proportion) estimates.
- **Standard deviation across 5 random seeds** for F1 and composite metrics.
- **Bootstrap (10,000 resamples)** for effect size comparisons.

### C.6.3 Multiple Comparisons

The full transfer matrix involves 56 pairwise tests. Bonferroni correction sets the per-comparison significance threshold at $\alpha = 0.05 / 56 = 0.0009$. The conservative significance level of $\alpha = 0.001$ specified in `config_bip.yaml` satisfies this requirement.

### C.6.4 Variance Decomposition

For the full tensor experiment (Chapter 12, Section 12.2), a MANOVA decomposes variance in $z_\text{bond}$ across five factors: Time Period, Language, Genre, Bond Type, and Hohfeldian State. The key prediction is:

| Factor | Predicted $\eta^2$ | BIP Interpretation |
|--------|--------------------|--------------------|
| Hohfeldian State | > 0.30 | Large effect: $z_\text{bond}$ is organized by moral structure |
| Bond Type | > 0.20 | Large effect: domain-specific moral content preserved |
| Time Period | < 0.05 | Negligible: temporal variation successfully removed |
| Language | < 0.05 | Negligible: linguistic variation successfully removed |
| Genre | < 0.10 | Small: some genre signal may remain |

The bootstrap comparison of effect sizes ($n_\text{bootstrap} = 10{,}000$) tests the directional hypothesis $H_1: \eta^2(\text{Time}) < \eta^2(\text{Hohfeld})$.

---

## C.7 Temporal Invariance Protocol

### C.7.1 Temporal Bin Definitions

The eight temporal bins (seven ancient/medieval, one modern) are defined in Section C.1.1. For the Temporal Invariance Protocol specifically, the bins serve as both the holdout variable and the adversarial target. The critical design choice is that the bins are defined by scholarly periodization (based on literary, linguistic, and historical criteria), not by the model. This prevents circular reasoning.

### C.7.2 Cross-Temporal Validation Procedure

The primary cross-temporal test uses the **temporal holdout** split:

1. **Train** on all passages from periods BIB through RIS (500 BCE--1500 CE).
2. **Validate** on ACH (1500--1800 CE)---the most recent ancient period, serving as a bridge.
3. **Test** on MOD (1956--2020 CE)---the Dear Abby corpus, maximally distant from training.

The temporal gap between the latest training data (Rishonim, ~1500 CE) and the test data (Dear Abby, 1956--2020) is approximately 450--2,500 years depending on training period.

The **leave-one-era-out** protocol provides finer-grained analysis. For each era $e$, the model is trained on $\{E \setminus e\}$ and tested on $e$. This produces a per-era transfer profile: which eras transfer to which? The transfer score for each cell is:

$$T_{s \to t} = \text{Hohfeld\_acc}_{s \to t} \times (1 - \text{Time\_acc}_{s \to t})$$

This penalizes configurations where Hohfeldian accuracy is high but the model is also successfully predicting time period---indicating that temporal features, not invariant structure, are driving the classification.

### C.7.3 Controls for Confounds

**Translation artifact control.** Hohfeldian labels for ancient texts are extracted from English translations, but the model is trained on original Hebrew/Aramaic. This design ensures that any transfer to English cannot be mediated by translation artifacts in the training signal. The model must learn structure present in the original language that happens to transfer to English---exactly the invariance claim.

**Corpus size control.** The Sefaria corpus (~3.9M passages) is ~57x larger than Dear Abby (~68K). In bidirectional transfer, the Sefaria test set is subsampled to 68K passages to match.

**Genre control.** The adversarial genre head forces $z_\text{bond}$ to discard genre information. The Dear Abby corpus is maximally genre-distant from all Sefaria categories, making genre-based shortcuts impossible.

**Encoder pretraining control.** The multilingual encoder was pretrained on general-purpose web text, not on either experimental corpus. It provides a shared multilingual coordinate system; moral structure must be learned by the task-specific heads.

---

## C.8 Reproducibility Checklist

### C.8.1 Random Seeds

All experiments use 5 random seeds: {42, 123, 456, 789, 1024}. For each seed, `torch.manual_seed(seed)`, `numpy.random.seed(seed)`, and `random.Random(seed)` are set. Results are reported as mean $\pm$ standard deviation across seeds.

### C.8.2 Hardware

The experiments were developed and tested on the following hardware:

| Resource | Specification |
|----------|--------------|
| Primary development | SJSU College of Engineering HPC cluster |
| GPU (full tensor) | NVIDIA H100 (80 GB VRAM) |
| GPU (transfer matrix) | NVIDIA P100 (12 GB VRAM) x 10, SLURM array |
| GPU (standard training) | NVIDIA V100 (16 GB VRAM) |
| CPU (preprocessing) | 16 cores, 64 GB RAM |
| Storage | 524 TB Lustre scratch (checkpoints), 100 TB /data (corpora) |

For replication on more modest hardware, a single GPU with 12+ GB VRAM (e.g., NVIDIA T4) is sufficient for training with a reduced batch size (16 instead of 32). Preprocessing is CPU-only.

### C.8.3 Software Versions

```
python              >= 3.10
torch               >= 2.0.0
transformers        >= 4.35.0
sentence-transformers >= 2.2.0
datasets            >= 2.14.0
numpy               >= 1.24.0
pandas              >= 2.0.0
scipy               >= 1.11.0
scikit-learn        >= 1.3.0
spacy               >= 3.6.0  (with en_core_web_lg model)
nltk                >= 3.8.0
hebrew-tokenizer    >= 2.3.0
pyarabic            >= 0.6.0
matplotlib          >= 3.7.0
seaborn             >= 0.12.0
wandb               >= 0.15.0  (optional, for experiment tracking)
tqdm                >= 4.65.0
pyyaml              >= 6.0.0
```

### C.8.4 Expected Runtimes

| Phase | Hardware | Expected Time |
|-------|----------|---------------|
| Sefaria git clone | Any (network-bound) | ~15 minutes |
| Preprocessing (4M passages) | 16 CPU cores | ~2 hours |
| Embedding extraction | 1x P100 | ~4 hours |
| Transfer matrix (56 experiments) | 10x P100 in parallel | ~2 hours |
| Full tensor training (20 epochs) | 1x H100 | ~8--12 hours |
| MANOVA analysis | 16 CPU cores | ~1 hour |
| Manifold analysis (UMAP + clustering) | 1x A100 | ~2 hours |
| **Total wall time (with parallelization)** | | **~18 hours** |
| **Total GPU-hours** | | **~70 hours** |

On a single T4 GPU (Kaggle-class hardware), the full pipeline requires approximately 72 hours of wall time. The transfer matrix cannot be parallelized and dominates the runtime.

### C.8.5 Data Availability

| Resource | Location | Size |
|----------|----------|------|
| Sefaria-Export | `github.com/Sefaria/Sefaria-Export` | ~8.3 GB |
| Dear Abby dataset | Kaggle (see repository README) | ~50 MB |
| Chinese Classics | `ctext.org` | ~5 MB (curated sample) |
| Code and configuration | `github.com/ahb-sjsu/sqnd-probe` | ~100 MB |

### C.8.6 Directory Structure

```
sqnd-probe/
+-- config_bip.yaml              # Primary configuration
+-- corpora.yaml                 # Corpus definitions and future plans
+-- data/
|   +-- raw/
|   |   +-- Sefaria-Export/      # Cloned repository (~8.3 GB)
|   |   +-- dear_abby.csv       # Kaggle dataset
|   |   +-- chinese/             # Chinese classics (JSON)
|   |   +-- islamic/             # Islamic texts (JSON)
|   +-- processed/
|   |   +-- passages.jsonl       # Preprocessed passages
|   |   +-- bond_structures.jsonl # Extracted bond structures
|   |   +-- corpus_stats.json    # Corpus statistics
|   +-- splits/
|       +-- all_splits.json      # All split definitions
+-- src/
|   +-- data/
|   |   +-- preprocess.py        # Corpus loading and preprocessing
|   |   +-- extract_bonds.py     # Bond structure extraction
|   |   +-- generate_splits.py   # Train/valid/test split generation
|   |   +-- verify_data.py       # Data verification
|   +-- models/
|   |   +-- bip_model.py         # Model architecture
|   +-- train.py                 # Training loop
|   +-- evaluate.py              # Evaluation and statistical tests
+-- models/
|   +-- checkpoints/             # Saved model weights
+-- results/
    +-- metrics/                 # JSON metric files
    +-- figures/                 # Generated plots
```

---

## C.9 Key Results Summary

For reference, the primary results reported in Chapter 11 are:

| Metric | Value | 95% CI |
|--------|-------|--------|
| Bond F1 (macro), Ancient to Modern | 44.5% | 42.1--46.9% |
| Bond Accuracy, Ancient to Modern | 50.7% | 48.3--53.1% |
| Chance Baseline | 25.0% | --- |
| $z$-statistic | 52.3 | $p < 10^{-50}$ |
| Cohen's $h$ | 0.52 | Medium effect |
| Language Probe Accuracy from $z_\text{bond}$ | 0.0% | (chance = 25%) |
| Mixed Training F1 (ceiling) | 79.99% | --- |
| Transfer Efficiency (transfer / ceiling) | 55.6% | --- |
| Structural/Surface Perturbation Ratio | 11.1x | $p = 0.023$ |
| PCA: Components for 90% Variance | 3 | --- |
| Obligation-Permission Transfer Accuracy | 100% | --- |

Per-language transfer F1 (v10.8): Hebrew 64.5%, English 41.5%, Arabic 40.7%, Classical Chinese 64.9%.

---

## C.10 Replication Quickstart

For a graduate student wishing to replicate the primary result (Direction A: Ancient to Modern):

```bash
# 1. Clone and install
git clone https://github.com/ahb-sjsu/sqnd-probe.git
cd sqnd-probe
pip install -e ".[dev]"

# 2. Acquire data
mkdir -p data/raw
cd data/raw
git clone --depth 1 https://github.com/Sefaria/Sefaria-Export.git
# Place dear_abby.csv from Kaggle in data/raw/
cd ../..

# 3. Preprocess
python src/data/preprocess.py --config config_bip.yaml

# 4. Extract bond structures
python src/data/extract_bonds.py --config config_bip.yaml

# 5. Generate splits
python src/data/generate_splits.py --config config_bip.yaml

# 6. Train (temporal holdout split)
python src/train.py --config config_bip.yaml --split temporal_holdout

# 7. Evaluate
python src/evaluate.py --config config_bip.yaml \
    --model models/checkpoints/temporal_holdout/best_model.pt
```

Expected output: Hohfeldian classification F1 in the range 42--47% on the Dear Abby test set, with time prediction accuracy from $z_\text{bond}$ near or below chance.

---

## References

Ganin, Y., Ustinova, E., Ajakan, H., Germain, P., Larochelle, H., Laviolette, F., Marchand, M., & Lempitsky, V. (2016). Domain-adversarial training of neural networks. *Journal of Machine Learning Research*, 17(1), 2096--2030.

Hohfeld, W. N. (1913). Some fundamental legal conceptions as applied in judicial reasoning. *Yale Law Journal*, 23(1), 16--59.

Hohfeld, W. N. (1917). Fundamental legal conceptions as applied in judicial reasoning. *Yale Law Journal*, 26(8), 710--770.

Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *Proceedings of EMNLP*.

Sefaria Project. (n.d.). Sefaria: A living library of Torah texts online. https://sefaria.org

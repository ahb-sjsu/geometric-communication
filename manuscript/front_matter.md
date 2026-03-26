# Front Matter

---

## Title Page

**Geometric Communication: Language, Signal, and the Topology of Meaning**

Andrew H. Bond
Senior Member, IEEE
Department of Computer Science
San Jose State University

Book 7 of the Geometric Series

*San Jose, 2026*

---

## Series Foreword

This is the seventh volume in the Geometric Series.

The series began with a simple observation: across domains --- ethics, law, economics, cognition, medicine, communication --- the standard methodology compresses multi-dimensional structure into scalar numbers and then wonders why the numbers behave badly. GDP does not capture economic wellbeing. IQ does not capture intelligence. BLEU does not capture translation quality. QALYs do not capture patient health. Binary verdicts do not capture legal reasoning. The pattern is universal and the diagnosis is the same: scalar reduction destroys geometric structure, and the destruction is irreversible.

*Geometric Methods in Computational Modeling* (Book 1) assembled the mathematical toolkit: Riemannian geometry, hyperbolic embeddings, persistent homology, SPD manifolds, gauge theory. *Geometric Reasoning: From Search to Manifolds* (Book 2) developed the parent framework --- the heuristic field formalism, geodesic deviation, the four failure modes, gauge invariance, and the Scalar Irrecoverability Theorem that unifies them. *Geometric Ethics* (Book 3) was the first domain instantiation, demonstrating the framework on the 9-dimensional stratified moral manifold with its $D_4 \times U(1)_H$ symmetry group. Books 4 through 6 --- *Geometric Economics*, *Geometric Law*, and *Geometric Cognition* --- extended the instantiation to markets, courts, and minds.

This book turns to communication itself. The domain is, in some ways, the most natural home for the geometric framework. Communication is the process by which meaning is encoded, transmitted, and decoded --- and meaning, this book argues, is a geometric object. It lives on a manifold. It has topology (some meanings are neighbors; others require traversal through intermediate meanings). It has symmetry (the same meaning can be expressed in different languages, different registers, different media). It has curvature (some regions of semantic space are densely packed and easily navigated; others are sparse and treacherous). Scalar evaluation destroys all of this structure. Geometric analysis recovers it.

What distinguishes this volume from the others is its empirical breadth. The evidence spans five communication systems across 4,000 years and three biological kingdoms: sperm whale codas, birdsong, Akkadian cuneiform, rabbinic Hebrew and Aramaic, and modern English moral discourse. The same three-geometry toolkit --- hyperbolic embeddings, SPD manifolds, persistent homology --- applies without domain-specific modification to all five. That this is possible at all is the book's central empirical claim. That it works as well as it does is, frankly, surprising even to its author.

---

## Preface

### The Whale and the Tablet

In the spring of 2025, I was sitting in a windowless room at San Jose State University, staring at a persistence diagram of sperm whale codas and wondering what it meant. The diagram showed the topological structure of inter-click intervals --- the timing between the sharp, broadband clicks that sperm whales produce in patterned sequences called codas. Each point in the diagram represented a topological feature: a cluster, a loop, a void in the point cloud reconstructed from the click timings. The features had different lifespans --- some appeared briefly and vanished (noise), while others persisted across a wide range of spatial scales (signal). The persistent features were the topological skeleton of the communication.

I had developed this pipeline --- Takens embedding, point cloud reconstruction, persistent homology --- as part of the eris-ketos toolkit for analyzing cetacean vocalizations. The mathematics was borrowed from dynamical systems theory: Takens' theorem guarantees that a time-delay embedding of a scalar observation reconstructs the topology of the underlying dynamical system, and persistent homology extracts that topology in a form that is robust to noise. The pipeline worked. It produced coda-type-specific topological signatures that were invariant to recording amplitude, background noise, and equipment differences. Regular codas (evenly spaced clicks) produced tight clusters. Accelerating codas (clicks that speed up) produced spiral structures. The topology tracked the rhythm, not the acoustics.

What I did not yet appreciate was how far the same mathematics would travel.

A few months later, I began working on the Deep Past initiative --- a project to apply modern machine translation to Akkadian cuneiform, the wedge-shaped script used across Mesopotamia for nearly three millennia. The challenge was extreme data scarcity: roughly 1,500 parallel sentence pairs, where a modern neural MT system expects millions. The standard approach --- throw a ByT5 model at the data and hope for the best --- worked poorly. The model memorized the training set and hallucinated on everything else.

The breakthrough came from an unexpected direction. Akkadian cuneiform has a hierarchical structure: each physical sign (wedge pattern) can have multiple readings (phonetic values), and each reading can participate in multiple words. The sign AN, for instance, can be read as the syllable /an/, the logogram for "heaven" (Sumerian AN, Akkadian *shamu*), the logogram for "god" (Sumerian DINGIR, Akkadian *ilu*), or the proper name Anu (the sky god). This is a tree --- form branches to readings, readings branch to meanings --- and trees embed naturally in hyperbolic space.

I had just built a hyperbolic embedding system for whale coda types. The coda taxonomy is also a tree: codas branch by click count, then by rhythm class, then by ornamentation. I had embedded this tree in the Poincare ball --- the unit disk model of hyperbolic geometry, where the distance metric stretches exponentially toward the boundary, giving exponential volume growth that matches the exponential branching of trees. The embedding worked because hyperbolic space is the natural geometry for hierarchical data, just as Euclidean space is the natural geometry for grid-structured data.

So I embedded the cuneiform sign hierarchy in the same Poincare ball and injected the resulting distances into the transformer's attention mechanism as an additive bias. Tokens whose signs were hierarchically related --- the same sign with different readings, or signs in the same semantic category --- attended to each other more strongly. The bias was not learned; it was a fixed geometric prior derived from Assyriology. And it worked. On sentences containing rare signs --- exactly the cases where data scarcity is most crippling --- the hyperbolic attention bias improved translation quality by compensating for missing data with structural knowledge.

The coincidence bothered me. The same mathematical object --- a Poincare ball embedding of a hierarchical taxonomy --- had proved useful for whale communication and cuneiform translation. Was this a coincidence of the toolkit, or was it telling me something about communication?

I tested the hypothesis further. The BirdCLEF project required classifying birdsong recordings by species. The standard approach used convolutional neural networks on mel-spectrograms. I added the geometric pipeline: SPD manifold features (spectral covariance matrices, analyzed on the manifold of symmetric positive-definite matrices), TDA features (persistent homology of time-delay embedded waveforms), and trajectory features (geodesic deviation on the spectral manifold). The same three geometries I had used for whale codas. The 156-dimensional geometric feature vector was competitive with deep learning baselines, ran on CPU, and captured structure --- cross-frequency correlations, waveform topology, spectral trajectory complexity --- that convolutional filters missed.

Three communication systems. Three biological kingdoms. The same geometry.

The final piece fell into place with the BIP experiments --- the Bias Invariance Principle applied to cross-lingual moral reasoning. We trained an encoder on 3.9 million passages from the Sefaria database (Hebrew Bible, Mishnah, Talmud, Midrash, spanning 500 BCE to 1800 CE) to recognize Hohfeldian moral relations (Right, Duty, Liberty, No-Right). We then tested it on 68,000 Dear Abby letters in American English. The cross-lingual transfer succeeded at 44.5% F1 (chance = 25%, $p < 10^{-50}$). Moral meaning --- at least its relational structure --- was invariant under the most extreme gauge transformation we could devise: translation across 2,500 years, two language families, and the entire distance from ancient rabbinic jurisprudence to mid-century American advice columns.

This book is the account of those discoveries and the framework that unifies them. The central claim is stark: communication has geometric structure, and scalar evaluation destroys it. The structure is not metaphorical. It is the literal geometry of the spaces in which communication operates --- hyperbolic for hierarchies, Riemannian for covariance, topological for shape. The claim is supported empirically across five communication systems, and the evidence converges on a single conclusion: meaning is not a number. It is a point on a manifold, and the operations that preserve meaning --- translation, paraphrase, signal encoding --- are the isometries of that manifold.

### Who This Book Is For

This book is written for three audiences, and it asks something different of each.

For **computational linguists, NLP researchers, and speech scientists**, the book offers a geometric alternative to scalar evaluation. If you have ever been frustrated by BLEU scores that do not track translation quality, or sentiment classifiers that cannot distinguish sarcasm from sincerity, or language model evaluations that rank GPT-4 above Claude on one benchmark and below on the next, the geometric framework explains *why* these metrics misbehave and provides tools that do not. The mathematics is self-contained (Appendix A covers the prerequisites), but the reader who has encountered word embeddings, attention mechanisms, and evaluation metrics will find the terrain more familiar.

For **bioacousticians and animal communication researchers**, the book offers a unified geometric pipeline for extracting structure from vocalizations of any species. The eris-ketos toolkit and its three-geometry approach (hyperbolic embeddings for taxonomic structure, SPD manifolds for spectral covariance, persistent homology for rhythmic topology) are presented in detail in Part II and applied to cetacean communication in Part III. The approach does not require semantic access --- it extracts structural invariants from signal alone --- which is precisely the constraint that non-human communication research operates under.

For **mathematicians and physicists** curious about applications of differential geometry, gauge theory, and algebraic topology to the human sciences, the book provides a worked example of what it means to take the geometric metaphor seriously --- not as a vague analogy between "semantic space" and actual manifolds, but as a literal claim about the mathematical structure of meaning, supported by computation and experiment.

The book assumes basic linear algebra and probability. It does not assume differential geometry, topology, or gauge theory --- these are developed from first principles in Chapter 4 and Appendix A. It does assume intellectual seriousness: the reader should be prepared to follow a mathematical argument across three pages and an empirical argument across three kingdoms.

### A Note on Scope

This book does not solve the problem of communication. It does not decode whale language, crack undeciphered scripts, or produce a universal translation machine. What it does is establish that communication --- all communication, from whale clicks to cuneiform to tweets --- has mathematical structure that current methods ignore, and it builds the tools to analyze that structure. The results are real: Menzerath's law holds in whale codas ($r = -0.269$, $p < 10^{-144}$). Hyperbolic attention bias improves cuneiform MT. Cross-lingual moral transfer works at 44.5% F1. These are not theoretical predictions; they are measurements.

The book also does not pretend that geometry is the final word. Chapter 18 is honest about what the framework cannot yet explain, and the open questions listed there are genuine --- they are problems I do not know how to solve. The frontier is real, and acknowledging it is more useful than pretending it does not exist.

---

## Acknowledgments

A book that spans five communication systems across 4,000 years and three biological kingdoms is necessarily a collaborative enterprise, even when written by a single author. The debts are many.

The geometric framework that underpins this book was developed in conversation with the Geometric Reasoning research group at San Jose State University. I am grateful to the group members --- particularly Lena Thiele, whose co-authorship on the selective invariance paper sharpened my thinking about gauge violation in communication; David Hartmann, who first suggested that the BirdCLEF pipeline could be recast in terms of SPD manifolds; and Priya Suresh, whose careful implementation of the Poincare ball embedding for cuneiform signs turned a theoretical possibility into an empirical result.

The cetacean communication work owes a primary debt to the Dominica Sperm Whale Project and the researchers who collected and curated the coda dataset. The 8,719-coda corpus that underlies Chapters 5--7 represents years of fieldwork in conditions that a computer scientist can only admire from a distance. I am particularly grateful to the marine bioacoustics community for making their data available and for treating a geometer's intrusion into their field with generosity rather than suspicion.

The Deep Past cuneiform translation project was supported by the Digital Humanities Initiative at San Jose State University. The 1,561 Akkadian-English parallel pairs that underlie Chapters 9--10 were prepared with the assistance of Assyriology colleagues who patiently corrected my naive assumptions about cuneiform orthography. Any remaining transliteration errors are mine.

The BIP cross-lingual transfer experiments relied heavily on the Sefaria digital library, whose open-source database of rabbinic literature made it possible to assemble a training corpus spanning 2,300 years of Hebrew and Aramaic moral reasoning. The Dear Abby corpus was assembled from publicly available syndicated columns; I am grateful to the archivists who maintained the digital record.

The BirdCLEF geometric features pipeline was developed during the Kaggle BirdCLEF competition, and I thank the competition organizers and the broader Kaggle community for providing both the data and the competitive incentive to make the pipeline actually work under real constraints.

Institutional support came from the Department of Computer Science at San Jose State University, the College of Science, and the SJSU Research Foundation. Computing resources were provided by the university's High-Performance Computing cluster and, for the larger experiments, by cloud computing credits generously allocated through the university's research computing program.

The series editors and early readers of the manuscript --- including colleagues at the IEEE Computational Intelligence Society, workshop participants at NeurIPS 2025 and ACL 2026, and anonymous reviewers of the component papers --- improved the book immeasurably through their criticism. The errors that remain are proof that I did not always listen.

Finally, and as always: to my family, who have endured two years of dinner-table monologues about whale communication, cuneiform grammar, and the topological structure of birdsong, and who have responded with patience, humor, and the occasional sharp observation that no persistence diagram could capture.

Andrew H. Bond
San Jose, California
March 2026

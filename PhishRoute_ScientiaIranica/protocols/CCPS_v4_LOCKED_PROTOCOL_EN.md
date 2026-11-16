# CCPS-URL: Locked computational protocol (not prospectively registered)

**Intended journal:** Scientia Iranica, Transactions D — Computer Science & Engineering.

**Hypothesis:** A class-conditional provenance penalty combined with a minimum-across-source discrimination score may yield more robust phishing URL predictions on unseen URL corpora than ordinary filter-based selection, prefix normalization, and conventional fully featured classifiers.

**Important novelty caveat:** Conditional invariant representations have been studied for years (e.g., Li et al., AAAI 2018; Heinze-Deml & Meinshausen, Machine Learning 2021). Novelty cannot be claimed from conditional invariance alone. The claim to test is the practical joint source-conditional feature ranking, zero-target adaptation, reproducible evaluation and explicit class-retention diagnostics. A strong cross-corpus advantage is necessary but not sufficient for intellectual novelty.

## Data and labels

PhiUSIIL (0 malicious, 1 benign), URL-Phish V2 (1 malicious, 0 benign), LegitPhish V2 (0 malicious, 1 benign) and CompPhish V4 (1 malicious, 0 benign). All converted to `1=phishing` and `0=benign`. Use URL strings only; other dataset-specific features, HTML, site titles, DOM and collection identifiers are excluded.

## Feature scoring (source training only)

For every feature j and training source s, calculate AUC_{j,s}. Set orientation sign sigma_j by source-training pooled AUC, then

`A_j = max(0, min_s sigma_j * (AUC_{j,s}-0.5))`.

`B_j = max_{y in {0,1}} max_{s!=t} KS(X_j | Y=y, S=s; X_j | Y=y, S=t)`.

`J_j = A_j - lambda * B_j`.

Select the top K features by J_j. Tune lambda in `{0, 0.1, 0.3}` and K in `{8, 16, 24}` solely by source-only inner leave-one-source-out, prioritizing the worst held-out Youden index across valid source folds. If no inner holdout meets both-class and domain diversity requirements, use a flagged fixed fallback (`lambda=0.1`, `K=16`). Uncertainty remains; no claims of guaranteed or source-free deployment performance.

## Models and baselines

LogisticRegression with StandardScaler, balanced class weights, deterministic random_state. The following comparisons run with identical selected feature budgets where applicable: full-feature LR, mutual-information selection, minimum-source class discrimination, conditional provenance-only ranking, mean-source discrimination plus provenance penalty, the full CCPS score, and prefix-ablation full LR. Additionally compare HistGradientBoosting on full features and on CCPS-selected features. All model-selection steps are target-blind.

## Splitting and evaluation

Four leave-one-corpus-out folds. Source-only per-domain train/cal split based on deterministic SHA-256 domain hashing (shared between all training corpora). Never allow any registered domain to appear on both sides. Deduplicate conflicting/duplicate URL strings across training corpora and report counts. Cap source class counts and domain-group contributions to control monopolization by recurring domains; no target-row capping.

Calibration: pick maximum per-source upper benign score quantile corresponding to empirical FPR ≤ 1%; lock threshold before external scoring. Report each source's calibration count. This is NOT a bound on the external FPR.

The external target has two separate estimands: (a) full target sample, and (b) unseen registered domains after excluding domains shared with any training-source corpus, including calibration. Report class counts, unique domains and per-class retention rates before interpreting metrics. `strict_unseen` is designated as the main inferential view ONLY if >=10% of both classes, >=100 samples of both classes, and >=15 distinct registered domains per class survive. These are descriptive gates, not statistical guarantees.

Metrics: test FPR, phishing recall, MCC and PR-AUC, Clopper-Pearson binomial 95% intervals, and paired registered-domain cluster bootstrap intervals for CCPS vs LR_full, MI, stability-only and HGB_full. No target labels for training, calibration, ranking, or selection. Report negative findings.

## Risks and limitations

Corpus/source itself is confounded with collection procedure, website type and class prevalence, which cannot be cleanly separated without provenance metadata. Some source domain/category combinations may have very few benign domains. Source-domain duplication can shrink test representativeness markedly. Empirical calibration does not provide a distribution-free FPR guarantee under shift. A single selected seed and bootstrap assess some uncertainty but do not demonstrate complete seed robustness. This is a source-domain robustness study, not live phishing detection, latency evaluation, or causal intervention.

## References for claims of prior art

- Li et al., *Domain Generalization via Conditional Invariant Representations*, AAAI 2018, DOI 10.1609/aaai.v32i1.11682.
- Heinze-Deml and Meinshausen, *Conditional variance penalties and domain shift robustness*, Machine Learning 2021, DOI 10.1007/s10994-020-05924-1.
- Rashid et al., *Phishing URL detection generalisation using Unsupervised Domain Adaptation*, Computer Networks 2024, DOI 10.1016/j.comnet.2024.110398.
- Afonso et al., *Rethinking Phishing Detection*, IEEE ACIT 2025, DOI 10.1109/ACIT65614.2025.11185656.
- Misiek & Hyla, IEEE Access 2026, DOI 10.1109/ACCESS.2026.3672690.
- CompPhish V4, DOI 10.17632/fmbs4kp9wz.4.
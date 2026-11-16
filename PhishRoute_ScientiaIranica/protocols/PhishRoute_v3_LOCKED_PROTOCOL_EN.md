# PhishRoute v3 final diagnostic protocol — defined after reviewing v1/v2

**Status:** Post-hoc follow-up protocol, NOT externally preregistered. Fixed implementation, predeclared seeds, representations, overlap policies, and threshold targets. Target: Scientia Iranica Transactions D. Claims to be decided after real results and related-work assessment.

## Research question

Do conclusions about generalization of URL-based phishing classifiers remain stable under (i) bidirectional transfer between two independent public sources, (ii) strict versus permissive domain-overlap exclusion, (iii) source-only operating-point calibration and (iv) three independent source-internal registered-domain group partitions? Does presentation ablation improve cross-source FPR **without** an unacceptable cost in phishing recall?

## Data and code constraints

Original source UCI PhiUSIIL (2024), original Mendeley LegitPhish V2 (2025), original Mendeley URL-Phish V2 (2026). Internal positive class is phishing=1; original PhiUSIIL/LegitPhish label is phishing=0 and URL-Phish phishing=1. No source-supplied numerical features; all URL features are computed with one identical lexical extractor. All exact-URL duplicates within a source are removed; conflicting labels for identical URL are quarantined. Cross-source exact conflicts are counted and not resolved by assumption. File SHA256 checksums recorded.

## Training and partitions

Two training origins are evaluated separately: PhiUSIIL and URL-Phish. Three registered-domain group partitions use seeds 42, 52 and 62 and approximately 60/20/20 train/calibration/internal test proportions. LegitPhish is excluded as a training origin due to its small, source-disjoint benign support after primary overlap filtering, but retained as an external descriptive source with transparent sample counts. External tests never influence model training or decision thresholds.

## Models and thresholds

HGB classifier with max_leaf_nodes=25, max_depth=5, min_samples_leaf=30, max_iter=130, learning_rate=.07, l2_regularization=1, no early stopping. Four feature representations: full raw URL lexical, scheme-and-www presentation-ablated (changes extracted features, NOT underlying website), hostname-only diagnostic, formatting-only LR diagnostic. Calibration thresholds target upper bounds of FPR 0.5%, 1%, and 2% on source negatives. Evaluate internal and strict-external at all thresholds without tuning external labels. Report realized calibration FPR because ties affect feasibility.

## Overlap sensitivity and definition of independence

`strict_all`: exclude every external sample with any registered domain found anywhere in training source, including its held-out internal test group. This is the only primary cross-source estimate. `training_cal_domains`: remove groups in training plus calibration partitions; this admits domains in the source's internal test, so it is exploratory. `exact_urls`: remove exact URL overlaps only; external registered-domain overlap remains. `unfiltered`: contamination stress test, NOT independent validation. All four policies are reported without cherry-picking.

## Metrics

External and internal confusion counts, FPR, phishing recall, F1, MCC, ROC-AUC and PR-AUC, Brier score, and illustrative weighted loss (false positive cost=10 and false negative cost=1 per 1000 URLs). These costs are **not empirically estimated**, so weighted loss cannot be interpreted as financial/economic effectiveness. Data prevalence and class diversity are part of every interpretation. Registered-domain clustered paired bootstrap (400 resamples) compares ablated versus raw only at seed 42, strict-all, 1% calibration FPR. CIs describe sampling uncertainty, not systematic source bias.

## Inference gate and limitations

Outcomes with fewer than 100 examples of either class or fewer than 20 distinct registered domains in either class are explicitly flagged as weak; strict external evaluations that retain under 10% of either original source class are also flagged as fragile (a descriptive safeguard, not a guarantee of validity). No model uses real-time URL crawling. Sampling times, labeling criteria and source populations differ between corpora, so cross-corpus comparisons cannot isolate causes or represent prospective deployment risk. Repeated group splits have correlated data and do not count as independent study replications. The prior v1/v2 results informed this protocol; do not call this a blinded confirmatory experiment.

## Submission gate

A Q2 journal submission is not recommended until literature comparison establishes a distinct engineering/methodological contribution beyond the 2025 IEEE ACIT study *Rethinking Phishing Detection: How Dataset Quality Affects Model Generalization*, the outcomes hold with strict domain independence and two-way transfer, and the final paper includes full reproducibility and source-bias disclaimers. Null results must remain in the paper.
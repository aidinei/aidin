# PhishRoute / Scientia Iranica Research Artifacts

Research code and **archived negative-result evidence** for:

**When Domain Exclusion Changes the Evaluation Population in Cross-Corpus Phishing URL Detection**  
Author: Alireza Esmaeili Jobani · Department of Computer Engineering, Istanbul Aydin University, Türkiye  
Target journal: *Scientia Iranica*, Transactions D (manuscript in preparation; **not** accepted or peer reviewed).

## Scope and limitations

The analyses audit cross-corpus phishing URL detection under registered-domain overlap exclusion, source-only threshold calibration, and class-specific retention. The authors do **not** claim that CCPS feature selection or SCOMS operational selection improved performance across held-out corpora. For SCOMS, the prespecified success criterion was not met. Strict-unseen results estimate performance **conditional on remaining after domain exclusion**, not necessarily performance on the original full target population.

**Exploratory provenance:** v3–v5 protocols were developed after earlier experiment results had been inspected; the study is retrospective and does not claim pristine prospective validation.

## Reproduction

See `PhishRoute_ScientiaIranica/notebooks/` for three executable Kaggle notebooks:

- `PhishRoute_v3_FINAL_Kaggle.ipynb`: transfer, overlap-policy, and operating-threshold sensitivity analysis
- `CCPS_URL_FULL_STUDY_Kaggle.ipynb`: class-conditional provenance stability feature-selection study
- `SCOMS_FINAL_FULL_STUDY_Kaggle.ipynb`: source-constrained operational model selection and fallback rules

Each notebook requires the original, separately downloaded input datasets. Source URLs:

1. [PhiUSIIL (UCI)](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset)
2. [LegitPhish V2](https://data.mendeley.com/datasets/hx4m73v2sf/2)
3. [URL-Phish V2](https://data.mendeley.com/datasets/65z9twcx3r/2)
4. [CompPhish V4](https://data.mendeley.com/datasets/fmbs4kp9wz/4) (the mapping spreadsheet suffices for URL-only experiments).

Input files are **not** redistributed here. For reproducing the **published numeric rows**, preserve original parsing, labels (positive=phishing), splits, thresholds, and corpus-exclusion rules. Use Kaggle `Add Input`, then `Run All`. The exact published results may depend on library versions; notebooks specify dependencies and the accompanying run artifacts describe configuration.

## Dataset audit warning

Removing registered domains shared with source corpora can radically alter the retained class composition. In the archived SCOMS strict-unseen LegitPhish test, only **66 of 37,380 benign samples** remain, so that test is **not** treated as a representative primary external assessment.

## Data availability and transparency

The `analysis/` directory contains minimal, de-identified tables and scripts for the manuscript's retention-aware logical bounds. Extended archived Kaggle model output files and validation logs can be provided as supplementary files with the submission; **do not infer that they are present here unless they are listed in the repository**. No claim of a Zenodo DOI is made here.

The reported bounds are *logical identification bounds*, **not** confidence intervals. No new detector superiority is asserted by this repository.

## License and reuse

No software license is granted by default pending the author's selection. Third-party datasets retain their respective licenses; download from the providers directly.

## Contact

Corresponding author: Alireza Esmaeili Jobani · alirezajobani@stu.aydin.edu.tr

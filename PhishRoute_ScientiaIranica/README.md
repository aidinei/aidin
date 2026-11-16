# PhishRoute: Reproducible Research Package

This directory contains archived, de-identified study artifacts for the manuscript *When Domain Exclusion Changes the Evaluation Population in Cross-Corpus Phishing URL Detection* (target: Scientia Iranica, Transactions D).

- `notebooks/`: v3 cross-corpus audit, v4 CCPS and v5 SCOMS full Kaggle notebooks.
- `protocols/`: archived, frozen-after-earlier-experiments study protocols. This is retrospective/exploratory, **not preregistered**.
- `analysis/`: published class retention, operating metrics, model selection, primary paired comparisons, and partial-identification bounds. `reproduce_table5.py` reconstructs Table 5 from archived v5 CSVs.

The algorithms CCPS and SCOMS did **not** meet the required generalization improvement criteria. A high F1, selected subset FPR, or low fallback FPR must not be interpreted as evidence of a successful novel detector.

There are **no raw phishing URL dumps**, user identifiers, personal browsing histories, or vendor-restricted datasets here. Download original corpora from their maintainers (links in repository root README).

Repository publication does **not** constitute journal acceptance, independent prospective validation, endorsement, or an archived DOI. A fixed release/tag and optional Zenodo archive can be added after the author approves the archival version.

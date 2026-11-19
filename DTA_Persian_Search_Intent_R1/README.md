# Persian Search Intent Classification — DTA reproducibility archive

Reproducibility materials accompanying the **revised** manuscript **DTA-10-2026-1387.R1**, *Domain-Aware Persian Search Intent Classification from Real-World Search Console Logs*. **Revision under consideration; not a published or accepted article.**

## Contents

- `data/source_anonymized_query_dataset.csv` — **546 human-adjudicated, anonymized** Persian query texts, broad domain categories and final five-class intent labels. Original GSC clicks, impressions, CTR, ranking, URLs, site identities and raw exports are excluded. Preserve row order and zero-based source ID; only 544 unique normalized texts occur due to masked `[brand]` placeholders.
- `code/full_transformer_r1_gpu_546.py` — experiment runner **as archived**, for 72 SVM, multilingual sentence-embedding SVM and ParsBERT comparisons: stratified holdouts, 3-seed 5-fold CV, LODO and few-shot adaptation. The dataset is copied beside the script for direct execution.
- `code/DTA_R1_546_Full_Reevaluation_Colab.ipynb` — the previously executed Colab notebook; choose a GPU runtime and upload the included `DTA_R1_GPU_546_Source_Package.zip` at its prompt. Does **not** call OpenAI API.
- `code/dta_cpu_benchmark_recorded.py` and the CPU Notebook — common-CPU timing protocol and its recorded artifacts. Hardware, library versions and model acquisition affect timings.
- `recorded_evidence/` — per-split predictions, metrics, confusion matrices, selected training settings, model-run manifests and common-CPU benchmark reports.
- `code/verify_recorded_results.py` — offline check that recomputes and validates saved accuracy, five-class macro-F1 and split IDs without GPU or network access.
- `annotation_protocol/` — archived labeling rules; **historical prompt excerpt attested by author**; separately named *reconstructed* historical operational prompt; and the *exact logged prompt* for the new 18 Nov 2026 LLM replication. These documents are **not interchangeable**.

## Run

1. Create Python environment and install packages from `code/requirements_gpu.txt`, plus a PyTorch build suitable for your CPU/GPU.
2. GPU rerun: in Colab upload `code/DTA_R1_546_Full_Reevaluation_Colab.ipynb`, select NVIDIA T4 GPU and upload `DTA_R1_GPU_546_Source_Package.zip` when prompted; or run `python code/full_transformer_r1_gpu_546.py` from the top-level folder (requires GPU and downloads model weights from Hugging Face).
3. Metrics-only audit: `python code/verify_recorded_results.py` (see script for its input expectations). Results from the archived 72 runs are stored under `recorded_evidence/gpu_evidence_546`.
4. Common-CPU benchmark: see the CPU notebook. Its archived copy uses the original training/test manifest and hardware details. Review scripts before running in a different Colab environment.

**Historical nuance:** the author reports using the OpenAI model `gpt-4.1-mini-2025-04-14` for original LLM-assisted labeling. The original API request metadata were not preserved. The original wording provided by the author and the archived operational rule file disagree on tie-breaking order (Local vs Transactional); the project therefore retained both artifacts and used independent human adjudication. The **18 November 2026** replication with the same model ID is logged separately and is *not* an original-run API log. The original GSC export was dated **15 June 2026**, with date filter **Last 12 months**; author reports a study window of **15 June 2025 to 15 June 2026**. Query-specific daily timestamps are not present.

## Privacy, scope, and reuse

All three properties are reported as author-owned. The 546-text dataset has been anonymized and screened heuristically for emails, URLs, and phone-like strings; this is **not a formal guarantee** of anonymization. Do not attempt to re-identify the underlying Search Console properties or individual searchers. Raw logs and personally identifying exports are not provided. The paper analyzes *pilot* domain-dependent classification, not universal Persian search-intent generalization.

**License:** No additional reuse license is granted by the public posting. For re-distribution, contact the repository owner. GitHub visibility should not be interpreted as a license or consent to reidentify.

## Peer-review anonymization warning

This GitHub repository belongs to the researcher. **A personal GitHub URL can compromise double-anonymous peer review.** If the journal uses double-anonymous reviewing, share this link with the editorial office as confidential material rather than inserting the identifying URL into the blinded manuscript or reviewer-facing response without editorial approval.

## Contact and citation

Reference the revised manuscript by its ID **DTA-10-2026-1387.R1** pending a publication DOI. Do not cite it as an accepted publication.

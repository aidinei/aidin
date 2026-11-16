"""Recompute partial-identification bounds in manuscript Table 5.
Run from the project root: python PhishRoute_ScientiaIranica/analysis/reproduce_table5.py
Reads only archived SCOMS class-retention and outer-performance CSVs.
No model retraining or target-specific tuning.
"""
import csv
from pathlib import Path

DIR = Path(__file__).resolve().parent
def read_csv(filename):
    with (DIR / filename).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

retention = read_csv("SCOMS_Table_Class_Retention.csv")
performance = read_csv("SCOMS_Table_Outer_Performance.csv")
observed = read_csv("Table5_Identification_Bounds.csv")
for corpus in ["PhiUSIIL", "URL-Phish", "LegitPhish", "CompPhish"]:
    row = next(r for r in retention if r["target"] == corpus and r["policy"] == "strict_unseen")
    p = next(r for r in performance if r["target"] == corpus and r["policy"] == "strict_unseen" and r["model"] == "SCOMS_selected")
    r = float(row["retention_benign"])
    fpr_ret = float(p["FPR"])
    low, high = r * fpr_ret, r * fpr_ret + 1 - r
    assert 0 <= low <= high <= 1
    print(f"{corpus}: retention={100*r:.5f}%, strict FPR={100*fpr_ret:.5f}%, compatible full-target FPR=[{100*low:.5f}%, {100*high:.5f}%]")

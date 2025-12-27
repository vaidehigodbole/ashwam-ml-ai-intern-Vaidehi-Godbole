**Project Title: Evidence-Grounded Extraction and Evaluation**
This project implements a small evaluation pipeline that extracts information from journal entries and scores the extracted results against a golden reference. The goal is to extract evidence-based information without hallucination and evaluate performance using objective metrics.

**Project Description**
The system reads journal entries from a dataset, identifies phrases related to symptoms, food, and mind/emotional states, and extracts them only if they appear directly in the text. Each extraction includes polarity, intensity or arousal, and a time bucket (today, last_night, past_week, unknown). The predictions are compared with the gold dataset to calculate precision, recall, F1 score, and other evaluation metrics.

**This project focuses on:**

Evidence-grounded extraction (no hallucination)

Deterministic outputs (same input gives same result)

Evaluation without canonical label mapping

Objective scoring based on exact evidence spans

**How to Run the Project**

Make sure you are inside the project folder and run the following command:

python -m project

After running, two output files will be created in the "out" folder:

predictions.jsonl

score_summary.json

**Project Structure**

ashwam_eval/
data/ (contains input journals and gold references)
out/ (automatically generated outputs)
project/ (contains extractor, scorer, and main CLI file)

**Extraction Schema Used**

domain: symptom, food, mind (no canonical mapping)
label_free_text: phrase as it appears in the journal
evidence_span: exact substring from the text (required)
polarity: present, absent, uncertain
intensity_or_arousal: low, medium, high, unknown
time_bucket: today, last_night, past_week, unknown

**Example Score Output**

precision: 0.50
recall: 0.60
f1: 0.55

**Key Rules Followed**

Every extracted span must appear in the original text (no hallucination).

If the information is unclear, the system uses “uncertain”.

No canonical labels or fixed vocabulary are used.

Extraction logic is deterministic and rule-based.

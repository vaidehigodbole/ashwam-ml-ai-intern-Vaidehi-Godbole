import json

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def match(gold_items, pred_items):
    pairs = []
    for g in gold_items:
        for p in pred_items:
            if g["evidence_span"].lower() == p["evidence_span"].lower() and g["domain"] == p["domain"]:
                pairs.append((g,p))
                break
    return pairs

def score(predictions, golds):
    total_tp, total_fp, total_fn = 0, 0, 0
    correct_pol, correct_bucket, correct_time = 0, 0, 0

    for pred, gold in zip(predictions, golds):
        g_items = gold["extractions"]
        p_items = pred["extractions"]

        matched = match(g_items, p_items)
        tp = len(matched)
        fp = len(p_items) - tp
        fn = len(g_items) - tp

        total_tp += tp
        total_fp += fp
        total_fn += fn

        for g,p in matched:
            if g["polarity"] == p["polarity"]:
                correct_pol += 1
            if g["intensity_or_arousal"] == p["intensity_or_arousal"]:
                correct_bucket += 1
            if g["time_bucket"] == p["time_bucket"]:
                correct_time += 1

    precision = total_tp / (total_tp + total_fp + 1e-9)
    recall = total_tp / (total_tp + total_fn + 1e-9)
    f1 = 2 * precision * recall / (precision + recall + 1e-9)

    return {
        "precision": round(precision, 2),
        "recall": round(recall, 2),
        "f1": round(f1, 2),
        "polarity_accuracy": correct_pol,
        "bucket_accuracy": correct_bucket,
        "time_accuracy": correct_time
    }

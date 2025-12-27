import json

# Keyword groups for simple extraction
SYMPTOMS = ["head", "nausea", "tight", "pain", "hurt"]
FOOD = ["pasta", "breakfast", "chips", "orange juice", "coffee"]
MIND = ["anxiety", "mind racing", "low energy"]

def detect_domain(span):
    s = span.lower()
    if any(w in s for w in SYMPTOMS): return "symptom"
    if any(w in s for w in FOOD): return "food"
    if any(w in s for w in MIND): return "mind"
    return "unknown"

def detect_polarity(span):
    text = span.lower()
    if "not" in text or "no " in text or "skipped" in text:
        return "absent"
    if "maybe" in text or "not sure" in text:
        return "uncertain"
    return "present"

def detect_intensity(span):
    text = span.lower()
    if "mild" in text or "low" in text: return "low"
    if "heavy" in text or "high" in text or "racing" in text: return "high"
    return "unknown"

def detect_time(text):
    text = text.lower()
    if "today" in text: return "today"
    if "last night" in text or "yesterday" in text: return "last_night"
    if "week" in text: return "past_week"
    return "unknown"

def extract_spans(text):
    results = []
    for word_list in [SYMPTOMS, FOOD, MIND]:
        for word in word_list:
            if word in text.lower():
                results.append(word)
    return results

def load_journals(path):
    with open(path, "r") as f:
        return [json.loads(line) for line in f]

def extract_all(journals):
    all_out = []
    for j in journals:
        text = j["text"]
        spans = extract_spans(text)
        objects = []
        for span in spans:
            objects.append({
                "domain": detect_domain(span),
                "label_free_text": span,
                "evidence_span": span,
                "polarity": detect_polarity(text),
                "intensity_or_arousal": detect_intensity(text),
                "time_bucket": detect_time(text)
            })
        out = {"journal_id": j["id"], "extractions": objects}
        all_out.append(out)
    return all_out

from .extractor import load_journals, extract_all
from .scorer import score, load_jsonl
import json

def main():
    journals = load_journals("./data/journals.jsonl")
    gold = load_jsonl("./data/gold.jsonl")

    predictions = extract_all(journals)

    # Save predictions
    with open("./out/predictions.jsonl", "w") as f:
        for p in predictions:
            f.write(json.dumps(p) + "\n")

    results = score(predictions, gold)

    # Save scores
    with open("./out/score_summary.json", "w") as f:
        json.dump(results, f, indent=2)

    print("🎉 Pipeline executed successfully!")

if __name__ == "__main__":
    main()

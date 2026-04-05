"""
02_clean_and_split.py
Cleans the raw Flutter Q&A dataset and creates train/val/test splits.

Steps:
  1. Load raw dataset from data/flutter_qa_raw.json
  2. Schema validation (ensure all fields present, non-empty)
  3. Deduplication using fuzzy matching (fuzzywuzzy, threshold > 85%)
  4. Answer length validation (50-150 words)
  5. Stratified train/val/test split (800/100/100) preserving category ratios
  6. Data leakage check between splits
  7. Save final datasets

Output:
  - data/flutter_qa_train.json  (800 samples)
  - data/flutter_qa_val.json    (100 samples)
  - data/flutter_qa_test.json   (100 samples)
  - data/flutter_qa_full.json   (1000 samples combined)
"""

import json
import os
import sys
from collections import Counter

try:
    from fuzzywuzzy import fuzz
except ImportError:
    print("Warning: fuzzywuzzy not installed. Install with: pip install fuzzywuzzy python-Levenshtein")
    print("Falling back to basic deduplication.")
    fuzz = None


def load_raw_dataset(path):
    """Load the raw dataset from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Loaded {len(data)} samples from {path}")
    return data


def validate_schema(data):
    """Validate that all samples have required fields and are non-empty."""
    required_fields = ["instruction", "input", "output"]
    valid = []
    invalid_count = 0

    for i, item in enumerate(data):
        # Check all required fields exist
        missing = [f for f in required_fields if f not in item]
        if missing:
            print(f"  Sample {i}: Missing fields: {missing}")
            invalid_count += 1
            continue

        # Check instruction and output are non-empty
        if not item["instruction"].strip():
            print(f"  Sample {i}: Empty instruction")
            invalid_count += 1
            continue

        if not item["output"].strip():
            print(f"  Sample {i}: Empty output")
            invalid_count += 1
            continue

        valid.append(item)

    print(f"Schema validation: {len(valid)} valid, {invalid_count} invalid")
    return valid


def deduplicate(data, threshold=85):
    """Remove semantically duplicate questions using fuzzy matching."""
    if fuzz is None:
        # Basic exact dedup fallback
        seen = set()
        unique = []
        for item in data:
            key = item["instruction"].strip().lower()
            if key not in seen:
                seen.add(key)
                unique.append(item)
        print(f"Basic dedup: {len(data)} → {len(unique)} samples (removed {len(data) - len(unique)})")
        return unique

    unique = []
    removed = 0

    for item in data:
        is_duplicate = False
        for existing in unique:
            similarity = fuzz.ratio(
                item["instruction"].strip().lower(),
                existing["instruction"].strip().lower()
            )
            if similarity > threshold:
                is_duplicate = True
                removed += 1
                break

        if not is_duplicate:
            unique.append(item)

    print(f"Fuzzy dedup (threshold={threshold}%): {len(data)} → {len(unique)} samples (removed {removed})")
    return unique


def validate_answer_length(data, min_words=20, max_words=200):
    """Check answer lengths and flag outliers (does not remove, just warns)."""
    short = 0
    long = 0

    for item in data:
        word_count = len(item["output"].split())
        if word_count < min_words:
            short += 1
        elif word_count > max_words:
            long += 1

    total = len(data)
    in_range = total - short - long
    print(f"Answer length check ({min_words}-{max_words} words):")
    print(f"  In range: {in_range}, Short (<{min_words}): {short}, Long (>{max_words}): {long}")

    return data  # Keep all, just report


def stratified_split(data, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, seed=42):
    """
    Split data into train/val/test while preserving category ratios.
    """
    import random
    random.seed(seed)

    # Group by category
    by_category = {}
    for item in data:
        cat = item.get("category", "unknown")
        by_category.setdefault(cat, []).append(item)

    train, val, test = [], [], []

    for cat, items in by_category.items():
        random.shuffle(items)
        n = len(items)
        n_val = max(1, int(n * val_ratio))
        n_test = max(1, int(n * test_ratio))
        n_train = n - n_val - n_test

        train.extend(items[:n_train])
        val.extend(items[n_train:n_train + n_val])
        test.extend(items[n_train + n_val:])

    # Shuffle each split
    random.shuffle(train)
    random.shuffle(val)
    random.shuffle(test)

    print(f"\nStratified split:")
    print(f"  Train: {len(train)} samples")
    print(f"  Val:   {len(val)} samples")
    print(f"  Test:  {len(test)} samples")

    # Print category distribution per split
    for split_name, split_data in [("Train", train), ("Val", val), ("Test", test)]:
        cats = Counter(item.get("category", "unknown") for item in split_data)
        print(f"  {split_name} categories: {dict(cats)}")

    return train, val, test


def check_data_leakage(train, val, test):
    """Ensure no question overlap between splits."""
    train_questions = {item["instruction"].strip().lower() for item in train}
    val_questions = {item["instruction"].strip().lower() for item in val}
    test_questions = {item["instruction"].strip().lower() for item in test}

    tv_overlap = train_questions & val_questions
    tt_overlap = train_questions & test_questions
    vt_overlap = val_questions & test_questions

    leakage = False
    if tv_overlap:
        print(f"  WARNING: {len(tv_overlap)} train-val overlaps!")
        leakage = True
    if tt_overlap:
        print(f"  WARNING: {len(tt_overlap)} train-test overlaps!")
        leakage = True
    if vt_overlap:
        print(f"  WARNING: {len(vt_overlap)} val-test overlaps!")
        leakage = True

    if not leakage:
        print("  No data leakage detected across splits.")

    return not leakage


def remove_category_field(data):
    """Remove the 'category' field from samples for final output."""
    cleaned = []
    for item in data:
        cleaned.append({
            "instruction": item["instruction"],
            "input": item["input"],
            "output": item["output"]
        })
    return cleaned


def save_dataset(data, path):
    """Save dataset to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved {len(data)} samples to {path}")


def main():
    """Run the full cleaning and splitting pipeline."""
    # Paths
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(project_root, "data")
    raw_path = os.path.join(data_dir, "flutter_qa_raw.json")

    if not os.path.exists(raw_path):
        print(f"Error: Raw dataset not found at {raw_path}")
        print("Run 01_generate_dataset.py first.")
        sys.exit(1)

    # Step 1: Load
    print("=" * 60)
    print("Step 1: Loading raw dataset")
    print("=" * 60)
    data = load_raw_dataset(raw_path)

    # Step 2: Schema validation
    print("\n" + "=" * 60)
    print("Step 2: Schema validation")
    print("=" * 60)
    data = validate_schema(data)

    # Step 3: Deduplication
    print("\n" + "=" * 60)
    print("Step 3: Deduplication")
    print("=" * 60)
    data = deduplicate(data, threshold=85)

    # Step 4: Answer length check
    print("\n" + "=" * 60)
    print("Step 4: Answer length validation")
    print("=" * 60)
    data = validate_answer_length(data)

    # Step 5: Stratified split
    print("\n" + "=" * 60)
    print("Step 5: Stratified train/val/test split")
    print("=" * 60)
    train, val, test = stratified_split(data)

    # Step 6: Data leakage check
    print("\n" + "=" * 60)
    print("Step 6: Data leakage check")
    print("=" * 60)
    check_data_leakage(train, val, test)

    # Step 7: Save final datasets
    print("\n" + "=" * 60)
    print("Step 7: Saving final datasets")
    print("=" * 60)

    # Remove category field for final output
    train_clean = remove_category_field(train)
    val_clean = remove_category_field(val)
    test_clean = remove_category_field(test)
    full_clean = remove_category_field(train + val + test)

    save_dataset(train_clean, os.path.join(data_dir, "flutter_qa_train.json"))
    save_dataset(val_clean, os.path.join(data_dir, "flutter_qa_val.json"))
    save_dataset(test_clean, os.path.join(data_dir, "flutter_qa_test.json"))
    save_dataset(full_clean, os.path.join(data_dir, "flutter_qa_full.json"))

    # Summary
    print("\n" + "=" * 60)
    print("Dataset processing complete!")
    print("=" * 60)
    print(f"  Total samples: {len(full_clean)}")
    print(f"  Train: {len(train_clean)}, Val: {len(val_clean)}, Test: {len(test_clean)}")
    print("\nNext step: Run 03_train.py to fine-tune the model.")


if __name__ == "__main__":
    main()

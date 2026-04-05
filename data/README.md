# Flutter Q&A Dataset

## Overview

This dataset contains **1000 Flutter interview question-answer pairs** in Alpaca-style instruction format, designed for fine-tuning a Large Language Model for domain-specific question answering.

## Data Source & Generation Method

- **Source:** Synthetically generated using structured domain knowledge
- **Validation:** All answers verified against official Flutter documentation (docs.flutter.dev)
- **Format:** JSON with Alpaca instruction format

## Schema

Each sample follows this structure:

```json
{
  "instruction": "What is StatefulWidget in Flutter?",
  "input": "",
  "output": "A StatefulWidget is a widget in Flutter that maintains mutable state..."
}
```

| Field         | Type   | Description                                |
|---------------|--------|--------------------------------------------|
| `instruction` | string | The Flutter-related question               |
| `input`       | string | Additional context (empty for this task)   |
| `output`      | string | Expected answer — concise, accurate        |

## Category Distribution

| Category     | Topics Covered                                              | Count |
|-------------|-------------------------------------------------------------|-------|
| Basic        | Flutter overview, Dart basics, widget types, hot reload     | ~300  |
| Intermediate | Widget lifecycle, navigation, layouts, forms, animations    | ~400  |
| Advanced     | State management, performance, platform channels, testing   | ~300  |

## Train/Val/Test Split

| Split       | File                      | Count | Purpose                  |
|-------------|---------------------------|-------|--------------------------|
| Training    | `flutter_qa_train.json`   | ~800  | Model fine-tuning         |
| Validation  | `flutter_qa_val.json`     | ~100  | Hyperparameter tuning     |
| Test        | `flutter_qa_test.json`    | ~100  | Final evaluation          |
| Full        | `flutter_qa_full.json`    | ~1000 | Combined reference         |

**Split methodology:** Stratified random split preserving category ratios (seed=42).

## Cleaning Steps Applied

1. **Schema validation:** All three fields present and non-empty
2. **Deduplication:** Fuzzy matching with fuzzywuzzy (threshold > 85% similarity)
3. **Answer length check:** Target range 20-200 words per answer
4. **Data leakage check:** No question overlap between train/val/test splits
5. **Consistency check:** Uniform tone and formatting

## Answer Characteristics

- Length: 2-4 sentences (50-150 words typical)
- Style: Technically accurate, concise, and self-contained
- Coverage: Conceptual, practical, and comparison-type questions
- Verified against Flutter official documentation

## Usage

Generate the raw dataset:
```bash
python scripts/01_generate_dataset.py
```

Clean and split:
```bash
python scripts/02_clean_and_split.py
```

## File Structure

```
data/
├── flutter_qa_raw.json        # Raw generated data (before cleaning)
├── flutter_qa_train.json      # Training split
├── flutter_qa_val.json        # Validation split
├── flutter_qa_test.json       # Test split
├── flutter_qa_full.json       # All samples combined
└── README.md                  # This file
```

# Fine-Tuning Mistral 7B for Flutter Domain-Specific Question Answering

## Overview

This project fine-tunes **Mistral 7B Instruct v0.2** using **QLoRA (Quantized Low-Rank Adaptation)** to build a specialized Flutter interview question answering system.

Pre-trained LLMs are general-purpose and often produce generic or inaccurate answers for domain-specific questions. By fine-tuning on a curated Flutter Q&A dataset, the model learns to generate precise, context-aware answers suitable for interview preparation and developer assistance.

## Project Structure

```
├── data/                          # Dataset files
│   ├── flutter_qa_train.json      # Training set (800 samples)
│   ├── flutter_qa_val.json        # Validation set (100 samples)
│   ├── flutter_qa_test.json       # Test set (100 samples)
│   └── README.md                  # Dataset documentation
├── scripts/
│   ├── 01_generate_dataset.py     # Synthetic dataset generation
│   ├── 02_clean_and_split.py      # Cleaning, dedup, and train/val/test split
│   ├── 03_train.py                # QLoRA fine-tuning pipeline
│   ├── 04_evaluate.py             # Automated evaluation (BLEU, ROUGE, F1)
│   └── 05_inference.py            # Inference & comparison demo
├── outputs/
│   ├── model/                     # Saved LoRA adapter weights
│   ├── logs/                      # Training logs
│   └── results/                   # Evaluation results
├── report/
│   └── report.pdf                 # Final report (8-10 pages)
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Tech Stack

| Component        | Choice                              |
|------------------|-------------------------------------|
| Base Model       | Mistral 7B Instruct v0.2            |
| Fine-Tuning      | QLoRA + PEFT (LoRA rank=8)          |
| Quantization     | 4-bit NormalFloat (NF4)             |
| Training Library | HuggingFace TRL (SFTTrainer)        |
| Platform         | Google Colab / Kaggle (T4 GPU)      |
| Dataset          | 1000 Flutter Q&A pairs (Alpaca fmt) |

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate Dataset
```bash
python scripts/01_generate_dataset.py
```

### 3. Clean & Split Dataset
```bash
python scripts/02_clean_and_split.py
```

### 4. Fine-Tune Model
```bash
python scripts/03_train.py
```

### 5. Evaluate
```bash
python scripts/04_evaluate.py
```

### 6. Run Inference
```bash
python scripts/05_inference.py --question "What is StatefulWidget in Flutter?"
```

## Dataset

- **Size:** 1000 Q&A pairs (800 train / 100 val / 100 test)
- **Format:** Alpaca-style JSON (instruction, input, output)
- **Categories:** Basic (300), Intermediate (400), Advanced (300)
- **Source:** Synthetically generated + manually validated

## Model Details

- **Architecture:** Transformer (Decoder-only), 7.24B parameters
- **LoRA Config:** rank=8, alpha=16, dropout=0.05, targets=q_proj+v_proj
- **Trainable Params:** ~4-8M (< 0.1% of total)
- **GPU Memory:** ~6-8 GB (vs ~28 GB for full fine-tune)

## Evaluation Metrics

| Metric      | Base Model (expected) | Fine-Tuned (target) |
|-------------|----------------------|---------------------|
| Avg BLEU    | 0.10 – 0.20         | 0.50 – 0.70        |
| Avg ROUGE-L | 0.15 – 0.25         | 0.55 – 0.75        |
| Human Score | 2.0 – 3.0 / 5       | 4.0 – 4.5 / 5      |

## License

This project is for educational purposes (Assignment-2: Generative AI & LLMs).

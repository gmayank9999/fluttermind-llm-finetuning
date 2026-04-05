# 📘 Implementation Plan: Fine-Tuning an LLM for Flutter Domain-Specific Question Answering

---

## 1. 📌 Project Overview

This project focuses on fine-tuning a pre-trained Large Language Model (LLM) to perform **domain-specific question answering** in the **Flutter development domain**.

Pre-trained models are general-purpose and may lack depth in specific domains. Fine-tuning enables the model to learn structured, accurate, and context-aware answers for Flutter-related questions — making it suitable for interview preparation, developer onboarding, and quick reference.

---

## 2. 🎯 Problem Definition

### Problem

Pre-trained LLMs are trained on large general-purpose datasets and may not perform well on domain-specific tasks. When asked Flutter-specific questions, base models often produce generic, incomplete, or inaccurate responses that lack the depth expected from a specialized assistant.

### Objective

Build a **Flutter Interview Question Answering System** that:

- Takes a Flutter-related question as input
- Generates accurate, concise, and domain-specific answers
- Outperforms the base model on Flutter-specific queries measurably

### Example

**Input:** What is StatefulWidget?
**Output:** A StatefulWidget is a widget in Flutter that maintains mutable state. Unlike StatelessWidget, it can rebuild its UI dynamically when its internal state changes during runtime using the setState() method. It consists of two classes — the StatefulWidget class itself and a corresponding State class that holds the mutable state.

---

## 3. 📊 Dataset Creation Strategy

### 3.1 Dataset Type

Synthetic dataset generated using LLM (ChatGPT / Claude) + manual curation and validation.

### 3.2 Dataset Size

| Split      | Count | Purpose                    |
| ---------- | ----- | -------------------------- |
| Training   | 800   | Model fine-tuning          |
| Validation | 100   | Hyperparameter tuning      |
| Test       | 100   | Final evaluation & metrics |
| **Total**  | **1000** | —                       |

### 3.3 Dataset Schema

Each data point follows the Alpaca-style instruction format:

```json
{
  "instruction": "What is the purpose of the BuildContext in Flutter?",
  "input": "",
  "output": "BuildContext is a reference to the location of a widget in the widget tree. It is used to obtain references to themes, media queries, and other inherited widgets. Each widget has its own BuildContext, which becomes the parent of the BuildContext for child widgets."
}
```

**Field Definitions:**

| Field         | Type   | Description                                   |
| ------------- | ------ | --------------------------------------------- |
| `instruction` | string | The Flutter-related question                   |
| `input`       | string | Additional context (empty for this task)       |
| `output`      | string | Expected answer — concise, accurate, complete  |

### 3.4 Dataset Categories

| Category     | Topics Covered                                             | Count |
| ------------ | ---------------------------------------------------------- | ----- |
| Basic        | Flutter overview, Dart basics, widget types, hot reload    | 300   |
| Intermediate | Widget lifecycle, navigation, layouts, forms, animations   | 400   |
| Advanced     | State management (Bloc, Provider, Riverpod), performance optimization, platform channels, testing, CI/CD | 300   |

### 3.5 Dataset Generation Process

#### Step 1: Generate Using LLM

Use ChatGPT / Claude with structured prompts:

```
Generate 100 Flutter interview Q&A pairs for the "Basic" category.
Topics: Flutter overview, Dart basics, widget types, hot reload, project structure.
Rules:
- Answers should be 2-4 sentences, technically accurate
- Cover conceptual, practical, and comparison-type questions
- Use JSON array format with keys: instruction, input, output
- "input" should always be an empty string
```

Repeat with category-specific prompts until ~1100 raw samples are collected (buffer for removal during cleaning).

#### Step 2: Manual Cleaning & Validation

- **Deduplication:** Remove semantically duplicate questions using fuzzy matching (e.g., fuzzywuzzy library with threshold > 85% similarity)
- **Accuracy check:** Verify all answers against official Flutter documentation (docs.flutter.dev)
- **Consistency:** Ensure uniform tone, answer length (50–150 words), and formatting
- **Balance check:** Verify category distribution matches the target split

#### Step 3: Schema Validation

Run a validation script to ensure:

- All three fields (`instruction`, `input`, `output`) are present in every sample
- No empty `instruction` or `output` fields
- No data leakage — test/validation questions do not overlap with training set
- Answer length is within acceptable range

#### Step 4: Save Final Dataset

```
data/
├── flutter_qa_train.json      (800 samples)
├── flutter_qa_val.json        (100 samples)
├── flutter_qa_test.json       (100 samples)
└── flutter_qa_full.json       (1000 samples — combined)
```

### 3.6 Dataset Documentation

A `data/README.md` file will be included describing:

- Data source and generation method
- Category distribution
- Cleaning steps applied
- Schema and format
- Train/val/test split methodology (stratified random split preserving category ratios)

---

## 4. 🤖 Model Selection

### Selected Model

**Mistral 7B Instruct v0.2** (`mistralai/Mistral-7B-Instruct-v0.2`)

### Model Architecture

| Property           | Detail                          |
| ------------------ | ------------------------------- |
| Architecture       | Transformer (Decoder-only)      |
| Parameters         | 7.24 Billion                    |
| Attention          | Grouped-Query Attention (GQA)   |
| Context Length      | 8192 tokens (extendable)       |
| Vocabulary Size    | 32,000 tokens                   |
| Hidden Dimension   | 4096                            |
| Layers             | 32                              |
| Attention Heads    | 32 (8 KV heads via GQA)        |

### Why Mistral 7B

- Lightweight enough to fine-tune on free-tier GPUs (Google Colab T4)
- Strong baseline performance for instruction-following tasks
- Open-source with permissive Apache 2.0 license
- Supports efficient fine-tuning via 4-bit quantization
- Active community and well-documented HuggingFace integration

---

## 5. ⚙️ Fine-Tuning Approach

### Method: QLoRA (Quantized Low-Rank Adaptation) with PEFT

| Component      | Role                                                        |
| -------------- | ----------------------------------------------------------- |
| **QLoRA**      | Combines 4-bit quantization with LoRA for memory efficiency |
| **LoRA**       | Injects trainable low-rank matrices into attention layers    |
| **PEFT**       | HuggingFace library for parameter-efficient fine-tuning      |
| **BitsAndBytes** | Enables 4-bit NormalFloat (NF4) quantization              |

### How LoRA Modifies the Model

Instead of updating all 7B parameters, LoRA freezes the base model and injects small trainable matrices (rank `r`) into the query and value projection layers of each transformer block. This reduces trainable parameters from ~7B to ~4–8M (< 0.1% of total), making fine-tuning feasible on consumer GPUs.

### Why This Approach

- Reduces GPU memory from ~28 GB (full fine-tune) to ~6–8 GB (QLoRA)
- Training time drops from days to 2–4 hours
- No significant quality loss compared to full fine-tuning for this task scale
- LoRA weights are small (~20–50 MB) and portable

---

## 6. 🛠️ System Setup

### 6.1 Environment

| Resource   | Specification                              |
| ---------- | ------------------------------------------ |
| Platform   | Google Colab (Free/Pro) or Kaggle Notebooks |
| GPU        | NVIDIA T4 (16 GB VRAM) — minimum           |
| RAM        | 12–16 GB system RAM                        |
| Storage    | ~15 GB (model + dataset + outputs)         |
| Python     | 3.10+                                      |

### 6.2 Required Libraries

```
# requirements.txt
transformers==4.40.0
datasets==2.19.0
peft==0.10.0
accelerate==0.29.0
bitsandbytes==0.43.0
trl==0.8.1
torch==2.2.0
scikit-learn==1.4.0
rouge-score==0.1.2
nltk==3.8.1
fuzzywuzzy==0.18.0
python-Levenshtein==0.25.0
```

Install command:

```bash
pip install -r requirements.txt
```

### 6.3 Project Directory Structure

```
flutter-llm-finetuning/
├── data/
│   ├── flutter_qa_train.json
│   ├── flutter_qa_val.json
│   ├── flutter_qa_test.json
│   └── README.md
├── scripts/
│   ├── 01_generate_dataset.py
│   ├── 02_clean_and_split.py
│   ├── 03_train.py
│   ├── 04_evaluate.py
│   └── 05_inference.py
├── outputs/
│   ├── model/                  (LoRA adapter weights)
│   ├── logs/                   (training logs)
│   └── results/                (evaluation outputs)
├── report/
│   └── report.pdf
├── requirements.txt
└── README.md
```

---

## 7. 🔄 Training Pipeline

### Step 1: Load Model & Tokenizer

- Load `Mistral-7B-Instruct-v0.2` from HuggingFace
- Enable 4-bit quantization using BitsAndBytes config:
  - `load_in_4bit = True`
  - `bnb_4bit_quant_type = "nf4"`
  - `bnb_4bit_compute_dtype = float16`
- Load tokenizer with `padding_side = "right"`

### Step 2: Apply LoRA Configuration

| Parameter        | Value                    |
| ---------------- | ------------------------ |
| `r` (rank)       | 8                        |
| `lora_alpha`     | 16                       |
| `lora_dropout`   | 0.05                     |
| `target_modules` | `["q_proj", "v_proj"]`   |
| `bias`           | `"none"`                 |
| `task_type`      | `"CAUSAL_LM"`            |

### Step 3: Dataset Preprocessing & Formatting

Convert each sample into the Mistral instruction prompt template:

```
<s>[INST] Answer the following Flutter development question accurately and concisely.

Question: {instruction} [/INST]
{output}</s>
```

Preprocessing steps:
- Tokenize using the model's tokenizer
- Set `max_length = 512` (sufficient for Q&A pairs)
- Apply padding and truncation
- Create attention masks
- Save as HuggingFace `Dataset` object

### Step 4: Training Configuration

| Parameter              | Value               |
| ---------------------- | ------------------- |
| Epochs                 | 3                   |
| Per-device batch size  | 2                   |
| Gradient accumulation  | 4 (effective batch = 8) |
| Learning rate          | 2e-4                |
| LR scheduler           | Cosine              |
| Warmup ratio           | 0.05                |
| Weight decay           | 0.01                |
| Max gradient norm      | 0.3                 |
| Logging steps          | 10                  |
| Save strategy          | Per epoch           |
| Eval strategy          | Per epoch           |
| FP16                   | True                |

### Step 5: Train

- Use `SFTTrainer` from the `trl` library (preferred over base Trainer for instruction tuning)
- Monitor training loss and validation loss per epoch
- Save LoRA adapter weights after training to `outputs/model/`
- Save training logs for loss curve plotting

### Step 6: Merge & Export (Optional)

- Merge LoRA adapter with base model for standalone deployment
- Save merged model for easier inference

---

## 8. 🔍 Inference Pipeline

### Loading the Fine-Tuned Model

```python
# Pseudocode
base_model = load_model("mistralai/Mistral-7B-Instruct-v0.2", quantization=4bit)
model = PeftModel.from_pretrained(base_model, "outputs/model/")
```

### Running Inference

```python
prompt = "<s>[INST] Answer the following Flutter development question accurately and concisely.\n\nQuestion: What is hot reload in Flutter? [/INST]"
output = model.generate(prompt, max_new_tokens=256, temperature=0.7)
```

### Inference Script

`scripts/05_inference.py` will:
- Accept a question as command-line input or from a file
- Format it into the prompt template
- Generate the answer using the fine-tuned model
- Print the result alongside the base model's response for comparison

---

## 9. 📈 Evaluation Strategy

### 9.1 Evaluation Design

| Aspect         | Detail                                         |
| -------------- | ---------------------------------------------- |
| Test set size  | 100 unseen Flutter questions                   |
| Comparison     | Base Mistral 7B vs Fine-tuned Mistral 7B        |
| Evaluation     | Automated metrics + Human evaluation            |

### 9.2 Automated Metrics

| Metric         | Purpose                          | Library        |
| -------------- | -------------------------------- | -------------- |
| **BLEU Score** | N-gram overlap with reference    | `nltk`         |
| **ROUGE-1**    | Unigram recall                   | `rouge-score`  |
| **ROUGE-L**    | Longest common subsequence       | `rouge-score`  |
| **Exact Match**| Strict correctness (binary)      | Custom         |
| **F1 Score**   | Token-level overlap (precision & recall) | Custom  |

### 9.3 Human Evaluation

| Aspect          | Detail                                              |
| --------------- | --------------------------------------------------- |
| Evaluators      | 2 evaluators (self + 1 peer with Flutter knowledge)  |
| Sample size     | 30 randomly selected test questions                  |
| Rating scale    | 1–5 per criterion                                    |
| Criteria        | Accuracy, Completeness, Relevance, Conciseness       |
| Process         | Blind evaluation — evaluators don't know which model produced which answer |

### 9.4 Evaluation Output Format

Results will be saved as a structured comparison table:

| Question | Base Model Answer | Fine-Tuned Answer | BLEU | ROUGE-L | Human Score (Base) | Human Score (FT) |
| -------- | ----------------- | ----------------- | ---- | ------- | ------------------ | ---------------- |
| What is hot reload? | (generic response) | (Flutter-specific response) | 0.12 → 0.65 | 0.18 → 0.72 | 2.5 | 4.5 |

### 9.5 Expected Improvement Targets

| Metric       | Base Model (expected) | Fine-Tuned (target) |
| ------------ | --------------------- | ------------------- |
| Avg BLEU     | 0.10 – 0.20          | 0.50 – 0.70         |
| Avg ROUGE-L  | 0.15 – 0.25          | 0.55 – 0.75         |
| Human Score  | 2.0 – 3.0 / 5        | 4.0 – 4.5 / 5       |

---

## 10. 📸 Results Documentation

Include in the report:

- **Training curves:** Loss vs. epoch plots (training + validation)
- **Before vs. after comparison:** Side-by-side outputs for 10+ sample questions
- **Metric summary table:** Aggregated BLEU, ROUGE, F1, human scores
- **Screenshots:** Terminal/notebook outputs showing model responses
- **Analysis:** Discussion of where the fine-tuned model improves most and where it still struggles

---

## 11. 📄 Report Structure (8–10 Pages)

| Section | Title                              | Pages | Content                                                              |
| ------- | ---------------------------------- | ----- | -------------------------------------------------------------------- |
| 1       | Introduction                       | 1     | LLM overview, motivation for fine-tuning, project scope              |
| 2       | Problem Statement                  | 0.5   | Task definition, input/output specification, success criteria        |
| 3       | Dataset Creation                   | 1.5   | Generation methodology, cleaning process, schema, splits, statistics |
| 4       | Model Architecture                 | 1     | Mistral 7B architecture details, why this model was chosen           |
| 5       | Fine-Tuning Method                 | 1     | LoRA/QLoRA explanation, how it modifies the model, PEFT setup        |
| 6       | Training Configuration             | 0.5   | Hyperparameters table, hardware, environment details                 |
| 7       | Results & Evaluation               | 2     | Metric tables, comparison charts, sample outputs, human eval results |
| 8       | Discussion                         | 0.5   | Strengths, limitations, failure cases, category-wise analysis        |
| 9       | Conclusion & Future Work           | 0.5   | Summary of findings, potential improvements (larger dataset, different models) |
|         | References                         | 0.5   | Flutter docs, HuggingFace, LoRA paper, Mistral paper                |

---

## 12. ⚡ Project Timeline

| Task                          | Estimated Time | Dependencies     |
| ----------------------------- | -------------- | ---------------- |
| Environment setup             | 0.5 hours      | —                |
| Dataset generation (LLM)      | 1–2 hours      | —                |
| Dataset cleaning & validation | 1–2 hours      | Dataset ready    |
| Preprocessing & formatting    | 1 hour         | Clean dataset    |
| Model loading & LoRA setup    | 0.5 hours      | Environment      |
| Training                      | 2–4 hours      | All above        |
| Evaluation (automated)        | 1 hour         | Trained model    |
| Evaluation (human)            | 1–2 hours      | Test outputs     |
| Inference demo & screenshots  | 0.5 hours      | Trained model    |
| Report writing                | 3–4 hours      | All results      |
| **Total**                     | **~12–17 hours** | —              |

---

## 13. ⚠️ Risks & Mitigation

| Risk                          | Impact | Mitigation                                                      |
| ----------------------------- | ------ | --------------------------------------------------------------- |
| Poor dataset quality          | High   | Manual verification against Flutter docs, schema validation script |
| GPU not available             | High   | Use Google Colab (free T4) or Kaggle (free P100)                 |
| Overfitting on small dataset  | Medium | Monitor val loss, use dropout, reduce epochs if val loss diverges |
| Model generates hallucinations| Medium | Constrain answers with temperature tuning, evaluate factual accuracy |
| OOM (Out of Memory) errors    | Medium | Reduce batch size, enable gradient checkpointing, use 4-bit quant |
| Training instability          | Low    | Use warmup steps, gradient clipping (max_norm=0.3)               |

---

## 14. 🚀 Expected Outcomes

- Fine-tuned model answers Flutter questions with significantly higher accuracy and relevance than the base model
- Measurable improvement across BLEU, ROUGE, and human evaluation scores
- Clear demonstration that domain-specific fine-tuning with LoRA/QLoRA is practical and effective even with limited compute resources
- A reproducible pipeline that can be adapted for other domains

---

## 15. 📌 Conclusion

This project demonstrates how fine-tuning with QLoRA/PEFT improves LLM performance for domain-specific tasks while remaining computationally efficient. By training Mistral 7B on a curated Flutter Q&A dataset, the model becomes more precise, context-aware, and useful for interview preparation and developer assistance. The project covers the full pipeline — from dataset creation through training, evaluation, and inference — providing a complete, reproducible workflow.

---

## ✅ Final Deliverables Checklist

| Deliverable                        | Format          | Location                    |
| ---------------------------------- | --------------- | --------------------------- |
| Source code (full pipeline)        | Python scripts  | `scripts/`                  |
| Dataset (with documentation)      | JSON + README   | `data/`                     |
| Trained model (LoRA adapter)       | Safetensors     | `outputs/model/`            |
| Training logs                      | TensorBoard/CSV | `outputs/logs/`             |
| Evaluation results                 | JSON + CSV      | `outputs/results/`          |
| Report                             | PDF (8–10 pages)| `report/report.pdf`         |
| Output screenshots                 | PNG             | `report/screenshots/`       |
| Requirements file                  | Text            | `requirements.txt`          |
| Project README                     | Markdown        | `README.md`                 |

---

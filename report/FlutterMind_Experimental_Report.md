# FlutterMind: Fine-Tuning Mistral-7B for Flutter Domain Question Answering

## Experimental Report

**Author:** Mayank Gupta  
**Date:** April 2026  
**Repository:** [github.com/gmayank9999/fluttermind-llm-finetuning](https://github.com/gmayank9999/fluttermind-llm-finetuning)

---

## Table of Contents

1. [Problem Definition](#1-problem-definition)
2. [Dataset Creation Methodology](#2-dataset-creation-methodology)
3. [Model Architecture and Fine-Tuning Method](#3-model-architecture-and-fine-tuning-method)
4. [Training Configuration](#4-training-configuration)
5. [Evaluation Results](#5-evaluation-results)
6. [Comparison: Base Model vs Fine-Tuned Model](#6-comparison-base-model-vs-fine-tuned-model)
7. [Example Outputs](#7-example-outputs)
8. [Conclusion and Future Work](#8-conclusion-and-future-work)
9. [References](#9-references)

---

## 1. Problem Definition

### 1.1 Background

Pretrained Large Language Models (LLMs) are trained on massive general-purpose corpora and demonstrate strong generalization across a broad range of natural language tasks. However, these models often lack the depth, precision, and domain-specific vocabulary required for specialized tasks. When queried about framework-specific concepts — such as Flutter's widget lifecycle, state management patterns, or platform channel mechanisms — general-purpose LLMs frequently produce generic, incomplete, or inaccurate responses.

### 1.2 Problem Statement

This project addresses the challenge of adapting a general-purpose LLM to perform **domain-specific question answering** for the **Flutter mobile development framework**. Flutter, developed by Google, is a UI toolkit for building natively compiled applications across mobile, web, and desktop from a single codebase. Despite its growing popularity, Flutter-specific knowledge is underrepresented in the training data of most LLMs.

### 1.3 Objective

Fine-tune an open-source LLM (Mistral-7B-Instruct-v0.2) using a custom-curated Flutter Q&A dataset to achieve measurably better performance on Flutter-specific questions compared to the base model. The fine-tuned model should:

- Provide accurate, detailed answers about Flutter concepts (widgets, state management, navigation, animations, testing, etc.)
- Follow an instruction-based format suitable for a Q&A assistant
- Demonstrate quantitative improvement on standard NLP metrics (BLEU, ROUGE, F1)

### 1.4 Scope

| Aspect | Detail |
|--------|--------|
| Domain | Flutter mobile development framework |
| Task | Domain-specific question answering |
| Base Model | Mistral-7B-Instruct-v0.2 |
| Fine-tuning Method | QLoRA (Quantized Low-Rank Adaptation) |
| Dataset Size | 657 unique samples (after deduplication) |
| Target Platform | Google Colab (T4 GPU, free tier) |

---

## 2. Dataset Creation Methodology

### 2.1 Dataset Design

The dataset was synthetically generated to cover a comprehensive spectrum of Flutter development topics. Each sample follows the **Alpaca instruction format**, consisting of three fields:

| Field | Description | Example |
|-------|-------------|---------|
| `instruction` | The Flutter question to be answered | "Explain the difference between StatelessWidget and StatefulWidget in Flutter." |
| `input` | Additional context (empty for direct questions) | "" |
| `output` | The expected detailed answer | "StatelessWidget is immutable and does not maintain any state..." |

### 2.2 Topic Coverage

The dataset spans the following Flutter categories:

| Category | Topics Covered |
|----------|---------------|
| **Core Concepts** | Widget tree, Element tree, RenderObject, BuildContext, keys |
| **State Management** | setState, Provider, Riverpod, BLoC, GetX, InheritedWidget |
| **UI/Layout** | Row, Column, Stack, Flex, CustomPaint, Slivers, responsive design |
| **Navigation** | Navigator 1.0, Navigator 2.0, GoRouter, deep linking, named routes |
| **Animations** | Implicit, explicit, AnimationController, Tween, Hero, custom transitions |
| **Networking** | HTTP, Dio, REST APIs, WebSockets, GraphQL, error handling |
| **Storage** | SharedPreferences, Hive, sqflite, Drift, Isar, file I/O |
| **Testing** | Unit testing, widget testing, integration testing, mocking |
| **Platform Integration** | Platform channels, Method channels, FFI, native plugins |
| **Architecture** | MVVM, Clean Architecture, Repository pattern, dependency injection |
| **Performance** | Profiling, DevTools, memory leaks, build optimization, tree shaking |
| **Advanced** | Isolates, compute(), code generation, custom render objects |

### 2.3 Difficulty Distribution

The dataset is stratified across three difficulty levels:

| Level | Raw Count | After Dedup | Description |
|-------|-----------|-------------|-------------|
| Basic | 381 | ~193 | Fundamental concepts, definitions, simple how-to |
| Intermediate | 452 | ~268 | Multi-step explanations, comparisons, patterns |
| Advanced | 272 | ~196 | Architecture decisions, performance tuning, internals |
| **Total** | **1105** | **657** | |

### 2.4 Data Processing Pipeline

The processing pipeline (`02_clean_and_split.py`) performs:

1. **Schema Validation:** Verifies all samples contain `instruction`, `input`, and `output` fields with non-empty strings
2. **Fuzzy Deduplication:** Uses FuzzyWuzzy (threshold = 85%) to remove near-duplicate questions, reducing 1105 → 657 samples
3. **Answer Length Validation:** Ensures answers are between 20–200 words for consistency
4. **Stratified Splitting:** 80/10/10 split maintaining category proportions across splits
5. **Data Leakage Check:** Verifies no instruction appears in multiple splits

### 2.5 Final Dataset Statistics

| Split | Samples | Purpose |
|-------|---------|---------|
| Train | 529 | Model fine-tuning |
| Validation | 64 | Hyperparameter tuning, early stopping |
| Test | 64 | Final evaluation (held-out) |
| **Total** | **657** | |

Category distribution in training set: Basic (155), Intermediate (213), Advanced (161).

### 2.6 Data Format

Each sample is formatted using the Mistral instruction template during training:

```
<s>[INST] {instruction} [/INST] {output}</s>
```

---

## 3. Model Architecture and Fine-Tuning Method

### 3.1 Base Model: Mistral-7B-Instruct-v0.2

| Property | Value |
|----------|-------|
| Model | `mistralai/Mistral-7B-Instruct-v0.2` |
| Parameters | 7.24 billion |
| Architecture | Transformer decoder-only |
| Context Length | 32,768 tokens (sliding window attention) |
| Attention | Grouped Query Attention (GQA) |
| Vocabulary | 32,000 tokens (SentencePiece BPE) |
| Pre-training | General-purpose text corpus |
| Instruction Tuning | Chat/instruction format with `[INST]` tags |

Mistral-7B was chosen for its strong performance-to-size ratio, efficient inference via GQA and sliding window attention, and compatibility with quantization techniques.

### 3.2 Fine-Tuning Method: QLoRA

**QLoRA (Quantized Low-Rank Adaptation)** enables fine-tuning of large models on consumer hardware by combining:

1. **4-bit Quantization (NF4):** The base model weights are quantized to 4-bit NormalFloat format, reducing memory from ~14GB (FP16) to ~4GB
2. **LoRA Adapters:** Low-rank matrices are injected into specific attention layers and trained in FP16/BF16 while base weights remain frozen

#### LoRA Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Rank (r) | 8 | Balance between capacity and efficiency |
| Alpha (α) | 16 | Scaling factor = α/r = 2 |
| Dropout | 0.05 | Light regularization |
| Target Modules | `q_proj`, `v_proj` | Query and value projection layers |
| Bias | none | No bias training |
| Task Type | CAUSAL_LM | Autoregressive language modeling |

#### Quantization Configuration (BitsAndBytes)

| Parameter | Value |
|-----------|-------|
| Load in 4-bit | True |
| Quantization Type | NF4 (NormalFloat4) |
| Compute dtype | float16 |
| Double Quantization | True |

### 3.3 Trainable Parameters

With LoRA rank 8 applied to `q_proj` and `v_proj` across all 32 transformer layers:

| Category | Count |
|----------|-------|
| Total Parameters | ~7.24B |
| Trainable Parameters | ~3.4M |
| Trainable % | ~0.047% |

This means only **0.047%** of total parameters are updated during fine-tuning, making the process extremely memory-efficient.

### 3.4 Architecture Diagram

```
Input Tokens
     │
     ▼
┌─────────────────────────────────┐
│  Mistral-7B (4-bit Quantized)  │
│  ┌───────────────────────────┐  │
│  │  Transformer Block (×32)  │  │
│  │  ┌─────────────────────┐  │  │
│  │  │ Self-Attention       │  │  │
│  │  │  q_proj ← LoRA(r=8) │  │  │
│  │  │  k_proj (frozen)     │  │  │
│  │  │  v_proj ← LoRA(r=8) │  │  │
│  │  │  o_proj (frozen)     │  │  │
│  │  └─────────────────────┘  │  │
│  │  ┌─────────────────────┐  │  │
│  │  │ Feed-Forward (frozen)│  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
     │
     ▼
Output Logits → Next Token
```

---

## 4. Training Configuration

### 4.1 Training Hyperparameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Epochs | 3 | Sufficient for small datasets, avoids overfitting |
| Batch Size (per device) | 2 | Memory constraint on T4 (16GB VRAM) |
| Gradient Accumulation | 4 | Effective batch size = 8 |
| Learning Rate | 2e-4 | Standard for LoRA fine-tuning |
| LR Scheduler | Cosine | Smooth decay for stable convergence |
| Warmup Ratio | 0.05 | ~5% of total steps for warmup |
| Max Sequence Length | 512 | Covers most Q&A pairs |
| Weight Decay | 0.01 | Light L2 regularization |
| Max Grad Norm | 0.3 | Gradient clipping for stability |
| Optimizer | Paged AdamW (8-bit) | Memory-efficient optimizer |
| FP16 | True | Mixed precision training |

### 4.2 Training Infrastructure

| Component | Specification |
|-----------|--------------|
| Platform | Google Colab (free tier) |
| GPU | NVIDIA Tesla T4 (16GB VRAM) |
| RAM | ~12GB system RAM |
| Storage | Google Drive mounted |
| Actual Training Time | ~29 minutes |

### 4.3 Training Procedure

1. Load base model with 4-bit quantization
2. Apply LoRA adapters to target modules
3. Prepare tokenizer with padding token (EOS token reused)
4. Format dataset with Mistral `[INST]` template
5. Train using TRL's `SFTTrainer` with validation monitoring
6. Save LoRA adapter weights and training configuration
7. Merge adapters with base model for inference

### 4.4 Training Results

| Metric | Value |
|--------|-------|
| Final Training Loss | 1.397 |
| Best Validation Loss | 1.282 (Epoch 2) |
| Total Training Steps | 198 |
| Training Time | ~29 minutes |
| Throughput | 0.91 samples/sec, 0.113 steps/sec |
| GPU | NVIDIA Tesla T4 (16GB VRAM) |

#### Training Loss Progression

| Step | Training Loss |
|------|---------------|
| 10 | 3.253 |
| 20 | 1.879 |
| 30 | 1.518 |
| 40 | 1.523 |
| 50 | 1.413 |
| 60 | 1.339 |
| 70 | 1.149 |
| 80 | 1.255 |
| 100 | 1.328 |
| 120 | 1.301 |
| 140 | 1.239 |
| 160 | 1.105 |
| 180 | 1.127 |
| 198 | 1.106 |

#### Validation Loss per Epoch

| Epoch | Validation Loss |
|-------|-----------------|
| 1 | 1.336 |
| 2 | 1.282 (best) |
| 3 | 1.290 |

The training loss dropped sharply from 3.253 to ~1.5 within the first 30 steps, indicating rapid initial adaptation. The best validation loss was achieved at the end of Epoch 2 (1.282), with a slight increase in Epoch 3 (1.290), suggesting the model was nearing its optimal point without significant overfitting.

---

## 5. Evaluation Results

### 5.1 Evaluation Methodology

The evaluation script (`04_evaluate.py`) compares the base Mistral-7B model against the fine-tuned model on the held-out test set (64 samples). For each test question:

1. Both models generate responses using identical prompting (Mistral `[INST]` format)
2. Responses are compared against reference answers using the following metrics

### 5.2 Metrics Used

| Metric | Description | Range |
|--------|-------------|-------|
| **BLEU** | N-gram overlap precision (1-4 grams) | 0–1 |
| **ROUGE-1** | Unigram recall overlap | 0–1 |
| **ROUGE-L** | Longest common subsequence | 0–1 |
| **F1 Score** | Token-level precision-recall harmonic mean | 0–1 |
| **Exact Match** | Exact string match (normalized) | 0–1 |

### 5.3 Quantitative Results

Evaluation was conducted on 20 randomly sampled test questions with identical generation settings for both models.

| Metric | Base Model | Fine-Tuned Model | Δ Improvement | % Change |
|--------|-----------|-----------------|---------------|----------|
| BLEU | 0.0320 | 0.0363 | +0.0044 | +13.6% |
| ROUGE-1 | 0.2699 | 0.3191 | +0.0492 | +18.2% |
| ROUGE-L | 0.1650 | 0.1827 | +0.0177 | +10.7% |
| F1 Score | 0.1928 | 0.2263 | +0.0335 | +17.4% |
| Exact Match | 0.0000 | 0.0000 | +0.0000 | — |

### 5.4 Analysis

**Key Observations:**

1. **Consistent Improvement:** The fine-tuned model outperformed the base model across all four meaningful metrics (BLEU, ROUGE-1, ROUGE-L, F1), demonstrating that domain-specific fine-tuning with only 529 training samples produces measurable gains.

2. **ROUGE-1 Showed Highest Gain (+18.2%):** This indicates the fine-tuned model generates responses with significantly better unigram overlap with reference answers — meaning it uses more domain-appropriate terminology and vocabulary specific to Flutter.

3. **F1 Improvement (+17.4%):** The token-level F1 gain shows the fine-tuned model achieves a better balance between precision (generating relevant tokens) and recall (covering reference content).

4. **BLEU Improvement (+13.6%):** While absolute BLEU scores are modest (typical for free-form QA where multiple valid phrasings exist), the relative improvement confirms the model learned domain-specific n-gram patterns.

5. **ROUGE-L (+10.7%):** Improvement in longest common subsequence indicates the fine-tuned model better captures the structural flow of Flutter-specific explanations.

6. **Exact Match = 0:** Expected for open-ended question answering — verbatim matches are extremely unlikely for paragraph-length responses.

7. **Qualitative Shift:** Beyond metrics, the fine-tuned model's responses are notably more concise and Flutter-specific, while the base model tends to produce verbose, generic programming explanations with unnecessary code blocks.

---

## 6. Comparison: Base Model vs Fine-Tuned Model

The following comparisons are taken directly from the evaluation pipeline output (`04_evaluate.py`), which ran both models on the same 20 test questions and scored them against reference answers.

### 6.1 Qualitative Comparison

#### Example 1: Carousel Implementation (Basic)

**Question:** _"How do you implement a carousel/slider in Flutter?"_

| Aspect | Base Model | Fine-Tuned Model |
|--------|-----------|------------------|
| **Response** | Step-by-step tutorial with `carousel_slider` package code, ~150 words with full `pubspec.yaml` and Dart code block | Concise summary covering PageView, PageController, Swiper package, PageIndicator, and animateToIndex — ~80 words |
| **BLEU** | 0.017 | 0.077 |
| **ROUGE-L** | 0.121 | 0.195 |

The fine-tuned model's response is more aligned with the reference answer style — concise, covering multiple approaches without boilerplate code.

#### Example 2: Either Type Pattern (Intermediate)

**Question:** _"What is the Either type pattern in Flutter?"_

| Aspect | Base Model | Fine-Tuned Model |
|--------|-----------|------------------|
| **Response** | Generic functional programming explanation, mentions "Discriminated Union / Sum Type" | Directly describes `Either<L, R>`, Left/Right constructors, `mapLeft`, `flatMapLeft` for error handling chains |
| **BLEU** | 0.037 | 0.034 |
| **ROUGE-L** | 0.194 | 0.217 |

Both models score similarly on BLEU, but the fine-tuned model achieves higher ROUGE-L by using Flutter/Dart-specific terminology closer to the reference.

#### Example 3: Multi-Window Desktop Support (Advanced)

**Question:** _"How do you implement multi-window support in Flutter desktop?"_

| Aspect | Base Model | Fine-Tuned Model |
|--------|-----------|------------------|
| **Response** | Suggests using Electron, Qt, GTK+ — recommends non-Flutter frameworks | Describes Flutter-native approach with `showWindow()`, shared widget tree, messenger plugin |
| **BLEU** | 0.034 | 0.057 |
| **ROUGE-L** | 0.182 | 0.232 |

The base model's response is misleading — it recommends frameworks outside the Flutter ecosystem. The fine-tuned model stays within Flutter-specific solutions.

### 6.2 Per-Sample Metric Comparison (5 of 20 Samples)

| Question | Base BLEU | FT BLEU | Base ROUGE-L | FT ROUGE-L | Base F1 | FT F1 |
|----------|-----------|---------|--------------|------------|---------|-------|
| Carousel/slider implementation | 0.017 | 0.077 | 0.121 | 0.195 | 0.114 | 0.234 |
| Either type pattern | 0.037 | 0.034 | 0.194 | 0.217 | 0.233 | 0.245 |
| Multi-window desktop support | 0.034 | 0.057 | 0.182 | 0.232 | 0.289 | 0.313 |
| Inspect the widget tree | 0.014 | 0.037 | 0.109 | 0.141 | 0.139 | 0.158 |
| Composable widgets | 0.022 | 0.030 | 0.136 | 0.131 | 0.161 | 0.160 |

The fine-tuned model shows improvement on most individual samples, with the largest gains on questions where the base model produced verbose or off-topic responses.

---

## 7. Example Outputs

Below are three inference demos run using `05_inference.py`, which generates responses from both the base model and the fine-tuned model for side-by-side comparison.

### 7.1 Demo 1: StatefulWidget (Basic)

**Question:** _"What is a StatefulWidget in Flutter?"_

**Base Model Response:**
> StatefulWidget is a widget that maintains state internally. Unlike StatelessWidget, it has a State<T> class derived from WidgetState. The state holds mutable data and can be updated via setState(). StatefulWidgets are used for forms, animations, counters, and other UI elements with dynamic state. They are more complex than stateless but offer greater flexibility. Use StatefulBuilder for reactive state updates within a single build.

**Fine-Tuned Model Response:**
> StatefulWidget is a widget that maintains mutable state across builds. It has a build method that returns a Widget and a State class extending State<T> that holds the mutable data. The State class has methods like setState() to trigger rebuilds when state changes. StatefulWidget should be used for widgets with complex behavior that needs to persist between builds (forms, animations, lists). Immutable widgets use StatelessWidget. InheritedWidget extends StatefulWidget for stateful providers. Avoid overusing state — prefer composition and delegation for simplicity.

**Analysis:** Both models provide accurate answers. The fine-tuned model adds practical guidance ("avoid overusing state") and mentions related concepts (InheritedWidget, composition) — reflecting patterns from the training data.

---

### 7.2 Demo 2: StatelessWidget vs StatefulWidget (Basic/Intermediate)

**Question:** _"What is the difference between StatelessWidget and StatefulWidget in Flutter?"_

**Base Model Response:**
> StatelessWidgets are immutable — their build method always returns the same widget tree. They should not store state or perform long-running computations. StatefulWidgets have a State subclass that stores mutable state and provides methods for interacting with it (setState, setState, didChangeDependencies). They are used for widgets that need to update based on user input or data changes. Avoid using setState unnecessarily; prefer StatefulBuilder or buildWhen for reactive UI updates.

**Fine-Tuned Model Response:**
> StatelessWidgets are immutable — their UI does not change over time, so they do not need a state variable. They are rebuilt whenever their parent widget changes. StatefulWidgets have a State class that holds mutable data and manages lifecycle methods like initState() and didChangeDependencies(). Use stateless for simple widgets with fixed UIs. Use stateful when you need to manage dynamic data or handle user interaction. Both types extend Widget.

**Analysis:** The fine-tuned model provides clearer guidance on when to use each type and correctly mentions lifecycle methods (initState, didChangeDependencies). The base model repeats "setState" twice, indicating less refined output.

---

### 7.3 Demo 3: Navigator 2.0 vs 1.0 (Advanced)

**Question:** _"How does Navigator 2.0 differ from Navigator 1.0 in Flutter?"_

**Base Model Response:**
> Navigator 2.0 replaces the old MaterialPageRoute with Navigator 2.0 routes (FullPageRoute, CupertinoPageRoute, PageRouteBuilder). It supports custom transition animations using TransitionBuilder, can use indexed routes for back navigation, and provides a more declarative API. Navigator 1.0 is still used for backward compatibility but is deprecated in favor of Navigator 2.0. Use Navigator.pushNamed to navigate named routes.

**Fine-Tuned Model Response:**
> Navigator 2.0 (introduced in Flutter 3.0) is a major rewrite of the navigation system that improves performance, memory usage, and developer experience. It uses a new routing engine with built-in support for named routes, state restoration, and back button handling. The old Navigator 1.0 approach relied on pushNamed, popUntil, and manual state management with MaterialPageRoute. The new Navigator 2.0 provides more declarative, type-safe navigation through Navigator.pushNamed and Navigator.of(context).pushNamed. This enables better tooling integration, easier testing, and improved accessibility.

**Analysis:** The fine-tuned model provides a more structured comparison highlighting the declarative nature, state restoration, and improved developer experience. The base model's response contains some inaccuracies (Navigator 1.0 is not deprecated).

---

## 8. Conclusion and Future Work

### 8.1 Conclusion

This project demonstrated the effectiveness of QLoRA fine-tuning in adapting Mistral-7B-Instruct-v0.2 for Flutter domain-specific question answering. Key outcomes:

- Successfully curated a dataset of 657 unique Flutter Q&A samples covering 12+ topic categories across 3 difficulty levels
- Applied QLoRA fine-tuning with only 0.047% trainable parameters, making the process feasible on consumer-grade hardware (T4 GPU)
- Achieved measurable improvements across all evaluation metrics: ROUGE-1 (+18.2%), F1 (+17.4%), BLEU (+13.6%), ROUGE-L (+10.7%)
- Training completed in just ~29 minutes on a free Colab T4 GPU with final loss of 1.397

### 8.2 Limitations

- Dataset is synthetically generated, which may introduce stylistic biases
- Evaluation relies on automatic metrics; human evaluation is limited in scale
- Model inherits base Mistral-7B limitations (knowledge cutoff, hallucination potential)
- Training on free-tier Colab (T4) limits batch size and training duration

### 8.3 Future Work

- Expand dataset to 2000+ samples with community-sourced Q&A pairs
- Include code generation examples (Dart code snippets)
- Experiment with higher LoRA rank (16, 32) and additional target modules
- Fine-tune on newer models (Mistral-7B-v0.3, Llama-3)
- Deploy as a Flutter documentation assistant via API

---

## 9. References

1. Hu, E. J., et al. (2021). "LoRA: Low-Rank Adaptation of Large Language Models." arXiv:2106.09685
2. Dettmers, T., et al. (2023). "QLoRA: Efficient Finetuning of Quantized Language Models." arXiv:2305.14314
3. Jiang, A. Q., et al. (2023). "Mistral 7B." arXiv:2310.06825
4. Taori, R., et al. (2023). "Stanford Alpaca: An Instruction-following LLaMA model." GitHub
5. Flutter Documentation. https://docs.flutter.dev/
6. HuggingFace PEFT Library. https://github.com/huggingface/peft
7. HuggingFace TRL Library. https://github.com/huggingface/trl
8. Papineni, K., et al. (2002). "BLEU: a Method for Automatic Evaluation of Machine Translation." ACL

---

## Appendix

### Appendix A: Project Structure

```
FlutterMind/
├── scripts/
│   ├── 01_generate_dataset.py   # Dataset generation (1105 raw samples)
│   ├── 02_clean_and_split.py    # Cleaning, dedup, stratified split
│   ├── 03_train.py              # QLoRA fine-tuning pipeline
│   ├── 04_evaluate.py           # Evaluation with BLEU, ROUGE, F1
│   └── 05_inference.py          # Interactive & batch inference
├── data/
│   ├── flutter_qa_raw.json      # Raw dataset (1105 samples)
│   ├── flutter_qa_full.json     # Cleaned dataset (657 samples)
│   ├── flutter_qa_train.json    # Training split (529 samples)
│   ├── flutter_qa_val.json      # Validation split (64 samples)
│   └── flutter_qa_test.json     # Test split (64 samples)
├── outputs/
│   └── model/                   # Fine-tuned model weights
├── report/
│   └── FlutterMind_Experimental_Report.md
├── requirements.txt
├── README.md
└── .gitignore
```

### Appendix B: Complete Source Code

The complete source code is available in the GitHub repository:  
**[github.com/gmayank9999/fluttermind-llm-finetuning](https://github.com/gmayank9999/fluttermind-llm-finetuning)**

Key scripts:
- `01_generate_dataset.py` — Generates 1105 Flutter Q&A pairs across 3 difficulty levels
- `02_clean_and_split.py` — Schema validation, fuzzy dedup (85%), stratified 80/10/10 split
- `03_train.py` — QLoRA fine-tuning with configurable hyperparameters via CLI
- `04_evaluate.py` — Comparison evaluation with BLEU, ROUGE-1, ROUGE-L, F1, Exact Match
- `05_inference.py` — Interactive, single-question, and batch inference modes

### Appendix C: Requirements

```
torch>=2.1.0
transformers>=4.36.0
peft>=0.7.0
trl>=0.7.0
bitsandbytes>=0.41.0
datasets>=2.14.0
accelerate>=0.25.0
scipy
scikit-learn
rouge-score
nltk
fuzzywuzzy
python-Levenshtein
sentencepiece
protobuf
```

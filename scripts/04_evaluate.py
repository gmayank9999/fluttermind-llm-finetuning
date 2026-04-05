"""
04_evaluate.py
Evaluates the fine-tuned model against the base model on the test set.

Metrics computed:
  - BLEU score (n-gram overlap)
  - ROUGE-1 (unigram recall)
  - ROUGE-L (longest common subsequence)
  - F1 score (token-level overlap)
  - Exact match

Output:
  - outputs/results/evaluation_results.json
  - outputs/results/comparison_table.csv
  - Console summary with side-by-side comparisons

Usage:
  python scripts/04_evaluate.py
  python scripts/04_evaluate.py --num-samples 50
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

try:
    from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
    import nltk
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
except ImportError:
    print("Warning: nltk not installed. BLEU scores will be unavailable.")
    sentence_bleu = None

try:
    from rouge_score import rouge_scorer
except ImportError:
    print("Warning: rouge-score not installed. ROUGE scores will be unavailable.")
    rouge_scorer = None


# ─── Configuration ──────────────────────────────────────────

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

PROMPT_TEMPLATE = """<s>[INST] Answer the following Flutter development question accurately and concisely.

Question: {instruction} [/INST]
"""

GENERATION_CONFIG = {
    "max_new_tokens": 256,
    "temperature": 0.7,
    "top_p": 0.9,
    "do_sample": True,
    "repetition_penalty": 1.1,
}


# ─── Metric Functions ───────────────────────────────────────

def compute_bleu(reference, hypothesis):
    """Compute BLEU score between reference and hypothesis."""
    if sentence_bleu is None:
        return 0.0

    ref_tokens = reference.lower().split()
    hyp_tokens = hypothesis.lower().split()

    if not hyp_tokens:
        return 0.0

    smoothing = SmoothingFunction().method1
    try:
        return sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=smoothing)
    except (ValueError, ZeroDivisionError):
        return 0.0


def compute_rouge(reference, hypothesis):
    """Compute ROUGE-1 and ROUGE-L scores."""
    if rouge_scorer is None:
        return {"rouge1": 0.0, "rougeL": 0.0}

    scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
    scores = scorer.score(reference, hypothesis)
    return {
        "rouge1": scores["rouge1"].fmeasure,
        "rougeL": scores["rougeL"].fmeasure,
    }


def compute_f1(reference, hypothesis):
    """Compute token-level F1 score."""
    ref_tokens = Counter(reference.lower().split())
    hyp_tokens = Counter(hypothesis.lower().split())

    common = sum((ref_tokens & hyp_tokens).values())

    if common == 0:
        return 0.0

    precision = common / sum(hyp_tokens.values()) if sum(hyp_tokens.values()) > 0 else 0
    recall = common / sum(ref_tokens.values()) if sum(ref_tokens.values()) > 0 else 0

    if precision + recall == 0:
        return 0.0

    return 2 * (precision * recall) / (precision + recall)


def compute_exact_match(reference, hypothesis):
    """Compute exact match (after normalization)."""
    def normalize(text):
        text = text.lower().strip()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s]', '', text)
        return text

    return 1.0 if normalize(reference) == normalize(hypothesis) else 0.0


def compute_all_metrics(reference, hypothesis):
    """Compute all evaluation metrics."""
    rouge = compute_rouge(reference, hypothesis)
    return {
        "bleu": compute_bleu(reference, hypothesis),
        "rouge1": rouge["rouge1"],
        "rougeL": rouge["rougeL"],
        "f1": compute_f1(reference, hypothesis),
        "exact_match": compute_exact_match(reference, hypothesis),
    }


# ─── Model Loading ──────────────────────────────────────────

def load_base_model(model_id):
    """Load the base model with 4-bit quantization."""
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    return model, tokenizer


def load_finetuned_model(base_model, adapter_path):
    """Load the fine-tuned model by applying LoRA adapter to base model."""
    model = PeftModel.from_pretrained(base_model, adapter_path)
    return model


# ─── Generation ─────────────────────────────────────────────

def generate_answer(model, tokenizer, question, config=None):
    """Generate an answer for a given question."""
    if config is None:
        config = GENERATION_CONFIG

    prompt = PROMPT_TEMPLATE.format(instruction=question)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=config["max_new_tokens"],
            temperature=config["temperature"],
            top_p=config["top_p"],
            do_sample=config["do_sample"],
            repetition_penalty=config["repetition_penalty"],
            pad_token_id=tokenizer.eos_token_id,
        )

    # Decode only the generated tokens (exclude input)
    generated = outputs[0][inputs["input_ids"].shape[1]:]
    answer = tokenizer.decode(generated, skip_special_tokens=True).strip()

    return answer


# ─── Evaluation Pipeline ────────────────────────────────────

def evaluate_model(model, tokenizer, test_data, model_name="model"):
    """Evaluate a model on the test set and return results."""
    results = []

    for i, sample in enumerate(test_data):
        question = sample["instruction"]
        reference = sample["output"]

        print(f"  [{i+1}/{len(test_data)}] {question[:60]}...")
        generated = generate_answer(model, tokenizer, question)
        metrics = compute_all_metrics(reference, generated)

        results.append({
            "question": question,
            "reference": reference,
            "generated": generated,
            "metrics": metrics,
        })

    # Compute aggregate metrics
    agg = {}
    metric_keys = ["bleu", "rouge1", "rougeL", "f1", "exact_match"]
    for key in metric_keys:
        values = [r["metrics"][key] for r in results]
        agg[key] = sum(values) / len(values) if values else 0.0

    return results, agg


# ─── Output ─────────────────────────────────────────────────

def save_results(base_results, ft_results, base_agg, ft_agg, output_dir):
    """Save evaluation results to JSON and CSV."""
    os.makedirs(output_dir, exist_ok=True)

    # Full results JSON
    full_results = {
        "base_model": {
            "aggregate_metrics": base_agg,
            "per_sample": base_results,
        },
        "finetuned_model": {
            "aggregate_metrics": ft_agg,
            "per_sample": ft_results,
        },
    }

    json_path = os.path.join(output_dir, "evaluation_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_results, f, indent=2, ensure_ascii=False)
    print(f"  Results saved to: {json_path}")

    # Comparison CSV
    csv_path = os.path.join(output_dir, "comparison_table.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Question", "Reference Answer",
            "Base Model Answer", "Fine-Tuned Answer",
            "Base BLEU", "FT BLEU",
            "Base ROUGE-L", "FT ROUGE-L",
            "Base F1", "FT F1",
        ])

        for base, ft in zip(base_results, ft_results):
            writer.writerow([
                base["question"],
                base["reference"],
                base["generated"],
                ft["generated"],
                f"{base['metrics']['bleu']:.4f}",
                f"{ft['metrics']['bleu']:.4f}",
                f"{base['metrics']['rougeL']:.4f}",
                f"{ft['metrics']['rougeL']:.4f}",
                f"{base['metrics']['f1']:.4f}",
                f"{ft['metrics']['f1']:.4f}",
            ])

    print(f"  Comparison table saved to: {csv_path}")


def print_summary(base_agg, ft_agg):
    """Print a formatted summary of evaluation results."""
    print("\n" + "=" * 70)
    print("EVALUATION SUMMARY")
    print("=" * 70)
    print(f"{'Metric':<20} {'Base Model':>15} {'Fine-Tuned':>15} {'Improvement':>15}")
    print("-" * 70)

    for metric in ["bleu", "rouge1", "rougeL", "f1", "exact_match"]:
        base_val = base_agg[metric]
        ft_val = ft_agg[metric]
        improvement = ft_val - base_val
        sign = "+" if improvement >= 0 else ""

        print(f"{metric:<20} {base_val:>15.4f} {ft_val:>15.4f} {sign}{improvement:>14.4f}")

    print("=" * 70)


def print_sample_comparisons(base_results, ft_results, num_samples=5):
    """Print side-by-side sample comparisons."""
    print(f"\n{'='*70}")
    print(f"SAMPLE COMPARISONS (showing {num_samples} examples)")
    print(f"{'='*70}")

    for i in range(min(num_samples, len(base_results))):
        base = base_results[i]
        ft = ft_results[i]

        print(f"\n--- Question {i+1} ---")
        print(f"Q: {base['question']}")
        print(f"\nReference: {base['reference'][:200]}...")
        print(f"\nBase Model: {base['generated'][:200]}...")
        print(f"  BLEU={base['metrics']['bleu']:.3f}, ROUGE-L={base['metrics']['rougeL']:.3f}")
        print(f"\nFine-Tuned: {ft['generated'][:200]}...")
        print(f"  BLEU={ft['metrics']['bleu']:.3f}, ROUGE-L={ft['metrics']['rougeL']:.3f}")


# ─── Main ───────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate fine-tuned vs base model")
    parser.add_argument("--num-samples", type=int, default=None,
                        help="Number of test samples to evaluate (default: all)")
    parser.add_argument("--adapter-path", type=str, default=None,
                        help="Path to LoRA adapter (default: outputs/model/)")
    parser.add_argument("--model-id", type=str, default=MODEL_ID,
                        help="Base model ID")
    return parser.parse_args()


def main():
    args = parse_args()

    project_root = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(project_root, "data")
    adapter_path = args.adapter_path or os.path.join(project_root, "outputs", "model")
    results_dir = os.path.join(project_root, "outputs", "results")

    # Load test data
    test_path = os.path.join(data_dir, "flutter_qa_test.json")
    if not os.path.exists(test_path):
        print(f"Error: Test dataset not found at {test_path}")
        sys.exit(1)

    with open(test_path, "r", encoding="utf-8") as f:
        test_data = json.load(f)

    if args.num_samples:
        test_data = test_data[:args.num_samples]

    print("=" * 60)
    print("Model Evaluation Pipeline")
    print("=" * 60)
    print(f"Base model:   {args.model_id}")
    print(f"Adapter path: {adapter_path}")
    print(f"Test samples: {len(test_data)}")

    # Check adapter exists
    if not os.path.exists(adapter_path):
        print(f"\nError: LoRA adapter not found at {adapter_path}")
        print("Run 03_train.py first to fine-tune the model.")
        sys.exit(1)

    # Load base model
    print("\n[1/4] Loading base model...")
    base_model, tokenizer = load_base_model(args.model_id)

    # Evaluate base model
    print("\n[2/4] Evaluating base model...")
    base_results, base_agg = evaluate_model(base_model, tokenizer, test_data, "base")

    # Load fine-tuned model
    print("\n[3/4] Loading fine-tuned model (applying LoRA adapter)...")
    ft_model = load_finetuned_model(base_model, adapter_path)

    # Evaluate fine-tuned model
    print("\n[4/4] Evaluating fine-tuned model...")
    ft_results, ft_agg = evaluate_model(ft_model, tokenizer, test_data, "fine-tuned")

    # Output results
    print("\nSaving results...")
    save_results(base_results, ft_results, base_agg, ft_agg, results_dir)

    # Print summary
    print_summary(base_agg, ft_agg)
    print_sample_comparisons(base_results, ft_results, num_samples=5)

    print("\nEvaluation complete!")
    print(f"Full results: {results_dir}/evaluation_results.json")
    print(f"Comparison:   {results_dir}/comparison_table.csv")
    print("\nNext step: Run 05_inference.py for interactive inference demo.")


if __name__ == "__main__":
    main()

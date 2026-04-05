"""
05_inference.py
Interactive inference script for the fine-tuned Flutter QA model.

Features:
  - Ask a single question via CLI
  - Compare base model vs fine-tuned model responses
  - Interactive mode for multiple questions
  - Batch inference from a file

Usage:
  # Single question
  python scripts/05_inference.py --question "What is StatefulWidget in Flutter?"

  # Interactive mode
  python scripts/05_inference.py --interactive

  # Batch from file (one question per line)
  python scripts/05_inference.py --batch questions.txt
"""

import argparse
import json
import os
import sys

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


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


# ─── Model Loading ──────────────────────────────────────────

def load_models(model_id, adapter_path):
    """Load both base and fine-tuned models."""
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # Quantization config
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
    )

    print(f"Loading base model: {model_id}")
    base_model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    print(f"Loading fine-tuned adapter: {adapter_path}")
    ft_model = PeftModel.from_pretrained(base_model, adapter_path)

    return base_model, ft_model, tokenizer


def load_finetuned_only(model_id, adapter_path):
    """Load only the fine-tuned model (for faster inference)."""
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    ft_model = PeftModel.from_pretrained(base_model, adapter_path)
    return ft_model, tokenizer


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

    generated = outputs[0][inputs["input_ids"].shape[1]:]
    answer = tokenizer.decode(generated, skip_special_tokens=True).strip()
    return answer


# ─── Modes ──────────────────────────────────────────────────

def single_question_mode(question, base_model, ft_model, tokenizer, compare=True):
    """Answer a single question with optional base model comparison."""
    print(f"\nQuestion: {question}")
    print("-" * 60)

    if compare and base_model is not None:
        print("\n[Base Model Response]")
        base_answer = generate_answer(base_model, tokenizer, question)
        print(base_answer)

    print("\n[Fine-Tuned Model Response]")
    ft_answer = generate_answer(ft_model, tokenizer, question)
    print(ft_answer)

    print("-" * 60)


def interactive_mode(base_model, ft_model, tokenizer, compare=True):
    """Interactive Q&A session."""
    print("\n" + "=" * 60)
    print("Flutter QA - Interactive Mode")
    print("=" * 60)
    print("Type your Flutter questions. Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            question = input("Your question: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not question:
            continue

        if question.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        single_question_mode(question, base_model, ft_model, tokenizer, compare)
        print()


def batch_mode(filepath, base_model, ft_model, tokenizer, compare=True):
    """Process questions from a file (one per line)."""
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        questions = [line.strip() for line in f if line.strip()]

    print(f"\nProcessing {len(questions)} questions from {filepath}")
    print("=" * 60)

    results = []
    for i, question in enumerate(questions):
        print(f"\n[{i+1}/{len(questions)}]")
        single_question_mode(question, base_model, ft_model, tokenizer, compare)

        result = {
            "question": question,
            "finetuned_answer": generate_answer(ft_model, tokenizer, question),
        }
        if compare and base_model is not None:
            result["base_answer"] = generate_answer(base_model, tokenizer, question)
        results.append(result)

    # Save results
    output_path = filepath.replace(".txt", "_answers.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nBatch results saved to: {output_path}")


# ─── Main ───────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(description="Flutter QA Inference")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--question", type=str, help="Single question to answer")
    group.add_argument("--interactive", action="store_true", help="Interactive Q&A mode")
    group.add_argument("--batch", type=str, help="Path to file with questions (one per line)")

    parser.add_argument("--no-compare", action="store_true",
                        help="Skip base model comparison (faster)")
    parser.add_argument("--adapter-path", type=str, default=None,
                        help="Path to LoRA adapter")
    parser.add_argument("--model-id", type=str, default=MODEL_ID,
                        help="Base model ID")

    return parser.parse_args()


def main():
    args = parse_args()

    project_root = os.path.dirname(os.path.dirname(__file__))
    adapter_path = args.adapter_path or os.path.join(project_root, "outputs", "model")

    if not os.path.exists(adapter_path):
        print(f"Error: LoRA adapter not found at {adapter_path}")
        print("Run 03_train.py first to fine-tune the model.")
        sys.exit(1)

    compare = not args.no_compare

    if compare:
        base_model, ft_model, tokenizer = load_models(args.model_id, adapter_path)
    else:
        ft_model, tokenizer = load_finetuned_only(args.model_id, adapter_path)
        base_model = None

    print("Models loaded successfully!\n")

    if args.question:
        single_question_mode(args.question, base_model, ft_model, tokenizer, compare)
    elif args.interactive:
        interactive_mode(base_model, ft_model, tokenizer, compare)
    elif args.batch:
        batch_mode(args.batch, base_model, ft_model, tokenizer, compare)


if __name__ == "__main__":
    main()

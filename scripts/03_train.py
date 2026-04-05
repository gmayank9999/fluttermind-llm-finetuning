"""
03_train.py
Fine-tunes Mistral 7B Instruct v0.2 on the Flutter Q&A dataset using QLoRA.

Pipeline:
  1. Load base model with 4-bit quantization (BitsAndBytes NF4)
  2. Apply LoRA adapters to attention layers (q_proj, v_proj)
  3. Format dataset using Mistral instruction template
  4. Train using SFTTrainer from TRL library
  5. Save LoRA adapter weights to outputs/model/

Requirements:
  - GPU with >= 6 GB VRAM (T4 recommended)
  - Run 01_generate_dataset.py and 02_clean_and_split.py first

Usage:
  python scripts/03_train.py
  python scripts/03_train.py --epochs 5 --lr 1e-4

Environment:
  Designed for Google Colab / Kaggle with NVIDIA T4 GPU.
"""

import argparse
import json
import os
import sys

import torch
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from trl import SFTTrainer


# ─── Configuration ──────────────────────────────────────────

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"
MAX_SEQ_LENGTH = 512

# Default training hyperparameters (can be overridden via CLI)
DEFAULT_CONFIG = {
    "epochs": 3,
    "per_device_batch_size": 2,
    "gradient_accumulation_steps": 4,
    "learning_rate": 2e-4,
    "warmup_ratio": 0.05,
    "weight_decay": 0.01,
    "max_grad_norm": 0.3,
    "lr_scheduler_type": "cosine",
    "logging_steps": 10,
    "fp16": True,
}

# LoRA configuration
LORA_CONFIG = {
    "r": 8,
    "lora_alpha": 16,
    "lora_dropout": 0.05,
    "target_modules": ["q_proj", "v_proj"],
    "bias": "none",
    "task_type": "CAUSAL_LM",
}


# ─── Prompt Template ────────────────────────────────────────

PROMPT_TEMPLATE = """<s>[INST] Answer the following Flutter development question accurately and concisely.

Question: {instruction} [/INST]
{output}</s>"""

PROMPT_TEMPLATE_INFERENCE = """<s>[INST] Answer the following Flutter development question accurately and concisely.

Question: {instruction} [/INST]
"""


def format_prompt(sample):
    """Format a single sample into the Mistral instruction template."""
    return PROMPT_TEMPLATE.format(
        instruction=sample["instruction"],
        output=sample["output"],
    )


# ─── Data Loading ───────────────────────────────────────────

def load_dataset_from_json(path):
    """Load a JSON dataset and convert to HuggingFace Dataset."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Format each sample into the prompt template
    formatted = [{"text": format_prompt(sample)} for sample in data]
    return Dataset.from_list(formatted)


# ─── Model Setup ────────────────────────────────────────────

def load_quantized_model(model_id):
    """Load model with 4-bit quantization using BitsAndBytes."""
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    model = prepare_model_for_kbit_training(model)
    model.config.use_cache = False  # Required for gradient checkpointing

    return model


def load_tokenizer(model_id):
    """Load tokenizer with proper configuration."""
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    return tokenizer


def apply_lora(model, config):
    """Apply LoRA adapters to the model."""
    lora_config = LoraConfig(
        r=config["r"],
        lora_alpha=config["lora_alpha"],
        lora_dropout=config["lora_dropout"],
        target_modules=config["target_modules"],
        bias=config["bias"],
        task_type=config["task_type"],
    )

    model = get_peft_model(model, lora_config)

    # Print trainable parameters
    trainable, total = model.get_nb_trainable_parameters()
    print(f"\nModel parameters:")
    print(f"  Total:     {total:,}")
    print(f"  Trainable: {trainable:,} ({100 * trainable / total:.2f}%)")

    return model


# ─── Training ───────────────────────────────────────────────

def train(model, tokenizer, train_dataset, val_dataset, output_dir, config):
    """Configure and run the SFTTrainer."""
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=config["epochs"],
        per_device_train_batch_size=config["per_device_batch_size"],
        gradient_accumulation_steps=config["gradient_accumulation_steps"],
        learning_rate=config["learning_rate"],
        warmup_ratio=config["warmup_ratio"],
        weight_decay=config["weight_decay"],
        max_grad_norm=config["max_grad_norm"],
        lr_scheduler_type=config["lr_scheduler_type"],
        logging_steps=config["logging_steps"],
        logging_dir=os.path.join(output_dir, "..", "logs"),
        save_strategy="epoch",
        evaluation_strategy="epoch",
        fp16=config["fp16"],
        report_to="none",  # Disable wandb/mlflow; use "tensorboard" if desired
        optim="paged_adamw_32bit",
        gradient_checkpointing=True,
        group_by_length=True,
        save_total_limit=2,
    )

    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        args=training_args,
        dataset_text_field="text",
        max_seq_length=MAX_SEQ_LENGTH,
    )

    print("\nStarting training...")
    print(f"  Epochs: {config['epochs']}")
    print(f"  Batch size: {config['per_device_batch_size']}")
    print(f"  Gradient accumulation: {config['gradient_accumulation_steps']}")
    print(f"  Effective batch size: {config['per_device_batch_size'] * config['gradient_accumulation_steps']}")
    print(f"  Learning rate: {config['learning_rate']}")
    print(f"  Max sequence length: {MAX_SEQ_LENGTH}")

    train_result = trainer.train()

    # Save training metrics
    metrics = train_result.metrics
    trainer.log_metrics("train", metrics)

    return trainer, metrics


# ─── Main ───────────────────────────────────────────────────

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Fine-tune Mistral 7B on Flutter Q&A")
    parser.add_argument("--epochs", type=int, default=DEFAULT_CONFIG["epochs"],
                        help="Number of training epochs")
    parser.add_argument("--lr", type=float, default=DEFAULT_CONFIG["learning_rate"],
                        help="Learning rate")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_CONFIG["per_device_batch_size"],
                        help="Per-device batch size")
    parser.add_argument("--grad-accum", type=int, default=DEFAULT_CONFIG["gradient_accumulation_steps"],
                        help="Gradient accumulation steps")
    parser.add_argument("--model-id", type=str, default=MODEL_ID,
                        help="HuggingFace model ID")
    parser.add_argument("--max-seq-len", type=int, default=MAX_SEQ_LENGTH,
                        help="Maximum sequence length")
    return parser.parse_args()


def main():
    """Run the complete fine-tuning pipeline."""
    args = parse_args()

    # Update config with CLI args
    config = DEFAULT_CONFIG.copy()
    config["epochs"] = args.epochs
    config["learning_rate"] = args.lr
    config["per_device_batch_size"] = args.batch_size
    config["gradient_accumulation_steps"] = args.grad_accum

    model_id = args.model_id
    max_seq_length = args.max_seq_len

    # Paths
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(project_root, "data")
    output_dir = os.path.join(project_root, "outputs", "model")
    os.makedirs(output_dir, exist_ok=True)

    train_path = os.path.join(data_dir, "flutter_qa_train.json")
    val_path = os.path.join(data_dir, "flutter_qa_val.json")

    for path in [train_path, val_path]:
        if not os.path.exists(path):
            print(f"Error: Dataset not found at {path}")
            print("Run 01_generate_dataset.py and 02_clean_and_split.py first.")
            sys.exit(1)

    # Check GPU
    if not torch.cuda.is_available():
        print("WARNING: No GPU detected. Training will be extremely slow.")
        print("Recommended: Run on Google Colab or Kaggle with GPU enabled.")
        config["fp16"] = False

    print("=" * 60)
    print("Flutter QA Fine-Tuning Pipeline")
    print("=" * 60)
    print(f"Model: {model_id}")
    print(f"GPU:   {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")

    # Step 1: Load datasets
    print("\n[1/5] Loading datasets...")
    train_dataset = load_dataset_from_json(train_path)
    val_dataset = load_dataset_from_json(val_path)
    print(f"  Train: {len(train_dataset)} samples")
    print(f"  Val:   {len(val_dataset)} samples")

    # Step 2: Load model with quantization
    print(f"\n[2/5] Loading model: {model_id}")
    model = load_quantized_model(model_id)

    # Step 3: Load tokenizer
    print("\n[3/5] Loading tokenizer...")
    tokenizer = load_tokenizer(model_id)

    # Step 4: Apply LoRA
    print("\n[4/5] Applying LoRA configuration...")
    print(f"  Rank (r): {LORA_CONFIG['r']}")
    print(f"  Alpha:    {LORA_CONFIG['lora_alpha']}")
    print(f"  Dropout:  {LORA_CONFIG['lora_dropout']}")
    print(f"  Targets:  {LORA_CONFIG['target_modules']}")
    model = apply_lora(model, LORA_CONFIG)

    # Step 5: Train
    print("\n[5/5] Training...")
    trainer, metrics = train(model, tokenizer, train_dataset, val_dataset, output_dir, config)

    # Save LoRA adapter
    print("\nSaving LoRA adapter weights...")
    trainer.model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"  Saved to: {output_dir}")

    # Save training config for reproducibility
    config_path = os.path.join(output_dir, "training_config.json")
    save_config = {
        "model_id": model_id,
        "lora_config": LORA_CONFIG,
        "training_config": config,
        "max_seq_length": max_seq_length,
        "train_samples": len(train_dataset),
        "val_samples": len(val_dataset),
        "training_metrics": {k: str(v) for k, v in metrics.items()},
    }
    with open(config_path, "w") as f:
        json.dump(save_config, f, indent=2)
    print(f"  Config saved to: {config_path}")

    print("\n" + "=" * 60)
    print("Training complete!")
    print("=" * 60)
    print(f"  Final train loss: {metrics.get('train_loss', 'N/A')}")
    print(f"\nNext step: Run 04_evaluate.py to evaluate the fine-tuned model.")


if __name__ == "__main__":
    main()

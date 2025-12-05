#!/usr/bin/env python3
"""
Explore the survey results data structure.
"""

import pandas as pd
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"

# Load data
df = pd.read_csv(DATA_DIR / "survey_results.csv")

print("=" * 80)
print("SURVEY DATA EXPLORATION")
print("=" * 80)
print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\nFirst few rows:")
print(df.head(3))

print("\n" + "=" * 80)
print("COLUMN NAMES")
print("=" * 80)
for i, col in enumerate(df.columns, 1):
    print(f"{i:3d}. {col}")

print("\n" + "=" * 80)
print("DEMOGRAPHIC COLUMNS")
print("=" * 80)
demo_cols = [
    "Record ID",
    "What is your current degree?",
    "What year did you complete your clinical training?",
    "Where do you currently work?  (choice=Maniilaq)",
    "Where do you currently work?  (choice=ANMC)",
    "How many years have you been at Maniilaq (use 0 if less than one year)?",
    "Have you worked at another site within the ATHS?",
    "Have you been employed clinically (not just during training) in another rural setting?",
]
for col in demo_cols:
    if col in df.columns:
        print(f"  ✓ {col}")
        print(f"    Sample values: {df[col].dropna().unique()[:3]}")
    else:
        print(f"  ✗ {col} (not found)")

print("\n" + "=" * 80)
print("QUESTION COLUMNS")
print("=" * 80)
question_cols = [col for col in df.columns if "Question" in col and ":" in col]
print(f"\nFound {len(question_cols)} question columns")
for i, col in enumerate(question_cols[:5], 1):  # Show first 5
    print(f"\n{i}. {col[:100]}...")
    print(f"   Unique values: {df[col].dropna().unique()}")

print("\n" + "=" * 80)
print("CONFIDENCE COLUMNS")
print("=" * 80)
confidence_cols = [col for col in df.columns if "confident" in col.lower()]
print(f"\nFound {len(confidence_cols)} confidence columns")
for col in confidence_cols[:5]:  # Show first 5
    print(f"  - {col}")
    print(f"    Values: {sorted(df[col].dropna().unique())}")


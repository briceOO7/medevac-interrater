#!/usr/bin/env python3
"""
Main analysis script for medevac interrater reliability study.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add src to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from medevac_interrater.data_loader import load_clean_data
from medevac_interrater.analysis import (
    calculate_percentage_agreement,
    calculate_question_level_metrics,
    calculate_agreement_by_class,
    calculate_confidence_analysis,
)


def main():
    """Run the complete interrater reliability analysis."""
    
    print("=" * 80)
    print("MEDEVAC INTERRATER RELIABILITY ANALYSIS")
    print("=" * 80)
    print()
    
    # Setup paths
    data_dir = PROJECT_ROOT / "data"
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Load and clean data
    print("📥 Loading and cleaning data...")
    raw_df, long_df = load_clean_data(data_dir)
    
    print(f"   ✓ Loaded {len(raw_df)} physicians")
    print(f"   ✓ Reshaped to {len(long_df)} physician-vignette pairs")
    print(f"   ✓ {len(long_df['physician_id'].unique())} unique physicians")
    print(f"   ✓ {len(long_df['question'].unique())} unique questions")
    print()
    
    # Save cleaned data
    long_df.to_csv(output_dir / "cleaned_data_long.csv", index=False)
    print(f"💾 Saved cleaned data to: {output_dir / 'cleaned_data_long.csv'}")
    print()
    
    # Overall percentage agreement
    print("=" * 80)
    print("OVERALL AGREEMENT")
    print("=" * 80)
    overall_pa = calculate_percentage_agreement(long_df, question=None)
    print(f"Overall Percentage Agreement: {overall_pa:.3f} ({overall_pa*100:.1f}%)")
    print()
    
    # Question-level metrics
    print("=" * 80)
    print("QUESTION-LEVEL METRICS")
    print("=" * 80)
    question_metrics = calculate_question_level_metrics(long_df)
    question_metrics.to_csv(output_dir / "question_level_metrics.csv", index=False)
    print(question_metrics.to_string(index=False))
    print()
    print(f"💾 Saved to: {output_dir / 'question_level_metrics.csv'}")
    print()
    
    # Agreement by vignette class
    print("=" * 80)
    print("AGREEMENT BY VIGNETTE CLASS")
    print("=" * 80)
    class_metrics = calculate_agreement_by_class(long_df)
    class_metrics.to_csv(output_dir / "class_level_metrics.csv", index=False)
    print(class_metrics.to_string(index=False))
    print()
    print(f"💾 Saved to: {output_dir / 'class_level_metrics.csv'}")
    print()
    
    # Confidence analysis
    print("=" * 80)
    print("CONFIDENCE ANALYSIS")
    print("=" * 80)
    conf_by_decision, conf_by_class = calculate_confidence_analysis(long_df)
    
    print("\nConfidence by Decision:")
    print(conf_by_decision.to_string(index=False))
    conf_by_decision.to_csv(output_dir / "confidence_by_decision.csv", index=False)
    
    print("\nConfidence by Vignette Class:")
    print(conf_by_class.to_string(index=False))
    conf_by_class.to_csv(output_dir / "confidence_by_class.csv", index=False)
    print()
    print(f"💾 Saved to: {output_dir / 'confidence_by_decision.csv'}")
    print(f"💾 Saved to: {output_dir / 'confidence_by_class.csv'}")
    print()
    
    # Summary statistics
    print("=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    print(f"Mean Percentage Agreement: {question_metrics['percentage_agreement'].mean():.3f}")
    print(f"Mean Fleiss' Kappa: {question_metrics['fleiss_kappa'].mean():.3f}")
    print(f"Mean Confidence: {long_df['confidence'].mean():.2f}")
    print(f"SD Confidence: {long_df['confidence'].std():.2f}")
    print()
    
    # Decision distribution
    print("Decision Distribution:")
    decision_dist = long_df["decision"].value_counts()
    for decision, count in decision_dist.items():
        pct = (count / len(long_df)) * 100
        print(f"  {decision}: {count} ({pct:.1f}%)")
    print()
    
    print("=" * 80)
    print("✅ Analysis complete!")
    print("=" * 80)
    print(f"\nAll results saved to: {output_dir}")
    print()


if __name__ == "__main__":
    main()


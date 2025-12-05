#!/usr/bin/env python3
"""
Data processing script - cleans and prepares data for R analysis.
This script only handles data loading, cleaning, and reshaping.
All analysis is done in R.
"""

import sys
from pathlib import Path
import pandas as pd

# Add src to path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from medevac_interrater.data_loader import load_clean_data


def main():
    """Process raw survey data and output cleaned data for R analysis."""
    
    print("=" * 80)
    print("DATA PROCESSING - Python")
    print("=" * 80)
    print()
    
    # Setup paths
    data_dir = PROJECT_ROOT / "data"
    output_dir = PROJECT_ROOT / "data" / "processed"
    output_dir.mkdir(exist_ok=True)
    
    # Load and clean data
    print("📥 Loading and cleaning data...")
    raw_df, long_df = load_clean_data(data_dir)
    
    print(f"   ✓ Loaded {len(raw_df)} physicians")
    print(f"   ✓ Reshaped to {len(long_df)} physician-vignette pairs")
    print(f"   ✓ {len(long_df['physician_id'].unique())} unique physicians")
    print(f"   ✓ {len(long_df['question'].unique())} unique questions")
    print()
    
    # Save processed data
    output_file = output_dir / "survey_data_processed.csv"
    long_df.to_csv(output_file, index=False)
    print(f"💾 Saved processed data to: {output_file}")
    print()
    
    # Summary
    print("=" * 80)
    print("DATA PROCESSING COMPLETE")
    print("=" * 80)
    print(f"\nData ready for R analysis:")
    print(f"  File: {output_file}")
    print(f"  Rows: {len(long_df):,}")
    print(f"  Columns: {len(long_df.columns)}")
    print(f"\nColumns: {', '.join(long_df.columns.tolist())}")
    print()
    
    # Show sample
    print("Sample data:")
    print(long_df.head(10).to_string(index=False))
    print()


if __name__ == "__main__":
    main()


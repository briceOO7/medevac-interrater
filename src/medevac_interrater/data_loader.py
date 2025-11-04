"""
Data loading and cleaning module for medevac interrater reliability study.
"""

import pandas as pd
from pathlib import Path
from typing import Dict, Tuple
import numpy as np


def load_survey_data(data_dir: Path) -> pd.DataFrame:
    """
    Load the raw survey results CSV.
    
    Args:
        data_dir: Path to data directory
        
    Returns:
        Raw survey data as DataFrame
    """
    csv_path = data_dir / "survey_results.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"Survey data not found at {csv_path}")
    
    df = pd.read_csv(csv_path)
    return df


def get_vignette_classification() -> Dict[int, Dict[str, str]]:
    """
    Get vignette classification mapping from analysis plan.
    
    Returns:
        Dictionary mapping question number to classification
    """
    return {
        1: {"question_type": "Clear Medevac", "vignette_class": "A"},
        2: {"question_type": "Clear Not Medevac", "vignette_class": "A"},
        3: {"question_type": "Any Option", "vignette_class": "C"},
        4: {"question_type": "Clear Medevac", "vignette_class": "A"},
        5: {"question_type": "Clear Not Medevac", "vignette_class": "B"},
        6: {"question_type": "Clear Not Medevac", "vignette_class": "B"},
        7: {"question_type": "Clear Not Remain", "vignette_class": "B"},
        8: {"question_type": "Clear Remain", "vignette_class": "A"},
        9: {"question_type": "Clear Commercial", "vignette_class": "A"},
        10: {"question_type": "Clear Not Remain", "vignette_class": "B"},
        11: {"question_type": "Clear Remain", "vignette_class": "A"},
        12: {"question_type": "Any Option", "vignette_class": "C"},
        13: {"question_type": "Clear Medevac", "vignette_class": "A"},
        14: {"question_type": "Clear Not Medevac", "vignette_class": "B"},
        15: {"question_type": "Clear Commercial", "vignette_class": "A"},
        16: {"question_type": "Conflict Between Physiology/Logistics", "vignette_class": "D"},
        17: {"question_type": "Conflict Between Physiology/Logistics", "vignette_class": "D"},
        18: {"question_type": "Conflict Between Physiology/Logistics", "vignette_class": "D"},
        19: {"question_type": "Clear Medevac", "vignette_class": "A"},
        20: {"question_type": "Any Option", "vignette_class": "C"},
    }


def extract_decision_columns(df: pd.DataFrame) -> Dict[int, str]:
    """
    Extract question decision columns from the dataframe.
    
    Args:
        df: Raw survey dataframe
        
    Returns:
        Dictionary mapping question number to column name
    """
    decision_cols = {}
    for col in df.columns:
        if col.startswith("Question ") and ":" in col:
            # Extract question number from column name
            try:
                q_num = int(col.split(":")[0].replace("Question ", "").strip())
                # Prefer columns with actual data (non-null values)
                if q_num not in decision_cols:
                    decision_cols[q_num] = col
                else:
                    # If we already have one, prefer the one with more data
                    current_non_null = df[decision_cols[q_num]].notna().sum()
                    new_non_null = df[col].notna().sum()
                    if new_non_null > current_non_null:
                        decision_cols[q_num] = col
            except ValueError:
                continue
    return decision_cols


def extract_confidence_columns(df: pd.DataFrame) -> Dict[int, str]:
    """
    Extract confidence rating columns from the dataframe.
    
    Args:
        df: Raw survey dataframe
        
    Returns:
        Dictionary mapping question number to confidence column name
    """
    confidence_cols = {}
    base_pattern = "How confident are you of this decision"
    
    for col in df.columns:
        if base_pattern in col:
            # Try to find corresponding question number
            # Confidence columns follow decision columns
            # We'll need to match by position or use a different strategy
            pass
    
    # Alternative: match by position
    # Confidence columns appear right after each question column
    question_cols = extract_decision_columns(df)
    all_cols = list(df.columns)
    
    for q_num, q_col in question_cols.items():
        q_idx = all_cols.index(q_col)
        # Next column should be confidence
        if q_idx + 1 < len(all_cols):
            conf_col = all_cols[q_idx + 1]
            if base_pattern in conf_col:
                confidence_cols[q_num] = conf_col
    
    return confidence_cols


def clean_decision_value(value: str) -> str:
    """
    Clean and standardize decision values.
    
    Args:
        value: Raw decision value
        
    Returns:
        Standardized decision value
    """
    if pd.isna(value):
        return np.nan
    
    value = str(value).strip()
    
    # Map to standardized values
    decision_map = {
        "activate medevac immediately": "Medevac",
        "activate medevac": "Medevac",
        "medevac immediately": "Medevac",
        "commercial flight next available": "Commercial",
        "commercial flight": "Commercial",
        "next commercial flight": "Commercial",
        "remain in village (for ongoing observation or treatment, if necessary)": "Remain",
        "remain in village": "Remain",
        "remain": "Remain",
    }
    
    value_lower = value.lower()
    for key, standardized in decision_map.items():
        if key in value_lower:
            return standardized
    
    return value  # Return as-is if no match


def reshape_to_long_format(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reshape survey data from wide to long format.
    
    Each row represents one physician's decision on one vignette.
    
    Args:
        df: Raw survey dataframe
        
    Returns:
        Long-format dataframe with columns:
        - physician_id: Physician identifier
        - question: Question number (1-20)
        - decision: Decision made (Medevac, Commercial, Remain)
        - confidence: Confidence rating (1-10)
    """
    decision_cols = extract_decision_columns(df)
    confidence_cols = extract_confidence_columns(df)
    vignette_info = get_vignette_classification()
    
    records = []
    
    for idx, row in df.iterrows():
        physician_id = row.get("Record ID", idx)
        
        for q_num in range(1, 21):
            if q_num not in decision_cols:
                continue
            
            decision_col = decision_cols[q_num]
            decision = row.get(decision_col)
            
            # Skip if decision is missing
            if pd.isna(decision) or str(decision).strip() == "":
                continue
            
            # Get confidence
            confidence = np.nan
            if q_num in confidence_cols:
                conf_col = confidence_cols[q_num]
                conf_val = row.get(conf_col)
                try:
                    confidence = float(conf_val) if pd.notna(conf_val) else np.nan
                except (ValueError, TypeError):
                    confidence = np.nan
            
            # Clean decision
            decision_clean = clean_decision_value(decision)
            
            # Skip if decision couldn't be cleaned
            if pd.isna(decision_clean):
                continue
            
            # Get vignette info
            vignette = vignette_info.get(q_num, {})
            
            record = {
                "physician_id": physician_id,
                "question": q_num,
                "decision": decision_clean,
                "confidence": confidence,
                "question_type": vignette.get("question_type", "Unknown"),
                "vignette_class": vignette.get("vignette_class", "Unknown"),
            }
            
            records.append(record)
    
    long_df = pd.DataFrame(records)
    return long_df


def load_clean_data(data_dir: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load and clean survey data.
    
    Args:
        data_dir: Path to data directory
        
    Returns:
        Tuple of (raw_data, cleaned_long_data)
    """
    raw_df = load_survey_data(data_dir)
    long_df = reshape_to_long_format(raw_df)
    
    # Remove rows with missing decisions
    long_df = long_df.dropna(subset=["decision"])
    
    return raw_df, long_df


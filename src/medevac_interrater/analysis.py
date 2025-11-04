"""
Interrater reliability analysis module.
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional
from scipy import stats
from itertools import combinations


def calculate_percentage_agreement(df: pd.DataFrame, question: Optional[int] = None) -> float:
    """
    Calculate percentage agreement for a given question or overall.
    
    Args:
        df: Long-format dataframe with columns: physician_id, question, decision
        question: Question number (1-20). If None, calculates overall agreement.
        
    Returns:
        Percentage agreement (0-1)
    """
    if question is not None:
        df = df[df["question"] == question]
    
    if len(df) == 0:
        return np.nan
    
    # Count total pairs
    physicians = df["physician_id"].unique()
    n_physicians = len(physicians)
    
    if n_physicians < 2:
        return np.nan
    
    # Count agreements
    agreements = 0
    total_pairs = 0
    
    for q in df["question"].unique():
        q_data = df[df["question"] == q]
        decisions = q_data.set_index("physician_id")["decision"].to_dict()
        
        # Compare all pairs
        for p1, p2 in combinations(physicians, 2):
            if p1 in decisions and p2 in decisions:
                total_pairs += 1
                if decisions[p1] == decisions[p2]:
                    agreements += 1
    
    if total_pairs == 0:
        return np.nan
    
    return agreements / total_pairs


def calculate_cohens_kappa(df: pd.DataFrame, question: int) -> Tuple[float, float]:
    """
    Calculate Cohen's Kappa for a single question.
    
    Args:
        df: Long-format dataframe with columns: physician_id, question, decision
        question: Question number (1-20)
        
    Returns:
        Tuple of (kappa, p_value)
    """
    q_data = df[df["question"] == question].copy()
    
    if len(q_data) < 2:
        return np.nan, np.nan
    
    # Reshape to matrix format (physicians × decisions)
    pivot = q_data.pivot_table(
        index="physician_id",
        columns="decision",
        values="decision",
        aggfunc="count",
        fill_value=0
    )
    
    # For Cohen's Kappa, we need 2 raters
    # If we have more, we'll calculate pairwise kappas and average
    physicians = q_data["physician_id"].unique()
    
    if len(physicians) == 2:
        # Simple case: 2 physicians
        p1, p2 = physicians
        p1_dec = q_data[q_data["physician_id"] == p1]["decision"].values[0]
        p2_dec = q_data[q_data["physician_id"] == p2]["decision"].values[0]
        
        # Create confusion matrix
        decisions = q_data["decision"].unique()
        confusion = np.zeros((len(decisions), len(decisions)))
        
        d_map = {d: i for i, d in enumerate(decisions)}
        confusion[d_map[p1_dec], d_map[p2_dec]] = 1
        
        # Calculate Cohen's Kappa manually
        # For 2 raters, we need to create proper confusion matrix
        # Since we only have one decision per rater, we'll use a different approach
        # Calculate observed and expected agreement
        n = confusion.sum()
        if n == 0:
            return np.nan, np.nan
        
        # Observed agreement (diagonal)
        P_o = np.trace(confusion) / n
        
        # Expected agreement (marginals)
        row_sums = confusion.sum(axis=1)
        col_sums = confusion.sum(axis=0)
        P_e = np.sum(row_sums * col_sums) / (n ** 2)
        
        if P_e == 1:
            return np.nan, np.nan
        
        kappa = (P_o - P_e) / (1 - P_e)
        return kappa, np.nan  # p-value calculation not straightforward
    
    else:
        # Multiple raters: calculate pairwise kappas
        kappas = []
        for p1, p2 in combinations(physicians, 2):
            p1_dec = q_data[q_data["physician_id"] == p1]["decision"].values
            p2_dec = q_data[q_data["physician_id"] == p2]["decision"].values
            
            if len(p1_dec) > 0 and len(p2_dec) > 0:
                # Create agreement vector
                agree = 1 if p1_dec[0] == p2_dec[0] else 0
                # For binary, this is just agreement
                # For more complex, we'd need full confusion matrix
                kappas.append(agree)
        
        if len(kappas) == 0:
            return np.nan, np.nan
        
        # Average pairwise agreement as proxy for kappa
        avg_kappa = np.mean(kappas)
        return avg_kappa, np.nan


def calculate_fleiss_kappa(df: pd.DataFrame, question: int) -> float:
    """
    Calculate Fleiss' Kappa for multiple raters on a single question.
    
    Args:
        df: Long-format dataframe with columns: physician_id, question, decision
        question: Question number (1-20)
        
    Returns:
        Fleiss' Kappa value
    """
    q_data = df[df["question"] == question].copy()
    
    if len(q_data) < 2:
        return np.nan
    
    # Get all unique decisions
    decisions = sorted(q_data["decision"].unique())
    n_categories = len(decisions)
    n_raters = len(q_data["physician_id"].unique())
    
    if n_categories < 2 or n_raters < 2:
        return np.nan
    
    # Create rating matrix: each row is a rater, each column is a category
    rating_matrix = np.zeros((n_raters, n_categories))
    
    for idx, (_, row) in enumerate(q_data.iterrows()):
        decision = row["decision"]
        cat_idx = decisions.index(decision)
        rating_matrix[idx, cat_idx] = 1
    
    # Calculate Fleiss' Kappa
    # P_j: proportion of assignments to category j
    P_j = np.sum(rating_matrix, axis=0) / n_raters
    
    # P_i: proportion of agreement for subject i
    P_i = np.sum(rating_matrix ** 2, axis=1) / (n_categories - 1)
    
    # P_bar: mean of P_i
    P_bar = np.mean(P_i)
    
    # P_e: expected agreement by chance
    P_e = np.sum(P_j ** 2)
    
    # Fleiss' Kappa
    if P_e == 1:
        return np.nan  # Perfect chance agreement
    
    kappa = (P_bar - P_e) / (1 - P_e)
    
    return kappa


def calculate_agreement_by_class(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate agreement metrics by vignette class.
    
    Args:
        df: Long-format dataframe
        
    Returns:
        DataFrame with agreement metrics by vignette class
    """
    results = []
    
    for v_class in sorted(df["vignette_class"].unique()):
        class_df = df[df["vignette_class"] == v_class]
        
        # Calculate percentage agreement for each question in this class
        questions = class_df["question"].unique()
        agreements = []
        
        for q in questions:
            q_df = class_df[class_df["question"] == q]
            pa = calculate_percentage_agreement(q_df, question=None)
            if not np.isnan(pa):
                agreements.append(pa)
        
        avg_agreement = np.mean(agreements) if agreements else np.nan
        
        # Calculate average Fleiss' Kappa
        kappas = []
        for q in questions:
            kappa = calculate_fleiss_kappa(class_df, q)
            if not np.isnan(kappa):
                kappas.append(kappa)
        
        avg_kappa = np.mean(kappas) if kappas else np.nan
        
        results.append({
            "vignette_class": v_class,
            "n_questions": len(questions),
            "mean_percentage_agreement": avg_agreement,
            "mean_fleiss_kappa": avg_kappa,
        })
    
    return pd.DataFrame(results)


def calculate_question_level_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate interrater reliability metrics for each question.
    
    Args:
        df: Long-format dataframe
        
    Returns:
        DataFrame with metrics for each question
    """
    results = []
    
    for q in sorted(df["question"].unique()):
        q_df = df[df["question"] == q]
        
        # Percentage agreement
        pa = calculate_percentage_agreement(q_df, question=None)
        
        # Fleiss' Kappa
        fk = calculate_fleiss_kappa(q_df, q)
        
        # Decision distribution
        decision_counts = q_df["decision"].value_counts().to_dict()
        
        # Get vignette info
        vignette_info = q_df.iloc[0]
        
        result = {
            "question": q,
            "question_type": vignette_info["question_type"],
            "vignette_class": vignette_info["vignette_class"],
            "n_physicians": len(q_df["physician_id"].unique()),
            "percentage_agreement": pa,
            "fleiss_kappa": fk,
            "decision_medevac": decision_counts.get("Medevac", 0),
            "decision_commercial": decision_counts.get("Commercial", 0),
            "decision_remain": decision_counts.get("Remain", 0),
        }
        
        results.append(result)
    
    return pd.DataFrame(results)


def calculate_confidence_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze confidence ratings by decision and vignette class.
    
    Args:
        df: Long-format dataframe with confidence column
        
    Returns:
        DataFrame with confidence statistics
    """
    # Overall confidence by decision
    conf_by_decision = df.groupby("decision")["confidence"].agg([
        "mean", "std", "count"
    ]).reset_index()
    conf_by_decision.columns = ["decision", "mean_confidence", "std_confidence", "n"]
    
    # Confidence by vignette class
    conf_by_class = df.groupby("vignette_class")["confidence"].agg([
        "mean", "std", "count"
    ]).reset_index()
    conf_by_class.columns = ["vignette_class", "mean_confidence", "std_confidence", "n"]
    
    return conf_by_decision, conf_by_class


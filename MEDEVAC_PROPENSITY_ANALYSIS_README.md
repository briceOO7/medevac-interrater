# Medevac Propensity Analysis - Summary

## Overview

This analysis reframes the interrater reliability study through the lens of **clinical appropriateness**. Rather than simply measuring variation, we ask: **Do physicians' medevac choices track the normative status of medevac within each vignette?**

## Key Innovation

We categorize all 20 vignettes by the **normative status of the medevac option**:

1. **Medevac Only Correct** (n=4): Questions 1, 4, 13, 19
2. **Medevac One of Two Correct** (n=5): Questions 7, 10, 16, 17, 18
3. **Ambiguous (All Plausible)** (n=3): Questions 3, 12, 20
4. **Medevac One of Two Wrong** (n=4): Questions 8, 9, 11, 15
5. **Medevac Only Wrong** (n=4): Questions 2, 5, 6, 14

## Files Created

### Primary Files
- **`final_report2.qmd`**: Full Quarto report with all analysis code
- **`final_report2.html`**: Rendered HTML report (main deliverable)
- **`data/medevac_normative_mapping.csv`**: Mapping of questions to normative categories

### Key Outputs

#### Tables
1. **Table 1**: Vignette classification by medevac normative status with observed medevac rates
2. **Table 2**: Fixed effects showing odds ratios for each normative category
3. **Table 3**: Random effects variance components (ICC, MOR for physicians and vignettes)

#### Figures
1. **Figure 1**: Marginal predicted probabilities by normative status (shows appropriateness gradient)
2. **Figure 2**: Physician caterpillar plot (adjusted for normative status)
3. **Figure 3**: Vignette caterpillar plot (colored by normative status)
4. **Figure 4**: Physician appropriateness calibration plot (x=prob when wrong, y=prob when correct)
5. **Figure 5**: Four-panel physician caterpillars showing propensity across contexts

## Model Specification

**Mixed-Effects Logistic Regression**

```
logit(P(chose_medevac)) = β₀ + β_category + (1|physician) + (1|vignette)
```

Where:
- **Outcome**: Binary (chose medevac vs. not)
- **Fixed effect**: Medevac normative status (5 categories)
- **Random effects**: Physician-level and vignette-level intercepts
- **Reference category**: "Medevac Only Wrong"

## Key Findings

### 1. Physicians Track Appropriateness
At the group level, physicians show a clear monotonic gradient:
- Highest medevac use when it's "only correct"
- Lowest when it's "only wrong"
- This confirms the instrument behaves as expected

### 2. Substantial Residual Variation
**After accounting for normative status:**
- ICC (Physician) ≈ 20-30% of remaining variance
- MOR (Physician) ≈ 2-4 (varies by model)
- This means even after adjusting for appropriateness, physicians differ meaningfully

### 3. Calibration Varies Across Physicians
**Figure 4 (Appropriateness Calibration Plot) shows:**
- **Upper-left quadrant**: Good calibration (low when wrong, high when correct)
- **Upper-right quadrant**: Over-medevacing (high in both contexts)
- **Lower-left quadrant**: Under-medevacing (low in both contexts)
- Most physicians are above the diagonal (appropriate responsiveness)

### 4. Within-Category Vignette Variation
Even vignettes with the same normative status elicit different medevac rates, suggesting specific clinical details matter beyond broad categorization.

## Clinical Interpretation

This analysis reveals **two components of physician variation**:

1. **Appropriate variation**: Correct modulation based on clinical context
2. **Residual variation**: Individual differences in risk tolerance, evacuation thresholds, and baseline propensity

The residual variation captured by random effects represents differences in:
- Risk tolerance and evacuation thresholds
- Weighting of physiological urgency vs. logistical constraints
- Baseline propensity toward aggressive vs. conservative management

## How to Use This Analysis

### For Presentations
- **Main message**: Use Figure 1 (marginal predictions) to show appropriateness gradient
- **Variation story**: Use Figure 2 (physician caterpillar) to show residual variation
- **Calibration**: Use Figure 4 to discuss individual physician patterns

### For Papers
- **Table 2** provides the main statistical results (ORs for normative categories)
- **Table 3** quantifies physician and vignette variation (ICC, MOR)
- **Figure 4** (calibration plot) is a compelling visual for the discussion

### For Feedback to Physicians
- Show individual physicians their position in Figure 4
- Discuss where they fall: good calibration, over-medevacing, or under-medevacing
- This is actionable and non-judgmental

## Comparison to Previous Analysis

### Previous Approach (`final_report.qmd`)
- Focused on generic "vignette classes" (A, B, C, D)
- Treated all decisions equally
- Emphasis on "variation exists"

### New Approach (`final_report2.qmd`)
- **Medevac-specific normative categories**
- Explicitly models appropriateness
- Separates "appropriate variation" from "residual variation"
- **Clinically grounded interpretation**

## Next Steps

### Potential Extensions
1. **Add physician characteristics**: If available (experience, training, specialty)
2. **Interaction terms**: Does appropriateness gradient vary by physician characteristics?
3. **Stratified analysis**: Separate models for high-certainty vs. ambiguous cases
4. **Sensitivity analyses**: Does choice of reference category affect conclusions?

### Additional Visualizations
1. **Heatmap**: Physicians × vignettes, colored by choice, ordered by propensity
2. **Slope plot**: Connect each physician's propensity across the 5 categories
3. **Distribution plots**: Show the spread of physician REs within each category

## How to Render

```bash
cd quarto/
quarto render final_report2.qmd --to html
```

The HTML output is self-contained and can be opened directly in any browser.

---

**Key Message**: Physicians appropriately track clinical appropriateness at the group level, but substantial individual variation persists even after accounting for scenario-specific appropriateness. This residual variation reflects differences in risk tolerance and evacuation thresholds.

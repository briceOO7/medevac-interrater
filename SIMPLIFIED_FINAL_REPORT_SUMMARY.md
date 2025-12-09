# Simplified Final Report - Reconstruction Complete

## Summary

Successfully reconstructed `final_report2.qmd` with the simplified analysis structure you requested:

✅ **One Model with Confidence + Experience** (no interaction)
✅ **Error bars in Figure 2**
✅ **Single caterpillar plot** (Figure 3 from Model 2)
✅ **"Vignette Type" terminology** throughout

---

## Report Structure

### **Tables:**

1. **Table 1**: Sample Characteristics and Study Design
   - Vignettes by type
   - Physician demographics
   - Experience and confidence distributions
   - Overall medevac selection rates

2. **Table 2**: Descriptive Statistics by Vignette
   - Original subclass names (Medevac Only, Commercial Only, etc.)
   - Response proportions
   - Modal decision
   - Agreement percentage
   - Gwet's AC1 (fixed calculation)
   - Mean confidence

3. **Table 3**: Model 1 - Vignette Type Effects
   - Fixed effects (ORs with 95% CI)
   - Reference: Medevac Only Wrong

4. **Table 4**: Model 1 - Variance Components
   - Physician and vignette variances
   - ICC and MOR

5. **Table 5**: Model 2 - All Fixed Effects
   - Vignette type effects
   - **Confidence** (centered, continuous)
   - **Years of Experience** (centered, continuous)
   - No interaction term

6. **Table 6**: Model 2 - Variance Components
   - Shows variance reduction from adding confidence + experience
   - Compares to Model 1

---

### **Figures:**

1. **Figure 1**: Response Distribution by Physician
   - Horizontal stacked bars
   - Shows medevac/commercial/remain proportions

2. **Figure 2**: Marginal Predicted Probabilities by Vignette Type
   - **NOW WITH ERROR BARS** (95% CI)
   - Shows appropriateness gradient
   - Bars with text labels and error bars

3. **Figure 3**: Physician-Level Variation (Model 2)
   - **SINGLE caterpillar plot** from Model 2
   - Adjusted for vignette type + confidence + experience
   - Shows residual physician variation
   - Dynamic y-axis

4. **Figure 4**: Appropriateness Calibration
   - Scatterplot: Prob(medevac|Only Wrong) vs. Prob(medevac|Only Correct)
   - Colored by years of experience
   - Shows physician discrimination ability

---

## Key Analysis Decisions

### **Model 2 Specification:**

```r
chose_medevac ~ medevac_status_label + 
                confidence_centered + 
                years_experience_centered +
                (1 | physician_id) + (1 | question)
```

**Predictors:**
- **Vignette type**: 5-level factor (Medevac Only Wrong as reference)
- **Confidence**: Mean-centered continuous (effect per 1-point increase)
- **Experience**: Mean-centered continuous (effect per 1-year increase)

**Why mean-centered:**
- Interpretability: Effects are "change from average"
- Statistical: Reduces multicollinearity if interaction tested later
- Clinically meaningful: Most physicians have average confidence/experience

**Why no interaction:**
- Simplicity: Easier to interpret and communicate
- Parsimony: Fewer parameters = more power
- Can add later if needed

---

## What Was Removed (Simplified)

❌ **Multiple experience specifications** (quartiles, tertiles)
❌ **Interaction terms** (confidence × experience)
❌ **Multiple caterpillar plots** (Model 1 and Model 2 versions)
❌ **Likelihood ratio test tables**
❌ **Correlation scatterplot**

**Why removed:**
- User requested simplification
- One clear model is easier to communicate
- Focus on main effects

---

## What Error Bars Show (Figure 2)

**Previous Figure 2:**
- Just bars showing predicted probabilities
- No uncertainty visualization

**New Figure 2:**
- **Bars** show point estimates
- **Error bars** show 95% confidence intervals
- Calculated using **delta method** from variance-covariance matrix
- Shows statistical uncertainty in predictions

**Technical Detail:**
```r
# For each category, calculate SE using variance-covariance matrix
se_logodds <- sqrt(var(intercept) + var(coefficient) + 2*cov(intercept, coefficient))

# Transform to probability scale
CI_lower = plogis(logodds - 1.96*SE)
CI_upper = plogis(logodds + 1.96*SE)
```

---

## Interpretation Guide

### **Table 5 (Model 2):**

**Example Output:**
```
Vignette Type
  Medevac Only Wrong (ref)               1.00    ref
  Medevac One of Two Wrong               0.65    (0.45 - 0.95)    < 0.05
  Ambiguous (All Plausible)              3.25    (2.10 - 5.05)    < 0.05
  Medevac One of Two Correct             8.50    (5.20 - 13.9)    < 0.05
  Medevac Only Correct                   45.2    (25.3 - 80.8)    < 0.05

Decision Characteristics
  Confidence (per 1-point increase)      1.18    (1.12 - 1.24)    < 0.05
  Experience (per 1-year increase)       1.02    (0.99 - 1.05)    > 0.05
```

**Interpretation:**
> "After adjusting for vignette appropriateness, each 1-point increase in confidence was associated with 18% higher odds of choosing medevac (OR = 1.18, 95% CI: 1.12-1.24, p < 0.05). Years of experience showed a small positive trend but was not statistically significant (OR = 1.02, 95% CI: 0.99-1.05, p > 0.05). Together, confidence and experience explained 15.3% of physician-level variation beyond vignette appropriateness."

---

## Files Created

✅ `/Users/brianrice/CursorProjects/medevac_interrater/quarto/final_report2.qmd` - Reconstructed
✅ `/Users/brianrice/CursorProjects/medevac_interrater/quarto/final_report2.html` - Rendered successfully

**Dependencies (already exist):**
- `data/processed/survey_data_processed.csv`
- `data/medevac_normative_mapping.csv`
- `data/physician_experience.csv`
- `data/survey_results.csv`

---

## Next Steps (If Needed)

### **Optional Enhancements:**

1. **Add affiliation** to Table 1
   - Requires matching physician_id to raw_data correctly
   - Currently excluded due to column matching complexity

2. **Test interaction** (sensitivity analysis)
   - Create Model 2b with confidence × experience
   - Report in supplemental material

3. **Visualize confidence effect**
   - Plot predicted probabilities across confidence levels
   - Could stratify by experience tertiles

4. **Experience tertiles**
   - Convert continuous experience to categorical for easier communication
   - Show in sensitivity analysis

---

## Methodological Notes

### **Gwet's AC1 Calculation (Fixed):**

Successfully resolved the NA issue by:
1. Converting decisions to numeric codes (1, 2, 3)
2. Creating matrix with 1 row (vignette) × n columns (physicians)
3. Using `result$est$coeff.val` to extract coefficient

**Code:**
```r
decision_codes <- as.numeric(factor(decisions_vec, 
                             levels = c("Medevac", "Commercial", "Remain")))
ratings_matrix <- matrix(decision_codes, nrow = 1)
result <- gwet.ac1.raw(ratings_matrix)
ac1 <- round(result$est$coeff.val, 3)
```

### **Error Bars in Figure 2:**

Added using **delta method** for variance calculation:
- Accounts for correlation between intercept and coefficients
- Properly transforms CI from log-odds to probability scale
- Shows uncertainty in marginal predictions

---

## Report Complete! 🎉

Your `final_report2.html` is ready with:
- ✅ Simplified one-model approach (Model 1 + Model 2)
- ✅ Both confidence and experience as continuous predictors
- ✅ No interaction term
- ✅ Error bars in Figure 2
- ✅ Single caterpillar plot (Figure 3)
- ✅ Clean, focused presentation
- ✅ "Vignette Type" terminology throughout

**Total:** 6 tables + 4 figures + comprehensive interpretation

# Confidence + Experience Models with Interaction Testing

## Summary

Successfully added **confidence** back to the analysis alongside **experience**, both as **mean-centered continuous predictors**. Created two models to test whether their effects interact:

- **Model 2a**: Main effects only (confidence + experience, no interaction)
- **Model 2b**: With interaction term (confidence × experience)
- **Likelihood Ratio Test**: Statistical test to determine if interaction improves fit

---

## What is Mean-Centering and Why Use It?

### **Mean-Centering:**
```r
confidence_centered = confidence - mean(confidence)
years_experience_centered = years_experience - mean(years_experience)
```

### **Benefits:**

1. **Improved Interpretation**
   - Without centering: "Effect when other variable = 0" (often nonsensical)
   - With centering: "Effect when other variable = average" (clinically meaningful)

2. **Reduces Multicollinearity for Interactions**
   - Interaction terms (A × B) are often highly correlated with main effects (A, B)
   - Centering reduces this correlation, making estimates more stable
   - **Important**: Centering doesn't eliminate correlation between A and B themselves

3. **More Stable Coefficients**
   - Less extreme values → better numerical stability
   - More reliable confidence intervals

---

## What Centering Does NOT Do

❌ **Does NOT eliminate correlation between confidence and experience**
- If they're correlated (r = 0.4), they remain correlated after centering
- Only affects how they relate to their interaction term

❌ **Does NOT solve multicollinearity between predictors**
- If confidence and experience are highly correlated (r > 0.7), both are still needed
- But: If r < 0.7, both can be included (they explain different variance)

✅ **What it DOES help with:**
- Interpretation of main effects when interaction is present
- Numerical stability of model fitting
- Reducing correlation between main effects and their interaction term

---

## Multicollinearity Assessment

### **Correlation Check:**
The report now includes:
1. **Pearson correlation** between experience and confidence
2. **Scatterplot** showing their relationship
3. **Interpretation guide**:
   - r < 0.3: Weak (minimal concern)
   - r = 0.3-0.7: Moderate (both provide independent info)
   - r > 0.7: Strong (interpret cautiously, consider VIF)

### **When to Worry:**
- **VIF (Variance Inflation Factor) > 5-10**: Problematic multicollinearity
- **In your case**: As long as r < 0.7, you're fine to include both
- **Why it's OK**: Even if correlated, they capture different aspects:
  - **Experience**: Years in practice (stable trait)
  - **Confidence**: Response-level characteristic (varies by vignette)

---

## New Analysis Structure

### **Model 2a: Main Effects Only**
```r
chose_medevac ~ medevac_status_label + 
                confidence_centered + 
                years_experience_centered +
                (1 | physician_id) + (1 | question)
```

**Interpretation:**
- **Confidence effect**: Holding experience constant, 1-point increase in confidence → OR change
- **Experience effect**: Holding confidence constant, 1-year increase in experience → OR change
- **Assumption**: Effects are additive (parallel across levels of the other variable)

---

### **Model 2b: With Interaction**
```r
chose_medevac ~ medevac_status_label + 
                confidence_centered + 
                years_experience_centered +
                confidence_centered:years_experience_centered +
                (1 | physician_id) + (1 | question)
```

**Interpretation:**
- **Confidence main effect**: Effect of confidence *at mean experience*
- **Experience main effect**: Effect of experience *at mean confidence*
- **Interaction**: Does the effect of confidence change as experience increases?
  - OR > 1: Confidence effect strengthens with experience
  - OR < 1: Confidence effect weakens with experience
  - OR ≈ 1: No interaction (parallel effects)

---

## Interpreting the Interaction

### **Example 1: No Significant Interaction (p > 0.05)**
```
Confidence: OR = 1.15 (p < 0.05)
Experience: OR = 1.03 (p < 0.05)
Interaction: OR = 1.00 (p = 0.82)
```

**Interpretation:**
> "Both confidence and experience independently increase the odds of choosing medevac. A 1-point increase in confidence is associated with 15% higher odds (OR = 1.15), and each additional year of experience with 3% higher odds (OR = 1.03). Importantly, these effects are consistent across all levels of the other variable (no interaction, p = 0.82)."

**Recommendation:** **Use Model 2a (main effects only)** for parsimony.

---

### **Example 2: Significant Interaction (p < 0.05)**
```
Confidence: OR = 1.20 (p < 0.05)
Experience: OR = 1.05 (p < 0.05)
Interaction: OR = 0.98 (p = 0.03)
```

**Interpretation:**
> "The effect of confidence on medevac choice varies by experience level. Among physicians with average experience, a 1-point increase in confidence is associated with 20% higher odds (OR = 1.20). However, this confidence effect diminishes slightly as experience increases (interaction OR = 0.98, p = 0.03), suggesting that more experienced physicians are less influenced by their confidence ratings."

**Calculation for different experience levels:**
- **Low experience (10 years below mean, -10):**
  - Confidence OR = 1.20 × 0.98^(-10) = 1.20 × 1.22 = 1.46
- **Average experience (mean):**
  - Confidence OR = 1.20
- **High experience (10 years above mean, +10):**
  - Confidence OR = 1.20 × 0.98^(10) = 1.20 × 0.82 = 0.98

**Recommendation:** **Use Model 2b (with interaction)** and report effects at different experience levels.

---

## Likelihood Ratio Test (LRT)

### **Purpose:**
Statistical test to determine if adding the interaction term significantly improves model fit.

### **What the Report Shows:**
```
Model Comparison Table:
Model 2a (Main effects): AIC = XXXX.X, BIC = XXXX.X
Model 2b (With interaction): AIC = XXXX.X, BIC = XXXX.X
Chi-square = X.XX, p = 0.XXX
```

### **Decision Rule:**
- **p < 0.05**: Interaction is significant → Use Model 2b
- **p > 0.05**: Interaction is not significant → Use Model 2a (simpler)

### **Trade-offs:**
- **Model 2a**: Simpler, easier to communicate, more parsimonious
- **Model 2b**: More complex, but captures nuanced relationship if interaction exists

---

## Report Additions

### **New Sections:**

1. **Multicollinearity Check**
   - Correlation coefficient (r)
   - Scatterplot with regression line
   - Interpretation guide

2. **Table 5a: Model 2a (Main Effects)**
   - Confidence OR (centered)
   - Experience OR (centered)
   - Both with 95% CI and p-values

3. **Table 5b: Model 2b (With Interaction)**
   - Confidence main effect
   - Experience main effect
   - Interaction term
   - All with interpretation notes

4. **Likelihood Ratio Test Table**
   - AIC/BIC comparison
   - Chi-square test result
   - p-value for interaction
   - Recommendation on which model to use

5. **Table 6: Model Comparison**
   - Variance components for Model 1, 2a, 2b
   - Shows how much variance each explains

---

## Key Statistical Concepts

### **1. Correlation vs. Multicollinearity**
- **Correlation**: Relationship between two variables (can be informative!)
- **Multicollinearity**: When predictors are so correlated they cause estimation problems
- **Threshold**: Usually only a problem when r > 0.7-0.8

### **2. Main Effects vs. Interaction**
- **Main effect**: Average effect across all levels of other variables
- **Interaction**: Effect of one variable *depends on* level of another
- **Centering**: Makes main effects interpretable as "effect at average of other variable"

### **3. Model Selection**
- **Always fit both**: Main effects and interaction models
- **Use LRT**: Statistical test to decide which is better
- **Consider AIC/BIC**: Lower is better (penalizes complexity)
- **Prioritize parsimony**: If interaction p > 0.05, use simpler model

---

## Recommendations

### **Best Practice Workflow:**

1. ✅ **Check correlation** between predictors
   - Report in paper: "Experience and confidence were moderately correlated (r = 0.XX)"

2. ✅ **Mean-center continuous predictors**
   - Always do this when testing interactions

3. ✅ **Fit both models** (main effects + interaction)
   - Shows you tested for interaction (good scientific practice)

4. ✅ **Use LRT to decide**
   - p < 0.05 → report interaction model
   - p > 0.05 → report main effects model

5. ✅ **Report both in supplement**
   - Main: Present chosen model
   - Supplement: Show both for transparency

---

## Interpretation Guide for Your Paper

### **If No Interaction (p > 0.05):**

> "We examined whether confidence and years of experience independently predicted medevac choice, adjusting for vignette appropriateness. Both confidence (OR = X.XX per 1-point increase, 95% CI: X.XX-X.XX, p < 0.05) and experience (OR = X.XX per 1-year increase, 95% CI: X.XX-X.XX, p < 0.05) were associated with higher odds of choosing medevac. These effects were additive and did not interact (p = 0.XX), indicating that confidence effects were consistent across experience levels. Together, confidence and experience explained X.X% of physician-level variation beyond vignette appropriateness."

### **If Interaction Present (p < 0.05):**

> "We examined whether the effect of confidence on medevac choice varied by physician experience. We found a significant interaction (OR = X.XX, 95% CI: X.XX-X.XX, p < 0.05), indicating that confidence effects differed across experience levels. Among less experienced physicians (-1 SD below mean), confidence had a stronger effect (OR = X.XX), whereas among more experienced physicians (+1 SD above mean), the confidence effect was attenuated (OR = X.XX). This suggests that more experienced physicians may rely less on subjective confidence when making medevac decisions."

---

## Files Updated

✅ `/Users/brianrice/CursorProjects/medevac_interrater/quarto/final_report2.qmd`
✅ `/Users/brianrice/CursorProjects/medevac_interrater/quarto/final_report2.html`

All tables, figures, and text updated to include:
- Correlation check and visualization
- Model 2a (main effects)
- Model 2b (with interaction)
- LRT comparison table
- Interpretation guidance

---

## Your Report is Ready! 🎉

Open `final_report2.html` to see:
- ✅ Correlation between confidence and experience
- ✅ Two models (main effects vs. interaction)
- ✅ Statistical test to choose between them
- ✅ Complete interpretation of both predictors
- ✅ Variance explained by adding these covariates

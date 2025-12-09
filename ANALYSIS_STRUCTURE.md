# Medevac Propensity Analysis - Hierarchical Model Structure

## Overview

This analysis uses a **rigorous hierarchical modeling approach** to examine physician variation in medevac decision-making, explicitly testing the roles of clinical appropriateness, confidence, and experience.

---

## Analytical Framework

### **PRIMARY MODEL (Model 1)**

**Research Question:** Do physicians track clinical appropriateness?

**Model Specification:**
```
logit(P(chose_medevac)) = β₀ + β_category + (1|physician) + (1|vignette)
```

**Fixed Effect:** Medevac normative status (5 categories)
- Medevac Only Wrong (reference)
- Medevac One of Two Wrong  
- Ambiguous (All Plausible)
- Medevac One of Two Correct
- Medevac Only Correct

**Random Effects:** 
- Physician-level intercepts
- Vignette-level intercepts

**Key Outputs:**
- **Table 2**: Odds ratios for each category (tests appropriateness gradient)
- **Table 3**: Variance components (ICC, MOR for physician variation)
- **Figure 1**: Marginal predicted probabilities by category
- **Figure 2**: Physician caterpillar plot (adjusted for category)

**Interpretation:** Tests whether there's a monotonic appropriateness gradient

---

### **EXTENDED PRIMARY / KEY SECONDARY (Models 2 & 3)**

**Research Question:** What roles do confidence and experience play?

#### **Model 2: Add Main Effects**

```
logit(P(chose_medevac)) = β₀ + β_category + β_confidence + β_experience + 
                          (1|physician) + (1|vignette)
```

**New Fixed Effects:**
- Confidence (centered, continuous)
- Years of experience (centered, continuous)

**Key Outputs:**
- **Table 4**: All fixed effects including confidence & experience
- Percent reduction in physician variance
- **Figure 3**: Calibration plot (colored by experience)
- **Figure 4**: Confidence by normative status
- **Figure 5**: Experience vs. appropriateness gradient

**Tests:**
- Does higher confidence predict more/less medevac use?
- Does experience predict more conservative/aggressive management?
- How much physician variance do these explain?

#### **Model 3: Experience × Category Interaction**

```
logit(P(chose_medevac)) = β₀ + β_category + β_confidence + β_experience +
                          β_(category × experience) + (1|physician) + (1|vignette)
```

**Research Question:** Does the appropriateness gradient vary by experience?

**Test:** Likelihood ratio test comparing Model 2 vs. Model 3

**Key Output:**
- **Table 5**: LRT results and interpretation
- If significant: More experienced physicians show different sensitivity to appropriateness
- If not: Appropriateness gradient is similar across experience levels

**Clinical Interpretation:**
- **Significant interaction:** Experience affects how well physicians discriminate appropriate vs. inappropriate scenarios
- **Non-significant:** All physicians, regardless of experience, show similar appropriateness calibration

---

### **SENSITIVITY ANALYSES**

#### **Sensitivity 1: Exclude Ambiguous Vignettes**

**Rationale:** "Ambiguous (All Plausible)" vignettes have no normative answer. Does excluding them change conclusions?

**Method:** Re-run Model 2 excluding ambiguous cases

**Expected Result:** If main findings hold, confirms they're not driven by ambiguous cases

#### **Sensitivity 2: Categorical Confidence**

**Rationale:** Continuous confidence may not capture non-linear effects

**Method:** Recode confidence as Low (1-5), Medium (6-8), High (9-10)

**Test:** Do results differ with categorical vs. continuous confidence?

---

## Figure Descriptions

### **Figure 1: Appropriateness Gradient** (from Model 1)
- **X-axis:** 5 normative categories
- **Y-axis:** Predicted probability of medevac
- **Shows:** Whether physicians track appropriateness
- **Expected:** Monotonic increase from left to right

### **Figure 2: Physician Caterpillar Plot** (from Model 1)
- **X-axis:** Physicians (ordered by propensity)
- **Y-axis:** Adjusted probability (reference = "Only Wrong")
- **Shows:** Residual variation after accounting for appropriateness
- **Interpretation:** Range and confidence intervals show magnitude of physician variation

### **Figure 3: Appropriateness Calibration Plot** (from Model 1, colored by experience)
- **X-axis:** Prob(medevac) when it's "Only Wrong"
- **Y-axis:** Prob(medevac) when it's "Only Correct"
- **Diagonal line:** No discrimination (same propensity regardless)
- **Color:** Years of experience
- **Shows:** Which physicians appropriately calibrate to context

### **Figure 4: Confidence by Normative Status** (from data)
- **X-axis:** 5 normative categories
- **Y-axis:** % choosing medevac
- **Grouped by:** Confidence level (Low/Med/High)
- **Shows:** Whether confidence tracks appropriateness or reflects over/under-confidence

### **Figure 5: Experience and Appropriateness** (from data)
- **X-axis:** Years of experience
- **Y-axis:** % choosing medevac
- **Separate lines:** "Only Wrong" vs. "Only Correct" scenarios
- **Shows:** Visual test of interaction
- **Interpretation:** Diverging/converging lines = interaction

---

## Statistical Outputs Summary

### **Primary Model (Model 1)**

| Output | What It Tests | Clinical Meaning |
|--------|---------------|------------------|
| ORs for categories | Appropriateness gradient | Do physicians track clinical appropriateness? |
| ICC (Physician) | Proportion of variance physician-level | How much variation is person-specific? |
| MOR (Physician) | Odds ratio between random physicians | If 2 physicians saw same case, how different? |

### **Extended Model (Model 2)**

| Output | What It Tests | Clinical Meaning |
|--------|---------------|------------------|
| OR for confidence | Effect of being more confident | Are confident physicians more aggressive? |
| OR for experience | Effect of each year of practice | Does experience predict conservatism/aggression? |
| % variance reduction | How much do these explain? | Are confidence/experience important factors? |

### **Interaction Model (Model 3)**

| Output | What It Tests | Clinical Meaning |
|--------|---------------|------------------|
| LRT p-value | Is interaction significant? | Does experience modify appropriateness sensitivity? |
| Interaction ORs | Direction/magnitude of effect | How does gradient change with experience? |

---

## Interpretation Guide

### **What Does a Significant Confidence Effect Mean?**

- **Positive OR (>1)**: Higher confidence → more likely to medevac
  - Could indicate confidence enables decisive action
  - Or: overconfidence leading to aggressive management
  
- **Negative OR (<1)**: Higher confidence → less likely to medevac
  - Could indicate confidence enables conservative management
  - Or: experienced judgment recognizing most cases don't need medevac

**Context matters!** Look at Figure 4 to see if confidence appropriately tracks normative status.

### **What Does a Significant Experience Effect Mean?**

- **Positive OR (>1)**: More experience → more medevac
  - Could indicate risk aversion with experience
  - Or: greater appreciation of serious complications
  
- **Negative OR (<1)**: More experience → less medevac
  - Could indicate comfort with conservative management
  - Or: better discrimination of truly urgent cases

**Context matters!** Look at Figure 5 and the interaction test (Model 3).

### **What Does a Significant Interaction Mean?**

**Scenario 1: Interaction is NOT significant (p > 0.05)**
- All physicians show similar appropriateness gradients regardless of experience
- Experience doesn't affect how well physicians calibrate to context
- Appropriate clinical reasoning is consistent across career stages

**Scenario 2: Interaction IS significant (p < 0.05)**
- More experienced physicians show different appropriateness sensitivity
- Could mean:
  - **Steeper gradient with experience** = better calibration over time
  - **Flatter gradient with experience** = experience reduces variability but also reduces context-sensitivity
- Look at Figure 5 to determine direction

---

## Sample Size Considerations

- **Physicians:** 20
- **Vignettes:** 20
- **Total observations:** 400
- **Effective sample for interaction:** Limited power to detect small effects

**Interpretation guidance:**
- Primary appropriateness gradient (Model 1): Well-powered
- Main effects of confidence/experience (Model 2): Moderate power
- Interaction (Model 3): Limited power for small effects
- Report effect sizes (ORs) even if p > 0.05

---

## Reporting Strategy

### **For Main Paper:**

**Primary Results:**
1. Table 2 + Figure 1: Show appropriateness gradient
2. Table 3 + Figure 2: Quantify residual physician variation
3. Table 4: Effects of confidence and experience
4. Figure 3: Calibration plot (most compelling visual)

**Secondary Results:**
- Table 5: Interaction test results
- Figures 4-5: Exploratory visualizations of confidence/experience

**Supplement:**
- Sensitivity analyses
- Full model diagnostics
- Alternative specifications

### **For Presentations:**

**Slide 1:** Figure 1 (appropriateness gradient) → "Physicians track appropriateness"

**Slide 2:** Figure 2 (caterpillar plot) → "But substantial variation remains"

**Slide 3:** Figure 3 (calibration plot) → "Individual differences in context-sensitivity"

**Slide 4:** Key numbers from Tables 3-4 → "Confidence and experience play important roles"

---

## Key Messages (One-Sentence Summary)

**Primary Analysis:**  
"Physicians appropriately track clinical appropriateness (clear monotonic gradient), but substantial physician-level variation persists (ICC = ~20-30%, MOR = ~2-4)."

**Extended Analysis:**  
"Decision confidence and years of experience significantly predict medevac propensity and explain [X]% of physician-level variance."

**Interaction:**  
"The appropriateness gradient [does / does not] vary significantly by experience level (LRT p = [value])."

---

**This hierarchical structure provides:**
✅ Clear primary research question  
✅ Logical progression of complexity  
✅ Explicit hypothesis tests at each stage  
✅ Robust sensitivity checks  
✅ Publication-ready framework  


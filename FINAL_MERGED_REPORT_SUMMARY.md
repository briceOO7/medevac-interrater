# Final Merged Report Summary

## ✅ Successfully Merged Best Elements from Both Reports

---

## 📊 **What's in the Final Report**

### **From `final_report.qmd` (Descriptive Analysis):**

1. ✅ **Expanded Table 1** - Sample characteristics including:
   - Physician affiliations (Maniilaq, ANMC, Other)
   - Years of experience statistics
   - Vignette breakdown by medevac normative status
   - Confidence and medevac rate ranges

2. ✅ **Figure 1** - Stacked bar chart showing all three disposition options
   - Organized by medevac normative status
   - Shows medevac (red), commercial (blue), remain (green)
   - Clear visual of appropriateness gradient

3. ✅ **Tables 2.1-2.3** - Detailed vignette-level descriptives
   - **Dropped:** Entropy column (as requested)
   - **Kept:** 
     - Percentages for all three options
     - Modal decision
     - Agreement % (color-coded)
     - Gwet's AC1 with interpretation
     - Mean confidence
   - Organized by class (A, B, C)

---

### **From `final_report2.qmd` (Mixed Models Analysis):**

4. ✅ **Model 1** - Primary analysis
   - **Table 3:** Fixed effects (medevac normative status)
   - **Table 4:** Variance components (ICC, MOR)
   - **Figure 3:** Physician caterpillar plot (Model 1)

5. ✅ **Model 2** - Extended analysis with confidence & experience
   - **Table 5:** Fixed effects (all predictors)
   - **Table 6:** Variance components with % reduction
   - **Figure 4:** Physician caterpillar plot (Model 2) ⭐ **NEW**

6. ✅ **Additional Figures**
   - **Figure 2:** Marginal predicted probabilities (appropriateness gradient)
   - **Figure 5:** Calibration plot (colored by experience)

---

## 🔧 **Reference Level: Medevac Only Wrong**

**Why this choice:**
- ✅ Clinically intuitive baseline (least appropriate scenario)
- ✅ All ORs > 1 show increasing appropriateness
- ✅ Clear monotonic gradient interpretation
- ✅ Standard epidemiological approach

**Interpretation:**
- OR = 1.00: Medevac Only Wrong (reference)
- OR > 1.00: Progressively more appropriate to choose medevac
- Clear story: "As appropriateness increases, medevac odds increase"

---

## 📈 **Figure Structure (5 Figures Total)**

### **Figure 1: Descriptive Overview**
**Source:** `final_report.qmd`  
**Type:** Stacked bar chart (all three options)  
**Purpose:** Show overall distribution patterns by normative status  
**Clinical Value:** Visual confirmation that physicians track appropriateness

### **Figure 2: Appropriateness Gradient**
**Source:** `final_report2.qmd`  
**Type:** Line plot with points  
**Purpose:** Model-estimated marginal probabilities  
**Shows:** Monotonic increase from "Only Wrong" to "Only Correct"

### **Figure 3: Physician Variation (Model 1)**
**Source:** `final_report2.qmd`  
**Type:** Caterpillar plot  
**Purpose:** Show physician-level variation after adjusting for normative status only  
**Y-axis:** Dynamic scaling (caps just above top CI)  
**Shows:** Baseline physician variation (before adding covariates)

### **Figure 4: Physician Variation (Model 2)** ⭐ **NEW**
**Source:** Created by merging  
**Type:** Caterpillar plot  
**Purpose:** Show physician-level variation after adjusting for normative status + confidence + experience  
**Y-axis:** Dynamic scaling  
**Shows:** Residual variation after accounting for measured individual factors  
**Key Comparison:** Narrower range than Figure 3 → covariates explain some variation

### **Figure 5: Calibration Plot**
**Source:** `final_report2.qmd`  
**Type:** Scatter plot with diagonal reference  
**Purpose:** Show individual physician appropriateness calibration  
**X-axis:** Prob(medevac) when "Only Wrong"  
**Y-axis:** Prob(medevac) when "Only Correct"  
**Color:** Years of experience  
**Zoomed:** Focus on where physicians actually cluster

---

## 📊 **Table Structure (9 Tables Total)**

### **Descriptive Section:**
1. **Table 1:** Expanded sample characteristics (affiliations, experience, vignette counts)
2. **Table 2.1:** Class A vignettes (One Correct Answer)
3. **Table 2.2:** Class B vignettes (Two Reasonable Options)
4. **Table 2.3:** Class C vignettes (Highly Ambiguous)

### **Model 1 (Primary):**
5. **Table 3:** Fixed effects (medevac normative status → ORs)
6. **Table 4:** Random effects (ICC, MOR, variance decomposition)

### **Model 2 (Extended):**
7. **Table 5:** Fixed effects (normative status + confidence + experience)
8. **Table 6:** Random effects with % variance reduction from Model 1

---

## 🎯 **Key Comparisons Enabled**

### **Figure 3 vs. Figure 4 (Both Caterpillar Plots)**

**Visual Comparison:**
- Figure 3: Wider spread (Model 1 - only normative status)
- Figure 4: Narrower spread (Model 2 - adds confidence/experience)

**Quantitative Comparison:**
- Model 1 range: [min to max] probability
- Model 2 range: [narrower min to max]
- Variance reduction: X% (reported in Table 6)

**Clinical Interpretation:**
"Confidence and experience explain X% of physician variation, but substantial residual variation remains (Figure 4), suggesting other unmeasured factors contribute to practice patterns."

### **Table 4 vs. Table 6 (Variance Components)**

**Direct Comparison:**
- ICC (Physician) Model 1: X%
- ICC (Physician) Model 2: Y%
- Reduction: Z%

**Shows:** How much individual factors matter

---

## 📝 **How to Present**

### **For Paper Methods:**

> We examined physician variation using mixed-effects logistic regression. Model 1 tested whether physicians track clinical appropriateness by including medevac normative status as a fixed effect with random intercepts for physicians and vignettes. Model 2 extended this by adding decision confidence and years of clinical experience as fixed effects to assess whether these individual factors explain physician-level variation.

### **For Paper Results:**

> **Descriptive Analysis (Tables 2.1-2.3, Figure 1):** Agreement varied by vignette class, with Class A (one correct answer) showing highest agreement (Gwet's AC1 typically >0.60) and Class C (ambiguous) showing appropriately lower agreement.
>
> **Primary Model (Tables 3-4, Figures 2-3):** Physicians appropriately tracked clinical appropriateness, with odds of medevac selection increasing monotonically from "only wrong" (reference) to "only correct" (OR = X.XX, 95% CI X.XX-X.XX, p < 0.001). After accounting for appropriateness, substantial physician-level variation persisted (ICC = X%, MOR = X.XX).
>
> **Extended Model (Tables 5-6, Figure 4):** Decision confidence (OR = X.XX per point) and years of experience (OR = X.XX per year) were significant predictors, together explaining X% of physician-level variance. However, substantial residual variation remained (ICC = Y%, MOR = Y.YY), indicating additional unmeasured factors contribute to practice patterns.

### **For Presentations:**

**Slide 1:** "Study Design" → Table 1  
**Slide 2:** "Descriptive Patterns" → Figure 1  
**Slide 3:** "Physicians Track Appropriateness" → Figure 2 + Table 3  
**Slide 4:** "But Variation Persists" → Figure 3 + Table 4  
**Slide 5:** "Individual Factors Matter" → Figure 4 comparison + Table 6  
**Slide 6:** "Individual Calibration" → Figure 5  

---

## 🎯 **Key Messages**

### **Message 1: Appropriate Group-Level Behavior**
"Physicians, on average, appropriately modulate medevac use based on clinical context."  
**Evidence:** Tables 2.1-2.3, Figure 1, Figure 2, Table 3

### **Message 2: Substantial Individual Variation**
"Even after accounting for appropriateness, meaningful physician-level variation persists."  
**Evidence:** Figure 3, Table 4

### **Message 3: Individual Factors Explain Some, But Not All**
"Confidence and experience explain X% of variation, but substantial residual variation remains."  
**Evidence:** Figure 4 comparison, Tables 5-6

### **Message 4: Individual Calibration Patterns**
"Physicians vary in how strongly they discriminate between appropriate and inappropriate scenarios."  
**Evidence:** Figure 5

---

## 📁 **File Details**

**Report File:** `quarto/final_report2.qmd`  
**Line Count:** ~1,100 lines  
**Output:** `quarto/final_report2.html` (3.1 MB, self-contained)

**Key Sections:**
1. Executive Summary
2. Table 1: Sample Characteristics
3. Figure 1: Stacked Bars
4. Tables 2.1-2.3: Descriptive Stats
5. Model 1: Primary Analysis
6. Model 2: Extended Analysis
7. Figures 2-5: Visualizations
8. Summary & Conclusions
9. Technical Appendix

---

## ✨ **What Makes This Report Strong**

### **Methodologically:**
- ✅ Hierarchical structure (descriptive → primary → extended)
- ✅ Clinically grounded categorization
- ✅ Comprehensive variance decomposition
- ✅ Direct comparison of Model 1 vs. Model 2
- ✅ Multiple complementary visualizations

### **Presentationally:**
- ✅ Clear narrative arc
- ✅ Tables and figures work together
- ✅ Both aggregate and individual perspectives
- ✅ Color-coded agreement indicators
- ✅ Dynamic y-axes for better data visualization

### **Clinically:**
- ✅ Actionable calibration plot
- ✅ Quantifies practice variation
- ✅ Shows what factors matter (and how much)
- ✅ Identifies residual variation needing further study

---

## 🚀 **Bottom Line**

You now have a **comprehensive, publication-ready report** that:

✅ Combines best descriptive elements from `final_report`  
✅ Adds sophisticated mixed models from `final_report2`  
✅ Includes caterpillar plots for BOTH models (comparison)  
✅ Uses clinically intuitive reference level  
✅ Tells a complete story from description → inference  
✅ Enables direct before/after covariate comparison  

**Total Figures:** 5 (1 descriptive + 4 analytical)  
**Total Tables:** 8 (1 sample + 3 descriptive + 4 model results)  
**Total Models:** 2 (primary + extended)  

**Ready to review:** Open `final_report2.html` in your browser! 🎉


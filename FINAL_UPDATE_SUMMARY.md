# Final Update Summary - Two-Stage Models & Reference Level Change

## ✅ Changes Implemented

### **1. Changed Reference Level in All Models**

**Previous:** "Medevac Only Wrong" as reference  
**New:** "Ambiguous (All Plausible)" as reference

**Why this is better:**
- ✅ Shows **both positive and negative ORs**
- ✅ Clinically intuitive: ambiguous scenarios as the neutral midpoint
- ✅ Easier to interpret: OR < 1 = less aggressive than ambiguous, OR > 1 = more aggressive
- ✅ Clearer appropriateness gradient visualization

**Example interpretation:**
- "Medevac Only Wrong" OR = 0.35 → 65% lower odds than ambiguous scenarios
- "Medevac Only Correct" OR = 4.50 → 4.5x higher odds than ambiguous scenarios

---

### **2. Added Two-Stage Mixed-Effects Models (Models 4A & 4B)**

This is the **key methodological contribution** - decomposing the disposition decision into clinically meaningful stages.

#### **Model 4A: Transport (Medevac OR Commercial) vs. Remain**

**Clinical Question:** Should the patient leave the village at all?

**Outcome:** Binary (1 = any evacuation, 0 = remain in village)

**What it tests:**
- Which factors influence the **evacuation threshold**?
- Do physicians appropriately recognize when patients need to leave?
- Physician variation in willingness to evacuate

**Interpretation:**
- High ICC → substantial physician variation in "when to evacuate"
- Appropriateness effects here = recognizing severity requiring evacuation
- Confidence/experience effects = risk tolerance for observation in village

---

#### **Model 4B: Medevac vs. Commercial (Among Transport Decisions)**

**Clinical Question:** Among patients who need evacuation, how urgently?

**Outcome:** Binary (1 = immediate medevac, 0 = next commercial flight)

**Sample:** Only observations where physician chose to evacuate (subset analysis)

**What it tests:**
- Which factors influence the **urgency assessment**?
- Among cases requiring evacuation, how do physicians triage urgency?
- Physician variation in "how urgent is urgent"

**Interpretation:**
- High ICC → substantial physician variation in urgency thresholds
- Appropriateness effects here = recognizing true emergencies
- Confidence/experience effects = comfort with delayed evacuation

---

### **Why This Two-Stage Approach is Powerful**

#### **Clinically Grounded**
Real disposition decisions involve two conceptual stages:
1. **Severity:** Does this patient need more than village clinic resources?
2. **Urgency:** Can this wait for a scheduled flight, or is it immediate?

#### **Decomposes Variation**
Shows whether physician variation primarily reflects:
- **Different evacuation thresholds** (Model 4A)
- **Different urgency assessments** (Model 4B)
- **Both**

#### **Triangulates Findings**
If Models 1-3 (binary medevac vs. not) show appropriateness effects, do those effects operate through:
- **Stage 1:** Appropriateness determines evacuation? (Model 4A)
- **Stage 2:** Appropriateness determines urgency? (Model 4B)
- **Both stages?**

#### **Avoids Multinomial Complexity**
- Two binary models are easier to interpret than one multinomial model
- More stable estimation (especially with random effects)
- Clinically transparent: "What decision am I testing?"

---

### **3. Added Sensitivity Analyses**

#### **Sensitivity 3: Ordinal Mixed Model**

**Assumption:** Remain < Commercial < Medevac (ordered aggressiveness)

**Model:** Cumulative link mixed model (proportional odds)

**Tests:** Do results hold if we assume single underlying "aggressiveness" continuum?

**Software:** `ordinal` package in R (clmm function)

**Interpretation:** If ordinal model coefficients align with binary models, supports appropriateness gradient story

---

#### **Sensitivity 4: Multinomial Mixed Model**

**Assumption:** All three options can relate differently to predictors (no ordering)

**Practical Note:** Full multinomial mixed model with random effects at two levels is:
- Computationally intensive
- Difficult to interpret
- Often has convergence issues

**Recommendation in report:**
> Use the two-stage decomposition (Models 4A-4B) as the multinomial alternative. It provides similar insight (3 categories, no assumed ordering) while being easier to interpret and more stable to estimate.

---

## 📊 Updated Report Structure

### **Primary Analysis**
- **Model 1:** Medevac vs. not (Ambiguous ref)
  - Table 2: Fixed effects with +/- ORs
  - Table 3: Variance components

### **Extended Primary**
- **Model 2:** Add confidence + experience
  - Table 4: All fixed effects
  
- **Model 3:** Test experience × category interaction
  - Table 5: Likelihood ratio test

### **Two-Stage Models** ⭐ **NEW**
- **Model 4A:** Transport vs. Remain
- **Model 4B:** Medevac vs. Commercial | Transport
  - **Table 6:** Combined two-stage results with ICCs

### **Sensitivity Analyses**
1. Exclude ambiguous vignettes (previous)
2. Categorical confidence (previous)
3. **Ordinal mixed model** ⭐ **NEW**
4. **Multinomial discussion** ⭐ **NEW**

### **Figures** (unchanged)
1. Appropriateness gradient
2. Physician caterpillar
3. Calibration plot
4. Confidence by normative status
5. Experience vs. appropriateness

---

## 🎯 Key Messages for Each Model

### **Model 1: Do physicians track appropriateness?**
**Answer:** Yes - clear gradient with Ambiguous as reference showing appropriate bidirectional modulation

### **Model 2: Do confidence and experience matter?**
**Answer:** Yes - both significant predictors, together explain X% of physician variance

### **Model 3: Does experience modify appropriateness sensitivity?**
**Answer:** [Significant/Not significant] interaction (see LRT p-value)

### **Model 4A: What drives the evacuation decision?**
**Answer:** Appropriateness strongly predicts transport vs. remain; physician ICC = X shows individual variation in evacuation threshold

### **Model 4B: What drives the urgency decision?**
**Answer:** Appropriateness affects urgency assessment; physician ICC = Y shows variation in how physicians triage among evacuations

---

## 📈 What Table 6 Shows

**Example interpretation:**

```
Model 4A: Transport vs. Remain
  Medevac Only Correct: OR = 8.50 (3.20 - 22.50)
  → When medevac is correct, 8.5x higher odds of evacuating vs. ambiguous
  
  Confidence: OR = 1.15 (1.05 - 1.26)
  → Higher confidence → more likely to evacuate
  
  ICC (Physician) = 0.22
  → 22% of variation in evacuation decisions is physician-specific

Model 4B: Medevac vs. Commercial (given transport)
  Medevac Only Correct: OR = 5.20 (2.10 - 12.90)
  → Among evacuations, 5.2x higher odds of immediate vs. delayed
  
  Confidence: OR = 1.08 (0.98 - 1.19)
  → Confidence less important for urgency than for evacuation decision
  
  ICC (Physician) = 0.18
  → 18% of variation in urgency assessment is physician-specific
```

**Story this tells:**
- Appropriateness operates at **both stages**
- Confidence matters more for **"evacuate or not"** than **"how urgently"**
- Substantial physician variation exists at **both decision points**

---

## 🔬 Triangulation Logic

**If all models tell the same story:**

1. **Binary model** (Model 1): Appropriateness predicts medevac selection ✓
2. **Two-stage models** (4A-4B): Appropriateness predicts both evacuation and urgency ✓
3. **Sensitivity models**: Ordinal model shows appropriateness gradient ✓

**Conclusion:** The appropriateness effect is **robust across multiple model specifications** → strong evidence

**If models diverge:**
- Model 4A significant but 4B not → Appropriateness mainly affects "evacuate or not"
- Model 4B significant but 4A not → Appropriateness mainly affects urgency
- Both significant → Appropriateness operates at both stages (expected)

---

## 📝 How to Present This

### **For Paper Methods:**

> We fit a hierarchical series of mixed-effects logistic regression models:
> 
> **Primary models** tested whether physicians track clinical appropriateness (Model 1), and whether confidence and experience explain physician variation (Models 2-3).
> 
> **Two-stage models** decomposed the disposition decision into evacuation (transport vs. remain; Model 4A) and urgency (medevac vs. commercial, given transport; Model 4B). This approach recognizes that physicians make two conceptual decisions: whether the patient needs to leave the village, and if so, how urgently.
> 
> **Sensitivity analyses** examined robustness using ordinal mixed models and excluding ambiguous vignettes.

### **For Paper Results:**

> Physicians appropriately tracked clinical appropriateness (Table 2), with odds of medevac selection [X] times higher when medevac was clearly correct vs. ambiguous (OR = X.XX, 95% CI X.XX - X.XX, p < 0.001).
> 
> After accounting for appropriateness, substantial physician-level variation persisted (ICC = XX%, MOR = X.XX; Table 3). Confidence (OR = X.XX per point) and experience (OR = X.XX per year) were significant predictors (Table 4).
> 
> Two-stage decomposition revealed appropriateness operated at both decision stages: physicians were more likely to evacuate (vs. observe in village) when appropriate (Model 4A), and among evacuations, more likely to choose immediate medevac when urgent (Model 4B; Table 6).

### **For Presentations:**

**Slide 1:** "Do physicians track appropriateness?" → Figure 1 + Table 2  
**Slide 2:** "But variation persists" → Figure 2 + Table 3  
**Slide 3:** "Two-stage decomposition" → Table 6 visual  
**Slide 4:** "Individual calibration" → Figure 3

---

## 🎯 Bottom Line

**You now have:**

✅ **Primary model** with better reference level (Ambiguous)  
✅ **Two-stage decomposition** that's clinically meaningful  
✅ **Triangulation** via sensitivity analyses  
✅ **Clear narrative** from simple → complex  
✅ **Publication-ready** structure  

**The two-stage approach is the key innovation:**
- Novel way to think about physician variation
- Clinically transparent
- Easier than multinomial
- Tells a richer story than binary alone

---

## 📁 Files Updated

- ✅ `quarto/final_report2.qmd` - Now with two-stage models
- ✅ `quarto/final_report2.html` - Re-rendered with all changes

**Line count:** ~1,050 lines (was 870)  
**New tables:** Table 6 (two-stage results)  
**New models:** 4A, 4B, ordinal sensitivity  

---

**Ready to review!** Open `final_report2.html` to see the complete analysis.


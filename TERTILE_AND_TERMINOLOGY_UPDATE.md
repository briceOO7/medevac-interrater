# Tertile and Terminology Updates - Final Report 2

## Summary of Changes

### 1. **Experience Variable: Quartiles → Tertiles**

**Previous (Quartiles):**
- 4 groups: Q1, Q2, Q3, Q4
- Q1 (least experienced) as reference
- 3 comparisons: Q2 vs Q1, Q3 vs Q1, Q4 vs Q1

**Now (Tertiles):**
- 3 groups: Low, Medium, High
- **Medium (middle tertile) as reference**
- 2 comparisons: Low vs Medium, High vs Medium

**Rationale:**
- Simpler interpretation with fewer groups
- Middle tertile as reference allows bidirectional comparison (less vs. more experienced)
- More statistical power per group (larger n per tertile)

---

### 2. **Terminology Change Throughout Document**

**Replaced:**
- "Medevac Normative Status" → **"Vignette Type"**
- "normative status" → **"vignette type"**

**Why:**
- More intuitive clinical language
- "Vignette Type" clearly describes categorization by appropriateness
- Consistent with Table 2 terminology

---

## Key Table Changes

### **Table 5: Model 2 Fixed Effects**

**Now Shows:**

```
Vignette Type
  Medevac Only Wrong (reference)         1.00    ref
  Medevac One of Two Wrong               0.XX    (...)
  Ambiguous (All Plausible)              X.XX    (...)
  Medevac One of Two Correct             X.XX    (...)
  Medevac Only Correct                   XX.X    (...)

Decision Characteristics
  Confidence (per 1-point increase)      X.XX    (...)

Years of Experience (Tertiles)
  Low: 5-10 years (n=X)                  X.XX    (...)
  Medium: 11-17 years (n=Y) (reference)  1.00    ref
  High: 18-25 years (n=Z)                X.XX    (...)
```

**Interpretation:**
- **Low vs. Medium**: Shows if least experienced differ from average
- **High vs. Medium**: Shows if most experienced differ from average
- Maintains order: Low → Medium → High for logical reading

---

## Statistical Advantages of Tertiles with Middle Reference

1. **Bidirectional Comparison**
   - Can see both directions of effect (lower and higher than average)
   - Q1 (low) vs Q2 (medium): Are novices different?
   - Q3 (high) vs Q2 (medium): Are experts different?

2. **Clinical Interpretation**
   - Medium tertile represents "typical" experience level
   - Deviations show practice pattern differences at extremes

3. **Power**
   - Fewer groups = more physicians per group
   - Better precision for each estimate

---

## Figures Updated

All figures and their subtitles now use "vignette type" language:

- **Figure 2**: "Model-estimated probability of choosing medevac by vignette type"
- **Figure 3**: "Adjusted for vignette type (Model 1)"
- **Figure 4**: "Adjusted for vignette type, confidence, and experience (Model 2)"

---

## Model Specification

### Model 2 (Extended)
```r
glmer(chose_medevac ~ medevac_status_label + 
                      confidence_centered + 
                      experience_tertile +  # Medium as reference
                      (1 | physician_id) + 
                      (1 | question),
      data = data, 
      family = binomial)
```

**Fixed Effects:**
- 5 vignette type categories (Medevac Only Wrong = ref)
- Confidence (centered, continuous)
- 3 experience tertiles (Medium = ref)

**Random Effects:**
- Physician-level intercepts (captures unexplained variation between physicians)
- Vignette-level intercepts (captures variation between clinical scenarios)

---

## Report Status

✅ **Rendered successfully:** `final_report2.html`

All tables, figures, and interpretation text updated to reflect:
1. Tertile-based experience analysis
2. "Vignette Type" terminology throughout
3. Medium tertile as reference level

---

## Next Steps (If Needed)

Consider sensitivity analyses:
1. Test continuous experience vs tertiles (likelihood ratio test)
2. Examine if experience × vignette type interaction exists
3. Stratified analysis by tertile to see if vignette type effects differ by experience level

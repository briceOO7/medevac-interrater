# Terminology Update: Never/Always Medevac

## Changes Made (Commit: ad204b5)

### **1. Terminology Changes Throughout Document**

**Old → New:**
- "Medevac Only Wrong" → **"Never Medevac"**
- "Medevac Only Correct" → **"Always Medevac"**

**Affected Locations:**
- Executive Summary
- Table 1 (Vignette breakdown)
- Table 2 (pack_rows groupings)
- Table 3 (reference level and predictor labels)
- Figure 2 (category labels and title)
- Figure 4 (axis labels and subtitle)
- All inline text references
- Data mapping file (medevac_normative_mapping.csv)

---

### **2. Table 1 Responses Section Expanded**

**New metrics added:**
- **Correct Responses to Always Medevac**: % (n=X)
  - Shows percentage of responses that correctly chose medevac when it was the single best option
- **Correct Responses to Never Medevac**: % (n=X)
  - Shows percentage of responses that correctly avoided medevac when it was inappropriate

**Implementation:**
```r
correct_responses <- data %>%
  mutate(
    correct_always = ifelse(medevac_status_label == "Always Medevac" & decision == "Medevac", 1, 0),
    correct_never = ifelse(medevac_status_label == "Never Medevac" & decision != "Medevac", 1, 0),
    ...
  )
```

---

### **3. Why This Change Matters**

**Clearer Communication:**
- "Never/Always" is more intuitive than "Only Wrong/Only Correct"
- Directly communicates when medevac is/isn't appropriate
- Easier for non-statistician reviewers to understand

**Clinical Relevance:**
- New metrics in Table 1 show physician accuracy on clear-cut cases
- Helps identify if variation is due to unclear scenarios vs. fundamental disagreement

---

### **4. Files Modified**

1. `quarto/final_report2.qmd` - All text, tables, and figures
2. `quarto/final_report2.html` - Rendered output
3. `data/medevac_normative_mapping.csv` - Source data labels

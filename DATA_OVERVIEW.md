# Data Overview - Medevac Interrater Reliability Study

## 📊 Data Files

### 1. `survey_results.csv`
- **Description**: Survey responses from physicians evaluating medevac decision vignettes
- **Structure**: 
  - 21 rows (20 physicians + 1 header)
  - Multiple columns for:
    - Demographics (degree, training year, workplace, experience)
    - 20 clinical vignettes with decision options
    - Confidence ratings for each decision

### 2. `Physician_Medevac_Analysis_Plan.docx`
- **Description**: Statistical analysis plan for the study
- **Key Information**:
  - 20 physicians
  - 20 standardized patient vignettes
  - 3 management options per vignette:
    1. Medevac (immediate)
    2. Next commercial flight
    3. Remain in village
  - 4 vignette classes (A, B, C, D)

## 📋 Vignette Classification

| Question | Question Type | Vignette Class |
|----------|--------------|----------------|
| 1 | Clear Medevac | A |
| 2 | Clear Not Medevac | A |
| 3 | Any Option | C |
| 4 | Clear Medevac | A |
| 5 | Clear Not Medevac | B |
| 6 | Clear Not Medevac | B |
| 7 | Clear Not Remain | B |
| 8 | Clear Remain | A |
| 9 | Clear Commercial | A |
| 10 | Clear Not Remain | B |
| 11 | Clear Remain | A |
| 12 | Any Option | C |
| 13 | Clear Medevac | A |
| 14 | Clear Not Medevac | B |
| 15 | Clear Commercial | A |
| 16 | Conflict Between Physiology/Logistics | D |
| 17 | Conflict Between Physiology/Logistics | D |
| 18 | Conflict Between Physiology/Logistics | D |
| 19 | Clear Medevac | A |
| 20 | Any Option | C |

## 🎯 Analysis Plan Overview

The study involves:
- **Repeated measures design**: Each physician responds to multiple vignettes
- **Interrater reliability**: Measure agreement between physicians
- **Vignette class analysis**: Compare agreement across different vignette types

## 📈 Expected Analyses

1. **Interrater Reliability**
   - Cohen's Kappa (for categorical agreement)
   - Fleiss' Kappa (for multiple raters)
   - Percentage agreement

2. **By Vignette Class**
   - Compare reliability across classes A, B, C, D
   - Class A: Clear cases (expected high agreement)
   - Class B: Clear not-X cases (expected high agreement)
   - Class C: Any option acceptable (expected lower agreement)
   - Class D: Conflict cases (expected lower agreement)

3. **Confidence Analysis**
   - Relationship between confidence and agreement
   - Confidence by vignette class

4. **Demographic Factors**
   - Experience level (years at Maniilaq)
   - Training year
   - Previous rural experience
   - Work location

## 🔧 Next Steps

1. Clean and structure the data
2. Calculate interrater reliability metrics
3. Analyze by vignette class
4. Create visualizations
5. Generate statistical report

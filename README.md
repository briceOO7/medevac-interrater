# Medevac Interrater Reliability Analysis

A Python project for analyzing interrater reliability in physician medevac decision-making using standardized clinical vignettes.

## 📊 Study Overview

This project analyzes agreement between 20 physicians evaluating 20 standardized patient vignettes. Each physician selects one of three management options:
- **Medevac** (immediate medical evacuation)
- **Commercial** (next available commercial flight)
- **Remain** (remain in village for observation/treatment)

Vignettes are classified into four categories:
- **Class A**: Clear cases (expected high agreement)
- **Class B**: Clear not-X cases (expected high agreement)
- **Class C**: Any option acceptable (expected lower agreement)
- **Class D**: Conflict between physiology/logistics (expected lower agreement)

## 🚀 Quick Start

### Workflow Overview

This project uses a **Python → R** workflow:
- **Python**: Data loading, cleaning, and processing
- **R**: Statistical analysis and reporting
- **Quarto**: Dynamic reports and documentation

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd medevac_interrater
   ```

2. **Python Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **R Dependencies:**
   ```r
   # In R or RStudio
   install.packages(c("dplyr", "ggplot2", "irr", "knitr", "kableExtra", "here", "quarto"))
   ```

### Workflow

#### Step 1: Process Data (Python)
```bash
source .venv/bin/activate
python scripts/python/process_data.py
```
This creates `data/processed/survey_data_processed.csv` for R analysis.

#### Step 2: Run Analysis (R)
```r
# In R or RStudio
source("scripts/r/run_analysis.R")
```
Or from command line:
```bash
Rscript scripts/r/run_analysis.R
```

#### Step 3: Generate Report (Quarto)
```bash
quarto render quarto/analysis_report.qmd
```
Or in RStudio, click "Render" on the `.qmd` file.

## 📈 Analysis Output

The analysis generates several output files in the `output/` directory:

- `cleaned_data_long.csv`: Reshaped data in long format (physician × question)
- `question_level_metrics.csv`: Agreement metrics for each of the 20 questions
- `class_level_metrics.csv`: Agreement metrics aggregated by vignette class
- `confidence_by_decision.csv`: Confidence ratings by decision type
- `confidence_by_class.csv`: Confidence ratings by vignette class

## 🔬 Analysis Methods

- **Percentage Agreement**: Simple agreement between all physician pairs
- **Fleiss' Kappa**: Interrater reliability metric for multiple raters (accounts for chance agreement)
- **Confidence Analysis**: Relationship between confidence ratings and agreement

## 📁 Project Structure

```
medevac_interrater/
├── data/
│   ├── raw/                # Raw data files
│   ├── processed/          # Processed data (Python output)
│   └── survey_results.csv  # Original survey data
├── scripts/
│   ├── python/             # Python data processing scripts
│   │   └── process_data.py # Main data processing script
│   └── r/                  # R analysis scripts
│       └── run_analysis.R  # Main analysis script
├── R/
│   └── R/                  # R package source
│       └── analysis.R      # Analysis functions
├── quarto/                 # Quarto documents
│   └── analysis_report.qmd # Main analysis report
├── output/                 # Analysis outputs (CSV files)
├── src/                    # Python source code
│   └── medevac_interrater/ # Python package
│       └── data_loader.py  # Data loading/cleaning
├── tests/                  # Test files
├── .venv/                  # Python virtual environment
├── requirements.txt        # Python dependencies
├── requirements.R          # R package list
└── README.md              # This file
```

## 🧪 Testing

```bash
pytest
pytest tests/ -v
```

## 📝 License

[Add your license here]

## 👥 Contributors

[Add contributors here]


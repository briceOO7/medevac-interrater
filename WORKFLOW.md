# Workflow Guide

This document describes the Python → R → Quarto workflow for the medevac interrater reliability study.

## Overview

The project follows a clean separation of concerns:

1. **Python**: Data processing (loading, cleaning, reshaping)
2. **R**: Statistical analysis (interrater reliability, confidence analysis)
3. **Quarto**: Reporting (dynamic documents with code, results, and visualizations)

## Step-by-Step Workflow

### 1. Data Processing (Python)

**Purpose**: Clean and prepare raw survey data for analysis.

**Script**: `scripts/python/process_data.py`

**Run**:
```bash
source .venv/bin/activate
python scripts/python/process_data.py
```

**Output**: 
- `data/processed/survey_data_processed.csv` - Clean, long-format data ready for R

**What it does**:
- Loads raw survey CSV
- Cleans and standardizes decision values
- Reshapes from wide to long format
- Adds vignette classifications
- Outputs clean CSV for R

### 2. Statistical Analysis (R)

**Purpose**: Calculate interrater reliability metrics and statistical analyses.

**Script**: `scripts/r/run_analysis.R`

**Run** (from R/RStudio):
```r
source("scripts/r/run_analysis.R")
```

**Or** (from command line):
```bash
Rscript scripts/r/run_analysis.R
```

**Output** (in `output/` directory):
- `question_level_metrics.csv` - Metrics for each of 20 questions
- `class_level_metrics.csv` - Metrics aggregated by vignette class
- `confidence_by_decision.csv` - Confidence ratings by decision type
- `confidence_by_class.csv` - Confidence ratings by vignette class

**What it does**:
- Calculates percentage agreement
- Calculates Fleiss' Kappa for multiple raters
- Analyzes confidence ratings
- Generates summary statistics

### 3. Generate Report (Quarto)

**Purpose**: Create publication-ready report with code, results, and visualizations.

**Document**: `quarto/analysis_report.qmd`

**Run**:
```bash
quarto render quarto/analysis_report.qmd
```

**Or** in RStudio: Open the `.qmd` file and click "Render"

**Output**: 
- `quarto/analysis_report.html` - Interactive HTML report

**What it does**:
- Loads processed data
- Runs analyses inline
- Creates visualizations
- Generates formatted tables
- Produces publication-ready document

## File Organization

```
data/
├── raw/                    # Original raw data (manual)
├── processed/              # Python output (auto-generated)
│   └── survey_data_processed.csv

scripts/
├── python/                 # Data processing
│   └── process_data.py
└── r/                      # Statistical analysis
    └── run_analysis.R

R/
└── R/                      # R functions
    └── analysis.R

quarto/
└── analysis_report.qmd     # Report document

output/                     # R analysis outputs (auto-generated)
├── question_level_metrics.csv
├── class_level_metrics.csv
└── ...
```

## Best Practices

1. **Always run Python first** - R analysis depends on processed data
2. **Don't modify processed data manually** - Re-run Python script if raw data changes
3. **Version control** - Commit raw data, processed data, and outputs
4. **Document changes** - Update analysis scripts with clear comments
5. **Reproducibility** - Use fixed seeds for any random processes

## Troubleshooting

### Python script fails
- Check that raw data file exists: `data/survey_results.csv`
- Verify virtual environment is activated
- Check Python dependencies: `pip install -r requirements.txt`

### R script fails
- Verify processed data exists: `data/processed/survey_data_processed.csv`
- Check R packages are installed
- Try running from project root directory

### Quarto won't render
- Install Quarto: https://quarto.org/docs/get-started/
- Verify R packages are installed (especially `quarto`, `knitr`, `ggplot2`)
- Check file paths in `.qmd` file

## Adding New Analyses

### To add a new Python processing step:
1. Edit `scripts/python/process_data.py`
2. Add new columns to processed data
3. Update data loader if needed

### To add a new R analysis:
1. Add function to `R/R/analysis.R`
2. Call function in `scripts/r/run_analysis.R`
3. Save results to `output/` directory

### To add to Quarto report:
1. Add code chunk to `quarto/analysis_report.qmd`
2. Load results from `output/` or run analysis inline
3. Add visualization or table

## Dependencies

### Python
- pandas
- numpy
- python-docx

### R
- dplyr
- ggplot2
- irr (for Fleiss' Kappa)
- knitr
- kableExtra
- quarto
- here



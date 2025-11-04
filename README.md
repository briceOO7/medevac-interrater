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

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd medevac_interrater
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Development

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the analysis
python scripts/run_analysis.py

# Explore the data
python scripts/explore_data.py

# Run tests
pytest
```

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
├── src/                    # Source code
│   └── medevac_interrater/ # Main package
├── tests/                  # Test files
├── data/                   # Data files
├── scripts/                # Executable scripts
├── notebooks/              # Jupyter notebooks
├── docs/                   # Documentation
├── .venv/                  # Virtual environment (git-ignored)
├── pyproject.toml          # Project configuration
├── requirements.txt        # Dependencies
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

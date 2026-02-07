# Setup Guide

This guide will help you set up the Customer Purchase Behavior Analysis project on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
  - Download from [python.org](https://www.python.org/downloads/)
  - Verify installation: `python --version`

- **Git**
  - Download from [git-scm.com](https://git-scm.com/)
  - Verify installation: `git --version`

- **Jupyter Notebook**
  - Will be installed via requirements.txt

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/retail-customer-analytics.git
cd retail-customer-analytics
```

### 2. Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Download the Dataset

Due to size constraints, the dataset is not included in this repository.

**Option A: Use Kaggle Dataset**
1. Visit [Kaggle](https://www.kaggle.com/) and search for "Black Friday" dataset
2. Download the CSV file
3. Place it in `data/raw/walmart_data.csv`

**Option B: Use Your Own Data**
1. Ensure your data has the same structure (see `data/README.md`)
2. Place it in `data/raw/`
3. Update the file path in the notebook if needed

### 5. Verify Installation

Test that everything is working:

```bash
python -c "import pandas; import numpy; import matplotlib; print('All packages imported successfully!')"
```

### 6. Launch Jupyter Notebook

```bash
jupyter notebook
```

This will open Jupyter in your web browser. Navigate to `notebooks/Customer_Purchase_Analysis.ipynb`.

## Project Structure

After setup, your directory should look like this:

```
retail-customer-analytics/
├── data/
│   ├── raw/
│   │   └── walmart_data.csv          # Your dataset (not in repo)
│   └── processed/                     # Generated during analysis
├── notebooks/
│   └── Customer_Purchase_Analysis.ipynb
├── reports/
│   └── figures/                       # Generated plots
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── statistical_analysis.py
│   └── visualization.py
├── requirements.txt
└── README.md
```

## Running the Analysis

### Quick Start

1. Open `notebooks/Customer_Purchase_Analysis.ipynb`
2. Run all cells: **Cell → Run All**
3. Review the outputs and visualizations

### Step-by-Step

1. Start with data loading and exploration
2. Follow the analysis sections in order
3. Examine visualizations as they're generated
4. Review statistical results and confidence intervals

## Troubleshooting

### Common Issues

**Issue: ModuleNotFoundError**
```bash
# Solution: Install missing package
pip install <package-name>
```

**Issue: Jupyter Notebook won't start**
```bash
# Solution: Try reinstalling jupyter
pip install --upgrade jupyter notebook
```

**Issue: File not found error for dataset**
```bash
# Solution: Check that data file is in correct location
ls data/raw/  # Should show your CSV file
```

**Issue: Virtual environment not activating**
```bash
# Windows: Try
venv\Scripts\activate.bat

# Or use
python -m venv venv --clear
```

**Issue: Memory error with large dataset**
- Try sampling the data:
```python
df = pd.read_csv('data/raw/walmart_data.csv', nrows=100000)
```

### Package Version Conflicts

If you encounter version conflicts:

```bash
# Create fresh environment
deactivate  # If in a venv
rm -rf venv  # Remove old environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Development Setup

If you plan to contribute to the project:

### 1. Install Development Dependencies

```bash
pip install -r requirements.txt
pip install jupyter black pylint pytest
```

### 2. Set Up Git Hooks (Optional)

```bash
# Add pre-commit hook to clear notebook outputs
pip install nbstripout
nbstripout --install
```

### 3. IDE Setup

**VS Code:**
- Install Python extension
- Install Jupyter extension
- Set Python interpreter to your virtual environment

**PyCharm:**
- Open project folder
- Configure Python interpreter to use venv
- Install Jupyter plugin

## Data Privacy

⚠️ **Important:** Never commit actual data files to GitHub
- The `.gitignore` file is configured to exclude `*.csv` files
- Only commit code, notebooks (with outputs cleared), and documentation

## Getting Help

If you encounter issues:

1. Check this SETUP.md file
2. Review the [README.md](README.md)
3. Check the [CASE_STUDY.md](CASE_STUDY.md) for context
4. Open an issue on GitHub with:
   - Your operating system
   - Python version
   - Error message (full traceback)
   - Steps to reproduce

## Next Steps

After setup:

1. ✅ Read the [CASE_STUDY.md](CASE_STUDY.md) to understand the business problem
2. ✅ Review the [README.md](README.md) for project overview
3. ✅ Open and run the Jupyter notebook
4. ✅ Explore the `src/` modules for reusable functions
5. ✅ Check out visualizations in `reports/figures/`

Happy analyzing! 📊

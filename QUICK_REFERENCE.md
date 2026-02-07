# Quick Reference Guide

## 🚀 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/yourusername/retail-customer-analytics.git
cd retail-customer-analytics
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run analysis
jupyter notebook notebooks/Customer_Purchase_Analysis.ipynb
```

## 📁 File Structure Overview

```
retail-customer-analytics/
├── 📊 data/                  # Data files (add your dataset here)
├── 📓 notebooks/             # Jupyter notebook with analysis
├── 📈 reports/               # Generated visualizations
├── 🐍 src/                   # Reusable Python modules
├── 📖 README.md              # Project overview (read first!)
├── 📋 CASE_STUDY.md          # Original requirements
└── ⚙️ SETUP.md               # Detailed setup instructions
```

## 🔧 Common Commands

### Virtual Environment
```bash
# Create
python -m venv venv

# Activate
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# Deactivate
deactivate
```

### Package Management
```bash
# Install all dependencies
pip install -r requirements.txt

# Install single package
pip install pandas

# Update packages
pip install --upgrade pandas numpy

# List installed packages
pip list

# Save current packages
pip freeze > requirements.txt
```

### Jupyter Commands
```bash
# Start Jupyter
jupyter notebook

# Start on specific port
jupyter notebook --port 8889

# List running notebooks
jupyter notebook list

# Convert notebook to HTML
jupyter nbconvert --to html notebooks/Customer_Purchase_Analysis.ipynb

# Convert to PDF (requires LaTeX)
jupyter nbconvert --to pdf notebooks/Customer_Purchase_Analysis.ipynb
```

### Git Commands
```bash
# Initial setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/retail-customer-analytics.git
git push -u origin main

# Regular workflow
git status
git add .
git commit -m "Your commit message"
git push

# Update from remote
git pull

# Create branch
git checkout -b feature/new-analysis
```

## 📊 Key Analysis Steps

### 1. Data Loading
```python
import pandas as pd
df = pd.read_csv('data/raw/walmart_data.csv')
```

### 2. Exploratory Analysis
```python
df.info()
df.describe()
df.head()
```

### 3. Calculate Confidence Interval
```python
from src.statistical_analysis import calculate_confidence_interval

mean, lower, upper, margin = calculate_confidence_interval(
    data=df['Purchase'], 
    confidence=0.95
)
```

### 4. Compare Groups
```python
from src.statistical_analysis import confidence_interval_comparison

results = confidence_interval_comparison(
    group1=df[df['Gender']=='M']['Purchase'],
    group2=df[df['Gender']=='F']['Purchase'],
    confidence=0.95
)
```

### 5. Visualize Results
```python
from src.visualization import plot_confidence_intervals

fig = plot_confidence_intervals(
    groups_data=[male_data, female_data],
    group_names=['Male', 'Female'],
    confidence=0.95
)
```

## 📚 Useful Functions

### From `src/data_preprocessing.py`
```python
from src.data_preprocessing import (
    load_data,              # Load CSV
    check_data_quality,     # Data quality report
    handle_missing_values,  # Handle NaN
    detect_outliers,        # Find outliers
    create_age_bins,        # Create age groups
)
```

### From `src/statistical_analysis.py`
```python
from src.statistical_analysis import (
    calculate_confidence_interval,      # CI calculation
    confidence_interval_comparison,     # Compare 2 groups
    sample_mean_distribution,           # Demonstrate CLT
    t_test_independent,                 # T-test
    effect_size_cohens_d,              # Effect size
)
```

### From `src/visualization.py`
```python
from src.visualization import (
    plot_distribution,           # Histogram + KDE
    plot_boxplot_by_group,      # Boxplot comparison
    plot_confidence_intervals,   # CI visualization
    plot_correlation_heatmap,    # Correlation matrix
)
```

## 🎯 Key Metrics to Calculate

1. **Average Purchase by Gender**
   - Male average spending
   - Female average spending

2. **Confidence Intervals (95%)**
   - Gender groups
   - Marital status groups
   - Age groups

3. **Statistical Tests**
   - Independent t-test
   - ANOVA for multiple groups
   - Effect sizes

4. **Central Limit Theorem**
   - Sample mean distribution
   - Different sample sizes
   - Convergence to normal

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | `pip install <package-name>` |
| Jupyter won't start | `pip install --upgrade jupyter` |
| Data file not found | Check path: `data/raw/walmart_data.csv` |
| Memory error | Sample data: `df = pd.read_csv(..., nrows=100000)` |
| Virtual env issues | Recreate: `rm -rf venv && python -m venv venv` |

## 📝 Before Committing to GitHub

```bash
# 1. Clear notebook outputs (keep code only)
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb

# 2. Check what will be committed
git status

# 3. Ensure .gitignore is working
git ls-files data/  # Should not show CSV files

# 4. Write meaningful commit message
git commit -m "Add: confidence interval analysis for age groups"
```

## 🎨 Customization Tips

### Change Plot Style
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style('whitegrid')  # or 'darkgrid', 'white', 'dark'
plt.style.use('ggplot')     # or 'seaborn', 'fivethirtyeight'
```

### Save Figures
```python
from src.visualization import save_figure

fig = plot_distribution(data)
save_figure(fig, 'distribution_plot.png', dpi=300)
```

## 🔗 Important Links

- [README.md](README.md) - Full project documentation
- [CASE_STUDY.md](CASE_STUDY.md) - Business problem details
- [SETUP.md](SETUP.md) - Detailed setup guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

## 📧 Getting Help

1. Check documentation files
2. Review notebook comments
3. Search issues on GitHub
4. Open new issue with details

---

**Pro Tip:** Bookmark this file for quick reference while working on the project!

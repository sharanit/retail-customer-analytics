# Customer Purchase Behavior Analysis
## Statistical Inference with Confidence Intervals and Central Limit Theorem

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## 📋 Table of Contents
- [Overview](#overview)
- [Business Problem](#business-problem)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [Recommendations](#recommendations)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project analyzes customer purchase behavior from a major retail corporation's Black Friday sales data. Using statistical inference techniques including **Confidence Intervals** and the **Central Limit Theorem (CLT)**, we investigate whether spending patterns differ significantly across demographic segments such as gender, marital status, and age groups.

The analysis provides actionable insights for retail businesses to optimize marketing strategies, inventory management, and customer targeting.

## 💼 Business Problem

**Objective:** Analyze customer purchase behavior to understand spending patterns across different demographic segments.

**Key Questions:**
- Do women spend more than men during Black Friday sales?
- How do spending patterns differ between married and unmarried customers?
- What are the spending trends across different age groups?
- Can we statistically validate these differences with confidence?

**Impact:** Insights from this analysis can help businesses:
- Design targeted marketing campaigns
- Optimize product placement and inventory
- Personalize customer experiences
- Improve revenue forecasting

## 📊 Dataset

The dataset contains transactional data from Black Friday sales with approximately 100 million customers (50M male, 50M female).

**Features:**
- `User_ID`: Unique customer identifier
- `Product_ID`: Unique product identifier
- `Gender`: Customer gender (M/F)
- `Age`: Age group bins
- `Occupation`: Masked occupation code
- `City_Category`: City classification (A, B, C)
- `Stay_In_Current_City_Years`: Residence duration
- `Marital_Status`: Marital status (0/1)
- `Product_Category`: Masked product category
- `Purchase`: Transaction amount (target variable)

**Dataset Size:** ~550,000 transactions

## 🔬 Methodology

### 1. Exploratory Data Analysis (EDA)
- Data quality assessment (missing values, outliers)
- Univariate analysis (distributions, summary statistics)
- Bivariate analysis (correlations, group comparisons)
- Visual analysis (histograms, box plots, heatmaps)

### 2. Statistical Inference
- **Sampling:** Random sampling from population segments
- **Central Limit Theorem:** Distribution of sample means
- **Confidence Intervals:** 90%, 95%, and 99% confidence levels
- **Hypothesis Testing:** Comparing spending across demographics

### 3. Comparative Analysis
Performed statistical analysis across:
- Gender (Male vs Female)
- Marital Status (Married vs Unmarried)
- Age Groups (0-17, 18-25, 26-35, 36-50, 51+)

## 🔍 Key Findings

> **Note:** Detailed findings are available in the Jupyter notebook and analysis report.

Key insights include:
- Statistical comparison of average spending by gender
- Confidence interval analysis for different demographic segments
- Distribution patterns of purchase amounts
- Recommendations for targeted business strategies

## 🚀 Installation

### Prerequisites
```bash
Python 3.8+
Jupyter Notebook
```

### Setup
1. Clone the repository:
```bash
git clone https://github.com/sharait/retail-customer-analytics.git
cd retail-customer-analytics
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. **Launch Jupyter Notebook:**
```bash
jupyter notebook
```

2. **Open the analysis notebook:**
```
notebooks/Customer_Purchase_Analysis.ipynb
```

3. **Run all cells** to reproduce the analysis

Alternatively, view the pre-rendered HTML report:
```
reports/analysis_report.html
```

## 📁 Project Structure

```
retail-customer-analytics/
│
├── data/
│   ├── raw/                      # Original dataset (not included in repo)
│   └── README.md                 # Data source and description
│
├── notebooks/
│   └── Customer_Purchase_Analysis.ipynb    # Main analysis notebook
│
├── reports/
│   ├── analysis_report.html      # HTML export of analysis
│   └── figures/                  # Generated visualizations
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py     # Data cleaning functions
│   ├── statistical_analysis.py   # Statistical inference functions
│   └── visualization.py          # Plotting utilities
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── CASE_STUDY.md                 # Original case study requirements
```

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations
- **SciPy** - Statistical functions and tests
- **Jupyter Notebook** - Interactive development environment

## 📈 Results

### Sample Size vs Confidence Interval Width
The analysis demonstrates how sample size affects the precision of population estimates using the Central Limit Theorem.

### Gender-Based Analysis
Statistical comparison of purchase amounts between male and female customers with confidence intervals.

### Demographic Segmentation
Analysis of spending patterns across marital status and age groups.

> **Detailed results, visualizations, and statistical tables are available in the notebooks and reports folders.**

## 💡 Recommendations

Based on the statistical analysis, key business recommendations include:

1. **Targeted Marketing Campaigns** - Focus resources on high-spending demographic segments
2. **Product Placement Optimization** - Align product categories with segment preferences
3. **Personalized Promotions** - Design offers based on demographic spending patterns
4. **Inventory Management** - Adjust stock levels based on segment-specific demand

*Full recommendations with supporting data are available in the analysis notebook.*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/sharanit)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/sharanvora)

## 🙏 Acknowledgments

- Dataset source: Retail transaction data (Black Friday sales)
- Inspired by real-world retail analytics challenges
- Statistical methodologies based on established inference techniques

---

⭐ **If you found this project helpful, please consider giving it a star!** ⭐

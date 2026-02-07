# Case Study: Customer Purchase Behavior Analysis

## Business Context

A major multinational retail corporation operates a chain of supercenters, discount departmental stores, and grocery stores, serving over 100 million customers worldwide. The management team seeks to analyze customer purchase behavior to make data-driven decisions about marketing, inventory, and customer targeting strategies.

## Problem Statement

The Management team wants to analyze customer purchase behavior (specifically, purchase amount) against customer demographics and various other factors to help the business make better decisions. The primary research questions include:

1. **Do spending habits differ between demographic segments?**
2. **Do women spend more on Black Friday than men?**
3. **How do other factors like marital status and age affect spending?**

**Assumption:** The customer base consists of 50 million male customers and 50 million female customers.

## Dataset Description

The company collected transactional data of customers who purchased products during Black Friday sales. 

### Features

| Feature | Description |
|---------|-------------|
| `User_ID` | Unique user identifier |
| `Product_ID` | Unique product identifier |
| `Gender` | Gender of the customer |
| `Age` | Age in bins/groups |
| `Occupation` | Occupation code (masked) |
| `City_Category` | Category of city (A, B, C) |
| `Stay_In_Current_City_Years` | Number of years in current city |
| `Marital_Status` | Marital status (0 = Unmarried, 1 = Married) |
| `Product_Category` | Product category (masked) |
| `Purchase` | Purchase amount in dollars |

## Analysis Requirements

### 1. Data Preparation & Exploration
- Import and explore dataset structure
- Check data types and characteristics
- Detect and handle missing values
- Identify and treat outliers using:
  - Box plots
  - `describe()` method
  - Mean vs median comparison
  - `.isnull()` checks

### 2. Exploratory Data Analysis

#### Non-Graphical Analysis
- Value counts for categorical variables
- Unique attributes identification
- Statistical summaries

#### Visual Analysis

**Univariate Analysis:**
- Distribution plots for continuous variables
- Count plots and histograms
- Category-wise distributions

**Bivariate Analysis:**
- Box plots for categorical vs continuous
- Correlation heatmaps
- Pair plots for relationships

### 3. Statistical Inference Tasks

#### Task 1: Sample Analysis
- Calculate average spending per transaction for male customers
- Calculate average spending per transaction for female customers
- Compare and draw initial inferences

#### Task 2: Confidence Intervals
Using the Central Limit Theorem:
- Use sample statistics to estimate population parameters
- Calculate confidence intervals for population average spending
- Analyze how sample size affects the distribution of sample means
- Experiment with different confidence levels (90%, 95%, 99%)
- Report observations on interval width vs confidence level

#### Task 3: Gender Comparison
- Compare confidence intervals for male and female average spending
- Determine if intervals overlap
- Interpret business implications

#### Task 4: Marital Status Analysis
- Perform same statistical analysis for Married vs Unmarried customers
- Calculate confidence intervals
- Compare spending patterns

#### Task 5: Age Group Analysis
Create age bins based on life stages:
- 0-17 years
- 18-25 years
- 26-35 years
- 36-50 years
- 51+ years

Perform confidence interval analysis for each age group.

### 4. Business Recommendations
- Provide actionable insights based on statistical findings
- Suggest improvements and changes
- Frame recommendations in non-technical language
- Ensure recommendations are practical and implementable

## Evaluation Criteria

### 1. Problem Definition & Basic Analysis (10 points)
- Clear problem statement
- Data shape and structure analysis
- Data type identification and conversion
- Statistical summary interpretation

### 2. Missing Values & Outlier Detection (10 points)
- Systematic detection approach
- Appropriate handling methods
- Documentation of decisions

### 3. Business Insights from Analysis (10 points)
- Range and distribution comments
- Variable relationship analysis
- Meaningful plot interpretations

### 4. Answering Key Questions (50 points)

**Question 1 (10 points):** Are women spending more money per transaction than men? Why or why not?

**Question 2 (10 points):** What do confidence intervals tell us about the distribution of mean expenses by gender?

**Question 3 (10 points):** Do confidence intervals overlap? What are the business implications?

**Question 4 (10 points):** What insights emerge from Married vs Unmarried analysis?

**Question 5 (10 points):** What insights emerge from age group analysis?

### 5. Final Insights (10 points)
- Comprehensive exploration insights
- CLT application and interpretation
- Population-level generalizations
- Variable relationship summaries

### 6. Recommendations (10 points)
- Clear, actionable items
- Business-friendly language
- Practical implementation focus
- No unnecessary technical jargon

## Expected Deliverables

1. **Jupyter Notebook** with complete analysis
2. **Insights Document** with findings and interpretations
3. **Recommendations** for business actions
4. **Visualizations** supporting key findings

## Learning Objectives

By completing this case study, you will:
- Apply Central Limit Theorem to real business problems
- Construct and interpret confidence intervals
- Make statistical inferences about populations from samples
- Translate statistical findings into business recommendations
- Communicate technical results to non-technical stakeholders

## Notes

- There is no single "correct" answer - business decisions involve uncertainty
- Focus on sound statistical reasoning and clear communication
- Support conclusions with appropriate evidence
- Consider practical business constraints in recommendations

---

**Important:** This case study emphasizes statistical thinking and business application over perfect technical execution. The goal is to develop skills in:
- Statistical inference
- Data-driven decision making
- Business communication
- Critical thinking about uncertainty

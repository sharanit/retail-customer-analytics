# Data Directory

## Overview
This directory contains the datasets used in the Customer Purchase Behavior Analysis project.

## Structure

```
data/
├── raw/              # Original, immutable data
└── processed/        # Cleaned and processed data
```

## Dataset Information

### Source
The dataset contains Black Friday sales transactions from a major retail corporation.

### File Format
- **Format:** CSV (Comma-Separated Values)
- **Encoding:** UTF-8
- **Size:** ~550,000 transactions

### Schema

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| User_ID | Integer | Unique customer identifier |
| Product_ID | String | Unique product identifier |
| Gender | String | Customer gender (M/F) |
| Age | String | Age group (bins) |
| Occupation | Integer | Masked occupation code (0-20) |
| City_Category | String | City classification (A/B/C) |
| Stay_In_Current_City_Years | String | Years in current city |
| Marital_Status | Integer | 0 = Unmarried, 1 = Married |
| Product_Category | Integer | Masked product category |
| Purchase | Integer | Purchase amount in dollars |

## Data Acquisition

### Option 1: Kaggle
The dataset can be downloaded from Kaggle (Black Friday dataset):
```bash
# Using Kaggle API
kaggle datasets download -d <dataset-name>
```

### Option 2: Manual Download
1. Visit the data source URL
2. Download the CSV file
3. Place it in the `data/raw/` directory
4. Rename to `walmart_data.csv` (or as referenced in notebooks)

## Usage Notes

### Privacy & Ethics
- All personal identifiers have been masked
- Data is anonymized and aggregated
- Use only for educational and research purposes

### Data Quality
- Check for missing values before analysis
- Handle outliers appropriately
- Validate data types after loading

### Best Practices
- Never modify raw data files
- Keep raw data in `raw/` directory
- Save processed data in `processed/` directory
- Document all data transformations

## Data Not Included

⚠️ **The actual dataset files are not included in this repository due to:**
- File size constraints (GitHub limits)
- Data privacy considerations
- Licensing restrictions

**To run the analysis, you must:**
1. Download the dataset separately (see instructions above)
2. Place it in `data/raw/`
3. Ensure the filename matches the notebook references

## Sample Data

For quick testing, a sample dataset with 1000 rows is available:
```
data/sample_data.csv
```

## Questions?

For data-related questions or issues:
- Check the main README.md
- Review the CASE_STUDY.md for context
- Open an issue on GitHub

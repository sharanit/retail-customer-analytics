"""
Data Preprocessing Utilities
============================
This module contains functions for loading, cleaning, and preprocessing
the retail customer data.
"""

import pandas as pd
import numpy as np


def load_data(filepath):
    """
    Load data from CSV file.
    
    Parameters
    ----------
    filepath : str
        Path to the CSV file
        
    Returns
    -------
    pd.DataFrame
        Loaded dataframe
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None


def check_data_quality(df):
    """
    Perform initial data quality checks.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
        
    Returns
    -------
    dict
        Dictionary containing quality metrics
    """
    quality_report = {
        'shape': df.shape,
        'missing_values': df.isnull().sum(),
        'duplicates': df.duplicated().sum(),
        'dtypes': df.dtypes
    }
    
    return quality_report


def handle_missing_values(df, strategy='drop'):
    """
    Handle missing values in the dataframe.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    strategy : str, default='drop'
        Strategy for handling missing values ('drop', 'fill_mean', 'fill_median')
        
    Returns
    -------
    pd.DataFrame
        Dataframe with missing values handled
    """
    df_clean = df.copy()
    
    if strategy == 'drop':
        df_clean = df_clean.dropna()
    elif strategy == 'fill_mean':
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].mean())
    elif strategy == 'fill_median':
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].median())
    
    print(f"Missing values handled using '{strategy}' strategy")
    return df_clean


def detect_outliers(df, column, method='iqr', threshold=1.5):
    """
    Detect outliers in a numeric column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name to check for outliers
    method : str, default='iqr'
        Method for outlier detection ('iqr' or 'zscore')
    threshold : float, default=1.5
        Threshold multiplier for IQR method
        
    Returns
    -------
    pd.Series
        Boolean series indicating outliers
    """
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        outliers = (df[column] < lower_bound) | (df[column] > upper_bound)
    
    elif method == 'zscore':
        z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
        outliers = z_scores > 3
    
    print(f"Found {outliers.sum()} outliers in '{column}' using {method} method")
    return outliers


def create_age_bins(df, age_column='Age'):
    """
    Create age bins based on life stages.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    age_column : str, default='Age'
        Name of the age column
        
    Returns
    -------
    pd.DataFrame
        Dataframe with age bins added
    """
    df_copy = df.copy()
    
    # Define age bin mapping (adjust based on your data format)
    age_mapping = {
        '0-17': '0-17',
        '18-25': '18-25',
        '26-35': '26-35',
        '36-45': '36-50',
        '46-50': '36-50',
        '51-55': '51+',
        '55+': '51+'
    }
    
    df_copy['Age_Group'] = df_copy[age_column].map(age_mapping)
    
    return df_copy


def convert_categorical(df, columns):
    """
    Convert specified columns to categorical data type.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    columns : list
        List of column names to convert
        
    Returns
    -------
    pd.DataFrame
        Dataframe with converted columns
    """
    df_copy = df.copy()
    
    for col in columns:
        if col in df_copy.columns:
            df_copy[col] = df_copy[col].astype('category')
    
    return df_copy


def get_summary_statistics(df, column):
    """
    Get comprehensive summary statistics for a column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name
        
    Returns
    -------
    dict
        Dictionary of summary statistics
    """
    stats = {
        'count': df[column].count(),
        'mean': df[column].mean(),
        'median': df[column].median(),
        'std': df[column].std(),
        'min': df[column].min(),
        'max': df[column].max(),
        'q1': df[column].quantile(0.25),
        'q3': df[column].quantile(0.75),
        'skewness': df[column].skew(),
        'kurtosis': df[column].kurtosis()
    }
    
    return stats

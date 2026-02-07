"""
Statistical Analysis Utilities
==============================
This module contains functions for statistical inference including
confidence intervals and hypothesis testing.
"""

import numpy as np
import pandas as pd
from scipy import stats


def calculate_confidence_interval(data, confidence=0.95):
    """
    Calculate confidence interval for a dataset.
    
    Parameters
    ----------
    data : array-like
        Sample data
    confidence : float, default=0.95
        Confidence level (0.90, 0.95, 0.99)
        
    Returns
    -------
    tuple
        (mean, lower_bound, upper_bound, margin_of_error)
    """
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    
    # Calculate margin of error
    margin = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)
    
    lower_bound = mean - margin
    upper_bound = mean + margin
    
    return mean, lower_bound, upper_bound, margin


def confidence_interval_comparison(group1, group2, confidence=0.95):
    """
    Compare confidence intervals of two groups.
    
    Parameters
    ----------
    group1 : array-like
        First group data
    group2 : array-like
        Second group data
    confidence : float, default=0.95
        Confidence level
        
    Returns
    -------
    dict
        Dictionary containing CIs for both groups and overlap status
    """
    mean1, lower1, upper1, margin1 = calculate_confidence_interval(group1, confidence)
    mean2, lower2, upper2, margin2 = calculate_confidence_interval(group2, confidence)
    
    # Check for overlap
    overlap = not (upper1 < lower2 or upper2 < lower1)
    
    results = {
        'group1': {
            'mean': mean1,
            'ci_lower': lower1,
            'ci_upper': upper1,
            'margin': margin1
        },
        'group2': {
            'mean': mean2,
            'ci_lower': lower2,
            'ci_upper': upper2,
            'margin': margin2
        },
        'overlap': overlap,
        'difference': mean1 - mean2
    }
    
    return results


def sample_mean_distribution(population, sample_size, num_samples=1000):
    """
    Demonstrate Central Limit Theorem by sampling from population.
    
    Parameters
    ----------
    population : array-like
        Population data
    sample_size : int
        Size of each sample
    num_samples : int, default=1000
        Number of samples to draw
        
    Returns
    -------
    np.ndarray
        Array of sample means
    """
    sample_means = []
    
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=False)
        sample_means.append(np.mean(sample))
    
    return np.array(sample_means)


def t_test_independent(group1, group2, alpha=0.05):
    """
    Perform independent samples t-test.
    
    Parameters
    ----------
    group1 : array-like
        First group data
    group2 : array-like
        Second group data
    alpha : float, default=0.05
        Significance level
        
    Returns
    -------
    dict
        Test results including t-statistic, p-value, and conclusion
    """
    t_stat, p_value = stats.ttest_ind(group1, group2)
    
    results = {
        't_statistic': t_stat,
        'p_value': p_value,
        'alpha': alpha,
        'reject_null': p_value < alpha,
        'significant': 'Yes' if p_value < alpha else 'No'
    }
    
    return results


def bootstrap_confidence_interval(data, num_bootstrap=10000, confidence=0.95, statistic=np.mean):
    """
    Calculate bootstrap confidence interval.
    
    Parameters
    ----------
    data : array-like
        Sample data
    num_bootstrap : int, default=10000
        Number of bootstrap samples
    confidence : float, default=0.95
        Confidence level
    statistic : callable, default=np.mean
        Statistic to calculate
        
    Returns
    -------
    tuple
        (statistic_value, lower_bound, upper_bound)
    """
    bootstrap_stats = []
    
    for _ in range(num_bootstrap):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_stats.append(statistic(sample))
    
    alpha = 1 - confidence
    lower_percentile = (alpha / 2) * 100
    upper_percentile = (1 - alpha / 2) * 100
    
    lower_bound = np.percentile(bootstrap_stats, lower_percentile)
    upper_bound = np.percentile(bootstrap_stats, upper_percentile)
    stat_value = statistic(data)
    
    return stat_value, lower_bound, upper_bound


def effect_size_cohens_d(group1, group2):
    """
    Calculate Cohen's d effect size.
    
    Parameters
    ----------
    group1 : array-like
        First group data
    group2 : array-like
        Second group data
        
    Returns
    -------
    float
        Cohen's d effect size
    """
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    n1, n2 = len(group1), len(group2)
    
    # Pooled standard deviation
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    cohens_d = (mean1 - mean2) / pooled_std
    
    return cohens_d


def calculate_sample_size(margin_of_error, std_dev, confidence=0.95):
    """
    Calculate required sample size for a given margin of error.
    
    Parameters
    ----------
    margin_of_error : float
        Desired margin of error
    std_dev : float
        Population or sample standard deviation
    confidence : float, default=0.95
        Confidence level
        
    Returns
    -------
    int
        Required sample size
    """
    z_score = stats.norm.ppf((1 + confidence) / 2)
    n = (z_score * std_dev / margin_of_error) ** 2
    
    return int(np.ceil(n))


def perform_anova(groups):
    """
    Perform one-way ANOVA test.
    
    Parameters
    ----------
    groups : list of array-like
        List of groups to compare
        
    Returns
    -------
    dict
        ANOVA results
    """
    f_stat, p_value = stats.f_oneway(*groups)
    
    results = {
        'f_statistic': f_stat,
        'p_value': p_value,
        'significant': 'Yes' if p_value < 0.05 else 'No'
    }
    
    return results


def summary_statistics_by_group(df, group_column, value_column):
    """
    Calculate summary statistics for each group.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    group_column : str
        Column to group by
    value_column : str
        Column to calculate statistics for
        
    Returns
    -------
    pd.DataFrame
        Summary statistics by group
    """
    summary = df.groupby(group_column)[value_column].agg([
        ('count', 'count'),
        ('mean', 'mean'),
        ('median', 'median'),
        ('std', 'std'),
        ('min', 'min'),
        ('max', 'max')
    ]).round(2)
    
    return summary

"""
Visualization Utilities
=======================
This module contains functions for creating visualizations for
retail customer analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


def plot_distribution(data, title="Distribution", xlabel="Value", bins=30, color='skyblue'):
    """
    Plot histogram with KDE overlay.
    
    Parameters
    ----------
    data : array-like
        Data to plot
    title : str
        Plot title
    xlabel : str
        X-axis label
    bins : int, default=30
        Number of bins
    color : str, default='skyblue'
        Color for histogram
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.hist(data, bins=bins, color=color, alpha=0.7, edgecolor='black', density=True)
    
    # Add KDE
    from scipy import stats
    kde = stats.gaussian_kde(data)
    x_range = np.linspace(data.min(), data.max(), 100)
    ax.plot(x_range, kde(x_range), color='red', linewidth=2, label='KDE')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.legend()
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_boxplot_by_group(df, group_col, value_col, title="Boxplot by Group"):
    """
    Create boxplot comparing groups.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    group_col : str
        Column for grouping
    value_col : str
        Column for values
    title : str
        Plot title
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.boxplot(data=df, x=group_col, y=value_col, ax=ax, palette='Set2')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(group_col, fontsize=12)
    ax.set_ylabel(value_col, fontsize=12)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_confidence_intervals(groups_data, group_names, confidence=0.95, 
                              title="Confidence Intervals Comparison"):
    """
    Plot confidence intervals for multiple groups.
    
    Parameters
    ----------
    groups_data : list of array-like
        List of data arrays for each group
    group_names : list of str
        Names of groups
    confidence : float, default=0.95
        Confidence level
    title : str
        Plot title
    """
    from src.statistical_analysis import calculate_confidence_interval
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    means = []
    lower_bounds = []
    upper_bounds = []
    
    for data in groups_data:
        mean, lower, upper, _ = calculate_confidence_interval(data, confidence)
        means.append(mean)
        lower_bounds.append(lower)
        upper_bounds.append(upper)
    
    x_pos = np.arange(len(group_names))
    errors = [[m - l for m, l in zip(means, lower_bounds)],
              [u - m for m, u in zip(means, upper_bounds)]]
    
    ax.errorbar(x_pos, means, yerr=errors, fmt='o', markersize=10, 
                capsize=10, capthick=2, linewidth=2, color='steelblue')
    
    ax.set_xticks(x_pos)
    ax.set_xticklabels(group_names)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_ylabel('Mean Value', fontsize=12)
    ax.grid(alpha=0.3)
    
    # Add confidence level to plot
    ax.text(0.02, 0.98, f'{int(confidence*100)}% Confidence Interval', 
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    return fig


def plot_sample_mean_distribution(sample_means, population_mean=None, 
                                  title="Distribution of Sample Means (CLT)"):
    """
    Plot distribution of sample means to demonstrate CLT.
    
    Parameters
    ----------
    sample_means : array-like
        Array of sample means
    population_mean : float, optional
        True population mean for reference
    title : str
        Plot title
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.hist(sample_means, bins=50, color='lightblue', edgecolor='black', 
            alpha=0.7, density=True)
    
    # Add normal curve
    from scipy import stats
    mu, sigma = np.mean(sample_means), np.std(sample_means)
    x = np.linspace(sample_means.min(), sample_means.max(), 100)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, 
            label=f'Normal Distribution\nμ={mu:.2f}, σ={sigma:.2f}')
    
    # Add population mean if provided
    if population_mean is not None:
        ax.axvline(population_mean, color='green', linestyle='--', 
                  linewidth=2, label=f'Population Mean: {population_mean:.2f}')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Sample Mean', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.legend()
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_correlation_heatmap(df, columns=None, title="Correlation Heatmap"):
    """
    Create correlation heatmap.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    columns : list, optional
        Specific columns to include
    title : str
        Plot title
    """
    if columns:
        corr_df = df[columns].corr()
    else:
        corr_df = df.select_dtypes(include=[np.number]).corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sns.heatmap(corr_df, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, ax=ax, square=True, linewidths=1)
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig


def plot_group_comparison(df, group_col, value_col, title="Group Comparison"):
    """
    Create violin plot with overlaid box plot.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    group_col : str
        Column for grouping
    value_col : str
        Column for values
    title : str
        Plot title
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    sns.violinplot(data=df, x=group_col, y=value_col, ax=ax, 
                   palette='muted', inner=None, alpha=0.6)
    sns.boxplot(data=df, x=group_col, y=value_col, ax=ax, 
                width=0.3, palette='dark', linewidth=1.5)
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(group_col, fontsize=12)
    ax.set_ylabel(value_col, fontsize=12)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_multiple_distributions(data_dict, title="Distribution Comparison", bins=30):
    """
    Plot multiple distributions on same axes.
    
    Parameters
    ----------
    data_dict : dict
        Dictionary with {label: data_array}
    title : str
        Plot title
    bins : int, default=30
        Number of bins
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = plt.cm.Set2(np.linspace(0, 1, len(data_dict)))
    
    for (label, data), color in zip(data_dict.items(), colors):
        ax.hist(data, bins=bins, alpha=0.5, label=label, color=color, edgecolor='black')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.legend()
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


def save_figure(fig, filename, output_dir='reports/figures', dpi=300):
    """
    Save figure to file.
    
    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save
    filename : str
        Output filename
    output_dir : str, default='reports/figures'
        Output directory
    dpi : int, default=300
        Resolution
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
    print(f"Figure saved to: {filepath}")

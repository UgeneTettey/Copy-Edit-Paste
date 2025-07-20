"""
This is a histogram generation file/code.
0. 'df' is the dataframe variable
1. Retrieve numerical columns into a list.
2. Create plot using a for-loop, iterating through the list of columns

"""
# libraries needed
import pandas as pd   #for data loading
import seaborn as sns   #for visualization
import matplotlib.pyplot as plt   #for visualization
import math


# df = pd.read_csv('your_dataset.csv')

# List of columns to plot
numerical_columns = df.select_dtypes(include="number").columns.tolist()

# Determine subplot grid size automatically
n_cols = 3  # number of columns in subplot grid
n_rows = math.ceil(len(numerical_columns) / n_cols)

# Create the figure
plt.figure(figsize=(6 * n_cols, 4 * n_rows))

# Iterate through the columns and create subplots
for i, column in enumerate(numerical_columns, 1):
    plt.subplot(n_rows, n_cols, i)                   #specifies the number of subplots to create, and the grid
    sns.histplot(df[column], kde=True, bins = 20)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()




# =============== F U N C T I O N A L    A P P R O A C H ================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

def plot_numerical_histograms(df, bins=20, n_cols=3, figsize_per_plot=(6, 4), kde=True):
    """
    Plots histograms for all numerical columns in a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing numeric columns.
    bins : int, optional (default=20)
        Number of bins for each histogram.
    n_cols : int, optional (default=3)
        Number of columns in the subplot grid.
    figsize_per_plot : tuple, optional (default=(6,4))
        Size of each subplot (width, height).
    kde : bool, optional (default=True)
        Whether to overlay a Kernel Density Estimate (smooth curve).
    """
    
    # Get list of numerical columns
    numerical_columns = df.select_dtypes(include="number").columns.tolist()
    
    if not numerical_columns:
        print("No numerical columns found in the DataFrame.")
        return
    
    # Determine grid size
    n_rows = math.ceil(len(numerical_columns) / n_cols)
    
    # Create figure
    plt.figure(figsize=(figsize_per_plot[0] * n_cols, figsize_per_plot[1] * n_rows))
    
    # Iterate through each column
    for i, column in enumerate(numerical_columns, 1):
        plt.subplot(n_rows, n_cols, i)
        sns.histplot(df[column], kde=kde, bins=bins)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
    
    plt.tight_layout()
    plt.show()

# Example usage:
# df = pd.read_csv('your_dataset.csv')
# plot_numerical_histograms(df, bins=30, n_cols=4, kde=True)

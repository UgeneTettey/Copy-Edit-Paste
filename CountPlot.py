"""
Code snippet for Count PLot with data labels. This can be handy when exploring 
class imbalance during ML prjects.
1. Data is assumed to be loaded as 'df'

"""
# libraries needed
import seaborn as sns
import matplotlib.pyplot as plt
import math

# ================== S I M P L E    A P P R O A C H =========================
"""User can use the code below to plot a simple countplot for a specified categorical feature in the dataframe."""

plt.figure(figsize=(8,6))
ax = sns.countplot(x = 'target', data=df, edgecolor ='black')
plt.title('Count of target: ')
plt.xlabel('target')
plt.yticks([])

# add data labels
ax.bar_label(ax.containers[0], label_type='edge', fontsize = 12)
plt.show()






# =========== F U N C T I O N A L    A P P R O A C H =========================
"""User can use the function below to plot countplots for specified categorical features in the dataframe."""

def plot_countplot(df, columns, n_cols=3, figsize_per_plot=(8,6), fontsize=12, rotation=0):
    """
    Plots countplots for specified categorical columns in the DataFrame as subplots.

    Args:
        df (pd.DataFrame): The dataset containing the columns to plot.
        columns (list): List of categorical column names to plot.
        n_cols (int): Number of columns in the subplot grid.
        figsize_per_plot (tuple): Size of each subplot (width, height).
        fontsize (int): Font size for data labels.
        rotation (int): Angle of x-axis labels.
    """
    cat_feats = len(columns)
    if cat_feats == 0:
        print('No columns specified to plot')
        return

    n_rows = math.ceil(cat_feats / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(figsize_per_plot[0] * n_cols, figsize_per_plot[1] * n_rows))
    axes = axes.flatten() if cat_feats > 1 else [axes]

    for i, column in enumerate(columns):
        ax = axes[i]
        sns.countplot(x=df[column], ax=ax)
        ax.set_title(f"Count of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Count")
        ax.tick_params(axis='x', labelrotation=rotation)
        ax.tick_params(axis='y', left=False, labelleft=False)
        for container in ax.containers:
            ax.bar_label(container, label_type='edge', fontsize=fontsize)

    # Hide unused subplots
    for j in range(i+1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()


# Example usage:
# plot_countplot(df, column='target')
# plot_countplot(df, ['target', 'gender', 'education'], n_cols=2, rotation=45)
# plot_countplot(df, column='gender', rotation=45)




# =========== A L T E R N A T I V E    F U N C T I O N =========================
"""User can use the function below to plot countplots for all categorical features in the dataframe."""

def plot_countplot(df, n_cols = 3, figsize_per_plot=(8,6), fontsize=12, rotation=0):
    """
    Creates a Seaborn countplot with data labels.

    Args:
    -----
    df (pd.DataFrame): The dataset containing the column to plot.
    n_cols (int): Number of columns in the subplot grid.
    figsize_per_plot (tuple): Size of each subplot (width, height).
    fontsize (int): Font size for data labels.
    rotation (int): Angle of x-axis labels (useful for long category names).
    """

    # get list of categorical features
    categorical_features = df.select_dtypes(exclude = 'number').columns.tolist()
    cat_feats = len(categorical_features)

    # condition to check if there are categorical features
    if cat_feats == 0:
        print('No categorical features to plot')
        return
    
    # countplot for categorical features
    n_rows = math.ceil(cat_feats/n_cols)   #grid size for plot
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(figsize_per_plot[0] * n_cols, figsize_per_plot[1] * n_rows))
    axes = axes.flatten() if cat_feats > 1 else [axes]  # Flatten in case of multiple rows/columns


    for i, column in enumerate(categorical_features, 1):
        ax = axes[i-1]
        sns.countplot(x= df[column], ax=ax)
        ax.set_title(f"Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Count")
        ax.tick_params(axis='x', labelrotation=rotation)
        for container in ax.containers:
            ax.bar_label(container, label_type='edge', fontsize=fontsize)
    
    # hide unused subplots
    for j in range(i, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()

# usage example
# plot_countplot(df)
# plot_countplot(df_1, n_cols=3, figsize_per_plot=(8,6), fontsize=12, rotation=45)

"""
Code snippet for Count PLot with data labels. This can be handy when exploring 
class imbalance during ML prjects.
1. Data is assumed to be loaded as 'df'

"""
# libraries needed
import seaborn as sns
import matplotlib.pyplot as plt


# countplot

plt.figure(figsize=(8,6))
ax = sns.countplot(x = 'target', data=df, edgecolor ='black')
plt.title('Count of target: ')
plt.xlabel('target')
plt.yticks([])

# add data labels
ax.bar_label(ax.containers[0], label_type='edge', fontsize = 12)
plt.show()






# =========== F U N C T I O N A L    A P P R O A C H =========================
import seaborn as sns
import matplotlib.pyplot as plt
import math

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

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

def labeled_countplot(df, column, title=None, figsize=(8,6), fontsize=12, rotation=0):
    """
    Creates a Seaborn countplot with data labels.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing the column to plot.
    column : str
        The name of the column to visualize (categorical or discrete).
    title : str, optional
        Title for the plot. Defaults to 'Count of <column>'.
    figsize : tuple, optional
        Size of the figure (width, height).
    fontsize : int, optional
        Font size for data labels.
    rotation : int, optional
        Angle of x-axis labels (useful for long category names).
    """
    
    plt.figure(figsize=figsize)
    ax = sns.countplot(x=column, data=df, edgecolor='black', order=df[column].value_counts().index)

    # Title
    if not title:
        title = f"Count of {column}"
    plt.title(title, fontsize=14)
    
    # Remove y-axis ticks (optional for cleaner look)
    plt.yticks([])

    # Rotate x-axis labels if needed
    plt.xticks(rotation=rotation)
    
    # Add data labels above bars
    ax.bar_label(ax.containers[0], label_type='edge', fontsize=fontsize)

    plt.xlabel(column)
    plt.ylabel('')  # remove redundant axis label
    plt.tight_layout()
    plt.show()

# Example usage:
# labeled_countplot(df, column='target')
# labeled_countplot(df, column='gender', rotation=45)

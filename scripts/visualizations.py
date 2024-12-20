import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(data, column, plot_type="hist", title="", xlabel="", ylabel="", manufacturer="Unknown"):
    """
    Perform univariate analysis using histograms or boxplots.

    Parameters:
    - data: DataFrame containing the dataset.
    - column: The column to analyze.
    - plot_type: Type of plot ("hist" for histogram or "box" for boxplot).
    - title: Title of the plot.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - manufacturer: Name of the manufacturer or product for additional context.
    """
    plt.figure(figsize=(10, 6))
    if plot_type == "hist":
        sns.histplot(data[column], bins=20, kde=True, color='blue')
    elif plot_type == "box":
        sns.boxplot(data[column], color='green')

    plt.title(f"{title} - {manufacturer}")
    plt.xlabel(f"{xlabel} ({manufacturer})")
    plt.ylabel(f"{ylabel} ({manufacturer})")
    plt.show()

def bivariate_analysis(data, x, y, kind="scatter", title="", xlabel="", ylabel="", hue=None, manufacturer="Unknown"):
    """
    Perform bivariate analysis using scatterplots or heatmaps.

    Parameters:
    - data: DataFrame containing the dataset.
    - x, y: The columns to analyze (x-axis and y-axis).
    - kind: Type of plot ("scatter" for scatter plot or "heatmap" for correlation heatmap).
    - title: Title of the plot.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - hue: Optional categorical variable for coloring the scatter plot.
    - manufacturer: Name of the manufacturer or product for additional context.
    """
    plt.figure(figsize=(10, 6))
    if kind == "scatter":
        sns.scatterplot(data=data, x=x, y=y, hue=hue, palette='deep')
    elif kind == "heatmap":
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")

    plt.title(f"{title} - {manufacturer}")
    plt.xlabel(f"{xlabel} ({manufacturer})")
    plt.ylabel(f"{ylabel} ({manufacturer})")
    if hue:
        plt.legend(title=hue)
    plt.show()

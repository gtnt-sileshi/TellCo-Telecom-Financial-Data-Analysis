import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(data, column, plot_type="hist", title="", xlabel="", ylabel=""):
    """
    Perform univariate analysis using histograms or boxplots.
    """
    plt.figure(figsize=(10, 6))
    if plot_type == "hist":
        sns.histplot(data[column], bins=20, kde=True, color='blue')
    elif plot_type == "box":
        sns.boxplot(data[column], color='green')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def bivariate_analysis(data, x, y, kind="scatter", title="", xlabel="", ylabel="", hue=None):
    """
    Perform bivariate analysis using scatterplots or heatmaps.
    """
    plt.figure(figsize=(10, 6))
    if kind == "scatter":
        sns.scatterplot(data=data, x=x, y=y, hue=hue, palette='deep')
    elif kind == "heatmap":
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if hue:
        plt.legend(title=hue)
    plt.show()

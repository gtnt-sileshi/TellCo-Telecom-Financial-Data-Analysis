import pandas as pd

def save_to_csv(data, filepath):
    """
    Save a pandas DataFrame to a CSV file.
    """
    data.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

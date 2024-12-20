import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from scripts.database import query_data

def get_engagement_metrics(engine):
    """
    Query user engagement metrics: session frequency, total duration, and total traffic.
    """
    query = """
    SELECT "MSISDN/Number" AS msisdn,
           COUNT("Bearer Id") AS session_frequency,
           SUM("Dur. (ms)") AS total_duration,
           SUM("Total DL (Bytes)" + "Total UL (Bytes)") AS total_traffic
    FROM public.xdr_data
    GROUP BY "MSISDN/Number";
    """
    return query_data(engine, query)


def normalize_metrics(data, columns):
    """
    Normalize specified columns in the DataFrame using MinMaxScaler.
    
    Parameters:
    - data: DataFrame containing the dataset.
    - columns: List of columns to normalize.
    
    Returns:
    - data: DataFrame with normalized columns added or None if there's an error.
    """
    try:
        if data is None:
            print("Data is None. Cannot normalize.")
            return None

        # Check if all the columns exist in the data
        missing_columns = [col for col in columns if col not in data.columns]
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return None  # If any column is missing, return None

        scaler = MinMaxScaler()
        normalized_data = scaler.fit_transform(data[columns])
        # Add the normalized columns to the original dataframe
        for i, col in enumerate(columns):
            data[f"{col}_norm"] = normalized_data[:, i]
        
        return data
    except Exception as e:
        print(f"Error in normalization: {e}")
        return None


def cluster_users(data, columns, n_clusters=3):
    """
    Perform K-means clustering on specified columns and assign cluster labels.
    
    Parameters:
    - data: DataFrame containing the dataset.
    - columns: List of columns to use for clustering.
    - n_clusters: Number of clusters for KMeans.
    
    Returns:
    - data: DataFrame with added 'engagement_cluster' column.
    - kmeans: Fitted KMeans model.
    """
    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        data['engagement_cluster'] = kmeans.fit_predict(data[columns])
        return data, kmeans
    except Exception as e:
        print(f"Error in clustering: {e}")
        return None


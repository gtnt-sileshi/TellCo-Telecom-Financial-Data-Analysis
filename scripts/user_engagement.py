from database import query_data
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

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
    Normalize specified columns in the DataFrame.
    """
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data[columns])
    data[[f"{col}_norm" for col in columns]] = normalized_data
    return data

def cluster_users(data, columns, n_clusters=3):
    """
    Perform K-means clustering on specified columns and assign cluster labels.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    data['engagement_cluster'] = kmeans.fit_predict(data[columns])
    return data, kmeans

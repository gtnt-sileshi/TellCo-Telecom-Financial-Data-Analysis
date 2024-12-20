from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

def connect_to_db():
    """
    Connect to a PostgreSQL database using credentials from the .env file and return an engine.
    """
    try:
        # Retrieve database credentials from environment variables
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")

        # Create database engine
        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
        print("Database connection successful!")
        return engine
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def query_data(engine, query):
    """
    Execute a SQL query using the provided engine and return the results as a pandas DataFrame.
    """
    try:
        df = pd.read_sql(query, engine)
        print("Query executed successfully!")
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

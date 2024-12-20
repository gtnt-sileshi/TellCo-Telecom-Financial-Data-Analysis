from database import query_data

def analyze_top_handsets(engine):
    """
    Query the top 10 handsets used by customers.
    """
    query = """
    SELECT "Handset Type", COUNT(*) AS count
    FROM public.xdr_data
    GROUP BY "Handset Type"
    ORDER BY count DESC
    LIMIT 10;
    """
    return query_data(engine, query)

def analyze_top_manufacturers(engine):
    """
    Query the top handset manufacturers and their most used handsets.
    """
    query = """
    SELECT "Handset Manufacturer", "Handset Type", COUNT(*) AS count
    FROM public.xdr_data
    GROUP BY "Handset Manufacturer", "Handset Type"
    ORDER BY "Handset Manufacturer", count DESC
    LIMIT 15;
    """
    return query_data(engine, query)

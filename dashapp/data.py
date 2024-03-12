import pandas as pd
from sqlalchemy import create_engine

def fetch_data(product_ids=['Product1', 'Product2', 'Product3']):
    engine = create_engine('sqlite:///path/to/data/projet.db')
    query = f"""
    SELECT 
    FROM 
    WHERE 
    ORDER 
    """
    #df = pd.read_sql_query()
    #return df

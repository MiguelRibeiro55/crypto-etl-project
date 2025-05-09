from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

def load_to_postgres(df, table_name='crypto_prices'):
    try:
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        db = os.getenv('DB_NAME')

        db_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
        engine = create_engine(db_url)

        df.drop_duplicates(subset=['id', 'etl_timestamp'], inplace=True)
        df.to_sql(table_name, engine, if_exists='append', index=False)

        logging.info(f"✅ Loaded {len(df)} rows into '{table_name}'")
    except Exception as e:
        logging.error(f"❌ Failed to load data: {e}")

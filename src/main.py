from extract import fetch_crypto_data
from transform import transform_data
from load import load_to_postgres


def run_etl():
    data = fetch_crypto_data()
    df = transform_data(data)
    load_to_postgres(df)
    
if __name__ == '__main__':
    run_etl()
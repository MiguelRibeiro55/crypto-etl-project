import pandas as pd
from datetime import datetime,timezone


def transform_data(data):
    df = pd.json_normalize(data)
    selected_columns = [
        'id','symbol','name','current_price','market_cap','total_volume','last_updated' 
    ]
    
    df = df[selected_columns]
    
    df['etl_timestamp'] = datetime.now(timezone.utc)
    
    return df
    
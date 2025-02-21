import pandas as pd

def preprocess_shantou_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def preprocess_zhelang_data(df):
    df.columns = ['station', 'day', 'hour', 'latitude', 'longitude', 'temperature', 'humidity', 'pressure', 'wind_direction', 'wind_speed']
    return df
import numpy as np

def split_data(df, test_size=0.2):
    train_size = int(len(df) * (1 - test_size))
    train, test = df[:train_size], df[train_size:]
    return train, test
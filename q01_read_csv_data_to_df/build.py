# %load q01_read_csv_data_to_df/build.py
# Default Imports
import pandas as pd

def read_csv_data_to_df(df):
    
# Path has been given to you already to use in function.
    path = 'data/ipl_dataset.csv'
    df = pd.read_csv(path)
    return df
# Solution






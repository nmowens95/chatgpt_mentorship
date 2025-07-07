import pandas as pd

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]
    return df

def drop_null_rows(df, threshold=0.5):
    return df.dropna(thresh=int(threshold * len(df.columns)))

def transform_file(df):
    df_cleaned = df.copy()
    df_cleaned = clean_column_names(df_cleaned)
    df_cleaned = drop_null_rows(df_cleaned)
    return df_cleaned
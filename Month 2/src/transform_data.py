import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype, is_datetime64_any_dtype
from datatools import clean_names, clean_currency, parse_dates

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]
    return df

def drop_null_rows(df, threshold=0.5):
    return df.dropna(thresh=int(threshold * len(df.columns)))

def apply_cleaning_values(col):
    if is_numeric_dtype(col):
        return clean_currency
    if is_string_dtype(col):
        return clean_names
    if is_datetime64_any_dtype(col):
        return parse_dates
    
def transform_file(df):
    df_cleaned = df.copy()
    df_cleaned = clean_column_names(df_cleaned)
    df_cleaned = drop_null_rows(df_cleaned)

    # Value cleaning
    for col in df_cleaned.columns:
        cleaner = apply_cleaning_values(df_cleaned[col])

        if cleaner:
            df[col] = cleaner(df_cleaned[col])
    
    return df_cleaned
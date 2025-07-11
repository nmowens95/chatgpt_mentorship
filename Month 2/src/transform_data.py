import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype, is_datetime64_any_dtype
from .datatools.transform_utils import clean_names, clean_currency, parse_dates
from .logger_config import logger_setup

logger = logger_setup()

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]
    return df

def drop_null_rows(df, threshold=0.5):
    return df.dropna(thresh=int(threshold * len(df.columns)))

# def apply_cleaning_values(col):
#     if is_numeric_dtype(col):
#         return clean_currency
#     if is_string_dtype(col):
#         return clean_names
#     if is_datetime64_any_dtype(col):
#         return parse_dates


TRANSFORM_REGISTRY = {
    "currency": clean_currency,
    "date": parse_dates,
    "name": clean_names
}
    
def transform_file(df, schema):
    df_cleaned = df.copy()
    df_cleaned = clean_column_names(df_cleaned)
    df_cleaned = drop_null_rows(df_cleaned)

    for col, rule in schema.items():
        if col in df_cleaned.columns and rule in TRANSFORM_REGISTRY:
            df_cleaned[col] = TRANSFORM_REGISTRY[rule](df_cleaned[col])
        else:
            logger.warning(f"Skipping transformation for column: {col} with rule: {rule}")            

    # Value cleaning
    # for col in df_cleaned.columns:
    #     cleaner = apply_cleaning_values(df_cleaned[col])

    #     if cleaner:
    #         df_cleaned[col] = cleaner(df_cleaned[col])
    
    return df_cleaned
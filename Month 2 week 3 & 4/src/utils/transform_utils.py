import pandas as pd
from pathlib import Path

def parse_dates(col: pd.Series) -> pd.Series:
    return pd.to_datetime(col, errors="coerce")

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def upper_str(col: pd.Series) -> pd.Series:
    return col.str.upper().str.strip()

def lower_str(col: pd.Series) -> pd.Series:
    return col.str.lower().str.strip()

def title_str(col: pd.Series) -> pd.Series:
    return col.str.title().str.strip()

def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    df["status"] = title_str(df["status"])
    df["date_of_birth"] = parse_dates(df["date_of_birth"])
    df["signup_date"] = parse_dates(df["signup_date"])
    df["is_active"] = title_str(df["is_active"])
    df["preferred_contact_method"] = title_str(df["preferred_contact_method"])
    return df

def transform_claims(df: pd.DataFrame) -> pd.DataFrame:
    df["currency"] = upper_str(df["currency"])
    df["full_name"] = title_str(df["full_name"])
    df["service_type"] = title_str(df["service_type"])
    df["claim_description"] = df["claim_description"].str.strip()
    df["follow_up_required"] = title_str(df["follow_up_required"])
    return df
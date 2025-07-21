import pandas as pd

def clean_currency(col: pd.Series) -> pd.Series:
    return col.astype(str).str.strip().str.replace("$","").str.replace(",","").astype(float).round(2)

def parse_dates(col: pd.Series) -> pd.Series:
    return col.apply(lambda x: pd.to_datetime(x, errors="coerce"))

def clean_names(col: pd.Series) -> pd.Series:
    return col.str.title().str.strip().str.replace(r"s\+", " ", regex=True)
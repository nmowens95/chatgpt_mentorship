import pandas as pd
import logging

logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d  %H:%M",
    level=logging.INFO
)

logger = logging.getLogger()

def include_dtype_fx(col: pd.Series) -> dict:
    col_dtype = str(col.dtypes)
    return {"dtype": col_dtype}

def include_null_fx(col: pd.Series) -> dict:
    col_isna = round(100 * (col.isna().sum() / len(col)), 1)
    return {"isna": col_isna}

def include_mode_fx(column: pd.Series) -> dict:
    col_mode = column.mode()
    return {"mode": col_mode.to_list()}

def summarize_df(df, include_dtype=True, include_null=True, include_mode=True):
    """
    Summarize a pandas DataFrame by generating stats per column.

    Parameters:
        df (pd.DataFrame): The DataFrame to summarize.
        include_dtype (bool): Include data type of columns.
        include_null (bool): Include percentage of null values.
        include_mode (bool): Include mode (most frequent values) of columns.

    Returns:
        dict: Summary dictionary with column statistics.
    """
    if not isinstance(df, pd.DataFrame):
        logger.info("The data frame trying to be passed is not matching an actual df type")
        raise TypeError("Value passed is not a dataframe type")
    
    if df.empty:
        logger.info("Value being passed has no values")
        raise ValueError("Empty DataFrame pass")

    # Dyncamically collect necessary functions
    features = []
    if include_dtype:
        features.append(include_dtype_fx)      

    if include_null:
        features.append(include_null_fx)

    if include_mode:
        features.append(include_mode_fx) 
    
    summary = {"columns": []}
    for column in df.columns:
        if df[column].isnull().all():
            logger.info(f"Skipping {column} due to being completely empty")
            continue

        column_summary = {"name": df[column].name}

        for func in features:
            column_summary.update(func(df[column]))
    
        summary["columns"].append(column_summary)

    return summary

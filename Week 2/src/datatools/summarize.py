import pandas as pd
import logging

logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d  %H:%M",
    level=logging.INFO
)

logger = logging.getLogger()

def summarize_df(df, include_dtype=True, include_null=True, include_mode=True):
    if not isinstance(df, pd.DataFrame):
        logger.info("The data frame trying to be passed is not matching an actual df type")
        raise TypeError("Value passed is not a dataframe type")
    
    if df.empty:
        logger.info("Value being passed has no values")
        raise ValueError("Empty DataFrame pass")          
        
    
    summary = {"columns": []}
    for column in df.columns:
        if df[column].isnull().all():
            logger.info(f"Skipping {column} due to being completely empty")
            continue

        column_summary = {"name": df[column].name}

        if include_dtype:
            column_summary["dtype"] = str(df[column].dtypes) # Convert to a string

        if include_null:
            column_summary["isna"] = round(100 * (df[column].isna().sum() / len(df)), 1)

        if include_mode:
            col_mode = df[column].mode()
            column_summary["mode"] = col_mode.to_list()

        summary["columns"].append(column_summary)

    return summary

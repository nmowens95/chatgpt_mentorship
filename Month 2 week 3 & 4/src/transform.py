import pandas as pd
from utils.transform_utils import clean_column_names, transform_customers, transform_claims
from utils.metadata_logger import metadata_writer, transform_metadata

TRANSFORM_REGISTRY = {
    "claims": transform_claims,
    "customers": transform_customers
}

def clean_file(df: pd.DataFrame, filename) -> pd.DataFrame:
    df_clean = clean_column_names(df)

    if filename in TRANSFORM_REGISTRY:
        df_clean = TRANSFORM_REGISTRY[filename](df_clean)

    metadata = transform_metadata(df, filename)
    metadata_writer(metadata, process="transform")

    return df_clean

def clean_and_loop_files(dfs: dict) -> dict:
    transformed_dfs = {}

    for file_name, df in dfs.items():
        df_transformed = clean_file(df, file_name)
        transformed_dfs[file_name] = df_transformed

        return transformed_dfs

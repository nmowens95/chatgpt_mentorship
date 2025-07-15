from src import logger_setup
from src import extract_file
from src import transform_file
from src import SCHEMA_REGISTRY
from src import load_files

logger = logger_setup()
dir_path = "data/raw"

def main(dir_path):
    dfs = extract_file(dir_path)

    for df, file_base_name, file_full_name in dfs:
        schema = SCHEMA_REGISTRY.get(file_base_name)

        if schema:
            df_transformed = transform_file(df, schema)
        else:
            logger.warning(f"No Schema found for {file_base_name}, skipping transformation")
            df_transformed = df
        
        load_files(df_transformed, file_full_name)

        print(f"Preview of {file_base_name}")
        print(df_transformed.head())
    logger.info("Pipeline finished running")


if __name__ == "__main__":
    main(dir_path)
    
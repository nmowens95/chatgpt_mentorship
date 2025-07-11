from src import logger_setup
from src import extract_file
from src import transform_file
from src import SCHEMA_REGISTRY

logger = logger_setup()
dir_path = "data/raw"

def main(dir_path):
    dfs = extract_file(dir_path)

    for df, file in dfs:
        schema = SCHEMA_REGISTRY.get(file)

        if schema:
            df_transformed = transform_file(df, schema)
        else:
            logger.warning(f"No Schema found for {file}, skipping transformation")
            df_transformed = df

        print(f"Preview of {file}")
        print(df_transformed.head())
    logger.info("Pipeline finished running")


if __name__ == "__main__":
    main(dir_path)
    
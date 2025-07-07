from src import logger_setup
from src import extract_file
from src import transform_file

logger = logger_setup()
dir_path = "data/raw"

def main(dir_path):
    dfs = extract_file(dir_path)

    for df, file in dfs:
        df_transformed = transform_file(df)
        print(f"Preview of {file}")
        print(df_transformed.head())
    logger.info("Pipeline finished running")


if __name__ == "__main__":
    main(dir_path)
    
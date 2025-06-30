import os
import pandas as pd
import argparse
import logging

# Create argparse and arguments
parser = argparse.ArgumentParser(description="Arguments to add optionally for summary")
parser.add_argument(
    "--features",
    help="Call if want data type or null in summary, arguments seperated by ',' and no space",
    type=str
)
args = parser.parse_args()

# Create a logger
logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO
)

logger = logging.getLogger()

# Create a custom raise exception
class FileDoesNotExist(Exception):
    "Raised incase there is no file in the path and it does not exist"
    pass

# Feature registry and summary functions
def summarize_null(df):
    return {col: df[col].isna().sum() for col in df}

def summarize_dtype(df):
    return {col: df[col].dtype for col in df}

FEATURE_REGISTRY = {
    "null": summarize_null,
    "dtype": summarize_dtype
}

# Primary file to summarize, or test fake
file_path = "customers.csv"
file_path_fake = "test_fake.csv"


# Main function
def summarize_df(file, features_list=None):
    try:
        if not os.path.exists(file):
            raise FileDoesNotExist(f"The file {file} doesn't exist")
        
        df = pd.read_csv(file)
        logger.info(f"Successfully loaded file: {file}")
        print(f"Summarizing file: {file}\n")

        for feature in features_list:
            if feature in FEATURE_REGISTRY:
                result = FEATURE_REGISTRY[feature](df)

                for col, value in result.items():
                    print(f"----- Summary for column: {col} -----")
                    print(f"{feature}: {value}")
            else:
                logger.warning(f"Feature '{feature}' is not recognized")

        print("\n----- End of summary -----\n")
    except Exception as e:
        print(f"Error: {e}")
    else:
        logger.info(f"Successfully summarized {file}")


# features
features_list = args.features.split(",") if args.features else []

summarize_df(file_path, features_list)
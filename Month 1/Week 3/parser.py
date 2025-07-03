import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Arguments to summarize csv files")
    parser.add_argument(
        "dir_path",
        type=str,
        help="Path for files to iterate over"
    )
    parser.add_argument(
        "--features",
        type=str,
        help="Comma seperated values for features: dtype,null,mode"
    )
    return parser.parse_args()
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
        type=lambda s: s.split(","),
        default=["null", "dtype", "mode"],
        help="Comma seperated values for features: dtype,null,mode"
    )
    parser.add_argument(
        "--writer",
        type=str,
        default="txt",
        choices=["txt", "json"],
        help="Writer to distinguish how output summary is writter (json or txt)"
    )
    return parser.parse_args()
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Pipeline arguments")
    parser.add_argument(
        "dir_path",
        type=str,
        help="Path to a csv file"
        )
    # parser.add_argument(
    #     "schema",
    #     type=str,
    #     required=True,
    #     help="Path to a schema"
    #    )
    
    return parser.parse_args()
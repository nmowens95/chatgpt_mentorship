import os
import argparse
from src.datatools import iterate_files, summarize_df, save_df



if __name__ == "__main__":
    # Inititate arguments to call - dir_path
    parser = argparse.ArgumentParser(description="Loop over .csv files and provides information")
    parser.add_argument(
        "dir_path", 
        type=str,
        help="Directory folder to loop over csv's"
        )
    parser.add_argument(
        "-s",
        "--save-summary",
        action="store_true",
        help="Saves summary of columns to a txt file"
        )
    parser.add_argument(
        "--include-null",
        action="store_true",
        help="Adds null summary if you want in summarize function"
    )
    parser.add_argument(
        "--include-mode",
        action="store_true",
        help="Includes mode if you want in summarize function"
    )
    parser.add_argument(
        "--include-dtype",
        action="store_true",
        help="Include dtype in summarize function"
    )
    
    args = parser.parse_args()

    # dir_path = "./helper_files/"
    # save_summary = "./output/" or None

    # Returns a list of pairs
    results = iterate_files(args.dir_path)

    for df, filetype, filename in results:
        summary = summarize_df(df, args.include_dtype, args.include_null, args.include_mode)

        if args.save_summary:
            # Create a unique output path
            basename = os.path.splitext(filename)[0]
            ext = "json" if filetype ==  "json" else "txt"
            save_path = f"./output/{basename}_summary.{ext}"
            
            save_df(filetype, summary, save_path)
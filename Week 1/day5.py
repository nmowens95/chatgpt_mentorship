import os
import pandas as pd
import argparse
import logging
import json

logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO,
)

logger = logging.getLogger()

def iterate_files(dir_path):
    results = []

    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)           

        try:
            if file.lower().endswith(".csv"):
                logging.info(f"csv file")
                df = pd.read_csv(full_path)
                filetype = "csv"
                logger.info(f"File - {file} read successfully!")
    
        
            elif file.lower().endswith(".ndjson") or file.lower().endswith(".json"):
                logging.info(f"json file")
                df = pd.read_json(full_path, lines=True)
                filetype = "json"
                logger.info(f"File - {file} read successfully!")
            
            else:
                None
            
            results.append([df, filetype, file])
        
        except Exception as e:
            logger.debug(f"Couldn't read file: {e}")

    return results


def summarize_df(df):
    summary = {"columns": []}
    for column in df.columns:
        column_name = df[column].name
        column_dtype = str(df[column].dtypes) # Convert to a string
        column_isna = round(100 * (df[column].isna().sum() / len(df)), 1)
        column_mode = df[column].mode()
        most_frequent = column_mode.iloc[0] if len(column_mode) > 0 else "N/A"

        column_summary = {
            "name": column_name,
            "dtype": column_dtype,
            "isna": column_isna,
            "mode": column_mode.to_list(),
            "most_frequent": most_frequent
        }

        summary["columns"].append(column_summary)

    return summary

def save_df(filetype, summary, save):
    if save:
        dir_path = os.path.dirname(save)
        if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
        
        if filetype == "json":
        # Write to file
            logger.info(f"Writing summary to {save}")
            with open(save, "a") as f:
                json.dump(summary, f)

        else:
            logger.info(f"Writing summary to {save}")
            with open(save, "a") as f:
                for col in summary["column"]:
                    f.write(f"Column name: {col['name']}\n")
                    f.write(f"Column dtype: {col['dtype']}\n")
                    f.write(f"Percent missing: {col['isna']}\n")
                    f.write(f"Column mode: {col['mode']}\n")
                    f.write(f"Column most frequent: {col['most_frequent']}\n")

                    f.write("---------------------------------------------\n")
    else:
        logger.INFO("File successfully summarized")  


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
    
    args = parser.parse_args()

    # dir_path = "./helper_files/"
    # save_summary = "./output/" or None

    # Returns a list of pairs
    results = iterate_files(args.dir_path)

    for df, filetype, filename in results:
        summary = summarize_df(df)

        if args.save_summary:
            # Create a unique output path
            basename = os.path.splitext(filename)[0]
            ext = "json" if filetype ==  "json" else "txt"
            save_path = f"./output/{basename}_summary.{ext}"
            
            save_df(filetype, summary, save_path)
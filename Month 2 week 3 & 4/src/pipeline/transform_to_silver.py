from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.utils.extract_files import extract_csv_files
from src.utils.transform_utils import clean_and_loop_files
from src.utils.file_writer import write_files_to_new_layer

def bronze_to_silver(file_dir) -> Path: # Create a args directory
    '''
    Arguments:
    -  file_dir: is a path to the bronze csv files
    Output: a path to where the bronze layer will be loaded

    - Extract using extract_csv_files, which loops over a directory, reads each csv file,
    writes the extracted metadata and stores all the dataframes to a dictionary "file_name": df
    - Transform using clean_and_loop_files, this will also return a dictionary of "file_name": df
    - Load to the data/silver path
    '''

    # Extract
    file_names_and_dfs = extract_csv_files(file_dir)

    # Transform
    transformed_file_names_and_dfs = clean_and_loop_files(file_names_and_dfs)

    # Load
    silver_output = write_files_to_new_layer(transformed_file_names_and_dfs, output_dir="data/silver", layer="silver")

    return silver_output

if __name__ == "__main__":
    result = bronze_to_silver(file_dir="data/bronze")
    print(bronze_to_silver)
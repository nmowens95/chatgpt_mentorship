'''
Goal:
Write a script that:

1. Takes a folder path as input (hardcoded or sys.argv)
2. Lists all .csv and .json files
3. For each file, prints:
- File name
- File size in KB
- File type (CSV or JSON)
- Number of rows (for CSVs using pandas, for JSON count top-level items)
4. Outputs a summary report: total files, total rows, total size

Constraints:
- Use only os, pandas, json, and sys
- No AI, no Google. Only docs if needed.
- Aim to finish in 45-90 minutes
'''

import os
import sys
import pandas as pd
import json

# Initialize argument for paht where files exist
args = sys.argv
dir_path = args[1]

# Initialize variables for total summary
total_files = 0
total_rows = 0
total_size = 0

for file in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file) # DRY principle: use os.path.join for file paths

    if file.endswith(".csv"): # Use endswith instead of slicing for better readability
        try: # add try-except to handle potential read errors
            df = pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading {file}: {e}")

        csv_len = len(df)
        size = os.path.getsize(file_path)

        print(file)
        print(size)
        print("CSV")
        print(csv_len)
        
        total_files += 1
        total_rows += csv_len
        total_size += size

    elif file.endswith(".json"): # Use endswith instead of slicing for better readability
        with open(file_path, 'r') as f:
            data = json.load(f)
            # Count top-level items in JSON, need to handle both list and dict types
            if isinstance(data, list):
                json_len = len(data)
            elif isinstance(data, dict):
                json_len = len(data.keys())
            else:
                json_len = 1

        size = os.path.getsize(file_path)

        print(file)
        print(size)
        print("JSON")
        print(json_len)

        total_files += 1
        total_rows += json_len
        total_size += size

    else:
        print(f"File {file} is not a CSV or JSON file.")

    # Print summary report
print("\nSummary Report:")
print(f"Total files: {total_files}")
print(f"Total rows: {total_rows}")
print(f"Total size: {total_size/1024:.2f} KB") # Convert size to KB
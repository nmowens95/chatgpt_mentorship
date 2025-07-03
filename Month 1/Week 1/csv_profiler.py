import os
import sys
import pandas as pd

'''
Goal:
Write a script that:

1. Takes a folder path as input (hardcoded or sys.argv)
2. Iterates over .csv files
3. For each file, prints:
- File name
- Number of rows & Columns
- For each column:
    - Data type
    - % Missing
    - Most frequent value (mode)
'''

args = sys.argv
dir_path = args[1]

for file in os.listdir(dir_path):
    full_path = os.path.join(dir_path, file)

    try:
        # Have it so if the file doesnt end with csv it will pass over
        if not file.lower().endswith(".csv"):
            continue

        df = pd.read_csv(full_path)
        rows = len(df)
        columns = len(df.columns)

        print(f"File name: {file}")
        print(f"Number of Rows: {rows} & Columns: {columns}\n")

        for column in df.columns:
            column_name = df[column].name
            column_dtype = df[column].dtypes
            column_isna = round(100 * (df[column].isna().sum() / len(df)), 1) # Total missing in column / total rows
            column_mode = df[column].mode()
            most_frequent = column_mode.iloc[0] if not column_mode.empty else "N/A"

            print(f"Column name: {column_name}")
            print(f"Column dtype: {column_dtype}")
            print(f"Percent missing: {column_isna}")
            print(f"Column mode: {most_frequent}\n")

        print(f"---------------------------------------------\n")
        
    except Exception as e:
        print(f"Error with file: {file}, exception: {e}")

    
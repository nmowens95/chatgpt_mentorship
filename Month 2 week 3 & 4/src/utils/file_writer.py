from pathlib import Path
import pandas as pd

def write_files_to_new_layer(files_and_dataframes: dict, output_dir, layer=None) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_name, df in files_and_dataframes.items():
        output_path = df.to_csv(output_dir/f"{file_name}_{layer}.csv", index=False)

    return output_path
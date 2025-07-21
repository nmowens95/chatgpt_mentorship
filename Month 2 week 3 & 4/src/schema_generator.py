import pandas as pd
from pathlib import Path
import yaml
from pandas.api.types import is_integer_dtype, is_float_dtype, is_string_dtype, is_datetime64_any_dtype

def normalize_dtypes(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "int"
    elif pd.api.types.is_float_dtype(dtype):
        return "float"
    elif pd.api.types.is_string_dtype(dtype):
        return "string"
    elif pd.api.types.is_bool_dtype(dtype):
        return "boolean"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "datetime"
    else:
        raise ValueError(f"Unknown datatype: {dtype}")

def schema_generator(csv_file: str, output_dir="schema") -> Path:
    df = pd.read_csv(csv_file, nrows=20, parse_dates=["Date of Birth", "Signup Date"]) # sample for inference

    # Auto generate schema
    columns = []
    for col_name, col_type in df.dtypes.items():
        col_schema = {
            "name": col_name,
            "dtype": normalize_dtypes(col_type),
            "nullable": bool(df[col_name].isnull().any())
        }
        columns.append(col_schema)

    schema = {
        "file": csv_file.name,
        "columns": columns
    }

    # Create a dir
    base_schema_dir = Path(output_dir)
    base_schema_dir.mkdir(parents=True, exist_ok=True)

    # Where to drop schema
    schema_output = Path(output_dir) / f"{csv_file.stem}{'.yaml'}"

    with open(schema_output, "w") as f:
        yaml.dump(schema, f, sort_keys=False)

    return schema_output

csv_path = Path("data/bronze") / f"customers.csv"

schema = schema_generator(csv_path)

print(schema)
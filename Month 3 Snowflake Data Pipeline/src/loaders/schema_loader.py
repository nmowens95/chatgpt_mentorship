import yaml
from pathlib import Path

def load_schema(file_stem, schema_dir="schemas"):
    schema_dir = Path(schema_dir)

    schema_path = schema_dir/file_stem

    if schema_path.exists():
        with open(schema_path, "r") as f:
            return yaml.safe_load(f)
        
    else:
        raise FileNotFoundError(f"Path not found for: {schema_path}")
import yaml
from pathlib import Path

def load_schema(file_stem, schema_dir="schemas"):
    for ext in [".yaml", ".yml"]:
        schema_path = Path(schema_dir)/f"{file_stem}{ext}"
        if schema_path.exists():
           with open(schema_path, "r") as f:
            return yaml.safe_load(f)
        
    raise FileNotFoundError(f"Could not find file for {schema_path}")
    
    
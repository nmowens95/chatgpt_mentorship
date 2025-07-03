import os
import json

def write_txt(summary, file_name, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{file_name}_summary.txt")

    with open(path, "w") as file:
        for feature, cols in summary.items():
            file.write(f"--- {feature.upper()} ---\n")
            for col, val in cols.items():
                file.write(f"{col}: {val}\n")
            file.write("\n")
    return path

def write_json(summary, file_name, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{file_name}_summary.json")

    with open(path, "w") as file:
        json.dump(summary, file, indent=2)
    return path


WRITER_REGISTRY = {
    "txt": write_txt,
    "json": write_json
}
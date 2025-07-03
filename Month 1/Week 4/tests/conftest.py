import pytest
import pandas as pd
import os

@pytest.fixture
def sample_csv_file(tmp_path):
    file_path = tmp_path / "test.csv"

    df = pd.DataFrame({"name": ["Bob", "Alice"], "age": [30, 35]})
    df.to_csv(file_path, index=False)

    return tmp_path

@pytest.fixture
def sample_csv2(tmp_path):
    full_path = tmp_path / "test2.csv"
    
    df = pd.DataFrame({
        "name": ["Joe", "John"],
        "age": [20, 30],
        "state": ["MO", "TN"]
        })
    
    df.to_csv(full_path, index=False)
    
    return tmp_path
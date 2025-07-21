import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.load_files import load_files
import pytest
import pandas as pd

# Generate fake data and output path
@pytest.fixture
def sample_data():
    df = pd.DataFrame({
        "name": ["John", "Joe"],
        "date": ["2023-01-01", "2025-05-12"]
    })
    return df

@pytest.fixture
def sample_path(tmp_path):
    return tmp_path


def test_load_files(sample_data, sample_path):
    result = load_files(sample_data, "test_file.csv", output_dir=sample_path)

    assert os.path.exists(result)
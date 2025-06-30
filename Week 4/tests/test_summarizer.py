import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from datatools.features import dtype_summary, null_summary, mode_summary
from datatools.file_loader import CustomFileReadError, load_csv_files
import pytest

def test_dtype_summary():
    data = {
        "name": ["lisa", "anna"], 
        "age": [20, 25]
        }
    
    df = pd.DataFrame(data)
    result = dtype_summary(df) 
    
    assert result["age"] == 'int64'

def test_null_summary():
    data = {
        "name": ["John", "Karen", None, "Rachel", None],
        "age": [20, 55, 60, None, 15]
    }
    df = pd.DataFrame(data)
    result = null_summary(df)

    assert result["name"] > 0
    assert result["age"] > 0

def test_mode_summary():
    data = {
        "name": ["John", "Karen", None, "Rachel", None],
        "age": [20, 55, 60, None, 15]
    }
    df = pd.DataFrame(data)
    result = mode_summary(df)

    assert result["name"] == "John"
    assert result["age"] != None


def test_CustomFileReadError():
    with pytest.raises(CustomFileReadError):
        load_csv_files("fake_dir")
        
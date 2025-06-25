import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from features import dtype_summary, null_summary, mode_summary

def test_dtype_summary():
    data = {
        "name": ["lisa", "anna"], 
        "age": [20, 25]
        }
    
    df = pd.DataFrame(data)
    result = dtype_summary(df) 
    
    assert result["age"] == 'int64'
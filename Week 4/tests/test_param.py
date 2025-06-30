import pytest
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from datatools.features import dtype_summary, null_summary

@pytest.mark.parametrize(
    "data,expected_dtype",
    [
        ({"col": [1, 2]}, "int64"),
        ({"col": ["john", 23, "jared", None]}, "object"),
        ({"col": []}, "float64"),
        ({"col": ["", " ", 1]}, "object")
    ]
)
def test_dtype_summary(data, expected_dtype):
    df = pd.DataFrame(data)
    result = dtype_summary(df)
    assert result["col"] == expected_dtype
    assert result != None
    assert len(result) == 1


@pytest.mark.parametrize(
    "data,expected_null",
    [
        ({"col": ["", " ", None, 1, 2, None]}, 2),
        ({"col": [1, 2, 3, 4]}, 0)
    ]
)
def test_null_summary(data, expected_null):
    df = pd.DataFrame(data)
    result = null_summary(df)
    assert result["col"] == expected_null
    assert result is not None
    assert isinstance(result["col"], (int, np.integer))
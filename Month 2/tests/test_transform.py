import pytest
from pandas.api.types import is_datetime64_dtype
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.transform_data import transform_file

@pytest.fixture
def sample_claim_df():
    return pd.DataFrame({
        "claim_amount": ["$1,000.50"],
        "incident_date": ["2023-01-01"],
        "status": ["approved"]
    })

def test_transform_file(sample_claim_df):
    schema = {
        "claim_amount": "currency",
        "incident_date": "date"
    }

    result = transform_file(sample_claim_df, schema)

    assert isinstance(result, pd.DataFrame)
    assert result["claim_amount"].iloc[0] == 1000.50
    assert pd.api.types.is_datetime64_dtype(result["incident_date"])
    assert "missing_col" not in result.columns
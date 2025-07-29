import pytest
import pandas as pd
from unittest.mock import MagicMock

@pytest.fixture
def valid_claims_file(tmp_path):
    df = pd.DataFrame({
        "claim_id": ["1", "2", "3"],
        "customer_id": ["a", "b", "c"]
    })
    file = tmp_path / "claims.csv"
    df.to_csv(file, index=False)
    return file

@pytest.fixture
def duplicate_claims_file(tmp_path):
    df = pd.DataFrame({
        "claim_id": ["1", "1", "2"],
        "customer_id": ["a", "b", "c"]
    })
    file = tmp_path / "claims.csv"
    df.to_csv(file, index=False)
    return file

@pytest.fixture
def null_customer_file(tmp_path):
    df = pd.DataFrame({
        "claim_id": ["1", "2", "3"],
        "customer_id": ["a", None, "c"]
    })
    file = tmp_path / "claims.csv"
    df.to_csv(file, index=False)
    return file

@pytest.fixture
def mock_conn():
    return MagicMock()
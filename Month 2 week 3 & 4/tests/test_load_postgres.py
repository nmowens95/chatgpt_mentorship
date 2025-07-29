import pandas as pd
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.pipeline.load_to_postgres import insert_csv_to_table
from pathlib import Path
import pytest
import sys

def test_valid_claims_load(mock_conn, valid_claims_file):
    insert_csv_to_table(mock_conn, valid_claims_file, "claims_gold")
    assert mock_conn.cursor.return_value.execute.called

def test_raises_on_duplicate_ids(mock_conn, duplicate_claims_file):
    with pytest.raises(ValueError, match="Duplicate 'claim_id'"):
        insert_csv_to_table(mock_conn, duplicate_claims_file, "claims_gold")

def test_raises_on_null_customer(mock_conn, null_customer_file):
    with pytest.raises(ValueError, match="Missing values in required column"):
        insert_csv_to_table(mock_conn, null_customer_file, "claims_gold")
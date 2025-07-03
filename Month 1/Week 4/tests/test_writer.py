import pandas as pd
from src.datatools.summarizer import summarize_df
from src.datatools.writer import write_txt
from unittest.mock import patch
from src.datatools import summarizer


@patch("src.datatools.writer.write_txt")
def test_writer_called(mock_write_txt):

    df = pd.DataFrame({
        "age": [25, 30, 35],
        "name": ["Alice", "Bob", "Charlie"]
    })

    summary = {
        "dtype": {
            "age": "int64",
            "name": "object"
        }
    }

    summarizer.WRITER_REGISTRY["txt"] = mock_write_txt

    # Act
    summarizer.summarize_df(
        df=df,
        file_name="test_file",
        file_type=".csv",
        features=["dtype"],
        writer="txt"
    )

    # Assert
    mock_write_txt.assert_called_once()
    mock_write_txt.assert_called_with(summary, "test_file", output_dir="output")
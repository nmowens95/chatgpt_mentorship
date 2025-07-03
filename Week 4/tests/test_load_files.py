import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from datatools.file_loader import load_files
import pytest

def test_file_load(sample_csv_file):
    # dir_path = os.path.abspath("helper_files")
    # fake_dir = ("fake_path")

    result_true = load_files(sample_csv_file)
    # result_false = load_files(fake_dir)

    assert result_true != None
    assert len(result_true) == 1 
    assert isinstance(result_true, list)


def test_load_files_2(sample_csv2):
    result = load_files(sample_csv2)

    assert result != None
    assert isinstance(result, list)

    df, name, ext = result[0]
    assert df.shape == (2,3)
    assert name == "test2"
    assert ext == ".csv"
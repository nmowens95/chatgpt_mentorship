import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from datatools.file_loader import load_files
import pytest

def test_file_load():
    dir_path = os.path.abspath("helper_files")
    # fake_dir = ("fake_path")

    result_true = load_files(dir_path)
    # result_false = load_files(fake_dir)

    assert result_true != None
    assert len(result_true) > 1 
    assert isinstance(result_true, list)
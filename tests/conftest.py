import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json
import pandas as pd

@pytest.fixture
def test_csv_database (): return pd.read_csv ("tests/test_database.csv")

@pytest.fixture
def expected_output ():
    with open("tests/expected_output.json", 'r') as file:
        data = json.load(file)
    return data
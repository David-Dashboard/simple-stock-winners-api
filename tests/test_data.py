import datetime
import pandas as pd

# Helper functions
from app.data import _consolidate_data_by_day, _get_latest_closing_prices, _sort_and_rank

# API Functions
from app.data import get_stock_winners


# Helper functions
def get_percent (df, company_name):
    return df[
        (df['Kod'] == company_name) & 
        (df['Datum'] == datetime.date(2017,1,2))
        ]["Kursskillnad (procent)"].item()
# Unit tests
def test__consolidate_data_by_day (test_csv_database):
    df = _consolidate_data_by_day(test_csv_database)
    
    assert abs(get_percent(df, 'AddLife B') - 40.74) < 1e-2
    assert abs(get_percent(df, 'NCC') - 1.68) < 1e-2
    assert abs(get_percent(df, 'ABB') - 1.36) < 1e-2

def test__get_latest_closing_prices (test_csv_database):
    c_df = _consolidate_data_by_day(test_csv_database)
    df = _get_latest_closing_prices(c_df)

    assert (df["Datum"] == datetime.date(2017,1,2)).all()

def test__sort_and_rank ():

    unsorted = pd.DataFrame ({
        "feature1": [  5, 0.32, 32, 0.32,  1],
        "percent":  [  5,   40, 30,   10, 20],
        "feature2": [0.5,   52, 32,   52, 61]
    })

    correct_sorted = pd.DataFrame ({
        "feature1": [0.32, 32,  1, 0.32,   5],
        "percent":  [  40, 30, 20,   10,   5],
        "feature2": [  52, 32, 61,   52, 0.5],
        "rank":     [   1,  2,  3,    4,   5],
    })

    sorted_df = _sort_and_rank (unsorted, by="percent")
    assert sorted_df.equals(correct_sorted)


# End-to-end API tests
def test_get_stock_winners (test_csv_database, expected_output):
    output = get_stock_winners(test_csv_database)
    print(expected_output)
    print(output)
    assert expected_output == output
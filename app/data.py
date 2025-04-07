import json
import numpy as np
import pandas as pd
from datetime import date, timedelta

def read_database (filepath):
    return pd.read_csv (filepath)

def get_stock_winners(database_df):

    data_med_kursavslut = _consolidate_data_by_day(database_df)
    latest_closing_prices = _get_latest_closing_prices(data_med_kursavslut)
    sorted_df = _sort_and_rank (latest_closing_prices, by="Kursskillnad (procent)")

    sorted_df = sorted_df.rename(columns={
        "Kod": "name",
        "Kursskillnad (procent)": "percent",
        "Kursavslut": "latest"
        })
    json_response = json.loads(
        sorted_df[["rank", "name", "percent", "latest"]].iloc[:3]
        .to_json(orient="records", double_precision=2)
        )

    utdata = {
            "winners": json_response
        }
    
    return utdata

def _consolidate_data_by_day(df):
    """
    Final DF with columns
         Kod         
         Datum  
         Kursavslut  
         Kursskillnad    
         Kursskillnad (procent)
    """

    # Format all data correct dtypes
    df["Date"] = pd.to_datetime(df["Date"])
    #assert df["Kurs"].dtype == np.int64

    df["Datum"] = df["Date"].apply(lambda x: x.date()) # Grab date without time
    
    latest_kurs_by_day = df.groupby(["Kod", "Datum"]).apply(lambda x: x.loc[x["Date"].idxmax(), "Kurs"], include_groups=False) # Grab latest kurs by day
    data_med_kursavslut = latest_kurs_by_day.reset_index(name='Kursavslut')

    # Antaganden: Finns inga dagar som saknas och de är sorterade
    # Räkna ut kursskillnad, saknas data från föregående dag 
    kursskillnad = data_med_kursavslut.groupby("Kod").apply(lambda x: x["Kursavslut"].diff())
    data_med_kursavslut["Kursskillnad"] = kursskillnad.reset_index(name="Kursskillnad")["Kursskillnad"]

    #100 * diff / (curr + diff)
    data_med_kursavslut["Kursskillnad (procent)"] = 100 * data_med_kursavslut["Kursskillnad"] / (data_med_kursavslut["Kursavslut"] - data_med_kursavslut["Kursskillnad"])
    return data_med_kursavslut

def _get_latest_closing_prices(df):

    latest_timestamp = pd.to_datetime(df["Datum"]).max().date()
    return df[df["Datum"] == latest_timestamp]
    
def _sort_and_rank (df, by="Kursskillnad (procent)"):
    sorted_df = df.sort_values(by, ascending=False)
    sorted_df = sorted_df.reset_index(drop=True)
    sorted_df["rank"] = sorted_df.index + 1
    return sorted_df

def get_sample_input (filepath:str = "tests/test_database.csv"):
    return pd.read_csv (filepath)

def get_sample_output (filepath:str = "tests/expected_output.json"):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    print("\nSample indata:\n", get_sample_input())
    print("\nSample utdata:\n", get_sample_output())
    print("\nSample utdata after computation using indata:\n", get_stock_winners(get_sample_input()))
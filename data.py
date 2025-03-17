import json
import numpy as np
import pandas as pd
from datetime import date, timedelta

def get_stock_winners():

    df = get_sample_indata ()

    # Format all data correct dtypes
    df["Date"] = pd.to_datetime(df["Date"])
    #assert df["Kurs"].dtype == np.int64

    # Set up computation
    company_names = df["Kod"].unique().tolist() # np.ndarray -> list

    df["Day"] = df["Date"].apply(lambda x: x.date()) # Grab date without time
    
    latest_kurs_by_day = df.groupby(["Kod", "Day"]).apply(lambda x: x.loc[x["Date"].idxmax(), "Kurs"], include_groups=False) # Grab latest kurs by day
    data_med_kursavslut = latest_kurs_by_day.reset_index(name='Kursavslut')

    # Antaganden: Finns inga dagar som saknas och de är sorterade
    # Räkna ut kursskillnad, saknas data från föregående dag 
    kursskillnad = data_med_kursavslut.groupby("Kod").apply(lambda x: x["Kursavslut"].diff())
    data_med_kursavslut["Kursskillnad"] = kursskillnad.reset_index(name="Kursskillnad")["Kursskillnad"]

    #100 * diff / (curr + diff)
    data_med_kursavslut["Kursskillnad (procent)"] = 100 * data_med_kursavslut["Kursskillnad"] / (data_med_kursavslut["Kursskillnad"] + data_med_kursavslut["Kursavslut"])
    

    latest_timestamp = df["Date"].max().date()
    sorterad_data = data_med_kursavslut[data_med_kursavslut["Day"] == latest_timestamp].sort_values(by="Kursskillnad (procent)", ascending=False)
    
    sorterad_data = sorterad_data.reset_index(drop=True)
    sorterad_data = sorterad_data.rename(columns={
        "Kod": "name",
        "Kursskillnad (procent)": "percent",
        "Kursavslut": "latest"
        })
    sorterad_data["rank"] = sorterad_data.index + 1

    
    utdata = {
            "winners": json.loads(sorterad_data[["rank", "name", "percent", "latest"]].iloc[:3].to_json(orient="records", double_precision=2))
        }
    


    # Missing Kurs for today
    # Missing Kurs for yesterday
    # Missing company for yesterday
    # Missing company for today

    return utdata

def get_sample_indata ():
    return pd.read_csv ("sample_data/sample_indata.csv")

def get_sample_utdata ():
    with open("sample_data/sample_utdata.json", 'r') as file:
        data = json.load(file)
    print(data)
    return data



if __name__ == "__main__":
    print("\nSample indata:\n", get_sample_indata())
    print("\nSample utdata:\n", get_sample_utdata())
    print("\nSample utdata after computation using indata:\n", get_stock_winners())
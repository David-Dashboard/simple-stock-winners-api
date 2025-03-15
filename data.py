import json
import pandas as pd

def get_stock_winners():

    df = get_sample_indata ()
    

    return get_sample_utdata ()

def get_sample_indata ():
    print(df)
    return pd.read_csv ("sample_data/sample_indata.csv")

def get_sample_utdata ():
    with open("sample_data/sample_utdata.json", 'r') as file:
        data = json.load(file)
    print(data)
    return data



if __name__ == "__main__":
    print(get_stock_winners())
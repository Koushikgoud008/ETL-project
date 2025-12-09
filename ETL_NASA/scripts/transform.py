import pandas as pd
import json
import glob
import os

def transform_data():
    os.makedirs("../data/staged", exist_ok = True)
    latest_file = sorted(glob.glob("../data/raw/nasa_apod_*.json"))[-1]
    with open(latest_file, "r") as f:
        data = json.load(f)

    df = pd.DataFrame([{
        "date": data.get("date"),
        "url": data.get("url"),
        "title": data.get("title"),
        "explanation": data.get("explanation"),
        "hdurl": data.get("hdurl"),
        "copyright": data.get("copyright")
    }])

    output_path = "../data/staged/NASA_cleaned.csv"
    df.to_csv(output_path)

    print(f"Transformed {len(df)} Image records saved to: {output_path}\n")
    return df

if __name__ == "__main__":
    transform_data()
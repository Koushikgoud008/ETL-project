import json
from pathlib import Path
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)
IMG_DIR = Path(__file__).resolve().parents[1] / "data" / "images"
IMG_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv()
nasa_key = os.getenv("NASA_KEY")

def extract_data():
    url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_key}"
    params = {
        "date" : datetime.now().strftime('%Y-%m-%d') ,
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    image_url = data.get("hdurl")
    img_resp = requests.get(image_url)
    img_resp.raise_for_status()

    filename = DATA_DIR / f"nasa_apod_{datetime.now().strftime('%y%m%d_%H%M%S')}.json"
    filename.write_text(json.dumps(data, indent=2))

    imgname = f"nasa_img_{datetime.now().strftime('%y%m%d_%H%M%S')}.jpg"
    imgpath = IMG_DIR / imgname
    imgpath.write_bytes(img_resp.content)
    print(f"Extracted NASA data saved to: {imgname}\n")
    print(f"Extracted NASA data saved to: {filename}\n")
    
    return data

if __name__ == "__main__":
    extract_data() 
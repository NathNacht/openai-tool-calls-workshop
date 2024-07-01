import os

import requests
from dotenv import load_dotenv

load_dotenv()
APILAYER_API_KEY = os.environ.get("APILAYER_API_KEY")


def google_search(q: str):
    url = f"https://api.apilayer.com/google_search?q={q}"

    payload = {}
    headers = {
        "apikey": APILAYER_API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    from pprint import pprint
    result = google_search("python")
    pprint(result)

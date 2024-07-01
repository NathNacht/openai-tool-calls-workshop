import os

import requests
from dotenv import load_dotenv

load_dotenv()
APILAYER_API_KEY = os.environ.get("APILAYER_API_KEY")


def google_search(q: str):
    print("google_search called with query:", q)
    url = f"https://api.apilayer.com/google_search?q={q}"

    payload = {}
    headers = {
        "apikey": APILAYER_API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.raise_for_status()
    return str(response.json())


if __name__ == "__main__":
    from pprint import pprint
    result = google_search("python")
    pprint(result)

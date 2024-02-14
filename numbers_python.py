import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_date_fact(fragment=True, json_format=True):
    url = f"https://numbersapi.p.rapidapi.com/6/21/date"
    querystring = {"fragment": str(fragment).lower(), "json": str(json_format).lower()}
    headers = {
        "X-RapidAPI-Key": os.getenv('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    fact = fetch_date_fact()
    print(fact)



import requests

def get_public_apis():
    url = "https://api.publicapis.org/entries"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

import requests

def fetch_headers(url):
    response = requests.get(url)
    return response.headers

import requests

API_URL = "https://catfact.ninja"


def get_fact():
    response = requests.get(f"{API_URL}/fact")
    return response.json()


def get_facts():
    response = requests.get(f"{API_URL}/facts")
    return response.json()


def get_breeds():
    response = requests.get(f"{API_URL}/breeds")
    return response.json()

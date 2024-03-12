import requests
import json


def get_data(url: str, body: dict):
	response = requests.get(url=url, json=body)
	return requests.json()

import requests
import json


def get_data(url: str, endpoint: str, headers = {
            "Content-Type": "application/json"}):
	response = requests.get(url=url+endpoint, headers=headers)
	return response.json()

import requests
import json
import asyncio


async def async_get_data(url: str, body: dict):
	response = await requests.get(url=url, json=body)
	return requests.json()
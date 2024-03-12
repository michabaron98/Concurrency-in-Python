from common import *
from async_http_request import async_get_data
from http_request import get_data
import asyncio


tasks = [asyncio.ensure_future(async_get_data(API_URL, Endpoints.DINOSAURS_RANDOM)) for i in range(0, 1)]
responses = (response for response in await asyncio.gather(*tasks))
print(responses)
for i in range(0, 1):
	print(get_data(API_URL, Endpoints.DINOSAURS_RANDOM))
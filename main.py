import asyncio
import aiohttp

from common import *
from async_http_request import async_get_data, async_get_data_aiohttp
from http_request import get_data
from timer import calculate_execution_time, calculate_async_execution_time


@calculate_execution_time
def main() -> None:

	@calculate_async_execution_time
	async def async_run():
		tasks = [asyncio.ensure_future(async_get_data(API_URL, Endpoints.DINOSAURS_RANDOM)) for i in range(0, max_range+1)]
		for data in await asyncio.gather(*tasks):
			print(data['Name'])

	@calculate_execution_time
	def run():
		for i in range(0, max_range+1):
			data = get_data(API_URL, Endpoints.DINOSAURS_RANDOM)
			print(data['Name'])

	@calculate_async_execution_time
	async def async_run_aiohttp():
		async with aiohttp.ClientSession() as session:
			tasks = [asyncio.ensure_future(async_get_data_aiohttp(API_URL, Endpoints.DINOSAURS_RANDOM, session)) for i in range(0, max_range+1)]
			for data in await asyncio.gather(*tasks):
				print(data['Name'])

	max_range=100
	asyncio.run(async_run())
	asyncio.run(async_run_aiohttp())
	run()

main()
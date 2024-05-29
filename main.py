import asyncio
import aiohttp

from common import *
from async_http_request import async_get_data, async_get_data_aiohttp
from http_request import get_data
from timer import calculate_execution_time, calculate_async_execution_time


@calculate_execution_time
def main() -> None:

	@calculate_async_execution_time
	async def async_run() -> None:
		data=[]
		tasks = [asyncio.ensure_future(async_get_data(API_URL, Endpoints.DINOSAURS_RANDOM)) for i in range(0, max_range)]
		for task_result in await asyncio.gather(*tasks):
			data.append(task_result['Name'])
		print(f"Extracted {len(data)} dinosaurs")

	@calculate_execution_time
	def run() -> None:
		data = []
		for i in range(0, max_range):
			task_result = get_data(API_URL, Endpoints.DINOSAURS_RANDOM)
			data.append(task_result['Name'])
		print(f"Extracted {len(data)} dinosaurs")

	@calculate_async_execution_time
	async def async_run_aiohttp() -> None:
		data = []
		async with aiohttp.ClientSession() as session:
			tasks = [asyncio.ensure_future(async_get_data_aiohttp(API_URL, Endpoints.DINOSAURS_RANDOM, session)) for i in range(0, max_range)]
			for task_result in await asyncio.gather(*tasks):
				data.append(task_result['Name'])
		print(f"Extracted {len(data)} dinosaurs")

	max_range=100
	asyncio.run(async_run())
	asyncio.run(async_run_aiohttp())
	run()

main()
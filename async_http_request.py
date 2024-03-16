import asyncio
import aiohttp
from http_request import get_data


async def async_get_data(url: str,
						endpoint: str):
	response = await asyncio.to_thread(get_data, url, endpoint)
	return response

async def async_get_data_aiohttp(url: str,
						endpoint: str,
                        session: aiohttp.ClientSession):
	
	url=url+endpoint
	async with session.get(url) as response:
		return await response.json()
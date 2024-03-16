import asyncio
from http_request import get_data


async def async_get_data(url: str,
						endpoint: dict):
	response = await asyncio.to_thread(get_data, url, endpoint)
	return response


import asyncio
from pprint import pprint

import aiohttp

character_list = ["1", "2", "3", "4", "5"]


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")
        return await response.text()


async def main():
    url = "https://rickandmortyapi.com/api/character/"

    urls = [url + char_id for char_id in character_list]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(f"Received {len(results)} responses")
        pprint(results)


asyncio.run(main())

import asyncio
import string

import aiohttp

import os
import random
from os import getcwd

from http import HTTPStatus


async def async_worker(count):
    path = os.path.join(getcwd(), "rick_and_morty_random")
    os.makedirs(path, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        for _ in range(count):
            random_name = "".join(random.choices(string.ascii_letters + string.digits, k=5))
            character_id = random.randint(1, 826)
            url = f"https://rickandmortyapi.com/api/character/avatar/{character_id}.jpeg"

            async with session.get(url) as response:
                if response.status == HTTPStatus.OK:
                    content = await response.read()
                    file_name = f"rick_and_morty_{random_name}.jpg"
                    with open(f"{path}/{file_name}", "wb") as f:
                        f.write(content)


async def main():
    tasks = [
        asyncio.create_task(async_worker(3)),
        asyncio.create_task(async_worker(4)),
        asyncio.create_task(async_worker(2)),
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())

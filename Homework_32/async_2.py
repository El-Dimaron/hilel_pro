import asyncio
import aiohttp


async def fetch_data_to_future(future):
    url = "https://rickandmortyapi.com/api/character?name=rick"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
            future.set_result(result["results"])


async def main():
    future = asyncio.Future()
    await asyncio.create_task(fetch_data_to_future(future))

    results = await future
    print("Future:")
    for record in results:
        print(record)


asyncio.run(main())

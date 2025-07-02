import asyncio
import os

import aiofiles
from faker import Faker

file_number = 2
file_path = os.getcwd() + "/generated_files"
os.makedirs(file_path, exist_ok=True)
files = [f"{file_path}/file_{i}.txt" for i in range(1, file_number + 1)]

for i in range(1, file_number + 1):
    with open(f"{file_path}/file_{i}.txt", "w") as f:
        f.write(Faker().text(max_nb_chars=500))


async def read_file(path):
    async with aiofiles.open(path, mode='r') as f:
        content = await f.read()
        file_name = os.path.split(path)[1]
        print(f"{file_name} has {len(content)} characters")


async def main():
    tasks = [read_file(path) for path in files]
    await asyncio.gather(*tasks)


asyncio.run(main())

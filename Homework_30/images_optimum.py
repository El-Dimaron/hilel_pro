import os
import random
import string
import time
from multiprocessing.pool import ThreadPool

import matplotlib.pyplot as plt
import requests


class timer:

    def __init__(self, message):
        self.message = message
        self.elapsed = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = (time.time() - self.start)


def fetch_pic(num_pic=10):
    url = "https://picsum.photos/400/600"
    path = os.path.join(os.getcwd(), "img")

    for _ in range(num_pic):
        random_name = "".join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{path}/{random_name}.jpg", "wb") as f:
                f.write(response.content)


DATA_SIZE = 100
workers = [1, 2, 4, 8, 16, 32, 64, 100]
generated_data = {}

for worker in workers:
    with timer("Elapsed time {}") as t:
        with ThreadPool(worker) as pool:
            input_data = [DATA_SIZE // worker for _ in range(worker)]
            pool.map(fetch_pic, input_data)
    generated_data.update({worker: round(t.elapsed, 4)})

x = list(generated_data.keys())
y = list(generated_data.values())

plt.plot(x, y, marker='o')

for i in range(len(x)):
    text = "Baseline"

    if i > 0:
        tendency = 100 - (y[i] * 100) / y[i - 1]
        text = f"{round(tendency, 0)}%"

    plt.text(x[i] + 1, y[i] + 1, text, fontsize=9, ha='left', va='bottom')

plt.title("Workers vs Time")
plt.xlabel("Workers (quantity)")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()

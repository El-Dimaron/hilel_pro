import random
import time

import multiprocess
import matplotlib.pyplot as plt


class timer:

    def __init__(self, message):
        self.message = message
        self.elapsed = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = (time.time() - self.start)


DATA_SIZE = 10_000_000
workers = [1, 2, 4, 8, 16, 32, 64, 128]
fill_list = []
generated_data = {}


def fill_data_1(n):
    while n > 0:
        n -= 1
        fill_list.append(random.randint(1, 100))


for worker in workers:
    with timer("Elapsed time {}") as t:
        with multiprocess.Pool(worker) as pool:
            input_data = [DATA_SIZE // worker for _ in range(worker)]
            pool.map(fill_data_1, input_data)
    generated_data.update({worker: round(t.elapsed, 4)})

x = list(generated_data.keys())
y = list(generated_data.values())

for i in range(len(x)):
    text = "Baseline"

    if i > 0:
        tendency = 100 - (y[i] * 100) / y[i - 1]
        text = f"{round(tendency, 0)}%"

    plt.text(x[i], y[i], text, fontsize=9, ha='left', va='bottom')

plt.plot(x, y, marker='o')
plt.title("Workers vs Time")
plt.xlabel("Workers (quantity)")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()

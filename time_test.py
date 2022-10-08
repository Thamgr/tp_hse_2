import numpy as np
import random
from main import _mul, _sum, _max, _min
import time
import matplotlib.pyplot as plt

def test_time(sz):
    array = random.sample(range(1, 1000000), sz)
    time_start = time.time_ns()
    _mul(array)
    _sum(array)
    _max(array)
    _min(array)
    time_finish = time.time_ns()
    return (time_finish - time_start) / 1e6

x, y = np.linspace(1, 100000, 10), []

for sz in x:
    y.append(test_time(int(sz)))

plt.plot(x, y)
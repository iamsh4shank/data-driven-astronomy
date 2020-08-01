import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  total = 0
  for i in range(ntrials):
    data = np.random.rand(size)
    start = time.perf_counter()
    res = func(data)
    total += time.perf_counter() - start
  return total/ntrials

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**6, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**6, 10)))

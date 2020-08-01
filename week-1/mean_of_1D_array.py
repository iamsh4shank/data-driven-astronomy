import numpy as np
import csv
def calc_stats(file):
  data = np.loadtxt(file, delimiter=',')
  return (round(np.mean(data),1), round(np.median(data),1))

if __name__ == '__main__':
  mean = calc_stats('data.csv')
  print(mean)          

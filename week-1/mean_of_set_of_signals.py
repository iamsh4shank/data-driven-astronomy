import numpy as np
def mean_datasets(file):
  flag = 0
  for f in file:
    newdata = np.loadtxt(f, delimiter=',')
    if flag == 0:
      data = newdata
      flag = 1
    else:
     data = data + newdata
  data = data/len(file)
  data = np.round(data,1) 
  
  return data

if __name__ == '__main__':
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))


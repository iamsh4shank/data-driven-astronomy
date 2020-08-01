def calculate_mean(list):
  x = sum(list)
  return float(x)/len(list)

if __name__ == '__main__':
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
  
 

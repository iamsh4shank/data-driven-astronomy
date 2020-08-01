import numpy as np

def list_stats(values):
    
    N = len(values)
    if N == 0:
       return

    mean = sum(values)/N

    values.sort()
    mid = int(N/2)
    if N%2 == 0:
        median = (values[mid] + values[mid - 1])/2
    else:
        median = values[mid]

    return median, mean

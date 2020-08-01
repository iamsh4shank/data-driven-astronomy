import time, numpy as np
from astropy.io import fits

def median_fits(filenames):

  start = time.time()   # Start timer
  FITS_list = []
  for filename in filenames: 
    hdulist = fits.open(filename)
    FITS_list.append(hdulist[0].data)
    hdulist.close()

  FITS_stack = np.dstack(FITS_list)

  median = np.median(FITS_stack, axis=2)
  memory = FITS_stack.nbytes
  #memory = 200 * 200 * len(filenames) * FITS_stack.itemsize

  memory /= 1024
  
  stop = time.time() - start   # stop timer
  return median, stop, memory

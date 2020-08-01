import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
def load_fits(fitsfile):
  hdulist = fits.open(fitsfile)
  data = hdulist[0].data
  indexOfMax = np.argmax(data) 
  shapeNumColumns = data.shape[1] 
  row = int(indexOfMax/len(data[0,:]))
  column = indexOfMax - row* len(data[0,:])
  return (row, column)


if __name__ == '__main__':
  bright = load_fits('image1.fits')
  print(bright)
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 


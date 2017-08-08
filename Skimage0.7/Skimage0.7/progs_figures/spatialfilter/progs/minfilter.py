import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/wave.png').convert('L')
# performing minimum filter
b = scipy.ndimage.filters.minimum_filter(a,size=5,
    footprint=None,output=None,mode='reflect',
    cval=0.0,origin=0)
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)
# saving b as mino.png
b.save('../Figures/mino.png')

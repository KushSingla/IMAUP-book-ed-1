import scipy.misc
from skimage import filter
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/steps1.png').convert('L') 
# performing vertical Prewitt
b = filter.vprewitt(a) 
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b) 
b.save('../Figures/vprewitt_output.png')

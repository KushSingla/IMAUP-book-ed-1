import scipy.misc
from skimage.filter import edges
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/cir.png').convert('L') 
# performing the Prewitt filter
b = edges.prewitt(a) 
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b) 
b.save('../Figures/prewitt_cir.png')
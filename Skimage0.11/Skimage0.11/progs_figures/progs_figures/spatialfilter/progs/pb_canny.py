import scipy.misc, numpy
from skimage import feature
from scipy.misc.pilutil import Image
 
# opening the image and converting it to grayscale 
a = Image.open('../Figures/maps1.png').convert('L')
# converting a to an ndarray
a = scipy.misc.fromimage(a)
# performing Canny edge filter
b = feature.canny(a, sigma=1.0)
# b is converted from ndarray to an image 
b = scipy.misc.toimage(b)  
# saving b as canny_output.png
#b.save('../Figures/canny_output.png')
b.show()

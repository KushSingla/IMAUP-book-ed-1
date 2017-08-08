from skimage import filters
import scipy.misc 
from PIL import Image
import numpy


# opening the image and converting it to grayscale 
a = Image.open('../Figures/adaptive_example1.png').convert('L')
# a is converted to an ndarray
a = scipy.misc.fromimage(a)
# performing adaptive thresholding 
b = filters.threshold_adaptive(a,40,offset = 10)
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)
# saving the image as adaptive_output.png 
# in the folder Figurespb
#b.save('../Figures/adaptive_output.png')
b.show()

import math
import scipy.misc 
import numpy as np
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale
im = Image.open('../Figures/imageinverse_input.png').convert('L')
# im is converted to an ndarray
im1 = scipy.misc.fromimage(im)
# performing the inversion operation
im2 = 255 - im1
# im2 is converted from an ndarray to an image 
im3 = scipy.misc.toimage(im2)
# saving the image as imageinverse_output.png in 
# Figures folder 
im3.save('../Figures/imageinverse_output.png')

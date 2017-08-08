import math, numpy
import scipy.misc 
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
im = Image.open('../Figures/hequalization_input.png').convert('L')
# im is converted to an ndarray
im1 = scipy.misc.fromimage(im)
# finding the maximum and minimum pixel values
b = im1.max()
a = im1.min()
print a,b
# converting im1 to float
c = im1.astype(float)
# contrast stretching transformation
im2 = 255*(c-a)/(b-a)
# im2 is converted from an ndarray to an image 
im3 = scipy.misc.toimage(im2)
# saving im3 as contrast_output.png in
# Figures folder 
im3.save('../Figures/contrast_output2.png') 

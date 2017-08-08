import numpy as np 
import scipy.ndimage 
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/ultrasound_muscle.png').convert('L') 
# initializing the filter of size 5 by 5
# the filter is divided by 25 for normalization 
k = np.ones((5,5))/25
# performing convolution
b = scipy.ndimage.filters.convolve(a, k) 
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)    
b.save('../Figures/mean_output.png')

from scipy.misc import pilutil, fromimage
import Image
import numpy as np
from skimage.filter.thresholding 
     import threshold_otsu
import skimage.exposure as imexp

# Defining function
def renyi_seg_fn(im,alpha):
    hist = imexp.histogram(im)	
    # Convert all values to float
    hist_float = [float(i) for i in hist[0]] 
    # compute the pdf 
    pdf  = hist_float/numpy.sum(hist_float)
    # compute the cdf
    cumsum_pdf = numpy.cumsum(pdf)

    s = 0
    e = 255 # assuming 8 bit image
    scalar = 1.0/(1-alpha)
    # A very small value to prevent 
    # division by zero 
    eps = numpy.spacing(1) 

    rr = e-s
    # The second parentheses is needed because 
    # the parameters are tuple 
    h1 = np.zeros((rr,1)) 
    h2 = np.zeros((rr,1))
    # the following loop computes h1 and h2
    # values used to compute the entropy
    for ii in range(1,rr): 
        iidash = ii+s
        temp1 = np.power(pdf[1:iidash]
                /cumsum_pdf[iidash],scalar)
        h1[ii] = np.log(numpy.sum(temp1)+eps)
        temp2 = np.power(pdf[iidash+1:255]
                /(1-cumsum_pdf[iidash]),
                scalar)
        h2[ii] = np.log(numpy.sum(temp2)+eps)

    T = h1+h2
    # Entropy value is calculated
    T = -T*scalar
    # location where the maximum entropy 
    # occurs is the threshold for the renyi entropy
    location = T.argmax(axis=0) 
    # location value is used as the threshold
    thresh = location 
    return thresh
	

# Main program
# opening the image and converting it to grayscale
a = Image.open('CT.png').convert('L')
# a is converted to an ndarray
a = fromimage(a)
# computing the threshold by calling the function
thresh = renyi_seg_fn(a,3)
b = a > thresh
# b is converted from an ndarray to an image 
b = pilutil.toimage(b)  
# saving the image as renyi_output.png
b.save('figures/renyi_output.png')

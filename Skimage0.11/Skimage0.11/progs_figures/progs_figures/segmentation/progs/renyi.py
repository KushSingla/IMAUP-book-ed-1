import dicom
import numpy as np
import skimage.exposure as imexp
from scipy.misc import toimage

def renyi_seg_fn(im,alpha):
    hist = imexp.histogram(im)	
    print len(hist[0]), type(hist[0]) 
    # Convert all values to float
    hist_float = [float(i) for i in hist[0]] 
    # compute the pdf 
    pdf  = hist_float/np.sum(hist_float)
    # compute the cdf
    cumsum_pdf = np.cumsum(pdf)

    s = min(hist[1])
    e = max(hist[1])
    scalar = 1.0/(1-alpha)
    # A very small value to prevent 
    # division by zero 
    eps = np.spacing(1) 

    rr = e-s
    # The second parentheses is needed because 
    # the parameters are tuple 
    h1 = np.zeros((rr,1)) 
    h2 = np.zeros((rr,1))
    # the following loop computes h1 and h2
    # values used to compute the entropy
    for ii in range(1,rr): 
        iidash = ii+s
        temp1 = np.power((pdf[1:iidash]+eps)/(cumsum_pdf[iidash]+eps),scalar)
        h1[ii] = np.log(np.sum(temp1)+eps)
        temp2 = np.power((pdf[iidash+1:255]+eps)/(1-cumsum_pdf[iidash]+eps),scalar)
        h2[ii] = np.log(np.sum(temp2)+eps)

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
dfh = dicom.read_file("../Figures/file_004699.dcm")
# a is converted to an ndarray
im = dfh.pixel_array
# computing the threshold by calling the function
thresh = renyi_seg_fn(im,3)
thresholdedimage = im > thresh
print "The threshold is :", thresh
thresharray = toimage(thresholdedimage)
thresharray.save('../Figures/renyi_output.png')
thresharray.show()

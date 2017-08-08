import scipy.misc
import numpy as np
from skimage import filter 
import matplotlib.pyplot as plt
from scipy.misc.pilutil import Image
from skimage.measure import label
from skimage.measure import regionprops
from skimage.feature import match_template

# opening the image and converting it to grayscale 
image =Image.open('../Figures/airline_seating.png').convert('L')
# converting the input image into an ndarray
image = scipy.misc.fromimage(image)
# reading the template image
temp = Image.open('../Figures/template1.png').convert('L')
# converting the template into an ndarray
temp = scipy.misc.fromimage(temp)
# performing template matching
result = match_template(image, temp)
thresh = 0.7
# thresholding the result from template 
# matching considering pixel values where the 
# normalized cross-correlation is greater than 0.7
res = result > thresh
# labeling the thresholded image
c = label(res, background = 0)
# performing regionprops to count the 
# number of labels
reprop = regionprops(c)
print "The number of seats are:", len(reprop) 
# converting the ndarray to image
d = scipy.misc.toimage(res)
d.show()

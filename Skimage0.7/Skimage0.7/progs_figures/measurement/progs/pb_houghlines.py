import numpy as np
import scipy.misc, cv2

# opening the image 
im = cv2.imread('../Figures/hlines2.png')
# converting the image to grayscale
a1 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# thresholding the image to obtain 
# only foreground pixels
thresh,b1 = cv2.threshold(a1, 0, 255,
            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# converting the thresholded ndarray to an image
b2 = scipy.misc.toimage(b1)
b2.save('../Figures/hlines_thresh.png')
# performing the Hough lines transform
lines = cv2.HoughLines(b1,5,0.1,200)
# printing the lines: distance and angle in radians
print lines


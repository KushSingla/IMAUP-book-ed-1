import cv2
import numpy
from scipy.ndimage import label
import scipy.misc
from PIL import Image
import numpy

# opening the image and converting it to a grayscale image
a = cv2.imread('../Figures/cellimage.png')
a1 = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
thresh,b = cv2.threshold(a1, 0, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
b1 = scipy.misc.toimage(b) 
b1.save('../Figures/waterhsed_otsu.png')
b2 = cv2.erode(b, None,iterations = 2)
b3 = scipy.misc.toimage(b2) 
b3.save('../Figures/watershed_erode.png')
dist_trans = cv2.distanceTransform(b2, 2, 3)
dist1 = scipy.misc.toimage(dist_trans) 
dist1.save('../Figures/watershed_distance.png')
thresh, dt = cv2.threshold(dist_trans, 1, 255, cv2.THRESH_BINARY)	
lbl, ncc = label(dt)
lbl_1 = scipy.misc.toimage(lbl) 
lbl_1.save('../Figures/watershed_label.png')
cv2.watershed(a, lbl)
dt1 = scipy.misc.toimage(lbl)  
# saving the image as sk_otsu.png
#dt1.save('../Figures/watershed_out.png')
dt1.show()


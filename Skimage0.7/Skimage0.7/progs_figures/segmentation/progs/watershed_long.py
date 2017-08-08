import cv2
import numpy as np
import scipy.misc
import scipy.ndimage as snd

# image is read and is converted to a numpy array
img = cv2.imread('../Figures/cellimage.png')
# image is convereted to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# binary thresholding is done using the threshold 
# from Otsu's method
ret1,thresh1 = cv2.threshold(gray,0,255,\
               cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# foreground pixels are determined by 
# performing erosion
fore_ground = cv2.erode(thresh1,None,iterations = 3)
# fore_ground = snd.morphology.grey_erosion(thresh, iterations=2)
# background pixels are determined by performing dilation 
bgt = cv2.dilate(thresh1,None,iterations = 3) 
# bgt = snd.morphology.grey_dilation(thresh, iterations=3)
# a threshold of 100 is used to determine background pixels 
ret,back_ground = cv2.threshold(bgt,1,100,1)
# marker is determined by adding foreground and background pixels 
marker = cv2.add(fore_ground,back_ground)
# converting marker to 32 int
marker32 = np.int32(marker)  
# marker32 = scipy.misc.toimage('../Figures/marker32.png')
# waterhsed is performed 
cv2.watershed(img,marker32)
# the output is converted to unit8 image
m = cv2.convertScaleAbs(marker32) 
# m = scipy.misc.toimage('../Figures/m_watershed.png')
# thresholding is performed to get mask
# binary thresholding is done using the threshold from Otsu's method
ret2,thresh2 = cv2.threshold(m,0,255,
		cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print ret2 #thresh2
# t2 = scipy.misc.toimage('../Figures/thresh2.png')
# the mask and the image are overlapped using cv2.bitwise_and
res = cv2.bitwise_and(img,img,mask = thresh2)
# res is converted from ndarray to iamge
res = scipy.misc.toimage(res)
# saving the image as watershed_output.png
res.save('../Figures/waterhsed_output.png')
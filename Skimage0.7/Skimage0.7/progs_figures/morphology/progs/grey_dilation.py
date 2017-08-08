# program to use morphological operation, grayscale dilation
# the website to find the function details is 
# http://docs.scipy.org/doc/scipy/reference/ndimage.html
from scipy.misc import toimage
import Image  
import scipy.ndimage 
import numpy as np

a = Image.open('../Figures/dil_image.jpg')
s = np.array([[0,1,0],[1,1,1], [0,1,0]],dtype=int) 
b = scipy.ndimage.morphology.grey_dilation(a, size=(3,3), structure=s)
b1 = scipy.ndimage.morphology.grey_dilation(b, size=(3,3), structure=s)
b2 = scipy.ndimage.morphology.grey_dilation(b1, size=(3,3), structure=s)
c = toimage(b2)
c.save('grey_dimage_output.jpg')  

import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a =Image.open('../Figures/imagefor_laplacian.png').convert('L')
# performing Laplacian filter
b = scipy.ndimage.filters.laplace(a,mode='reflect')
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)
b.save('../Figures/laplacian_new.png')   

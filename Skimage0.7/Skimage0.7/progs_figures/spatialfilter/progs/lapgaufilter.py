import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image 

# opening the image and converting it to grayscale
a = Image.open('../Figures/vhuman_t1.png').convert('L')
# performing Laplacian of Gaussian
b = scipy.ndimage.filters.gaussian_laplace(a,1,mode='reflect')
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)
b.save('../Figures/log_vh1.png')   

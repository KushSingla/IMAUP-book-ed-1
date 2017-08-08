import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale
a = Image.open('../figure/spinwheel.png').convert('L')
# performing Laplacian of Gaussian with sigma = 0.9
im1 = scipy.ndimage.filters.gaussian_laplace(a,0.9,mode='reflect')
# performing Laplacian of Gaussian with sigma = 1.3
im2 = scipy.ndimage.filters.gaussian_laplace(a,1.3,mode='reflect')
# determining the difference for obtaining edge
b = im1-im2
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)
#b.save('diff_log.png')
b.show()

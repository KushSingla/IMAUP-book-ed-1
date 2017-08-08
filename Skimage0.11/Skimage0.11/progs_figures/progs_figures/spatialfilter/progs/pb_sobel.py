import scipy.misc
from skimage import filters
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/cir.png').convert('L')
# performing Sobel filter
b = filters.sobel(a)
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)
#b.save('../Figures/sobel_cir.png')
b.show()

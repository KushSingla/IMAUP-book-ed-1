import scipy.misc
from skimage import filters
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/cir.png').convert('L') 
# performing vetical Sobel
b = filters.sobel_v(a) 
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b) 
#b.save('../Figures/vsobel_output.png')
b.show()

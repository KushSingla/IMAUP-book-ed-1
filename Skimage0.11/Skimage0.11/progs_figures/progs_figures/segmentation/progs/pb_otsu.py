from skimage.filters.thresholding import threshold_otsu
import scipy.misc
from PIL import Image 

# opening the image and converting it to grayscale
a = Image.open('../Figures/sem3.png').convert('L')
# a is converted to an ndarray
a = scipy.misc.fromimage(a)
# performing Otsu's thresholding 
thresh = threshold_otsu(a)
# pixels with intensity greater than 
# theshold are kept
b = a > thresh
# b is converted from ndimage to 
b = scipy.misc.toimage(b)  
# saving the image as sk_otsu.png
# b.save('../Figures/otsu_semoutput.png')
b.show()

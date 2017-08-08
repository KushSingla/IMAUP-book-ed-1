from scipy.misc import toimage, fromimage
from PIL import Image
import numpy
from skimage.morphology import skeletonize

# opening the image and converting it to grayscale
a = Image.open('../figures//steps1.png').convert('L')
# converting a to an ndarray and normalizing it
a = fromimage(a)/numpy.max(a)
# performing skeletonization  
b = skeletonize(a)
# converting b from an ndarray to an image
c = toimage(b)
# saving the image as skeleton_output.png
# in the folder Figures#c.save('../figures//skeleton_output.png')
c.show()

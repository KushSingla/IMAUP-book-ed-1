from scipy.misc.pilutil import Image
import numpy
from skimage.morphology import skeletonize
import scipy

# opening the image and converting it to grayscale
a = Image.open('../figure/dil_image1.png').convert('L')
# converting a to an ndarray and normalizing it
a = scipy.misc.fromimage(a)/numpy.max(a)
# performing skeletonization
b = skeletonize(a)
# converting b from an ndarray to an image
c = scipy.misc.toimage(b)
# saving the image 

#c.save('skeleton.png')
c.show()

import scipy.misc
import scipy.ndimage 
from scipy.misc.pilutil import Image

# opening the image and converting it to a greyscale image
a = Image.open('../figure/ct_saltandpepper.png').convert('L')
# performing maximum filter
b = scipy.ndimage.filters.minimum_filter(a,size=5, 
	footprint=None,output=None,mode='reflect',  
	cval=0.0,origin=0)
# b is converted from an ndarray to an image 
b = scipy.misc.toimage(b)
#b.save('max_ct_saltandpepper.png')
b.show()

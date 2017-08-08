import numpy, math
import scipy.misc
from skimage.measure  import label
from scipy.misc.pilutil import Image
from skimage.measure import regionprops


# opening the image and converting it to grayscale 
a = Image.open('../figure/houghcircles_segmented.png').convert('L') 
# a is converted to an ndarray
a = scipy.misc.fromimage(a)
# labelling is preformed on a
c = label(a)
# c is converted from an ndarray to an image 
c1 = scipy.misc.toimage(c)
# c1 is saved as label_output.png
#c1.save('label_output.png')
# on the labelled image c, regionprops is performed
d = regionprops(c)

print "The diameter of the circles are: "
for props in d:
    print 2*math.sqrt(props['Area']/math.pi)

from scipy.misc import toimage, fromimage
import Image
import numpy as np
import scipy.ndimage as snd

# opening the image and converting it to grayscale
a = Image.open('../Figures/thickening_input.png').convert('L')
# defining the structuring element
structure1 = np.array([[1, 1, 0], [1, 1, 1],[1, 1, 1]])
# performing the binary hit-or-miss
b = snd.morphology.binary_hit_or_miss(a,structure1=structure1)
# b is converted from an ndarray to an image
b = toimage(b)
# displaying the image
b.show()

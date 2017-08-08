from scipy.misc import toimage, fromimage
from PIL import Image
import scipy.ndimage as snd

# opening the image and converting it to grayscale
a = Image.open('../figures/dil_image.png').convert('L')
# defining the structuring element
s = [[0,1,0],[1,1,1], [0,1,0]]
# performing the binary closing for 5 iterations
b = snd.morphology.binary_closing(a,structure=s,
    iterations=5)
b = toimage(b)
b.show()

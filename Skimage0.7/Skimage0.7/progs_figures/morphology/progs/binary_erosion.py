from scipy.misc import toimage, fromimage
import Image
import scipy.ndimage as snd

# opening the image and converting it to grayscale
a = Image.open('../Figures/er_image.png').convert('L')
# performing binary erosion for 5 iterations
b = snd.morphology.binary_erosion(a,iterations=25)
# converting b from an ndarray to an image
b = toimage(b)
# displaying the image
b.show()

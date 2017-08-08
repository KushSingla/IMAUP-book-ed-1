from scipy.misc import toimage
import Image
import scipy.ndimage as snd

# opening the image and converting it to grayscale 
a = Image.open('../Figures/dil_image.png').convert('L')
# performing binary dilation for 5 iterations
b = snd.morphology.binary_dilation(a,iterations=5)
# converting b from an ndarray to an image
b = toimage(b) 
# displaying the image
b.show()

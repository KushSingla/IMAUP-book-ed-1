from scipy.misc import toimage
import Image
import scipy.ndimage as snd

# opening the image and converting it to grayscale
a = Image.open('../Figures/dil_image.png').convert('L')  
# defining the structuring element
s = [[0,1,0],[1,1,1], [0,1,0]] 
# performing the binary opening for 5 iterations
b = snd.morphology.binary_opening(a, structure=s,
    iterations=5)
# b is converted from an ndarray to an image
b = toimage(b)
# displaying the image
b.show()

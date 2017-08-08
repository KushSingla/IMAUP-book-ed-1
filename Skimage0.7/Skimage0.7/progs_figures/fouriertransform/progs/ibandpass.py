import scipy.misc 
import numpy, math 
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/fft1.png').convert('L') 
# a is converted to an ndarray
b = scipy.misc.fromimage(a)
# performing FFT
c = fftim.fft2(b)
# shifting the Fourier frequency image  
d = fftim.fftshift(c)

# intializing variables for convolution function
M = d.shape[0]
N = d.shape[1]
# H is defined and 
# values in H are initialized to 1
H = numpy.zeros((M,N)) 
center1 = M/2
center2 = N/2
d_0 = 30.0 # minimum cut-off radius
d_1 = 50.0 # maximum cut-off radius

# defining the convolution function for bandpass
for i in range(1,M):
    for j in range(1,N):
        r1 = (i-center1)**2+(j-center2)**2
        # euclidean distance from 
        # origin is computed
        r = math.sqrt(r1)
        # using min and max cut-off to create 
		# the band or annulus
        if r > d_0 and r < d_1:
            H[i,j] = 1.0 

# converting H to an image			
H = scipy.misc.toimage(H) 
# performing the convolution 
con = d * H 
# computing the magnitude of the inverse FFT
e = abs(fftim.ifft2(con))
# e is converted from an ndarray to an image 
f = scipy.misc.toimage(e) 
# f.show()
# saving the image as ibandpass_output.png in
# Figures folder
f.save('../Figures/ibandpass_output.png') 

import math, numpy 
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale 
a = Image.open('../Figures/fft1.png').convert('L') 
# a is converted to an ndarray
b = numpy.asarray(a)
# performing FFT
c = abs(fftim.fft2(b))
# shifting the Fourier frequency image 
d = fftim.fftshift(c)
# converting the d to floating type and saving it 
# as fft1_output.raw in Figures folder
d.astype('float').
   tofile('../Figures/fft1_output.raw')

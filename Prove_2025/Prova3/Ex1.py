
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi


plt.close('all')
x1= np.float64(io.imread('../Immagini/disk1.jpg'))
x1 = np.mean(x1,-1)
x2= np.float64(io.imread('../Immagini/disk2.jpg'))
x2 = np.mean(x2,-1)

plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(x1, clim=None, cmap='gray')
plt.title('Immagine di input 1')

plt.subplot(1,2,2)
plt.imshow(x2, clim=None, cmap='gray')
plt.title('Immagine di input 2')

# 1. calcolo del quadrato del Laplaciano delle due immagini
#maschera per il calcolo del laplaciano
h = np.array([[0,1,0],[1,-4,1],[0,1,0]])

y1= ndi.correlate(x1,h)**2
y2= ndi.correlate(x2,h)**2 

# plt.figure(2)
# plt.subplot(1,2,1)
# plt.imshow(y1, clim=None, cmap='gray')
# plt.title('Laplaciano di input 1')

# plt.subplot(1,2,2)
# plt.imshow(y2, clim=None, cmap='gray')
# plt.title('Laplaciano di input 2')

# valutazione del livello di attivit`a di ogni immagine
mean1= ndi.generic_filter(y1, np.mean, 5)
var1= ndi.generic_filter(y1, np.var, 5)
a1= mean1*(var1**2)

mean2= ndi.generic_filter(y2, np.mean, 5)
var2= ndi.generic_filter(y2, np.var, 5)
a2= mean2*(var2**2)

# normalizzazione
A1 = a1 / (a1+a2)
A2 = a2 / (a1+a2)

# fusione
xf = A1*x1 + A2*x2

plt.figure(3)
plt.imshow(xf, clim=None, cmap='gray')
plt.title('Risultato della fusione')

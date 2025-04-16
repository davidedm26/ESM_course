# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:23:05 2025

@author: david
"""

# Enhancement di un testo a bassa risoluzione.
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph

x= np.float64(io.imread('../Immagini/immagini_lab_morfologia/testo_fax_bool.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

b = np.array([[0,1,0],[1,1,1],[0,1,0]], bool) #elemento strutturante a 

y = morph.binary_dilation(x,b)

plt.figure(2)
plt.imshow(y, clim=[0,1], cmap='gray') #non servono tag
plt.title('Operazione di dilatazione')



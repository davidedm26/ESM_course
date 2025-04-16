# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:45:06 2025

@author: david
"""

#scegliere come elemento strutturante un quadrato 3x3

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph

x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/impronta_bool.tif'))
plt.figure(1)
plt.imshow(x, clim=[0,1], cmap='gray')
plt.title('input')

b = np.ones( (3,3)) #oppure morph.rectangle(3,3)
y = morph.binary_opening(x,b)
plt.figure(2)
plt.imshow(y, clim=[0,1], cmap='gray')
plt.title('opening')

z = morph.binary_closing(y,b)
plt.figure(3)
plt.imshow(z, clim=[0,1], cmap='gray')
plt.title('closing')

#Proviamo funzione thin
u=  morph.thin(z)
plt.figure(4)
plt.imshow(u, clim=[0,1], cmap='gray')
plt.title('thinning')

#Proviamo funzione skeleton
s=  morph.skeletonize(y)
plt.figure(5)
plt.imshow(s, clim=[0,1], cmap='gray')
plt.title('skeletonize')






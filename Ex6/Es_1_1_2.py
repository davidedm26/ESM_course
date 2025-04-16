# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 16:47:19 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph

x= np.float64(io.imread('../Immagini/quadrati.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

b = morph.rectangle(13, 13)
y = morph.opening(x,b)
plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')
plt.title('Applicazione dell opening')
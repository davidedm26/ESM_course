# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 19:25:27 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph

x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/circbw_bool.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

b = morph.rectangle(50, 60)
y = morph.opening(x,b)
plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')
plt.title('Applicazione dell opening')
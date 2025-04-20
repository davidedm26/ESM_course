# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 15:53:57 2025

@author: david
"""

#ES2
import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

x = np.load('../immagini/dati.npy')
plt.imshow(x, clim=None, cmap='gray')

#L'immagine fornita non corrisponde a quella richiesta dalla traccia!
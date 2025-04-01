# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:52:49 2025

@author: david
"""
import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

x = np.float64(io.imread('../immagini/circuito_rumoroso.jpg'))
# y = ndi.generic_filter(x, np.median, (5,5))
y = ndi.median_filter(x, 10)
plt.subplot(1,2,1); plt.imshow(x,clim=[0,255],cmap='gray');
plt.subplot(1,2,2); plt.imshow(y,clim=[0,255],cmap='gray');
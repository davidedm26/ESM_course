# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 16:21:39 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

x= np.float64(io.imread('../Immagini/yeast.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

from sklearn.cluster import k_means

#calcola immagini delle d_s locali con win3x3
x_ds = ndi.generic_filter(x, np.std, (3,3))

plt.figure(2)
plt.imshow(x_ds, clim=None, cmap='gray')
plt.title('Immagine delle deviazioni std')

mG = np.mean(x)
a=30
b=1.5

y = ( x > a*x_ds ) & ( x > b*mG )
plt.figure(3)
plt.imshow(y, clim=None, cmap='gray')
plt.title('Mappa')

#confronto con k-means
from sklearn.cluster import k_means

d = np.reshape(x, (-1,1))
K=2
centroid, idx, sum_var = k_means(d, K)

y = np.reshape(idx, x.shape)

plt.figure(4); plt.imshow(y, clim=[0,K-1], cmap='jet')
plt.title('output')










# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 19:24:01 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col

plt.close('all')
x = io.imread('../Immagini/auto.jpg')
plt.figure('input')
plt.imshow(x, cmap='gray', clim=[0,255])

# 1. si generano copie dell’immagine a diversa qualit`a xQ(m, n, k) (Q = 1 : 10 : 100);
Quality = [90]
Y = []
for Q in Quality:
    filename= 'q'+ str(Q) + '.jpg'
    io.imsave(filename, x, quality=Q ) #compressione
    xq =io.imread(filename)
    d= (x - xq )**2
    d = np.mean(d, -1)
    y = ndi.generic_filter(d, np.mean, (16,16))
    Y.append(y)
    plt.figure(filename)
    y = y<1
    plt.imshow(y, cmap='gray', clim=[0,1])
    y= morph.binary_closing(y, morph.disk(10))
    y= morph.binary_opening(y, morph.rectangle(10,10))
    plt.figure(filename+'2')
    plt.imshow(y, cmap='gray', clim=[0,1])
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 10:58:56 2025

@author: david
"""

#EX1

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col
import skimage.transform as tf

plt.close('all')

x = io.imread('./immagini/viola.jpg')/255
plt.figure('input')
plt.imshow(x)

#realizzo color balancing nello spazio CMY
x_cmy = 1 - x
plt.figure('cmy')
plt.imshow(x_cmy)

#modifico componente di magenta
x_cmy[:,:,1] = x_cmy[:,:,1]**2.5

#ritorno a rgb
x_rgb = 1 - x_cmy

plt.figure('rgb')
plt.imshow(x_rgb)

#confronto con l'originale in termini di MSE
originale= io.imread('./immagini/viola.jpg')/255
mse = np.mean( (originale- x_rgb)**2)

#segmento immagine in due regioni

#lavoro nello spazio hsv
x_hsv= col.rgb2hsv(x_rgb)

#valuto le 3 componenti
h,s,v = x_hsv[:,:,0], x_hsv[:,:,1], x_hsv[:,:,2]
plt.figure('HSV')
plt.subplot(1,3,1)
plt.imshow(h, clim=[0,1], cmap='gray')
plt.subplot(1,3,2)
plt.imshow(s, clim=[0,1], cmap='gray')
plt.subplot(1,3,3)
plt.imshow(v, clim=[0,1], cmap='gray')


mask = v > 0.10
mask = morph.opening(mask, morph.disk(10))
mask = morph.closing(mask, morph.disk(5))
plt.figure('mask')
plt.imshow(mask, cmap='gray', clim=[0,1])

#equalizza hist del solo sfondo #metodo veloce
from skimage.exposure import equalize_hist
# y_equalized = np.copy(x_rgb)
# for i in range(3):  # R, G, B
#     y_equalized[:,:,i] = equalize_hist(x_rgb[:,:,i], mask=1-mask, nbins=128)
x_rgb = x_rgb*255
plt.figure('x_rgb')
plt.imshow(x_rgb)

y_equalized = np.copy(x_rgb)
for i in range (3):
    y_equalized[:,:,i] = 127 * ( x_rgb[:,:,i] - np.min(x_rgb[:,:,i])) / (np.max(x_rgb[:,:,i])- np.min(x_rgb[:,:,i]))
    # y_equalized[:,:,i] = equalize_hist(x_rgb[:,:,i], mask=1-mask, nbins=128)
    
y_equalized =y_equalized/255
x_rgb = x_rgb/255

plt.figure('equalized ')
plt.imshow(y_equalized)

y = np.copy(x_rgb)
y[~mask] = y_equalized[~mask]

plt.figure('output con sfondo equalizzato')
plt.imshow(y)

#migliora aspetto visivo
#applico filtraggio gaussiano a componente V
#lavoro nello spazio hsv
y_hsv= col.rgb2hsv(y)
# y_hsv[:,:,2] = ndi.gaussian_filter(y_hsv[:,:,2], (2,2))
h,s,v = y_hsv[:,:,0], y_hsv[:,:,1], y_hsv[:,:,2]
plt.figure(' Y HSV')
plt.subplot(1,3,1)
plt.imshow(h, clim=[0,1], cmap='gray')
plt.subplot(1,3,2)
plt.imshow(s, clim=[0,1], cmap='gray')
plt.subplot(1,3,3)
plt.imshow(v, clim=[0,1], cmap='gray')
y_rgb = col.hsv2rgb(y_hsv)

# plt.figure('output migliorato')
# plt.imshow(y_rgb)
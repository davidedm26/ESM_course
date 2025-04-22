# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:34:52 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col
import skimage.transform as tf

x = np.reshape(np.fromfile('./immagini/mixed_noisy.y', dtype=np.float32), (256,256))

plt.figure('input')
plt.imshow(x, clim=[0,255], cmap='gray')

# 1. filtraggio mediante filtro gaussiano con finestra 5 X 5 e deviazione standard pari a 1:2;
y1 = ndi.gaussian_filter(x,  sigma=(1.2))

plt.figure('Filtraggio Gaussiano')
plt.imshow(y1, clim=[0,255], cmap='gray')

# calcolo dell’immagine dei coefficienti di variazione locali C = = su finestre scorrevoli 99;
def variazioni_locali(x):
    return np.std(x)/np.mean(x)
    
    
y2 = ndi.generic_filter(y1, variazioni_locali, (9,9))

plt.figure('Imamgine dei coefficienti di variazione locali')
plt.imshow(y2, clim=[0,255], cmap='gray')

mask = y2 > 0.07
plt.figure('Maschera non omogenei')
plt.imshow(mask, clim=[0,1], cmap='gray')

PSNR = 10*np.log10( 255*2/MSE)








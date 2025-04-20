# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 16:13:24 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as color

plt.close('all')
x1=io.imread('../Immagini/img1.png')
plt.figure(1)
plt.imshow(x1, clim=None, cmap='gray')
plt.title('Immagine di input 1')

import skimage.transform as tf
A = tf.AffineTransform( translation=(50,20), rotation =np.deg2rad(90), scale=(2) )
y1 = tf.warp(x1,A)

plt.figure(2)
plt.imshow(y1, clim=None, cmap='gray')
plt.title('Immagine di input 1')

#-------------------------------------#
# x2=io.imread('../Immagini/img2.png')
# plt.figure(2)
# plt.imshow(x2, clim=None, cmap='gray')
# plt.title('Immagine di input 2')
# #----------------------------------------#
# # Realizzate tutte le operazioni che ritenete necessarie per ottenere la mappa di
# # segmentazione binaria in cui avete localizzato il difetto delle immagini img1.png e img2.png.




# #vedo maschera della varianza
# var = ndi.generic_filter(x1, np.var, (4,4))
# plt.figure('Im1 - VAR')
# plt.imshow(var, clim=None, cmap='gray')



# var_med = ndi.median_filter(var, (10,10))

# var_med = var_med <10
# var_med = morph.binary_erosion(var_med, morph.rectangle(3,3))
# plt.figure('VAR ELABORATA')
# plt.imshow(var_med , clim=None, cmap='gray')

# #vedo maschera della varianza
# var = ndi.generic_filter(x2, np.var, (4,4))
# plt.figure('Im2 - VAR')
# plt.imshow(var, clim=None, cmap='gray')


# var_med = ndi.median_filter(var, (10,10))
# plt.figure('VAR ELABORATA (2)')
# plt.imshow(var_med <10, clim=None, cmap='gray')























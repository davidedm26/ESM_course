# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 15:44:26 2025

@author: david
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

##rappresentazione in falsi colori
plt.close()

R = io.imread('../Immagini/Washington_red.tif')
G = io.imread('../Immagini/Washington_green.tif')
B = io.imread('../Immagini/Washingyon_blue.TIF')
I = io.imread('../Immagini/Washington_infrared.tif')

# plt.figure(); plt.imshow(x);
z= np.stack((I,G,B), -1)
y = np.stack((R,G,B) , -1)

k = ndi.generic_filter( R, np.std, (10,10))

# plt.figure()
# plt.imshow(y)


# Crea il plot con due immagini affiancate
fig, axes = plt.subplots(1, 3, figsize=(10, 5))  # 1 riga, 2 colonne

axes[0].imshow(y)
axes[1].imshow(z)
axes[2].imshow(k)




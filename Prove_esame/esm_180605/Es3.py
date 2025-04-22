# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 08:54:52 2025

@author: david
"""

# Es3
# Si vuole segmentare l'immagine delle cellule cells.png. Realizzate tutte le operazione che
# ritenete necessarie (includendo eventuali operazioni morfologiche) per ottenere la mappa binaria di
# segmentazione in cui si evidenziano solo i bordi delle cellule presenti.
# In fine, provate a determinare due mappe binarie: una in cui sono identificate solo le cellule piu
# scure e l'altra con le cellule piu chiare.

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io
import skimage.morphology as morph

plt.close('all')

x = np.float64(io.imread('./immagini/cells.png'))
x = x[:,:,0]
plt.figure('input')
plt.imshow(x, clim=[0,255], cmap='gray')

mask = x > 45
plt.figure('mask')
plt.imshow(mask, clim=[0,1], cmap='gray')

#estraggo bordi con gradiente morfologico
dil = morph.dilation(mask, morph.disk(3))
ero = morph.erosion(mask, morph.disk(3))
edges = dil ^ ero
plt.figure('Edges')
plt.imshow(edges, clim=[0,1], cmap='gray')

edges = morph.closing(edges, morph.rectangle(3,3))
edges = morph.thin(edges)
plt.figure('Edges dopo morfologiche')
plt.imshow(edges, clim=[0,1], cmap='gray')

#azzero elementi fuori dal bordo
x[~mask] = 0
plt.figure('x isolato')
plt.imshow(x, clim=[0,255], cmap='gray')


# #immagine delle varianze
# var = ndi.generic_filter(x, np.var, (3,3))
# plt.figure('varianze e medie')
# plt.subplot(1,2,1)
# plt.imshow(var, clim=[0,255], cmap='gray')

# # #immagine delle medie
# means = ndi.generic_filter(x, np.mean, (3,3))
# plt.subplot(1,2,2)
# plt.imshow(means, clim=[0,255], cmap='gray')

chiare = x > 170
plt.figure('chiare')
plt.imshow(chiare, clim=[0,1], cmap='gray')

chiare = morph.binary_opening(chiare, morph.disk(3))
plt.figure('chiare opening')
plt.imshow(chiare, clim=[0,1], cmap='gray')

# dilation iterativa per prendere l'intre cellula
b = morph.disk(1)
for i in range(100):
    chiare = morph.binary_dilation(chiare, b) & mask

plt.figure('chiare dilation')
plt.imshow(chiare, clim=[0,1], cmap='gray')

scure = mask ^ chiare
plt.figure('scure')
plt.imshow(scure, clim=[0,1], cmap='gray')

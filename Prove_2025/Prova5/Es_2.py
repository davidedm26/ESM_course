# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 17:29:08 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col


#Esercizio in classe proposto dalla prof
#Prendere immagine '/immagini_lab_morfologia/cells.tif' e fare le operazioni per evidenziare i contorni delle cellule
#e mappare in due mappae cellule scure e cellule chiare

# EX. 3 Si vuole segmentare l'immagine delle cellule cells.png. Realizzate tutte le operazione che
# ritenete necessarie (includendo eventuali operazioni morfologiche) per ottenere la mappa binaria di
# segmentazione in cui si evidenziano solo i bordi delle cellule presenti.
# In fine, provate a determinare due mappe binarie: una in cui sono identificate solo le cellule piu
# scure e l'altra con le cellule piu chiare.

plt.close('all')
x= np.float64(io.imread('../Immagini/cells.png'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')


 
#evidenziare i contorni tramite laplaciano
# h = np.array([[0,1,0],[1,-5,1],[0,1,0]])
# y = np.copy(x)
# # y= ndi.correlate(x,h)
# y_max=np.max(y)
# y_min = np.min(y)
# y = 255*(y - y_min)/ (y_max- y_min)
# plt.figure('x - laplaciano')
# plt.imshow(y, clim=None, cmap='gray')

# x = ndi.median_filter(x ,(3,3))*255
y =  x > 17
plt.figure('x - laplaciano median filter')
plt.imshow(y, clim=None, cmap='gray')

from sklearn.cluster import k_means
d = np.reshape(y, (-1,1))
centroid, idx, sum_var = k_means(d,3)
y1 = np.reshape(idx, x.shape)
plt.figure('k_means')
plt.imshow(y1, clim=None, cmap='gray')



# mask = x>48
# x = x*mask
# plt.figure(2)
# plt.imshow(x, clim=[0,1], cmap='gray')
# plt.title('mask')

# b=morph.rectangle(10,10)
# y = morph.binary_opening(x,b)

# plt.figure(3)
# plt.imshow(y, clim=None, cmap='gray')
# plt.title('mask ripulita')

# b=morph.rectangle(3,3)
# y_ero= morph.binary_erosion(y,b)
# y_dil= morph.binary_dilation(y,b)
# y = y_dil ^ y_ero
# plt.figure(4)
# plt.imshow(y, clim=None, cmap='gray')
# plt.title('Gradiente morfologico')

 #Punto 2
# b = morph.disk(20)
# y = morph.opening(x,b)
# plt.figure(5)
# plt.imshow(y, clim=None, cmap='gray')
# plt.title('Opening')

# plt.figure(6)
# plt.imshow(x-y, clim=None, cmap='gray')
# plt.title('x-Opening')






# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 12:11:52 2025

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
x= np.float64(io.imread('../Immagini/cells.png'))/255
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')


x = col.rgb2gray(x[:,:,0:3])*255
#evidenziare i contorni 
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
b = morph.disk(20)
y = morph.opening(x,b)
plt.figure(5)
plt.imshow(y, clim=None, cmap='gray')
plt.title('Opening')

plt.figure(6)
plt.imshow(x-y, clim=None, cmap='gray')
plt.title('x-Opening')






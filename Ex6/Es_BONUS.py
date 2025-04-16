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

plt.close('all')
x= np.float64(io.imread('../Immagini/cells.png'))/255
plt.figure(1)
plt.imshow(x, clim=[0,1], cmap='gray')


z = col.rgb2gray(x[:,:,0:3])*255
#evidenziare i contorni 

plt.figure(2)
plt.imshow(z, clim=None, cmap='gray')

y = z >20
plt.figure(3)
plt.imshow(y, clim=None, cmap='gray')

b=morph.rectangle(3,3)
y_erosed = morph.binary_erosion(y,b)
plt.figure(4)
plt.imshow(y_erosed, clim=None, cmap='gray')

y_contorno = y ^ y_erosed
plt.figure(5)
plt.imshow(y_contorno, clim=None, cmap='gray')
plt.title('contorno')

#kmeans al momento possiamo usarlo solo sui grigi o sul colore
from sklearn.cluster import k_means
d = np.reshape(z, (-1, 1)) #reshape in -1,1 perchè mi restituisce un vettore
K=3
centroid, idx, sum_var = k_means(d, K) #k è il numero di classi
y = np.reshape(idx, z.shape)

plt.figure(6); plt.imshow(y, clim=[0,K-1], cmap='jet')
plt.title('output')

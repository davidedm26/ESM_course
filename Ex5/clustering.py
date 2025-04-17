# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:40:58 2025

@author: david
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from sklearn.cluster import k_means

x= np.float64(io.imread('../Immagini/granelli_riso.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

#kmeans al momento possiamo usarlo solo sui grigi o sul colore
d = np.reshape(x, (-1, 1)) #reshape in -1,1 perchè mi restituisce un vettore
#equivale a fare reshape(X, (M*N,1))

K=2 #k lo fisso io
#k means come input non vuole una matrice ma vuole un vettore
centroid, idx, sum_var = k_means(d, K) #k è il numero di classi

y = np.reshape(idx, x.shape)
plt.figure(2); plt.imshow(y, clim=[0,K-1], cmap='jet')
plt.title('output')

# plt.close('all')

# x= io.imread('../Immagini/Fiori256.bmp')
# plt.figure(3)
# plt.imshow(x)

# M,N,L = x.shape
# K=6
# d = np.reshape(x, (M*N, L)) #a colori usa la terza dimensione di X nel reshape
# centroid, idx, sum_var = k_means(d, K)
# y = np.reshape(idx, x.shape[:-1])

# plt.figure(4); plt.imshow(y, clim=[0,K-1], cmap='jet')
# plt.title('output')











# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:16:03 2025

@author: david

"""
##uso delle statistiche locali
#vogliamo enfatizzare la parte nascosta del filamento
#usa generic filter sui blocchi 3x3
#la media locale deve essere bassa rispetto alla media globale (vedi parametri dati)
#la varianza deve essere      rispetto alla varianza globale (vedi paramtri dati)

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

x= io.imread( '../immagini/filamento.jpg')

x = np.float64(x)

med = np.mean(x) ##media glob
# var= np.var(x)
dev = np.std(x) ##dev glob


# plt.subplot(1,2,1); plt.imshow(med, clim=[0,255], cmap='gray')
# plt.subplot(1,2,2); plt.imshow(dev, clim=[0,255], cmap='gray')


K=3

MED = ndi.generic_filter(x, np.mean, (K,K))
# VAR = ndi.generic_filter(x, np.var, (K,K))
DEV = ndi.generic_filter(x, np.std, (K,K))

mask =  (MED<=0.4*med) &  (DEV<= 0.4*dev) & ( DEV>= 0.02*dev) #calcola maschera

plt.figure(2)
plt.imshow(mask, clim=[0,1], cmap='gray')


y = mask*(4*x) + (1-mask)*x
plt.figure(3)
plt.imshow(y, clim=None, cmap='gray')


#metodo alternativo
y = np.copy(x)
y[mask] = 10*x[mask]
plt.figure(4)
plt.imshow(y, clim=None, cmap='gray')




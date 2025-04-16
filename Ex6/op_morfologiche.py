# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:21:14 2025

@author: david
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
from sklearn.cluster import k_means

x= np.float64(io.imread('../Immagini/granelli_riso.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

b = morph.disk(7)

plt.figure()
plt.imshow(b, clim=None, cmap='gray') #non servono tag
plt.title('Elemento strutturante')


#OPENING E CLOSING
#Rimuovere oggetti piccoli mantenedo le dimensioni degli oggetti piu grandi

plt.close('all')
x= np.float64(io.imread('../Immagini/immagini_lab_morfologia/circbw_bool.tif'))
plt.figure(1)
plt.imshow(x, clim=[0,1], cmap='gray')

s = morph.rectangle(40,30)
z = morph.binary_erosion(x,s)
y = morph.binary_dilation(z,s)

plt.figure(2)
plt.imshow(y, clim=[0,1], cmap='gray')


#ESTRAZIONE DEI BORDI
#Possiamo estrarre i bordi attraverso l'erosione (erosione e differenza con immagine originale) 
#+ dilatazione per aumentare spessore della linea ottenuta
plt.close('all')
x= np.float64(io.imread('../Immagini/immagini_lab_morfologia/volto_bool.tif'))
plt.figure(1)
plt.imshow(x, clim=[0,1], cmap='gray')

b= morph.disk(2)
y = morph.erosion(x,b)
y = x - y
y = morph.dilation(y, b)
plt.figure(2)
plt.imshow(y, clim=[0,1], cmap='gray')

# Trasformazione Hit-or-Miss
plt.close('all')
x= np.float64(io.imread('../Immagini/immagini_lab_morfologia/quadrati_bool.tif'))
plt.figure(1)
plt.imshow(x, clim=[0,1], cmap='gray')

S1 = np.array([[0,0,0],
               [0,1,1],
               [0,1,0]], np.bool)
S2 = np.array([[1,1,1],
               [1,0,0],
               [1,0,0]], np.bool)

C1 = morph.binary_erosion(x,S1)
C2 = morph.binary_erosion(np.logical_not(x),S2)
C = np.logical_and(C1,C2)

plt.figure(2)
plt.imshow(C, clim=[0,1], cmap='gray')

#Thinning e Skeletonization
y = morph.thin(x,np.inf)
plt.figure(3)
plt.imshow(y, clim=[0,1], cmap='gray')

y = morph.skeletonize(x)
plt.figure(4)
plt.imshow(y, clim=[0,1], cmap='gray')

# Applicate questa operazione sempre all’immagine dell’impronta digitale e confrontate il risultato ottenuto con
# la procedura di thinning
plt.close('all')
x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/impronta_bool.tif'))
plt.figure(1)
plt.imshow(x, clim=[0,1], cmap='gray')
plt.title('input')

y = morph.thin(x,np.inf)
plt.figure(2)
plt.imshow(y, clim=[0,1], cmap='gray')

##########################################################
#Immagini su scala di grigio
# Provate a realizzare l’erosione dell’immagine circuito.tif con un disco di raggio 2
plt.close('all')
x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/circuito.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

b= morph.disk(2)
y = morph.erosion(x,b)

y = x - y

# y = morph.thin(x,np.inf)
plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')


#Smoothing morfologico
plt.close('all')
x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/supernova.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

#provo apertura per rimuovere piccoli rumori brillanti
b = morph.disk(5)
y = morph.opening(x, b)

y = morph.closing(x,b)

plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')

# Gradiente morfologico
plt.close('all')
x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/vista_aerea.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

b = np.ones((3,3))

y = morph.erosion(x,b)
plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')
plt.title('erosion')

z = morph.dilation(x,b)
plt.figure(3)
plt.imshow(y, clim=None, cmap='gray')
plt.title('dilation')

y = z - y
plt.figure(4)
plt.imshow(y, clim=None, cmap='gray')
plt.title('dilation - erosion')

# Trasformazioni top-hat e bottom-hat
# plt.close('all')
# x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/granelli_riso.tif'))
# plt.figure(1)
# plt.subplot(1,2,1)
# plt.imshow(x, clim=None, cmap='gray')
# plt.title('input')

# #provo k-means
# d = np.reshape(x, (-1,1))
# centroid, idx, sum_var = k_means(d, 2)
# y = np.reshape(idx, x.shape)
# plt.subplot(1,2,2)
# plt.imshow(y, clim=None, cmap='gray')
# plt.title('input')

# #Per regolarizzare lo sfondo
# b = morph.disk(40)
# z = morph.opening(x,b)
# plt.figure(2)
# plt.imshow(z , clim=None, cmap='gray')
# plt.title('opening')

# plt.figure(3)
# plt.subplot(1,2,1)
# plt.imshow( x - z , clim=None, cmap='gray')
# plt.title('x - opening')

# #riprovo k-means

# d = np.reshape(x-z, (-1,1))
# centroid, idx, sum_var = k_means(d, 2)
# y = np.reshape(idx, x.shape)
# plt.subplot(1,2,2)
# plt.imshow(y, clim=None, cmap='gray')
# plt.title('input')

# Segmentazione di regioni con texture tramite operazioni morfologiche
plt.close('all')
x= np.float64(io.imread('../Immagini//immagini_lab_morfologia/blob.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

#Faccio closing (perchè ho elementi nero su bianco) con disk maggiore dei dischi piccoli
plt.figure(2)
b = morph.disk(30)
y = morph.closing(x,b)
plt.imshow(y, clim=None, cmap='gray')
plt.title('closing')

#Faccio apertura con disco maggiore della distanza dei cerchi
plt.figure(3)
b = morph.disk(60)
z = morph.opening(y,b)
plt.imshow(z, clim=None, cmap='gray')
plt.title('opening')

#voglio ottenere solo la linea di separazione, faccio gradiente morfologico
b = morph.rectangle(3, 3)
z_er = morph.erosion(z,b)
z_de = morph.dilation(z,b)
z = z_de - z_er
plt.figure(4)
plt.imshow(z, clim=None, cmap='gray')
plt.title('linea')




















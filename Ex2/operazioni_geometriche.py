# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 11:22:23 2025

@author: david
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import bitop as bo
import mylib as ml
from skimage.transform import rescale
from skimage.transform import warp, rotate

# Le operazioni geometriche consentono di ottenere, a partire da un’immagine x una nuova immagine y nella
# quale non si modificano i valori di luminosit`a, ma solo la posizione dei pixel.

#Ridimensionamento
x = ml.leggiJpeg('../immagini/dorian.jpg')
ml.showImage(x, 'dorian')

y = x[::2 , ::2]
ml.showImage(y, 'dorian decimato per 2')

#interpolazione
z = rescale(x, 2/4, order=3)
ml.showImage(z, "interpol")

plt.close('all')

#trasformazione affine tramite matrice

# x= np.float32(io.imread('../immagini/lena.jpg'))
# x = x[252:277,240:290];
# M,N = x.shape

# ml.showImage(x, 'occhio')

# #definisco matrice M
# T = np.array([[0.5,0,0],[0,0.5,0],[0,0,1]], dtype=np.float32)
# #ricavo A per warp
# A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta

# y1 = warp( x, A, output_shape=(2*M,N*2), order=1)
# ml.showImage(y1, 'interpolazione nearest')

x= np.float32(io.imread('../immagini/lena.jpg'))
T = np.array([[0.5,0,0],[0,0.5,0],[0,0,1]], dtype=np.float32)
A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta

plt.subplot(1,2,1)
plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('nput')
y1 = warp( x, A, order=1)
plt.subplot(1,2,2)
plt.imshow(y1, clim=[0,255], cmap='gray'); plt.title('zoom')

plt.close('all')
#provo traslazione

T = np.array([[1,0,0],[0,1,0],[100,45.6,1]], dtype=np.float32)
A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta

plt.subplot(1,2,1)
plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('nput')
y1 = warp( x, A, order=1)
plt.subplot(1,2,2)
plt.imshow(y1, clim=[0,255], cmap='gray'); plt.title('trasl')

plt.close('all')
#provo rotazione
theta= np.pi/3

T = np.array([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),0],[0,0,1]], dtype=np.float32)
A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta

plt.subplot(1,2,1)
plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('nput')
y1 = warp( x, A, order=1)
plt.subplot(1,2,2)
plt.imshow(y1, clim=[0,255], cmap='gray'); plt.title('trasl')


#voglio ruotare immagine rispetto al centro
#voglio prima ruotare e poi traslare

plt.close('all')
#provo rotazione
theta= -np.pi/3

T1 = np.array([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),0],[0,0,1]], dtype=np.float32)
T2 = np.array([[1,0,0],[0,1,0],[100,45.6,1]], dtype=np.float32)
T= T2@T1
A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta

plt.subplot(1,2,1)
plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('nput')
y1 = warp( x, A, order=1)
plt.subplot(1,2,2)
plt.imshow(y1, clim=[0,255], cmap='gray'); plt.title('trasl')

plt.close('all')

y = rotate(x, 90.0)
plt.imshow(y, clim=[0,255], cmap='gray'); plt.title('rotazione')





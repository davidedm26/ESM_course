# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 16:58:01 2025

@author: david
"""

import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml
from skimage.transform import warp

# Liveness detection. Per scoprire se un’impronta digitale `e autentica o contraffatta si pu`o operare nel
# dominio di Fourier, calcolando la frazione di energia contenuta alle medie frequenze, e dichiarando
# l’immagine autentica se tale frazione supera una certa soglia.

#Visualizzo Immagine input
x = io.imread('../immagini/impronta1.tif')
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(x,clim=None,cmap='gray')
plt.title('Immagine input 1')

x2 = io.imread('../immagini/impronta2.tif')
plt.subplot(1,2,2)
plt.imshow(x2,clim=None,cmap='gray')
plt.title('Immagine input 2')

#calcolo DFT2
X = np.abs(np.fft.fft2(x))

#mostra trasformata
plt.figure(2)
plt.imshow(np.log(1+X),clim=None,cmap='gray')
plt.title('Immagine trasformata')

#filtraggio in frequenza
M,N  = x.shape
n= np.fft.fftfreq(N)
m= np.fft.fftfreq(M)
l,k= np.meshgrid(n,m)

r1=0.10
r2=0.25
H = ( np.abs(l) <= r2) & ( np.abs(l) >= r1)  & ( np.abs(k) <= r2)  & ( np.abs(k) >= r1) 

#Visualizzo mask e immagine filtrata in frequenza
plt.figure(3)
plt.subplot(1,2,1)
plt.imshow(H,clim=None,cmap='gray')
plt.title('Mask')

Y = X * H;

plt.subplot(1,2,2)
plt.imshow(Y,clim=None,cmap='gray')
plt.title('Immagine filtrata')

#Valuta Energia per frequenze medie
Em = np.sum(Y**2)/np.sum(H)
E = np.sum(X**2)

print(Em)
print(E)
print(Em/E)


























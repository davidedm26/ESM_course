# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 11:49:51 2025

@author: utente
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col


plt.close('all')
x= np.float64(io.imread('../Immagini/barbara.jpg'))
x = np.mean(x , -1)
#aggiungo rumore gaussiano
M,N = x.shape
noisy = x + 20*np.random.randn(M,N)
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(noisy, clim=[0,255], cmap='gray')
plt.title('Immagine di input')

plt.subplot(1,2,2)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.title('Immagine di originale')

def elab(x, sigma):
    dim = np.size(x)
    x_c = x[dim//2]
    mask =  (x > (x_c - 2*sigma)) & ( x < (x_c + 2*sigma))
    print(x_c)
    if (np.sum(mask) >= 4):
        y = np.mean(x[mask])
    else:
        y = np.mean(x)
    return y

def filtro_sigma(x, K, sigma): 
    #calcola maschera dei valori della finestra da considerare
    mask = ndi.generic_filter(x, elab, (K,K), extra_arguments=((sigma,)))
    return mask

y = filtro_sigma(noisy,7,20)
plt.figure(2)
plt.imshow(y, clim=[0,255], cmap='gray')
plt.title('Immagine di output')

#Salto ultimo punto poichè è semplice
#calcola psnr
#mse = np.mean(originale-filtrata**2)
#10*log10(255**2/mse)
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 10:59:22 2025

@author: david
"""

#ES3
import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import matplotlib.pyplot as plt


plt.close('all')
y0=np.float32(io.imread('./Immagini/lenaB.png'))
plt.figure('lenaB')
plt.imshow(y0, clim=None, cmap='gray')

x=np.float32(io.imread('./Immagini/lenaA.png'))
plt.figure('lenaA')
plt.imshow(x, clim=None, cmap='gray')

th = -30
THETAS = np.arange(5,361, 5 )
print(THETAS)

#calcolo immagine y, versione ruotata di theta gradi di y0
from skimage.transform import warp, rotate

max = []

for th in THETAS:
    # th = np.deg2rad(th)
    #matrice di trasformazione per la rotazione
    # A = np.array([
    #     [np.cos(th),np.sin(th),0],
    #     [-np.sin(th),np.cos(th),0],
    #     [0,0,1]
    #     ], dtype=np.float32)
    
    # y = warp(y0, A, order=1)
    y = rotate(y0, th, resize=True)  # resize=True mantiene tutta l'immagine
    
    plt.figure(f'lenaB ruotata di {th}')
    plt.imshow(y, clim=[0,255], cmap='gray')
    
    #calcolo mutua correlazione nel dominio della frequenza
    from numpy import fft
    M1,N1 = x.shape
    M2,N2 = y.shape
    shape = (M1+M2-1, N1+N2-1)
    X = fft.fftshift(fft.fft2(x, shape))
    Y = fft.fftshift(fft.fft2(y, shape))
    
    R = X * np.conj(Y)
    r = np.real(fft.ifft2 ( fft.ifftshift(R)))
    
    M = np.max(r)
    
    max.append(M)
        
#mostro il grafico di M in funzione di theta

plt.figure('plot')
plt.plot(THETAS,max)
plt.xlabel('theta')
plt.ylabel('Rxy')

maxR= np.max(max) #massimo dei massimi
idx = np.argmax(max) #indice del massimo dei massimi
th_opt= THETAS[idx]










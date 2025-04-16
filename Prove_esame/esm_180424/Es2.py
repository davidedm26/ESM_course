# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 17:23:13 2025

@author: david
"""

#filtraggio in frequenza


import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi


x = np.fromfile('./im_180424/rumorosa.y', dtype= np.float32)
x = np.reshape(x, (380,572))
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.title('input')

X = np.fft.fftshift(np.fft.fft2(x))
plt.figure(2)
plt.imshow(np.log( 1 + np.abs(X))>10, clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('trasformata')

M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)

D=0.007
#genero filtro
filtro =1 - ( ( np.sqrt(k**2 + (l+0.1)**2) < D ) + ( np.sqrt(k**2 + (l-0.1)**2) < D ) )

plt.figure(3)
plt.imshow(filtro, clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('filtro')

#applico filtraggio
Y = X*filtro

Y = np.fft.ifftshift(Y)
y = np.real(np.fft.ifft2(Y))

#mostro risultato
plt.figure(4)
plt.imshow(y, clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('output')

#calcolo PSNR tra filtrata e originale
mse = np.mean( (x-y)**2 )
psnr = 10*np.log10(255**2/mse)

# def filtra_freq(x):
    














# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 09:57:55 2025

@author: david
"""

# Filtraggio in frequenza. Data l’immagine foto originale.tif, si vuole realizzare il filtraggio dell’immagine
# nel dominio della frequenza mediante il seguente filtro:
# H(μ, ν) =   1 |μ| ≤ 0.10 ,|ν| ≤ 0.25,
#             0 altrimenti
# Scrivete il codice relativo e mostrate l’immagine filtrata.

import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

x = io.imread('../immagini/foto_originale.tif')
plt.figure(1)
plt.imshow(x)
plt.title('input')

x = np.float64(x)/255
r = x[:,:,0]
g = x[:,:,1]
b = x[:,:,2]

R = np.fft.fftshift(np.fft.fft2(r))
plt.figure(2)
plt.title('spettro')
plt.imshow(np.log(1+np.abs(R)), clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])

M,N = R.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)

H = ((np.abs(l)<=0.10) & (np.abs(k)<=0.25))
# H = np.expand_dims(H, -1)
plt.figure(3)
plt.title('Filtro in freq')
plt.imshow(H, clim=[0,1], cmap='gray', extent=[-0.5,0.5,-0.5,0.5])

YR = R*H
YR = np.fft.ifftshift(YR)
yr = np.real(np.fft.ifft2(YR))*255
plt.figure(4)
plt.subplot(1,2,1)
plt.title('componente r')
plt.imshow(r, clim=[0,1], cmap='gray');
plt.subplot(1,2,2)
plt.title('componente r filtrata')
plt.imshow(yr, clim=[0,255], cmap='gray');

G = np.fft.fftshift(np.fft.fft2(g))
YG = G*H
YG = np.fft.ifftshift(YG)
yg = np.real(np.fft.ifft2(YG))*255

B = np.fft.fftshift(np.fft.fft2(b))
YB = B*H
YB = np.fft.ifftshift(YB)
yb = np.real(np.fft.ifft2(YB))*255

y = np.stack((yr,yg,yb),-1) /255
plt.figure(5)
plt.title('Filtraggio delle 3 componenti')
plt.imshow(y);

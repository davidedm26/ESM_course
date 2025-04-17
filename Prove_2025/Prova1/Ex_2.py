# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 17:16:07 2025

@author: david
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import random_noise
import scipy.ndimage as ndi
import skimage.color as clr

#Ex2
#Mostro input
x =io.imread('../immagini/pears_noise.png')/255
plt.figure(1)
plt.title('input')
plt.imshow(x)

#filtro in frequenza la componente di luminanza
#Ricavo Luminanza
y = clr.rgb2yuv(x)
y_l = y[:,:,0]
plt.figure(2)
plt.title('componente di luminanza')
plt.imshow(y_l, clim=None, cmap='gray')

Y = np.fft.fftshift ( np.fft.fft2(y_l))
#mostro spettro
plt.figure(3)
plt.title('componente di luminanza in frequenza')
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])

#filtro in frequenza notchano i due picchi sulla diag.secondaria
M,N = y_l.shape
m = np.fft.fftshift( np.fft.fftfreq(M))
n = np.fft.fftshift( np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)

d=0.1
r=0.04
h1 = (l+d)**2 + (k-d)**2 < r**2
h2 = (l-d)**2 + (k+d)**2 < r**2
h = 1 - (h1 + h2)
#mostro filtro realizzato
plt.figure(4)
plt.title('filtro realizzato')
plt.imshow(h, clim=[0,1], cmap='gray', extent=[-0.5,0.5,-0.5,0.5])

#mostro spettro filtrato
Z = Y * h
plt.figure(5)
plt.title('filtraggio effettuato')
plt.imshow(np.log(1+np.abs(Z)), clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])

#risultato spaziale del filtraggio
Z = np.fft.ifftshift(Z)
z = np.real(np.fft.ifft2(Z))
plt.figure(6)
plt.title('risultato del filtraggio nello spazio')
plt.imshow(z, clim=None, cmap='gray')

#mostro immagine originale
ori =io.imread('../immagini/pears.png')/255
plt.figure(8)
plt.title('originale')
plt.imshow(ori)

#riporto in RGB
y[:,:,0]= z
y_rgb = clr.yuv2rgb(y)
plt.figure(7)
plt.title('output senza rumore')
plt.imshow(y_rgb)

#calcolo errore quadratico medio tra filtrata e originale
mse = np.mean( (ori-y_rgb)**2 )
print(mse)

#Realizzo Enhancement per sistemare colori spenti
blue = y_rgb[:,:,2]
blue = blue**2
y_rgb[:,:,2] = blue
plt.figure(9)
plt.title('Enhanced')
plt.imshow(y_rgb)

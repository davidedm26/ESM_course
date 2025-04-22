# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 18:06:09 2025

@author: david
"""


import skimage.io as io
import skimage.exposure as exp
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import skimage.color as col

#rimozione del pattern di Moire
plt.close('all')
x = io.imread('./immagini/volto.png')
x = x[:,:,0:3]
x = col.rgb2gray(x)
x= np.float64(x)
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

#passo al dominio della frequenza
from numpy import fft
X = fft.fftshift( fft.fft2(x))

plt.figure(2)
plt.imshow(np.log(1 + np.abs(X)), clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('Spettro')

#rimuovo conchiglie
M,N = x.shape
m = fft.fftshift(fft.fftfreq(M))
n = fft.fftshift(fft.fftfreq(N))
l,k = np.meshgrid(n,m)

m1 =  (l<-0.34) & ((l>-0.38)) & ( k > - 0.02) & ( k <  0.022)
m2 =  (l>0.34) & ((l<0.38)) & ( k > - 0.02) & ( k <  0.022)
m3 = (l<-0.14) & ((l>-0.18)) & ( k > - 0.02) & ( k <  0.022)
m4 =  (l>0.14) & ((l<0.18)) & ( k > - 0.02) & ( k <  0.022)
m5 =  ((k>0.1)&(k<0.2))+ ((k>0.3)&(k<0.4)) + ((k<-0.1)&(k>-0.2))+ ((k<-0.3)&(k>-0.4)) & (np.abs(l)<0.008)

m = 1 - (m1+m2+m3+m4+m5)
plt.figure(3)
plt.imshow(m, clim=[0,1], cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('mask')

Y = X*m

y = np.real(fft.ifft2(fft.ifftshift(Y)))
plt.figure(4)
plt.imshow(y, clim=None, cmap='gray')
plt.title('output')

#valuto energia alle medie frequenze
r1 = 0.1
r2 = 0.2
omega = ( ((l**2+k**2) >= r1) & ((l**2+k**2) <= r2) )
plt.figure(5)
plt.imshow(omega, clim=[0,1], cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('omega mask')

Ex = np.mean( np.abs(X[omega])**2 )
Ey = np.mean( np.abs(Y[omega])**2 )


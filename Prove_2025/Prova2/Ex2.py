# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:59:47 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col

plt.close('all')
x= io.imread('../Immagini/fiori.jpg')

X = np.fft.fft2(x)

plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.title('Immagine di input')

def filtro(x,B):
    #progetto filtro passa banda ideale
    M,N = x.shape[:2]
    m = np.fft.fftshift(np.fft.fftfreq(M))
    n = np.fft.fftshift(np.fft.fftfreq(N))
    l,k = np.meshgrid(n,m)
    
    ni_0 = 0.25
    mu_0 = 0.25
    # B = 0.15
    
    f1 = ((l - ni_0)**2 + (k - mu_0)**2 < B**2) 
    f2 = ((l + ni_0)**2 + (k - mu_0)**2 < B**2) 
    f3 = ((l - ni_0)**2 + (k + mu_0)**2 < B**2) 
    f4 = ((l + ni_0)**2 + (k + mu_0)**2 < B**2) 
    filtro =1 - ( f1+f2+f3+f4 )
    
    # plt.figure(2)
    # plt.imshow(filtro , clim=[0,1], cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
    # plt.title('Filtro')
    
    #applico filtraggio all'immagine di input sulle 3 componenti
    # r,g,b = x[:,:,0],x[:,:,1],x[:,:,2]
    # R = np.fft.fftshift(np.fft.fft2(r))
    # G = np.fft.fftshift(np.fft.fft2(g))
    # B = np.fft.fftshift(np.fft.fft2(b))
    
    # YR = R*filtro
    # YG = G*filtro
    # YB = B*filtro
    
    # yr = np.real(np.fft.ifft2(np.fft.ifftshift(YR)))
    # yg = np.real(np.fft.ifft2(np.fft.ifftshift(YG)))
    # yb = np.real(np.fft.ifft2(np.fft.ifftshift(YB)))
    
    # y = np.stack((yr,yg,yb),-1)
    
    #provo a lavorare con le 3 componenti insieme
    X = np.fft.fftshift(np.fft.fft2(x))
    
    filtro = np.expand_dims(filtro, -1)
    Y = X*filtro
    y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))/255
    # print(np.max(y))
    
    # plt.figure(3)
    # plt.imshow(y)
    # plt.title('Risultato del Filtraggio')
    return y

snr = []
b = [0.05,0.10,0.15,0.20]

for i in b :
    y = filtro(x,i)
    mse = np.mean((x-y)**2)
    var = np.var(x)
    SNR = 10*np.log10(var/mse)
    # SNR = 10*np.log10(np.var(x)/np.var(np.abs(x-y)))
    snr.append(SNR)
    
plt.figure(5)
plt.plot(b,snr)
plt.xlabel('BANDE DI FILTRAGGIO')
plt.ylabel('SNR')            
plt.tight_layout()











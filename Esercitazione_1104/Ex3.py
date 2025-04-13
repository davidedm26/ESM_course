# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 18:43:27 2025

@author: david
"""

"""
Esercizio 3
Si vuole scoprire quale macchina fotografica, fra due disponibili, ha scattato una data
fotografia (identificazione di sorgente).
"""

import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

def test(x):
     #ritagliare sezione in alto a sx
    M,N = (512,512)
    y = x[:M, :N]
    plt.subplot(1,2,2)
    plt.imshow(y,  clim = [0,255], cmap='gray')
    
    #Calcolo delle feature
    #Estraggo bitplane 2
    from bitop import bitget
    B2 = bitget( np.uint16(y),1)
    B2 = np.float64(B2)
    # plt.figure(2)
    # plt.subplot(1,2,1)
    # plt.imshow(B2,  clim = [0,1], cmap='gray')
    
    sum = 0;
    for i in range (2,M):
        for j in range (1,N):
            temp = B2[i-1][j] - B2[i][j]
            sum += np.abs(temp)
    f1 = sum/ ((M-1)*(N))
    
    sum = 0;
    for i in range (1,M):
        for j in range (2,N):
            temp = B2[i][j-1] - B2[i][j]
            sum += np.abs(temp)
    f2 = sum/ ((M)*(N-1))
    
    #Applico filtro gaussiano 3x3 all'originale
    z = ndi.gaussian_filter(y, 0.5)
    
    #Calcola DFT di x e z
    X = np.fft.fft2(y)
    Z = np.fft.fft2(z)
    
    #ricava f3 e f4
    mse_abs = np.mean( (np.abs(X)-np.abs(Z))**2 )
    mse_pha = np.mean( (np.angle(X)-np.angle(Z))**2 )
    
    f3 = 10*np.log10(mse_abs)
    f4 = 10*np.log10(mse_pha)

    f = 0.7*f1 + 1.5*f2 + 0.01*f3 + 0.001*f4
    
    if f > 1.5 :
        return 1
    else:
        return 2
    
#leggi immagine
x = io.imread("4.png")
x = np.float64(x)

#mostra immagine
# plt.figure(1)
# plt.subplot(1,2,1)
# plt.imshow(x,  clim = [0,255], cmap='gray')

print(test(x))














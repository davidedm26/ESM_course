# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 15:06:38 2025

@author: david
"""

#EX1

import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from bitop import bitget, bitset

plt.close('all')
f = np.fromfile('../Immagini/firma.y', dtype=np.uint8)
f = np.reshape(f, (256,512))
plt.figure('firma')
plt.imshow(f, cmap='gray', clim=[0,1])

x = np.fromfile('../Immagini/upupa.y', dtype=np.uint8)
x = np.reshape(x, (256,512))
plt.figure('Input')
plt.imshow(x, cmap='gray', clim=[0,255])

#inserisco firma
y = bitset(x, 1, f)

#verifico inserimento
x_1 = bitget(y, 1)
plt.figure('Bitplane 6 di pupa')
plt.imshow(x_1, cmap='gray', clim=[0,1])


plt.figure('Output (inserita firma)')
plt.imshow(y, cmap='gray', clim=[0,255])

#verifico robustezza operazione
#comprimo immagine marcata in jpeg, estraggo firma e la confronto con quella originale
MSE = []
Quality = [80,90,100]
for Q in Quality:
    filename= 'q'+ str(Q) + '.jpg'
    io.imsave(filename, y, quality=Q ) #compressione
    z = io.imread(filename)
    b1 = bitget(z, 1)#estrazione bitplane 1
    mse = np.mean( (b1-f)**2) #calcolo mse fra b1 e f
    MSE.append(mse)

#visualizzo variazione MSE su grafico
print(MSE)
plt.figure('Grafico MSE')
plt.plot(Quality, MSE)
plt.xlabel('quality')
plt.ylabel('mse')

#VALUTO ROBUSTEZZA AL FILTRAGGIO
from numpy import fft
MSE2 = []
Cut_off = [0.2,0.3,0.4]
for D in Cut_off:
    x = np.copy(y)
    X = fft.fftshift(fft.fft2(x))
    
    M,N = x.shape
    m = fft.fftshift(fft.fftfreq(M))
    n = fft.fftshift(fft.fftfreq(N))
    l,k = np.meshgrid(n,m)
    
    H = l**2 + k**2 < D**2
    # plt.figure('Filtro ideale')
    # plt.imshow(H, cmap='gray', clim=[0,1], extent=[-0.5,0.5,-0.5,0.5])
    
    Y = X*H
    y = np.uint8(np.real(fft.ifft2 ( fft.ifftshift(Y))))
    
    # plt.figure('Risultato filtraggio')
    # plt.imshow(y, cmap='gray', clim=[0,255])
    
    #estrazione firma digitale
    b1 = bitget(y, 1)#estrazione bitplane 1
    mse = np.mean( (b1-f)**2) #calcolo mse fra b1 e f
    MSE2.append(mse)

#visualizzo variazione MSE su grafico
print(MSE2)
plt.figure('Grafico MSE - filtraggio')
plt.plot(Cut_off, MSE2)
plt.xlabel('fr. di cutoff')
plt.ylabel('mse')

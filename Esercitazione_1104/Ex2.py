# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 17:05:03 2025

@author: david
"""

import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist 
import scipy.ndimage as ndi
import mylib as ml
from skimage.color import rgb2hsv, hsv2rgb
import color_convertion as cc

# Per ridurre il rumore in un’immagine si vuole realizzate un filtraggio adattativo che opera
# mediante finestra scorrevole. I passi da seguire per realizzare l’algoritmo sono i seguenti:
# 1. calcolate l’immagine delle varianze locali su una finestra di dimensioni k × k;
# 2. definite una soglia T superata dal 30% delle varianze;
# 3. filtrate ogni blocco con un filtro media aritmetica di dimensioni k × k se la varianza locale `e
# inferiore a T, altrimenti utilizzate un filtro di dimensioni k − 2 × k − 2.
# Scrivete una funzione function y = adapt filter(x,k) che realizza tale filtraggio e applicatelo
# all’immagine cigno.jpg, cui avete aggiunto rumore gaussiano bianco con σ = 25.
# Calcolate il PSNR tra immagine originale e filtrata per k = 3, 5, 7, 9 e rappresentatelo graficamente
# confrontandolo con la soluzione non adattativa (filtro media aritmetica di dimensioni k×k).
# Infine, visualizzate e confrontate l’immagine filtrata con k = 5 per le due strategie.


def adapt_filter(x,k):
    var = ndi.generic_filter(x, np.var, (k,k))
    #definisco soglia T superata dal 30% delle varianza
    T = np.percentile(var.flatten(),70)
    #filtro uniforme kxk se var locale è < T, altrimenti uso filtro di dim k-2 x k-2
    mask= var < T

    # Filtro media di dimensione k × k su tutta l'immagine
    x_k = ndi.generic_filter(x, np.mean, size=k)
    
    # Filtro media di dimensione k-2 × k-2 su tutta l'immagine
    x_k2 = ndi.generic_filter(x, np.mean, size=(k-2, k-2))
    
    y = np.copy(x)
    # Assegna i valori filtrati (k × k) dove la maschera è True
    y[mask] = x_k[mask]
    # Assegna i valori filtrati (k-2 × k-2) dove la maschera è False
    y[~mask] = x_k2[~mask]
    return y

#visualizzo immagine
x = io.imread("./cigno.jpg")
x = np.float64(x)
plt.figure(1)
plt.imshow(x, clim= [0,255], cmap='gray')
plt.title('INPUT')
plt.colorbar()

#aggiungo rumore gaussiano bianco a x
d=25
M,N = x.shape
n = d*np.random.randn(M,N)
noisy = x + n

#visualizzo immagine con rumore
plt.figure(2)
plt.imshow(noisy, clim= [0,255], cmap='gray')
plt.title('INPUT CON RUMORE AGGIUNTO')

K_axis = []
adaptive_PSNR = []
mean_PSNR = []

for idx,k in enumerate([3,5,7,9]):
    y = adapt_filter(noisy, k)
    plt.figure(3+idx)
    plt.subplot(1,2,1)
    plt.imshow(y, clim= [0,255], cmap='gray')
    plt.title(f'filtraggio adattivo per K={k}')
    # plt.colorbar()
    #calcolo PSNR --10*log10 (MAX^2/MSE)
    max = np.max(y)
    mse = np.mean( (x-y)**2 )
    r = max**2/mse
    psnr= 10*np.log10(r)
    
    #soluzione non adattiva
    z = ndi.uniform_filter(noisy,(k,k))
    plt.subplot(1,2,2)
    plt.imshow(z, clim= [0,255], cmap='gray')
    plt.title(f'filtraggio standard per K={k}')
    # plt.colorbar()
    max = np.max(z)
    mse = np.mean( (x-z)**2 )
    r = max**2/mse
    psnr2= 10*np.log10(r)
    
    print(f'PSNR con soluzione adattiva: {psnr}  per K={k}')
    print(f'PSNR con soluzione standard: {psnr2}  per K={k}')
    print('---------------------------------------------')
    K_axis.append(k)
    adaptive_PSNR.append(psnr)
    mean_PSNR.append(psnr2)

plt.figure(7);
plt.title('PSNR plot')
plt.plot(K_axis, adaptive_PSNR, label='Filtraggio adattivo')
plt.plot(K_axis, mean_PSNR, label='Filtraggio mediato')
plt.legend()
plt.ylabel('PSNR')
plt.xlabel("K")















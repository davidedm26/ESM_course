# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 11:07:38 2025

@author: DavideDiMatteo
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

# Denoising. Aggiungete del rumore gaussiano bianco ad un immagine x con il comando: noisy = x + n
# con n = d*np.random.randn(M,N) dove d `e la deviazione standard del rumore. Effettuate il denoising
# dell’immagine con i filtri a media mobile (al variare della dimensione della finestra). Valutate l’efficacia
# del filtraggio sia visivamente, sia calcolando l’errore quadratico medio tra x e l’immagine “ripulita”, che
# rappresenta una misura quantitativa per stabilire quanto l’immagine elaborata sia simile all’originale.


#DENOISING
x= ml.leggiJpeg('../immagini/barbara.png')
ml.showImage(x, 'input')
M,N = x.shape
d= 25 #arbitrario , ci permette di scegliere la deviazione standard che vogliamo a partire dalla dist.normale
n = d* np.random.randn(M,N) #rand n sta per distribuzione NORMALE
noisy = x + n

ml.showImage(noisy, 'immagine con aggiunta di noise')

#ora faccio il denoising
#faccio filtro a media mobile
k = 5
y = ndi.uniform_filter(noisy, k)
ml.showImage(y, 'immagine filtrata con filtro uniforme')

k0 = (x-noisy)**2
mse_noisy = np.mean ( k0 )   #calcolo del MSE
print(mse_noisy)

k1 = (x-y)**2
mse_enhanced = np.mean ( k1 )   #calcolo del MSE
print(mse_enhanced)











# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:40:47 2025

@author: david
"""

import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

# 1. Spettro di ampiezza. Analizzate lo spettro di ampiezza di alcune immagini di test (circuito.jpg, impronta.
# tif, anelli.tif), siete in grado di legare il contenuto in frequenza con l’andamento spaziale dell’immagine?
imgs= np.array (('circuito.jpg','impronta1.tif','anelli.tif'))


for idx, k in enumerate(imgs):
    
    x = np.float64(io.imread(f'../immagini/{k}'))
    
    plt.figure(idx*3+1)
    plt.imshow(x, cmap='gray', clim=None)
    plt.title(f'input = {k}')
    
    X = np.fft.fft2(x);
    plt.figure(idx*3+2)
    plt.imshow(np.abs(X), cmap='gray', clim=None)
    plt.title(f'FFT di {k}')
    
    Y = np.log(1+np.abs(np.fft.fftshift(X)))
    plt.figure(idx*3+3);
    plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
    plt.title(f'spettro del modulo manipolato di {k}')





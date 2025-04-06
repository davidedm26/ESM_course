# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 16:43:52 2025

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


# 3. Risposta in frequenza del filtro media aritmetica. Calcolate la DFT del filtro media aritmetica di dimensione
# k = 5, 10, 15, utilizzando per la FFT un numero di punti relativamente elevato, allo scopo di
# ottenere un campionamento fine di H(ν, μ). Verificate il comportamento passa-basso del filtro.

keys= np.array([5,10,15]) #dimensione del filtro
P = 500; Q = 500;

for k in keys:
    #definisco filtro media aritmetica
    h=np.ones((k,k))/k**2
    #calcolo DFT del filtro
    H = np.fft.fft2(h, (P,Q))
    H = np.abs(np.fft.fftshift(H)) #centra sulla componente 0
    
    plt.figure()
    plt.imshow(H, clim=None, cmap='gray', extent=(-0.5,0.5,-0.5,0.5))
    plt.title('Risposta in frequenza del filtro media aritmetica per k=%d' %k)
    
    #Verifico nello spazio il comportamento passa-basso
    x = np.float64( io.imread('../immagini/volto.tif'))
    # ml.showImage(x, 'input')
    y= ndi.correlate(x, h)
    ml.showImage(y, 'input filtrato con k=%d' %k)
    

   




















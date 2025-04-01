# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 18:37:50 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

# x = io.imread('.\immagini\granelli.jpg');
# (M,N) = x.shape

# plt.figure(1) #assegna label
# plt.imshow(x, clim=[0,255], cmap= 'gray')
# plt.colorbar()

x = np.fromfile( '.\immagini\house.y', np.uint8) #lettura dei dati dal file senza formato
x = np.reshape(x , (512,512)) #forza risoluzione

x = np.uint8(x) #converte dati in unsigned int per la prossima operazione
io.imsave('.\immagini\immagine_q70.jpg',x , quality = 70) ##converte in formato jpeg con fattore di conversione 30/100

y= io.imread('.\immagini\immagine_q70.jpg') ##visualizza immagine prodotta5
plt.figure(1)
plt.imshow(y, clim=[0,255], cmap= 'gray')
plt.title('dopo la compressione')
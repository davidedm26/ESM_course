# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:33:17 2025

@author: DavideDiMatteo
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

def smooth(x):
    M,N = x.shape
    h= np.array([ [1,2,1],[2,4,2],[1,2,1]]) / 16
    y= ndi.correlate(x, h, mode='reflect')
    return y

#laboratorio sul filtraggio
x = np.float64(io.imread('../immagini/test.jpg')) ##importante fare il cast
# k=3; h= np.ones((k,k))/(k**2) #definisco maschera per media aritmetica matrice di tutti 1 e dividiamo per 9 1/9-1/9----
# y= ndi.correlate(x, h, mode='reflect') #posso metterci pure il constant per i bordi
# z= ndi.gaussian_filter(x, 35)

#ESERCIZIO 1.1
y= smooth(x)

ml.showImage(x, 'input')
ml.showImage(y, 'immagine filtrata con funzione smooth')


# ml.showImage(y, 'filtraggio gaussiano')
# ml.showImage(z, 'filtraggio gaussiano con funzione apposita')

# #FILTRO DI SMOOTHING
# h = np.array( [[],[],[]])
# y= ndi.correlate(x, h, mode='reflect') #posso metterci pure il constant per i bordi


# ml.showImage(x, 'input')
# plt.figure();
# plt.imshow(y, clim=[0,255], cmap='gray');
# plt.title('output')


# #provare ad aumentare la dimensione del filtro ##FARE A CASA

# #per questo che abbiamo fatto possiamo utilizzare ndi.uniform_filter dove dobbiamo dargli solo la dimensione





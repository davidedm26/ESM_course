# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:24:30 2025

@author: david
"""

#Enhancement locale
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

# Si consideri l’immagine bebe.jpg, che rappresenta una vecchia fotografia di un
# neonato, in cui sono presenti dei difetti dovuti al passare del tempo. Si vuole realizzare un algoritmo
# iterativo che effettui l’enhancement locale dell’immagine, riguardante cio`e le sole parti danneggiate,
# individuate dalla maschera binaria mask.bmp. Detta X1 l’immagine iniziale, che coincide con l’originale
# eccetto per le parti danneggiate, che sono poste a zero,

def local_en(x, k, mask):
    if (k==1):    #
        x1 = x * (mask>0)
        return x1
    
    a=0.073
    b=0.177
    h= np.array([[a,b,a],[b,0,b],[a,b,a]])
    x_k = local_en(x,k-1, mask)
    y = ndi.correlate(x_k, h)
    z = np.copy(x_k)
    z[mask == 0] = y[mask == 0]  #in output devo avere x_k ovunque tranne che nei punti della maschera, dove devo avere y
     
    return z

plt.close('all')

x=ml.leggiJpeg('../immagini/bebe.jpg')
x= np.float64(x)
ml.showImage(x, 'input' )
mask=( ml.leggiJpeg(('../immagini/mask.bmp')))
ml.showImage(mask, 'mask')

ris = local_en(x, 1000, mask)
ml.showImage(ris, 'result')
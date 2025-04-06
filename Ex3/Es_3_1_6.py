# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:09:45 2025

@author: david
"""

# Estrazione di Keypoint

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import mylib as ml

x = np.float64(io.imread('../immagini/tetto.png'))

plt.figure()
plt.imshow(x, cmap='gray', clim=None)
plt.colorbar();
plt.title('input')

# Creazione dei filtri per il calcolo delle derivate
V  = np.array([[0,-1,0],[0,1,0],[0,0,0]], dtype=np.float64)
H  = np.array([[0,0,0],[-1,1,0],[0,0,0]], dtype=np.float64)
D1 = np.array([[-1,0,0],[0,1,0],[0,0,0]], dtype=np.float64)
D2 = np.array([[0,0,-1],[0,1,0],[0,0,0]], dtype=np.float64)

# #calcola ciascuna derivata direzionale
v = ndi.correlate(x,V)
h = ndi.correlate(x,H)
d1= ndi.correlate(x,D1)
d2= ndi.correlate(x,D2)

#per ciascuna derivata valuta media dei valori al quadrato su finestra scorrevole 5x5
vv = ndi.generic_filter(v**2, np.mean, 3)
hh = ndi.generic_filter(h**2, np.mean, 3)
dd1 = ndi.generic_filter(d1**2, np.mean, 3)
dd2 = ndi.generic_filter(d2**2, np.mean, 3)

Qmin = np.minimum( np.minimum(vv,hh), np.minimum(dd1,dd2))

MQmin = ndi.generic_filter(Qmin, np.max, 3)

SP = (Qmin > 20) & (Qmin == MQmin)

plt.figure()
plt.imshow(SP, cmap='gray', clim=[0,1])









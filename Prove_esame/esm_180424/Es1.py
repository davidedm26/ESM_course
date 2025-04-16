# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 15:58:36 2025

@author: david
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

#definisco funzione di filtraggio direzionale

def confronta_var(x):
    m1 = np.zeros((9,9),dtype=int)
    m1[0:4,:]=1
    m1[4,4]=1
    m2 = m1.T

    m3 = np.zeros((9,9), dtype=int)
    m3[:,0:4]=1
    m3[4,4]=1

    m4 = m3.T

    m5 = 1 - np.triu(np.ones((9,9), dtype=int))
    m5[4,4]=1
    m6 = m5.T

    m7 = np.fliplr(m5)
    m8 = np.fliplr(m6)
    
    masks = np.array([m1,m2,m3,m4,m5,m6,m7,m8])
    
    x = x.reshape((9,9))
    varianza = []
    for i in range(8):
        xm = x[masks[:, :, i] > 0]
        varianza.append(np.var(xm))

    index = np.argmin(varianza)
    z = np.mean(x[masks[:, :, index] > 0])
    return z

def filtro_dir(x):

    y = ndi.generic_filter(x, confronta_var, (9,9))

    return y


x = np.float64(io.imread('./im_180424/test.png'))
#aggiungo rumore gaussiano 
n = 30*np.random.randn()
noisy = x + n

plt.figure(1)
plt.imshow(noisy, clim=[0,255], cmap='gray')
plt.title('Immagine rumorosa')

y = filtro_dir(noisy)

plt.figure(2)
plt.imshow(y, clim=[0,255], cmap='gray')
plt.title('output')












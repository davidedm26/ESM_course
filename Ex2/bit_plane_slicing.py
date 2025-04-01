# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:39:32 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import bitop as bo

x= io.imread( './immagini/frattale.jpg')

M,N = x.shape
bitplane = np.zeros( (M,N,8), dtype=bool ) #matrice 3D

# x = np.float64(x)
#bitop lavora su uint

for index in range(8):
    bitplane[:,:,index] = bo.bitget(x, index) #bitget non funziona come float

# Mostra tutti i bitplane in una singola figura
plt.figure(figsize=(12, 6))  # imposta la dimensione della figura
for i in range(8):
    plt.subplot(2, 4, i + 1)  # crea una griglia 2x4 per i subplot
    plt.imshow(bitplane[:, :, i], clim=[0, 1], cmap="gray")
    plt.title("Bitplane %d" % i)
    plt.axis('off')  # nasconde gli assi per una visualizzazione più pulita

plt.tight_layout()  # regola automaticamente i layout per prevenire sovrapposizioni
plt.show()

  
    
    #se metto a 0 il bit meno significativo equivale a fare una quantizzazione(approssimazione)
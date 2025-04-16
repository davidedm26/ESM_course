# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 09:22:27 2025

@author: david
"""

# Dehazing

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

x= (io.imread('../Immagini/paesaggio.jpg'))/255
plt.figure(1)
plt.imshow(x)

#Costanti
A1=0.7020
A2=A1
A3=0.7098
A =np.array([A1,A2,A3])
t0=0.1


K = np.min(x / A[None, None, :], axis=-1)
#   EQUIVALE A
    #for i in range(3):  # Per ogni canale R, G, B
    # x_norm[:, :, i] = x[:, :, i] / A[i]
    
x_dark= ndi.generic_filter(K, np.min, (15,15))
t = 1 - 0.95*x_dark    
y = np.copy(x)

for i in range(2):
    y[:,:,i] = ( ( x[:,:,i] - A[i] )/ (np.maximum(t,t0) ) ) + A[i]

plt.figure(2)
plt.imshow(y)





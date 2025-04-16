# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 19:18:35 2025

@author: david
"""

import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

x = io.imread('./house_rumorosa.png')
x= np.float64(x)
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

#applico filtro mediano classico
k=3
y = ndi.median_filter(x,(k,k))
plt.subplot(1,2,2)
plt.imshow(y, clim=None, cmap='gray')
plt.title('output filtraggio mediano')

plt.tight_layout()

MSE = np.mean( (x-y)**2)
print(f'MSE con filtraggio mediano: {MSE}')

#Filtraggio adattivo

#le funzioni applicate a generic_filter convertono la matrice in un vettore
#quindi n=1,w=3,c=4,e=5,s=7
def valuta(x):
    n=x[1]
    w=x[3]
    c=x[4]
    e=x[5]
    s=x[7]
    if ((np.max([n,s,c,w,e])) - (np.min([n,s,c,w,e])) <= 20):
        return (n+s+c+w+e)/5
    elif  ( ( np.abs(e-w) - (np.abs(n-s))) > 20 ):
        return (n+s+c)/3
    elif ( ( np.abs(n-s) - (np.abs(e-w))) > 20 ):
        return (e+w+c)/3
    else:
        return np.median(x)

#applico il filtraggio definito
z = ndi.generic_filter(x, valuta, (k,k))

#mostro risultati
plt.figure(2)
plt.subplot(1,2,1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

plt.subplot(1,2,2)
plt.imshow(z, clim=None, cmap='gray')
plt.title('output filtraggio adattivo')

MSE2 = np.mean( (x-z)**2)
print(f'MSE con filtraggio adattivo: {MSE2}')









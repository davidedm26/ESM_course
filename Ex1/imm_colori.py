# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 19:47:52 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
plt.close('all')


x= io.imread('./immagini/fragole.jpg')
plt.figure(); plt.imshow(x)

R = x[:,:,0]
plt.figure();
plt.imshow(R, clim=[0,255], cmap='gray');
plt.title('componente di rosso');

G = x[:,:,1]
plt.figure();
plt.imshow(G, clim=[0,255], cmap='gray');
plt.title('componente di verde');

B = x[:,:,2]
plt.figure();
plt.imshow(B, clim=[0,255], cmap='gray');
plt.title('componente di blu');

M= x.shape[0] #n righe
N= x.shape[1]#n colonne

R= np.zeros((M,N), x.dtype) #annulla componente di rosso
y= np.stack( (R,G,B), -1)
plt.figure();
plt.imshow(y);
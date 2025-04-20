# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:31:35 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col

plt.close('all')
x= np.fromfile('../Immagini/target_rumorosa.raw', dtype=np.float32)
x = np.reshape(x, (256,256))
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.title('Immagine di input')


#segmentazione tramite op.morfologiche (dilation-erosion)
b= morph.rectangle(4,5)
x1 = morph.dilation(x,b)
x2 = morph.erosion(x,b)
y = x1 - x2
y = y>80

y = morph.opening(y, morph.rectangle(2,2))

plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')
plt.title('Mappa dei contorni tramite op.morfologiche')

# #segmentazione tramite filtraggio spaziale (gradiente)
# #calcolo derivata prima rispetto a m
# m1= np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
# dm = ndi.correlate(x,m1)
# #calcolo derivata seconda rispetto a n
# m2= np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
# dn = ndi.correlate(x,m2)
# #calcolo gradiente
# y = np.sqrt(dm**2 + dn**2)
# #tresholding
# y = y>100



# plt.figure(3)
# plt.imshow(y, clim=None, cmap='gray')
# plt.title('Mappa dei contorni tramite gradiente')

# #strategia consigliata dalla traccia

# def elab(x):
#     m_a = np.mean(x)
#     m_g = np.prod(x)**(1/np.size(x))
#     return m_a/m_g

# k=5
# T= 1.15

# z = ndi.generic_filter(x**2,  elab, (k,k),)

# y = z >= T


# y = morph.opening(y, morph.disk(1))
# y = morph.thin(y)

# plt.figure(4)
# plt.imshow(y, clim=None, cmap='gray')
# plt.title('Mappa dei contorni tramite strategia consigliata')
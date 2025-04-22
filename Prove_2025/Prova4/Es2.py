# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 15:53:57 2025

@author: david
"""

#ES2
import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

p1 = np.load('../immagini/data_P1.npy')
plt.figure('PNRU')
plt.subplot(1,2,1)
plt.imshow(p1, clim=None, cmap='gray')

plt.subplot(1,2,2)
p2 = np.load('../immagini/data_P2.npy')
plt.imshow(p2, clim=None, cmap='gray')

def detect(p1,p2):
    p1_m = ndi.uniform_filter(p1, (127,127)) 
    p2_m = ndi.uniform_filter(p2, (127,127)) 
    
    a = (p1 - p1_m)
    b = (p2 - p2_m)
    num = ndi.generic_filter( a*b, np.sum, (127,127))
    
    c = ndi.generic_filter(a**2, np.sum, (127,127))
    d = ndi.generic_filter(b**2, np.sum, (127,127))
    den = np.sqrt(c) * np.sqrt(d)
    rho = num/den                                                                
    
    plt.figure('correlazione')
    plt.imshow(rho, cmap='jet')
    
    
    mask = rho < 0.03
    plt.figure('mask')
    plt.imshow(mask, clim=[0,1], cmap='gray')

    return mask

mask = detect(p1,p2)

io.imsave('mask.jpg', mask, quality = 50)




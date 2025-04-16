# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 18:08:36 2025

@author: david
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.color as clr


x = io.imread('./im_180424/I1.png')/255
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')
plt.title('input')

z = clr.rgb2gray(x)

h = np.array([[-1,2,-1],[2,-4,2],[-1,2,-1]])
x = ndi.correlate(z, h)

def elab(x):
    x_m = [x[0],x[1],x[2],x[5],x[8],x[7],x[6],x[3]]
    y=0
    for i in range(0,8):
        y+= (2**i)*(x_m[i]>=x[4])
    return y

x = ndi.generic_filter(x, elab, (3,3))

#valuta istogramma
plt.figure(2)
k = plt.hist(x.flatten(), bins = 256)
plt.title('hist')

dev = np.std(k[0])





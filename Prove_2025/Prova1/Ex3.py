# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:13:47 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import random_noise
import scipy.ndimage as ndi
import skimage.color as clr
from sklearn.cluster import k_means
# realizza il clustering K-means di x con K=2 e restituisce in t la semisomma dei due template.
def T_opt(x):
    d = np.reshape(x, (-1,1))
    centroid, idx ,sum_var = k_means(d,2)
    y = np.reshape(idx, x.shape)
    print("Centroidi:", centroid)  # Aggiungi questa linea per diagnosticare i centroidi
    t = np.mean(centroid)
    
    plt.figure(2)
    plt.title('clustering kmeans')
    plt.imshow(y, clim=[0,1], cmap='gray')
    return t

x = np.fromfile('../immagini/rice.y', dtype=np.uint8)
x = np.reshape(x, (256,256))
plt.figure(1)
plt.title('input')
plt.imshow(x, clim=[0,255], cmap='gray')
t = T_opt(x)
T=[]
#Thresholding adattivo
for i in [1,2,4,8,16,32,64,128,256]:
    y = x[0:i,:]
    print(y.shape)
    t = T_opt(y)
    T.append(t)



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
    
    # plt.figure(2)
    # plt.title('clustering kmeans')
    # plt.imshow(y, clim=[0,1], cmap='gray')
    return t

def adapt(x,L):
    #esegue segmentazione su blocchi di L righe
    M,N = x.shape
    num_blocks = M//L
    y = np.zeros((M,N), bool)
    for j in range(num_blocks):
        block = x[j*L:(j+1)*L,:]
        mask_block = block > T_opt(block)
        y[j*L:(j+1)*L,:]= mask_block
    return y

x = np.fromfile('../immagini/rice.y', dtype=np.uint8)
x = np.reshape(x, (256,256))
plt.figure(1)
plt.title('input')
plt.imshow(x, clim=[0,255], cmap='gray')
t = T_opt(x)

mask = x > t

plt.figure(2)
plt.imshow(mask,clim=[0,1], cmap='gray')
plt.title('immagine con segmentazione globale')

mask_ideal = np.reshape(np.fromfile('../immagini/rice_bw.y', np.uint8), (256,256))
mask_ideal = mask_ideal>0

T=[]
list_L = [1,2,4,8,16,32,64,128,256]
list_correct=[]

#Thresholding adattivo
for L in list_L:
    y = adapt(x,L)
    num_correct = np.sum(y==mask_ideal)
    list_correct.append(num_correct)
    
plt.figure(4)
plt.semilogx(list_L, list_correct, '-*')
plt.grid('on')
plt.ylabel('pixel corretti')


# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 18:04:23 2025

@author: david
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

masks = np.array([
    [
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0]
    ]
])

x=np.fromfile('../immagini/zebre.y', dtype=np.uint8);
x = np.reshape(x,(321,481))
ml.showImage(x, 'input')

M,N = x.shape
n = 25*np.random.randn(M,N) #gaussian noise

x_noisy = x +n
ml.showImage(x_noisy, 'noisy')


local_variances = []

for i in range (len(masks)):
    local_variances.append(ndi.generic_filter(x_noisy, np.var, footprint=masks[i]))

 # Creiamo una matrice per memorizzare l'indice della maschera con varianza minima per ciascun pixel
mask_indices = np.zeros_like(x_noisy, dtype=np.uint8)
filtered_image = np.zeros_like(x_noisy)  

for i in range(4, x_noisy.shape[0] - 4):
    for j in range(4, x_noisy.shape[1] - 4):
        variances_i_j = [local_variances[k][i][j] for k in range(len(local_variances))]
        min_index = np.argmin(variances_i_j)
        min_mask = masks[min_index]
        filtered_pixel_value = np.sum(min_mask * x_noisy[i-4:i+5, j-4:j+5]) / np.sum(min_mask)
        filtered_image[i][j] = filtered_pixel_value
        
z = ndi.uniform_filter(x, (5, 5))

max_pixel_value = np.max(x)
mse = np.mean((x - filtered_image) ** 2)
psnr = 10 * np.log10((max_pixel_value ** 2) / mse)

ml.showImage(z,'media')
ml.showImage(filtered_image,'procedura')




















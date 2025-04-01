# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:45:00 2025

@author: david
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import bitop as bo
import mylib as ml
from skimage.transform import rescale
from skimage.transform import warp, rotate
##rotazione centrale
x= np.float32(io.imread('../immagini/lena.jpg'))

theta= -np.pi/2
M,N= x.shape

T1 = np.array([[1,0,0],[0,1,0],[M/2,N/2,1]], dtype=np.float32)
T2 = np.array([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),0],[0,0,1]], dtype=np.float32)
T3 = np.array([[1,0,0],[0,1,0],[-M/2,-N/2,1]], dtype=np.float32)

T= T3@T2@T1
A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta

plt.subplot(1,2,1)
plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('nput')
y1 = warp( x, A, order=1)
plt.subplot(1,2,2)
plt.imshow(y1, clim=[0,255], cmap='gray'); plt.title('rot')


    
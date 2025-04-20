# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 18:04:22 2025

@author: david
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as col

#Ex1
plt.close('all')
x= np.float64(io.imread('../Immagini/barbara.jpg'))
x = np.mean(x, -1)
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

h = np.array([[1,0,0,0,1],
              [0,0,0,0,0],
              [0,0,-4,0,0],
              [0,0,0,0,0],
              [1,0,0,0,1]])
y = ndi.correlate(x, h)

plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')

def respfreq(h): #determina la risposta in frequenza del filtro
    H = np.fft.fftshift( np.fft.fft2(h))
    m = np.fft.fftshift(np.fft.fftfreq(H.shape[0]))
    n = np.fft.fftshift(np.fft.fftfreq(H.shape[1]))
    from mpl_toolkits.mplot3d import Axes3D
    ax = Axes3D(plt.figure('Risposta in frequenza')); # crea una figura per i grafici 3d
    l,k = np.meshgrid(n,m)
    ax.plot_surface(l,k,H, linewidth=0, cmap='jet')
    
    

respfreq(h)

#I restanti punti non sono stati completati.(Facili)













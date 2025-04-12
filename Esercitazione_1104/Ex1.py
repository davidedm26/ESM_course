# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:12:53 2025

@author: david
"""
import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist 
import scipy.ndimage as ndi
import mylib as ml
from skimage.color import rgb2hsv, hsv2rgb
import color_convertion as cc

# EX. 1 Si vuole realizzare l’enhancement dell’immagine ponte.gif. Nello script ex1.m, dopo aver
# visualizzato l’immagine, individuate i difetti che la caratterizzano, ed effettuate quindi tutte le
# elaborazioni che vi sembrano opportune per migliorarne la visualizzazione.

#visualizzo immagine
x = io.imread("./ponte.png")
plt.figure(1)
plt.imshow(x, clim= [0,255], cmap='gray')
plt.title('INPUT')
plt.colorbar()

plt.figure(2)
plt.hist(x.flatten(), bins=256)
plt.title('HISTO')

#proviamo mediano
z = ndi.median_filter(x, (3,3))
plt.figure(3)
plt.imshow(z, clim= [0,255], cmap='gray')
plt.title('mediano')
plt.colorbar()

#Noto che l'istogramma si può stretchare/equalizzare
# y = equalize_hist(z)
# plt.figure(4)
# plt.hist(y.flatten())
# y = y*255
# plt.title('HISTO equalizzato')

#FSHS
k=256
x_min = np.min(z);
x_max = np.max(z);
y = (k-1)* ( (z-x_min)/(x_max-x_min))
plt.figure(4)
plt.hist(y.flatten(), bins=256)
plt.title('HISTO stretchato')

#visualizzo immagine
plt.figure(5)
plt.imshow(y, clim= [0,255], cmap='gray')
plt.title('OUTPUT')
plt.colorbar()

#vediamo in frequenza se c'è qualcosa
plt.figure(6)
Y = np.fft.fftshift(np.fft.fft2(y))
plt.imshow(np.log(1+np.abs(Y)), clim= None, cmap='gray')
plt.title('Spettro')







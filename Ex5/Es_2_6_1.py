# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 12:02:20 2025

@author: david
"""
import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml
from skimage.color import rgb2hsv, hsv2rgb
import color_convertion as cc

 # 1. Variazione del colore. Considerate l’immagine Azzurro.jpg, dove ` e presente un accappatoio azzurro, e
 # generate l’immagine Rosso.jpg, in cui solo l’accappatoio diventa rosso. A tal fine, passate nello spazio
 # di colore HSI, individuate la regione dell’immagine occupata dall’accappatoio in base ai suoi valori di
 # tinta, saturazione e luminanza, e solo in tale regione operate una opportuna variazione della sola tinta

#Visualizzo Immagine input
x = io.imread('../immagini/azzurro.jpg')
x = np.float64(x) / 255
plt.figure(1)
plt.imshow(x) #non servono tag
plt.title('Immagine input')

#Passo allo spazio HSI
x_hsi = cc.rgb2hsi(x)
H = x_hsi[:,:,0]
S = x_hsi[:,:,1]
I = x_hsi[:,:,2]

plt.figure(2)
plt.subplot(1,3,1)
plt.imshow(H, clim=None, cmap='gray') #non servono tag
plt.title('Componente H')
plt.subplot(1,3,2)
plt.imshow(S, clim=None, cmap='gray') #non servono tag
plt.title('Componente S')
plt.subplot(1,3,3)
plt.imshow(I, clim=None, cmap='gray') #non servono tag
plt.title('Componente I')

mask = (H<0.60) & (H>0.57) & (S>0.3) & (S<0.5)

plt.figure()
plt.imshow(mask, clim=None, cmap='gray') #non servono tag
plt.title('Maschera')

#trasformare il colore dell'accappatoio da azzurro a rosso
yH = (H-0.6)%1
yH = mask*yH + (1-mask)*H
y_hsv= np.stack((yH,S,I), -1)
y=hsv2rgb(y_hsv)

plt.figure()
plt.imshow(y) #non servono tag
plt.title('Immagine elaborata')

io.imsave('Rosso.jpg', y)
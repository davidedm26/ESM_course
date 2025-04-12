# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:16:06 2025

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

# 4. Immagini sintetiche. Un modo per distinguere i volti sintetici da quelli reali `e attraverso l’analisi nel
# dominio della frequenza

# (a) Converto l’immagine in scale di grigi considerando la dinamica [0, 1];
x = io.imread('../immagini/volto2.png')
x = x /255
x = np.mean(x,-1)

#b Calcolo H(μ, ν) applicando la seguente formula:
# H(μ, ν) = log |X(μ, ν)|
H =np.log ( np.abs(( np.fft.fft2(x) ) ))

#Calcolo Densità alle basse frequenze con soglia tau=0.35
M,N = H.shape
m = np.fft.fftfreq(M)
n= np.fft.fftfreq(N)
l,k = np.meshgrid(n,m)

tau=0.35
mask = (np.abs(k)<= tau) & (np.abs(l)<=tau)

d = np.sum( H[mask]) / np.sum(H)

print("La densità alla basse frequenze è:", d)
if (d<0.7):
    print("IMMAGINE SINTETICA!!")


#Visualizzo Immagine input
plt.figure(1)
plt.imshow(x,clim=None,cmap='gray')
plt.title('Volto')


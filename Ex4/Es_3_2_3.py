# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 18:18:32 2025

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

# Immagini ridimensionate. Un algoritmo che permette di rivelare se un’immagine x(m, n) di dimensioni
# M × N `e stata ricampionata

#Visualizzo Immagine input
x = np.fromfile('../immagini/zoom.y', dtype=np.float32)
x = np.reshape(x,(128,128))

plt.figure(1)
plt.imshow(x,clim=None,cmap='gray')
plt.title('Immagine input')


def detect(x):
    M,N = x.shape
    #Calcolare la derivata seconda lungo le righe dell'immagine tramite:
    # d2(m, n) = 2x(m, n) − x(m, n + 1) − x(m, n − 1);
    h = np.array(([0,0,0],[-1,2,-1],[0,0,0]))
    der2_hori = ndi.correlate(x, h)
    #Valutare la pseudo varianza e la relativa derivata prima
    v_hori = np.sum( np.abs(der2_hori), 0)
    d_hori = v_hori[1:] - v_hori[:-1] #parte da 1 e finisce a n // parrte da 0 e arriva 
    #identificare la periodicità di d(n) nel dominio di Fourier tramite DFT su N-2 punti e mostrarla.
    D_hori = np.abs(np.fft.fftshift(np.fft.fft(d_hori, N-2)))
    f_hori = np.fft.fftshift(np.fft.fftfreq(N-2))
    # rivelare i picchi che identificano le periodicit`a per stimare il fattore di scala R. In particolare, una
    # volta identificata la frequenza ν0 cui si trova il picco nell’intervallo (0, 1/2), il fattore di scala `e
    # stimato come R = 1/ν0.
    ni_hori= f_hori[(D_hori==np.max(D_hori)) & (f_hori>0)]
    R_hori = 1/ ni_hori
    
    d2_vert = ndi.correlate(x,h.T)
    v_vert = np.sum(np.abs(d2_vert),1)
    d_vert = v_vert[1:] - v_vert[:-1] 
    D_vert = np.abs(np.fft.fftshift(np.fft.fft(d_vert,M-2)))
    f_vert = np.fft.fftshift(np.fft.fftfreq(M-2))
    ni_vert = f_vert[(D_vert==np.max(D_vert)) & (f_vert>0)]
    R_vert = 1/ni_vert
    
    return D_hori, D_vert, R_hori, R_vert


D_hori, D_vert, R_hori, R_vert = detect(x)

f_hori = np.fft.fftshift(np.fft.fftfreq(len(D_hori)))
f_vert = np.fft.fftshift(np.fft.fftfreq(len(D_vert)))

plt.figure() 
plt.subplot(2,1,1)
plt.plot(f_hori, D_hori,'-or')
plt.title(f'DFT derivata pseudo-varianza orizontale, fattori di scala: {R_hori}')
plt.subplot(2,1,2)
plt.plot(f_vert, D_vert,'-or')
plt.title(f'DFT derivata pseudo-varianza verticale, fattori di scala: {R_vert}')
plt.tight_layout()



















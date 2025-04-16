# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 18:11:13 2025

@author: david
"""

# EX. 1 Data l'immagine star trek.jpg si vuole e effettuare enhancement per migliorare la visualiz-
# zazione della zona scura. 
# Realizzate quindi l'equalizzazione dell'istogramma scrivendo una funzione
# function y = enhanc(x). Visualizzate il risultato finale e confrontatelo con l'immagine originale.
# Noterete che sebbene complessivamente l'immagine sia notevolmente migliorata, l'area chiara,
# ben visibile nell'immagine originale, dopo l'elaborazione ha perso nitidezza. Per evitare questo
# problema realizzate l'enhancement solo nella zona scura, calcolando opportunamente la maschera
# che la identifica (per esempio, mediante l'uso delle statistiche locali). A tale scopo scrivete una
# nuova funzione function y = enhanc_adapt(x) e confrontate il risultato finale con quello ottenuto
# precedentemente.

import skimage.io as io
import skimage.exposure as exp
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

x = io.imread('./star_trek.jpg')
x= np.float64(x)
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('input')

plt.subplot(1,2,2)
plt.hist(x.flatten(), bins=256)
plt.title('hist')

plt.tight_layout()


def enhanc(x):
    y = exp.equalize_hist(x)
    return y*255

y = enhanc(x)

plt.figure(2)
plt.subplot(1,2,1)
plt.imshow(y, clim=None, cmap='gray')
plt.title('immagine post equalizzazione hist')

plt.subplot(1,2,2)
plt.hist(y.flatten(), bins=256)
plt.title('hist equalizzato')
plt.tight_layout()

#Realizzare enhancement solo della zona scura
#Calcolando opportunamente la maschera in funzione delle statistiche locali


k=25
# w = ndi.generic_filter(y, np.mean, (k,k))
w = ndi.median_filter(y, (k,k))

plt.figure(3)
plt.imshow(w, clim=None, cmap='gray')
plt.title(f'filtro con finestra lato k={k}')

#Intercetto area chiara nell'immagine equalizzata
M,N= w.shape
l,k = np.meshgrid(M,N)
mask = (w > 190)& (l>k)
plt.figure(4)
plt.imshow(mask, clim=[0,1], cmap='gray')

#Realizza enhancement della sola zona scura
z = np.copy(y)
z[mask] = x[mask]
plt.figure(5)
plt.imshow(z, clim=None, cmap='gray')
plt.title('Enhancement')




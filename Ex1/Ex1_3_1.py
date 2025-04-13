# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 08:30:43 2025

@author: david
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

# Immagine delle medie. Scrivete una funzione dal prototipo medie(x,K) che fornisce l'immagine delle
# medie locali su finestre K X K. Fate poi un esperimento in cui calcolate l'immagine delle medie al
# variare di K = 3; 5; 7; 9 e visualizzate il risultato. Che osservazioni potete fare?

#RISPOSTA: Ovviamente più è grande K e più informazione sarà persa.

def medie(x,K):
    (M,N)= x.shape
    med = np.zeros( (M-K+1, N-K+1))
    
    for i in range (M-K+1):
        for j in range (N-K+1):
            med[i,j]= np.mean(x[i:i+K,j:j+K])
    return med

def varianze(x,K):
    return ndi.generic_filter(x, np.var, (K,K))

##main
x= io.imread('../immagini/dorian.jpg')    #prendi un'immagine
#converti in float64
x = np.float64(x)
#mostrala
# plt.figure(1);
# plt.imshow(x, clim=[0,255], cmap='gray');
#fai media
y = medie(x,20);

#mostra media
plt.subplot(1,3,1); plt.imshow(x, clim=[0,255], cmap='gray');
plt.subplot(1,3,2); plt.imshow(y, clim=[0,255], cmap='gray');

 

# 2. Immagine delle varianze. Scrivete adesso una funzione dal prototipo varianze(x,K) per calcolare
# l'immagine delle varianze locali su finestre K X K. Usate questa funzione per valutare e visualizzare
# l'immagine delle varianze dell'immagine filamento.jpg usando blocchi 33. Che tipo di informazioni
# vi da sull'immagine?   
plt.close('all')

x_fil = io.imread('../immagini/filamento.jpg')

x_var = varianze(x_fil,3);
plt.subplot(1,3,3); plt.imshow(x_var, clim=[0,255], cmap='gray');

# plt.close();

# plt.hist(x, bins=5, density=True)
# plt.show()








    
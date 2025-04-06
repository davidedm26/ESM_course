# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 18:05:45 2025

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


# Scrivete una funzione con il prototipo gaussLPF(x,sigma)
# che implementa il filtraggio passa-basso gaussiano con un assegnato valore di σ. Quindi applicate questo filtro
# all’immagine testo.tif, che mostra un esempio di testo a bassa risoluzione che caratterizza di solito un fax
# o una fotocopia. Il testo in questa forma si presta poco ad essere elaborato da un calcolatore che effettua
# riconoscimento automatico, dato che sono presenti dei vuoti nei caratteri, un opportuno filtro passa-basso
# pu`o migliorarne la visualizzazione. Questo filtro pu`o anche essere usato per ringiovanire l’aspetto della donna
# raffigurata nell’immagine volto.jpg. Fate degli esperimenti, in entrambi i casi, al variare di σ.

def gaussLPF(x, sigma):
    M,N = x.shape #definisce le dimensioni del filtro in base a quelle dell'immagine in input
    m = np.fft.fftshift(np.fft.fftfreq(M))
    n = np.fft.fftshift(np.fft.fftfreq(N))
    l,k = np.meshgrid(n,m) #sposta le coordinate centrando il centro in 0.0
    #definisce forma del filtro
    D = np.sqrt(k**2+ l**2) #definisce rho di ciascun pixel #ripreso dall'esercizio del LPF ideale
    
    H = np.exp(-(D**2) / (2*sigma**2)) #in funzione della formula data
    
    plt.figure(); 
    plt.imshow(H, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
    plt.title("filtro sintetizzato") #visualizza il filtro creato
    
    X = (np.fft.fft2(x)) #calcola DFT dell'input (centrandola in 0)np.fft.fftshift
    X = np.fft.fftshift(X)
    plt.figure(); 
    plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); #visualizza in maniera accettabile
    plt.title("immagine input  (frequenza)")
    
    
    Y = H * X #effettua filtraggio
    
    plt.figure(); 
    plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
    plt.title("immagine filtrata (frequenza)")
    
    #ricostruisce Y nello spazio
    Y = np.fft.ifftshift(Y)
    y = np.real(np.fft.ifft2(Y))
    
    return y

x = np.float64(io.imread('../immagini/testo.tif'))

y = gaussLPF(x, 0.15)

plt.figure();
plt.subplot(1,2,1)
io.imshow(x, clim=[0,255], cmap='gray');
plt.title("testo - input")  
    
plt.subplot(1,2,2)
plt.imshow(y, clim=None, cmap='gray');
plt.title("immagine filtrata con filtro gaussiano")

plt.tight_layout()

plt.close('all')

# Questo filtro pu`o anche essere usato per ringiovanire l’aspetto della donna
# raffigurata nell’immagine volto.jpg. Fate degli esperimenti, in entrambi i casi, al variare di σ.

x = np.float64(io.imread('../immagini/volto.tif'))

y = gaussLPF(x, 0.15)

plt.figure();
plt.subplot(1,2,1)
io.imshow(x, clim=[0,255], cmap='gray');
plt.title("volto - input")  
    
plt.subplot(1,2,2)
plt.imshow(y, clim=None, cmap='gray');
plt.title("immagine filtrata con filtro gaussiano")

plt.tight_layout()
    
    
    
    

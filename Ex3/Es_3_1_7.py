# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:43:58 2025

@author: david
# """

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import mylib as ml

# Segmentazione delle vene. Si vogliono identificare le vene nell’immagine del fondo oculare retina.tif
# attraverso opportuna segmentazione. A tale scopo scrivete una funzione function y = segmenta(x)
# che realizza i passi descritti di seguito sulla banda verde (G) dell’immagine.
# (a) Effettuate un’elaborazione a finestra scorrevole usando le seguenti 4 maschere 7 × 7:
# Per ogni maschera bisogna valutare la differenza tra la media dei pixel nelle quattro direzioni di
# interesse (regione evidenziata in bianco) e la media calcolata nella restante parte del blocco (regione
# evidenziata in nero);
# (b) per ogni pixel dell’immagine calcolate il minimo valore delle quattro differenze cos`ı ottenute;
# (c) realizzate un thresholding con soglia pari a −5 per ottenere una mappa binaria;
# (d) infine, eliminate il cerchio esterno che limita la retina.
# Mostrate a video l’immagine originale e la mappa di segmentazione.

x = np.float64(io.imread('../immagini/retina.tif'))/255

plt.figure()
plt.imshow(x, cmap='gray', clim=None)
plt.colorbar();
plt.title('retina')

def segmenta(x):
    g= x[:,:,1] #banda green sceglie il 2elemento sulla 3dim
    
    m1= np.zeros((7, 7), dtype=int) #orizzontale
    m1[3, :] = 1  # Riga centrale
    m2 = m1.T
    m3=np.eye(7, dtype=int)
    m4= m3.T
    
    #array maschere
    masks = np.stack( (m1,m2,m3,m4), 0)
    
    
    #normalizza i valori delle maschere
    #pixel_bianco/#bianchi
    #pixel_nero/#neri
    
    # maschere per i bianchi
    masks_bianco = masks / np.sum(masks, (1,2), keepdims=True) #crea le maschere dividendo i valori alti per il numero totali di valori alti
    
    # maschere per i neri
    masks_nero   = (1-masks) / np.sum((1-masks), (1,2), keepdims=True) 
    
    #elaborazione con maschere
    M,N =  g.shape
    y= np.zeros((M,N,4))
    for i in range(4): #itera per ciascuna tipologia di maschera
        y[:,:,i] = ndi.correlate(g, masks_bianco[i]) - ndi.correlate(g, masks_nero[i]) #differenza fra le due elaborazioni
    
    #per ogni pixel calcola il minimo valore tra le quattro differenze ottenute
    y = np.min(y,2)
    
    #thresholding per ottenere mappa binaria
    y= y < -5/255
    
    #eliminazione del cerchio esterno che limita la retina
    j,i = np.meshgrid(np.arange(N)-N/2, np.arange(M)-M/2) #fissa il centro dell'immagine come origine 0,0
    m = (j**2 + i**2) < 0.2*N*M #raggio < 1/5 delle delle dimensioni
    y = y*m
    return y
        
y = segmenta(x)
plt.figure(2)
plt.imshow(y, clim=[0,1], cmap='gray')
plt.title('risultato');
































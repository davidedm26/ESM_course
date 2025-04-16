# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:21:14 2025

@author: david
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph

x= np.float64(io.imread('../Immagini/granelli_riso.tif'))
plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')

b = morph.disk(7)

plt.figure()
plt.imshow(b, clim=None, cmap='gray') #non servono tag
plt.title('Elemento strutturante')


#OPENING E CLOSING
#Rimuovere oggetti piccoli mantenedo le dimensioni degli oggetti piu grandi

# plt.close('all')
# x= np.float64(io.imread('../Immagini/immagini_lab_morfologia/DIP3E_Original_Images_CH09/circbw.tif'))
# plt.figure(1)
# plt.imshow(x, clim=[0,1], cmap='gray')

#RECUPERARE


#ESTRAZIONE DEI BORDI
#Possiamo estrarre i bordi attraverso l'erosione (erosione e differenza con immagine originale) 
#+ dilatazione per aumentare spessore della linea ottenuta
# plt.close('all')
# x= np.float64(io.imread('../Immagini/circbw.tif'))
# plt.figure(1)
# plt.imshow(x, clim=[0,1], cmap='gray')

# Trasformazione Hit-or-Miss


#Esercizio in classe proposto dalla prof
#Prendere immagine '/immagini_lab_morfologia/cells.tif' e fare le operazioni per evidenziare i contorni delle cellule
#e mappare in due mappae cellule scure e cellule chiare

plt.close('all')
x= io.imread('../Immagini/cells.png')
plt.figure(1)
plt.imshow(x, clim=[0,1], cmap='gray')

#evidenziare i contorni 
#




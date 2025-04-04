# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 15:27:17 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

# Rumore sale e pepe. Scegliete un’immagine, quindi aggiungete rumore sale e pepe (usate la funzione
# skimage.util.random noise), applicate il filtro mediano e valutate il risultato sia visivamente sia
# tramite l’errore quadratico medio se la dimensione della finestra `e 5, 7, 9.

plt.close('all')
#rumore sale e pepe

x=ml.leggiJpeg('../immagini/dorian.jpg')

from skimage.util import random_noise
# # Add salt-and-pepper noise to the image.
noisy = random_noise(x/255, 's&p') *255
ml.showImage(x, 'original')
ml.showImage(noisy, 'noisy')




arr_k = np.array([5,7,9])

for k in arr_k:
    y = ndi.median_filter(x,k) #applicazione filtro mediano
    ml.showImage(y, f'median filtered img k={k}' ) 
   
    qse= np.mean( (y-x)**2  )  #calcolo errore quadratico medio 
    print (qse)

#I valori del QSE crescono col cresce della dimensione della finestra di filtraggio mediano
# 33.82203674316406
# 39.31272888183594
# 44.220977783203125


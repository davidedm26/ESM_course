# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:47:44 2025

@author: DavideDiMatteo
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

# 2. Smoothing seguito da thresholding. Un’importante applicazione dei filtri che realizzano la media spaziale
# `e quello di sfocare l’immagine in modo da confondere con lo sfondo oggetti piccoli di poco interesse ed
# enfatizzare oggetti pi`u grandi, che quindi possono essere facilmente rilevati. Consideriamo, ad esempio,
# l’immagine spazio.jpg, proveniente dal telescopio Hubble, in orbita intorno alla terra. Realizzate le
# seguenti operazioni:
# (a) visualizzate l’immagine;
# (b) applicate il filtro che effettua la media aritmetica su una finestra di dimensioni 15×15 e visualizzate
# il risultato;
# (c) realizzate un’operazione a soglia (thresholding ) per eliminare oggetti piccoli, in particolare considerate
# una soglia pari al 25 per cento del valore massimo presente nell’immagine filtrata;
# (d) visualizzate il risultato dell’elaborazione.
# Noterete che la scelta della dimensione della maschera deve essere confrontabile con gli oggetti che si
# vogliono trascurare, provate a modificarne la dimensione e valutatene gli effetti, variando anche la soglia
# opportunamente.

#visualizzo img
x = ml.leggiJpeg('../immagini/space.jpg')
x= np.float64(x)
ml.showImage(x, 'space')

#filtro gaussiano
y = ndi.uniform_filter(x, size=15);
ml.showImage(y, 'immagine filtrata')


max_in_filtered = np.max(y);
print(max_in_filtered);
soglia = max_in_filtered*0.30

mask = y>soglia   #la maschera vale 1 solo dove l'immagine y(filtrata) è maggiore della foglia
ml.showImage(mask, 'maschera')
x = mask*x
ml.showImage(x, 'x filtrata')

#soluzione alternativa
# x[y<soglia] = 0
# ml.showImage(x, 'x filtrata')
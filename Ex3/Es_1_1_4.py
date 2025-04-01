# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 11:26:54 2025

@author: DavideDiMatteo
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

#filtraggio spaziale adattativo
# Aggiungete rumore gaussiano per σ = 5, 10, ..., 35 all’immagine barbara.gif e
# tracciate la curva in cui mostrate l’MSE tra immagine originale e filtrata al variare di σ. Per realizzare
# un confronto tracciate poi sullo stesso grafico la curva relativa al filtro media aritmetica.
# N.B. Utilizzare il comando generic filter che permette di realizzare un’operazione a finestra scorrevole.

#lo facciamo in due modi

#1 modo standard senza generic filter
#calcolare le var locali ( con generic filter e uso della funzione np.std)
#la formula data lavora pixel per pixel quindi avrò bisogno di una maschera

x= ml.leggiJpeg('../immagini/barbara.png')
ml.showImage(x, 'input')

M,N = x.shape
x = np.float64(x)

d= 25 #arbitrario , ci permette di scegliere la deviazione standard che vogliamo a partire dalla dist.normale
n = d* np.random.randn(M,N) #rand n sta per distribuzione NORMALE
noisy = x + n

ml.showImage(noisy, 'noisy')

K=7

glob_var= np.var(noisy)
var_loc = ndi.generic_filter(noisy, np.var, (K,K))
mean_loc= ndi.generic_filter(noisy, np.mean, (K,K))


y = noisy - (d**2/var_loc)*( noisy - mean_loc) 

ml.showImage(y, 'filtro adattativo')

###RIVEDERE a casa dalla registrazioe














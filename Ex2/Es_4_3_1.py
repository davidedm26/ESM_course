# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:53:23 2025

@author: david
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import bitop as bo
import mylib as ml
from skimage.transform import rescale
from skimage.transform import warp, rotate
# Distorsione. Scrivete la funzione che realizza la distorsione di un’immagine lungo la direzione verticale e
# orizzontale e che abbia il prototipo: deforma(x,c,d). Scegliete un’immagine e al variare dei parametri
# c e d osservate il tipo di distorsione.


x= ml.leggiJpeg('../immagini/lena.jpg')
y = ml.deforma (x,1,1); 

y= ml.ruota(x, -np.pi/2)
ml.showImage(y, 'ruotata')   
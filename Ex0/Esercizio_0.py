# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 09:42:44 2025

@author: david
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

#esercizio A

def clip(x, limit):
    
    y = np.copy( x )
    
    for i in range(len(x)):
        if (x[i] > limit):
            y[i] = limit
        # elif x[i]< -limit:
        #     y[i]= -limit;
    return y

def clip(x):
    y = np.sort( np.copy(x) )
    z= y[-4:]
    return z
    
        

vettore = np.array([-10, 3, -6, 0, 1, -2, 3, 4, -15, 3, 21])
limite = 8

risultato = clip(vettore)
print(risultato)









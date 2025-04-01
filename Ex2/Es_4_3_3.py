# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:01:37 2025

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
from skimage.data import checkerboard

# Combinazione di operazioni geometriche. Scrivete una funzione dal prototipo rot shear(x,theta,c)
# per realizzare una rotazione e poi una distorsione verticale (attenzione all’ordine!). Fate le due operazioni
# rispetto al centro dell’immagine. Create l’immagine di ingresso usando il seguente comando x =
# np.float64(skimage.data.checkerboard()) in modo da generare una scacchiera su cui le modifiche
# risultano essere pi`u facilmente visibili.

def rot_shear(x, theta, c):
    M,N= x.shape
    T1 = np.array([[1,0,0],[0,1,0],[M/2,N/2,1]], dtype=np.float32)
    T2 = np.array([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),0],[0,0,1]], dtype=np.float32)
    T3 = np.array([[1,0,0],[0,1,0],[-M/2,-N/2,1]], dtype=np.float32)
    T4 = np.array([[1,0,0],[c,1,0],[0,0,1]], dtype=np.float32)
    
    T=T4@T3@T2@T1
    A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta
    
    y = warp( x, A, order=1)
    return y

x= np.float64(checkerboard())
y = rot_shear(x, np.pi/2, 3)
ml.showImage(y, 'immagine ruotata e deformata')


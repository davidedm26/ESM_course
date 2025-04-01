# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 19:36:55 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist
from skimage.transform import rescale
from skimage.transform import warp, rotate

def leggiJpeg(nomefile):
    x = io.imread(nomefile)
    return x;
    # plt.figure()
    # plt.imshow(x, clim=[0,255], cmap='gray')
    
def showImage(x, label): #mostra immagine con parametri None e Gray
    plt.figure()
    plt.imshow(x, clim=None, cmap='gray')
    plt.title(label)

def showHist(x, label):
    plt.figure()
    plt.hist(x.flatten(),256)
    plt.title('hist of '+ label)

# def show_histogram(x):
#     n, b = np.histogram(x, np.arange(257))  # istogramma
#     plt.figure()
#     plt.bar(np.arange(256), n)
#     plt.axis([0,255,0,1.1*np.max(n)])
#     plt.title('Istogramma di %d' %x)
    
def vediRAW(nomefile, nRighe, nColonne, tipo):
    x= np.fromfile(nomefile, tipo)
    x= np.reshape(x, (nRighe, nColonne))
    plt.figure()
    plt.imshow(x, clim=[0,255], cmap='gray')
    

#funzione che fa il Full Scale Histogram Strecth
#calcolo min calcolo max
# y = (k-1) (x-xmin)/(xmax - x)

def  fshs(x, k=256):
    # k = 256
    x_min = np.min(x);
    x_max = np.max(x);
    y = (k-1)* ( (x-x_min)/(x_max-x_min))
    return y

def  glob_equaliz(x):
    y = equalize_hist(x) #equalizza fra 0 e 1
    y = 255*y
    return y

def loc_equaliz(x):
    x = np.reshape(x, (3,3))
    x = equalize_hist(x/255)
    y = x[1][1];
    return y;

def deforma(x,c,d):
    x= x[::c, ::d]
    return x

def ruota(x, theta):
    M,N= x.shape
    T1 = np.array([[1,0,0],[0,1,0],[M/2,N/2,1]], dtype=np.float32)
    T2 = np.array([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),0],[0,0,1]], dtype=np.float32)
    T3 = np.array([[1,0,0],[0,1,0],[-M/2,-N/2,1]], dtype=np.float32)

    T= T3@T2@T1
    A = T[[1,0,2],:][:,[1,0,2]].T #inverte righe e colonne e fa la trasposta
    y = warp( x, A, order=1)
    return y;
    







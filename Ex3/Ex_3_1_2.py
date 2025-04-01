# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:00:41 2025

@author: david
"""

#Enhancement
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

plt.close('all')


x=ml.leggiJpeg('../immagini/luna.jpg')
x= np.float64(x)

h = np.array ( [ [0,-1,0],[-1,5,-1],[0,-1,0]  ])

y = ndi.correlate(x, h)

ml.showImage(y, 'filtrata con laplaciano' )
plt.colorbar()

# ml.showHist(y, 'hist')


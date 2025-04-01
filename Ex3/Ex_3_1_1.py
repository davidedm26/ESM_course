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

plt.close('all')
#rumore sale e pepe

x=ml.leggiJpeg('../immagini/dorian.jpg')

from skimage.util import random_noise
# # Add salt-and-pepper noise to the image.
# noisy = random_noise(x/255, 's&p') *255
ml.showImage(x, 'original')
# ml.showImage(noiys, 'noisy')

#applicazione filtro mediano
y = ndi.median_filter(x,5)

ml.showImage(y, 'median filtered img')
#calcolo errore quadratico medio 
qse= np.mean( (y-x)**2  )



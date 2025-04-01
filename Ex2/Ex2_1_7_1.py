# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 20:11:50 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage import exposure

import mylib as ml

x = io.imread('./immagini/quadrato.tif')
plt.figure(1); plt.imshow(x, clim=[0,255], cmap='gray');
plt.title('Pre-equalizzazione')
plt.figure(2);plt.hist(x.flatten(), 256)
plt.title('Pre-equalizzazione')

y = ml.glob_equaliz(x);
plt.figure(3); plt.imshow(y, clim=[0,255], cmap='gray');
plt.title('post-equalizzazione')
plt.figure(4);plt.hist(y.flatten(), 256)
plt.title('post-equalizzazione')

z = ndi.generic_filter(x, ml.loc_equaliz, (3,3));
ml.showImage(z, 'post equalizz. locale');
ml.showHist(z, 'post eq loc')

k = ml.fshs(z);
ml.showImage(k, 'post equalizz. locale + fshs');
ml.showHist(k, 'post eq loc + fshs')




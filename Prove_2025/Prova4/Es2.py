# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 15:53:57 2025

@author: david
"""

#ES2
import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

x = np.load('../immagini/dati.npy')
# plt.imshow(x, clim=None, cmap='gray')

#L'immagine fornita non corrisponde a quella richiesta dalla traccia!
import scipy.io
import numpy as np

# Carica il file .mat
mat_data = scipy.io.loadmat('../immagini/img_SAR.mat')

# Esamina il contenuto per capire quale variabile contiene l'immagine
# Ad esempio, se l'immagine è memorizzata in una variabile chiamata 'image'
image = mat_data['img']  # sostituisci 'image' con il nome corretto

# Salva come file .npy
np.save('image.npy', image)
x = image
# x = 255 * (x - np.min(x)) / (np.max(x) - np.max(min))
plt.figure()
plt.imshow(x, clim = [0,1], cmap='gray')






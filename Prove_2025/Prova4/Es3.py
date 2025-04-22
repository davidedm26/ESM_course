# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 16:13:24 2025

@author: david
"""

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as color

plt.close('all')
# x1=io.imread('../Immagini/img1.png')
# plt.figure(1)
# plt.imshow(x1, clim=None, cmap='gray')
# plt.title('Immagine di input 1')

# #-------------------------------------#
# # x2=io.imread('../Immagini/img2.png')
# # plt.figure(2)
# # plt.imshow(x2, clim=None, cmap='gray')
# # plt.title('Immagine di input 2')
# # #----------------------------------------#
# # # Realizzate tutte le operazioni che ritenete necessarie per ottenere la mappa di
# # # segmentazione binaria in cui avete localizzato il difetto delle immagini img1.png e img2.png.




# #vedo maschera della varianza
# var = ndi.generic_filter(x1, np.var, (4,4))
# plt.figure('Im1 - VAR')
# plt.imshow(var, clim=None, cmap='gray')



# var_med = ndi.median_filter(var, (10,10))

# var_med = var_med <10
# var_med = morph.binary_erosion(var_med, morph.rectangle(3,3))
# plt.figure('VAR ELABORATA')
# plt.imshow(var_med , clim=None, cmap='gray')

# #vedo maschera della varianza
# var = ndi.generic_filter(x2, np.var, (4,4))
# plt.figure('Im2 - VAR')
# plt.imshow(var, clim=None, cmap='gray')


# var_med = ndi.median_filter(var, (10,10))
# plt.figure('VAR ELABORATA (2)')
# plt.imshow(var_med <10, clim=None, cmap='gray')


# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 17:56:22 2025

prova 4, ex 3
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
plt.close('all')

x1 = np.float64(io.imread('../Immagini/img1.png'))
x2 = np.float64(io.imread('../Immagini/img2.png'))


m1 = ndi.gaussian_filter(x1, (10,10))<15
m2 = ndi.gaussian_filter(x2, (10,10))<15

plt.figure()
plt.subplot(1,2,1)
plt.imshow(x1, clim=[0,255], cmap='gray')
plt.title('immagine')
plt.subplot(1,2,2)

plt.imshow(m1, clim=[0,1], cmap='gray')
plt.title('risultato')

import skimage.morphology as morf
m1 = morf.dilation(m1, morf.disk(50)) 

plt.figure()
plt.subplot(1,2,1)
plt.imshow(x2, clim=[0,255], cmap='gray')
plt.title('immagine')
plt.subplot(1,2,2)
plt.imshow(m1, clim=[0,1], cmap='gray')
plt.title('risultato')





















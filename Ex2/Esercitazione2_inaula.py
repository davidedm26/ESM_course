# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 10:37:15 2025

@author: david
"""


import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage import exposure

import mylib as ml

# mask = x>0 #prende una matrice e verifica quando il singolo valore è maggiore di 0 ( restituisce una matrice booleana)

# x[mask] = 0 ##annulla tutti i valori maggiori di 0 x[true]

#psso compattare i due comandi
# x[x>255] = 255 ##operazione di saturazione

# plt.close();

# x = io.imread('./immagini/granelli.jpg')
# x = np.float64(x)

# plt.figure(1);
# plt.imshow(x, clim=[0,255], cmap='gray')


# # #per capire di quanto fare l'offset andiamo a vedere quanto vale il min e il max dell'immagine

# x_min = np.min(x)
# x_max= np.max(x);

# # #vediamo che il min è 90 e il max 138 dunque possiamo aggiungere anche 100 livelli per schiarirla

# y = x +50;

# plt.figure(2);
# plt.imshow(y, clim=None, cmap='gray')

# y_str = ml.fshs(y, 256)

# plt.figure(3);
# plt.imshow(y_str, clim=[0,255], cmap='gray')
 

# plt.figure(4);
# plt.imshow( 255-x, clim=[0,255], cmap='gray')
# plt.title('y invertita')

# plt.figure(5)
# plt.hist(y_str.flatten(), bins=256); #flatten vettorizza la matrice, bins sono i livelli di grigio
# # plt.xlim((0,255))

# # plt.figure(5)
# # plt.hist(y_str.flatten(), bins=256); #flatten vettorizza la matrice, bins sono i livelli di grigio
# # plt.xlim((0,255))

# for i in range(0, 5):
#     plt.close();


# # ###TRASFORMAZIONE LOG E POTENZA
# x = io.imread('./immagini/spettro.jpg')
# x = np.float64(x)
# plt.figure(1);plt.imshow(x, clim=None, cmap='gray');

# y= np.log(x+1) #mettiamo +1 per evitare log0 #quest'operazione modifica i livelli di grigio
# plt.figure(2); plt.imshow(np.log(x+1), clim=None, cmap='gray'); #se non voglio modificare i livelli di grigio ma voglio solo vederli 
# # #posso mettere il log direttamente nella visualizzazione

# plt.close('all');


# # ##prova di potenza su vista aerea
# x= io.imread('./immagini/vista_aerea.jpg')
# y = x**0.9
# plt.figure(1);plt.imshow(x, clim=[0,255], cmap='gray');
# plt.figure(2); plt.imshow(y, clim=[0,255], cmap='gray'); #se non voglio modificare i livelli di grigio ma voglio solo vederli 

# plt.close('all');

#equalizzazione dell'istogramma
# z= io.imread('./immagini/marte.jpg')
# plt.figure(1);plt.imshow(z, clim=[0,255], cmap='gray');
# plt.figure(2); plt.hist(z.flatten(), 256);
# plt.close()
x = io.imread('../immagini/granelli.jpg')
plt.figure(1); plt.imshow(x, clim=[0,255], cmap='gray');
plt.figure(2); plt.hist(x.flatten(), 256);

from skimage.exposure import equalize_hist
y = equalize_hist(x)
y = 255*y

plt.figure(3); plt.imshow(y, clim=[0,255], cmap='gray');
plt.figure(4); plt.hist(y.flatten(), 256);

# h = np.histogram(z)
# plt.figure(2)
# plt.imshow(h)

# z = exposure.equalize_hist(z);
# plt.imshow(z, clim=[0,255], cmap='gray');







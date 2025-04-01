# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:50:19 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import bitop as bo

#esercizio 2_1_1

# Ricostruzione mediante bit-plane. Ponete a zero i bit-plane meno significativi di un’immagine (usate
# la funzione bitset del file bitop.py ) e visualizzate il risultato al variare del numero di bit-plane che
# utilizzate nel processo di ricostruzione. Questo esperimento vi permette di stabilire fino a che punto
# (almeno da un punto di vista percettivo) sia possibile diminuire il numero di livelli usati nel processo di
# quantizzazione.

x= io.imread( '../Immagini/frattale.jpg')

# Mostra tutti i bitplane in una singola figura
plt.figure(figsize=(12, 6))  # imposta la dimensione della figura
for i in range(8):
    x = bo.bitset(x, i, 0)
    plt.subplot(2, 4, i + 1)  # crea una griglia 2x4 per i subplot
    plt.imshow(x, clim=[0, 255], cmap="gray")
    plt.title("Bitplane %d-esimo annullato" % i)
    plt.axis('off')  # nasconde gli assi per una visualizzazione più pulita

plt.tight_layout()  # regola automaticamente i layout per prevenire sovrapposizioni
plt.show()

plt.close('all')

# 2. Esempio di Watermarking. Provate adesso a realizzare una forma molto semplice di watermarking,
# che consiste nell’inserire una firma digitale all’interno di un’immagine. Sostituite il bit-plane meno
# significativo dell’immagine lena.y con l’immagine binaria marchio.y. Quest’ultima ha dimensioni 350×350
# quindi `e necessario estrarre una sezione delle stesse dimensioni dell’immagine lena.y. Provate poi a
# ricostruire l’immagine e visualizzatela, noterete che da un punto di vista visivo l’immagine non ha subito
# modifiche percettibili.
# Ripetete l’esperimento inserendo il watermark in un diverso bit-plane.

x = np.fromfile('../immagini/lena.y', np.uint8) #leggo cosi perchè il formato è .y
x = np.reshape( x, (512,512)) #reshape per poter lavorare con la libreria .plt

#devo tagliare x perchè il watermark è 350x350
x = x[0:350, 0:350] #


plt.figure(1)
plt.subplot(2,2,1);
plt.imshow(x, clim=[0,255], cmap='gray')
plt.title('input')

mark = np.fromfile('../immagini/marchio.y', np.uint8)
mark = np.reshape( mark, (350,350))

# plt.figure(2)
plt.subplot(2,2,2);
plt.imshow(mark, clim=None, cmap='gray')
plt.title('mark')

#metti marchio nel bitplane meno significativo
y = bo.bitset(x, 0, mark)
# plt.figure(3)
plt.subplot(2,2,3);
plt.imshow(y, clim=None, cmap='gray')
plt.title('output')

#metti marchio nel bitplane 4 
y1 = bo.bitset(x, 4, mark)
# plt.figure(3)
plt.subplot(2,2,4);
plt.imshow(y1, clim=None, cmap='gray')
plt.title('output')

plt.tight_layout();
# plt.close();



# from skimage.transform import warp

# x = np.float32(io.imread('./immagini/lena.jpg'))
# x = x[252:277,240:290];
# M = x.shape[0]; N = x.shape[1]

# A = np.array([ [0.5,0,0], [0,0.5,0], [0,0,1]], dtype=np.float32)
# y1 = warp(x, A, output_shape=(2*M,2*N), order = 0)
# y2 = warp(x, A, output_shape=(2*M,2*N), order = 1)
# y3 = warp(x, A, output_shape=(2*M,2*N), order = 3)

# plt.subplot(3,1,1);
# plt.imshow(y1,clim=[0,255],cmap='gray'); plt.title('interpolazione nearest');
# plt.subplot(3,1,2);
# plt.imshow(y2,clim=[0,255],cmap='gray'); plt.title('interpolazione bilinear');
# plt.subplot(3,1,3);
# plt.imshow(y3,clim=[0,255],cmap='gray'); plt.title('interpolazione bicubic');


# # #Riguarda Laboratorio e svolgi tutti gli esercizi




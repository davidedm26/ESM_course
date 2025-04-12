# -*- coding: utf-8 -*-
"""
Lo spazio HSI. La rappresentazione HSV si ottiene con skimage.color.rgb2hsv. Il modello HSV
`e leggermente diverso da quello HSI, dato che il solido di riferimento `e una piramide rovesciata, con la
cima nell’origine a differenza del caso HSI in cui il modello `e una doppia piramide. Per questo motivo
per il passaggio nello spazio HSI usate le funzioni disponibili sul sito del corso nella sezione materiale
didattico.
Visualizzate le componenti HSI dell’immagine fragole.jpg e quelle dell’immagine cubo.jpg che rappresenta
proprio il cubo dei colori. In quest’ultimo caso si possono fare alcune interessanti considerazioni.
Nell’immagine di tinta, si pu`o notare la forte discontinuit`a lungo la linea a 45o sul piano frontale del
cubo, che `e quello del rosso: si ha infatti lungo questa linea la transizione brusca tra valori alti (360o) e
valori bassi (0o) della tinta, dovuta alla sua rappresentazione circolare. L’immagine di saturazione mostra
valori pi`u scuri verso il vertice del bianco, dove i colori diventano progressivamente meno saturi. Infine,
nell’immagine di intensit`a, ogni pixel `e semplicemente la media dei valori RGB del pixel corrispondente
nell’immagine a colori.
"""

import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml
import skimage.exposure as ex
import skimage.color as col
import color_convertion as cc

#Visualizzo Immagine input
x = io.imread('../immagini/fragole.jpg')
x = np.float64(x) / 255
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(x) #non servono tag
plt.title('Immagine FRAGOLE')

#Visualizzo Immagine input
y = io.imread('../immagini/cubo.jpg')
y = np.float64(y) / 255
plt.subplot(1,2,2)
plt.imshow(y) #non servono tag
plt.title('Immagine CUBO')
plt.tight_layout()

f_h = cc.rgb2hsi(x)
c_h = cc.rgb2hsi(y)

H = f_h[:,:,0]
S = f_h[:,:,1]
I = f_h[:,:,2]

plt.figure(2)
plt.subplot(1,3,1)
plt.imshow(H, cmap='gray') #non servono tag
plt.title('COMPONENTE H')
plt.subplot(1,3,2)
plt.imshow(S, cmap='gray') #non servono tag
plt.title('COMPONENTE S')
plt.subplot(1,3,3)
plt.imshow(I, cmap='gray') #non servono tag
plt.title('COMPONENTE I')

H = c_h[:,:,0]
S = c_h[:,:,1]
I = c_h[:,:,2]

plt.figure(3)
plt.subplot(1,3,1)
plt.imshow(H, cmap='gray') #non servono tag
plt.title('COMPONENTE H')
plt.subplot(1,3,2)
plt.imshow(S, cmap='gray') #non servono tag
plt.title('COMPONENTE S')
plt.subplot(1,3,3)
plt.imshow(I, cmap='gray') #non servono tag
plt.title('COMPONENTE I')







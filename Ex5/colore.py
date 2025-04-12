# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 11:31:53 2025

@author: david
"""

import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml
from skimage.color import rgb2hsv, hsv2rgb
import color_convertion as cc
import skimage.exposure as ex

#SPAZIO RGB
#Tutte le funzioni che lavorano con le immagini a colori si aspettano il range [0,1].
#Dobbiamo quindi normalizzare l'immagine SEMPRE (apparte per gli uint8 che vogliono 0,255)



#Correzione di Toni e Colori

x = io.imread('../immagini/colori.jpg')
x = np.float64(x)/255 # convertiamo nel range [0,1]
y = x ** 4
plt.figure(1);
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine orignale');
plt.subplot(1,2,2); plt.imshow(y); plt.title('Immagine elaborata in RGB');


# Si consideri poi l’immagine montagna.jpg, che presenta un aspetto complessivamente molto scuro. Si determini il valore di
# γ che consente di migliorarne il contrasto. Provate a realizzare la stessa operazione nello spazio HSI (lavorando
# solo sull’intensit`a) e confrontate i risultati.
x = io.imread('../immagini/montagna.jpg')
x = np.float64(x)/255 # convertiamo nel range [0,1]
y = x ** 0.4
plt.figure(2);
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine orignale');
plt.subplot(1,2,2); plt.imshow(y); plt.title('Immagine elaborata in RGB');

#Elaboro in HSI
x_hsi = cc.rgb2hsi(x)
h = x_hsi[:,:,0]
s = x_hsi[:,:,1]
i = x_hsi[:,:,2]
i_elab = i**0.4
y_hsi  = np.stack((h,s,i_elab),2)
x_hsi= cc.hsi2rgb(y_hsi)

plt.figure(3);
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine orignale');
plt.subplot(1,2,2); plt.imshow(x_hsi); plt.title('Immagine elaborata in HSI');


#EQUALIZZAZIONE
# Considerate l’immagine a colori volto.tiff e provate ad effettuare l’equalizzazione (utilizzando la
# funzione skimage.exposure.equalize hist) sia nello spazio RGB su ognuna delle componenti che
# nello spazio HSI solo sulla componente I (ricordate di ritornare nello spazio RGB per la visualizzazione).
# Confrontate le immagini ottenute con i due approcci. Cosa potete osservare?
plt.close('all')

x = io.imread('../immagini/volto.tiff')
x = np.float64(x)/255


#EQUALIZZO IN RGB SULLE SINGOLE COMPONENTI
R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

R = ex.equalize_hist(R)
G = ex.equalize_hist(G)
B = ex.equalize_hist(B)

y =  np.stack((R,G,B), -1)

plt.figure(1);
plt.subplot(2,2,1); plt.imshow(x); plt.title('Immagine orignale');
plt.subplot(2,2,2); plt.imshow(y); plt.title('Immagine equalizzata');
plt.subplot(2,2,3); plt.hist(x.flatten()); plt.title('Hist orignale');
plt.subplot(2,2,4); plt.hist(y.flatten()); plt.title('Hist equalizzato');
plt.tight_layout()

#EQUALIZZO IN HSI
x_hsi = cc.rgb2hsi(x)

H = x_hsi[:,:,0]
S = x_hsi[:,:,1]
I  = x_hsi[:,:,2]

I = ex.equalize_hist(I)
y = np.stack((H,S,I),-1)
y = cc.hsi2rgb(y)
plt.figure(2);
plt.subplot(2,2,1); plt.imshow(x); plt.title('Immagine orignale');
plt.subplot(2,2,2); plt.imshow(y); plt.title('Immagine equalizzata');
plt.subplot(2,2,3); plt.hist(x.flatten()); plt.title('Hist orignale');
plt.subplot(2,2,4); plt.hist(y.flatten()); plt.title('Hist equalizzato in HSI');
plt.tight_layout()

plt.close('all')

#Color Balancing
#Vogliamo cambiare un solo colore perchè ce n'è troppo o troppo poco

 # Considerate l’immagine foto.jpg, che presenta un’elevata quantit`a di ciano, e, dopo aver effettuato la
 # conversione nello spazio CMY, realizzate un bilanciamento delle componenti di colore cercando di riottenere
 # l’immagine originale (memorizzata in foto_originale.tif). Se lavorate sulle componenti normalizzate tenete
 # presente che per γ > 1 diminuite il peso del colore nell’immagine, il contrario accade per γ < 1

x = io.imread('../immagini/foto.jpg')
x = np.float64(x)/255 # convertiamo nel range [0,1]

y = io.imread('../immagini/foto_originale.tif')
y = np.float64(y)/255 # convertiamo nel range [0,1]

plt.figure(1);
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine orignale in RGB');
plt.subplot(1,2,2); plt.imshow(y); plt.title('Immagine da ricostruire');
#notiamo che c'è troppo ciano

x_cmy = ml.rgb2cmy(x)
C = x_cmy[:,:,0]
M = x_cmy[:,:,1]
Y = x_cmy[:,:,2]

C = C**1.79 ##per lambda>1 il colore si riduce viceversa aumenta
M = M**0.92

z = np.stack((C,M,Y),-1)

z = ml.cmy2rgb(z)

plt.figure(2);
plt.subplot(1,2,1); plt.imshow(y); plt.title('Immagine da ottenere');
plt.subplot(1,2,2); plt.imshow(z); plt.title('Immagine ricostruita');
    
plt.close('all')
#FILTRAGGIO SPAZIALE
# Supponiamo di considerare il filtro che realizza la media artitmetica dei valori che appartengono alla maschera
x = io.imread('../immagini/volto.tiff')
x = np.float64(x)/255 # convertiamo nel range [0,1]
#Filtro a media aritmetica
R = x[:,:,0]; G = x[:,:,1]; B = x[:,:,2];
k=3
fR = ndi.uniform_filter(R, (k,k))
fG = ndi.uniform_filter(G, (k,k))
fB = ndi.uniform_filter(B, (k,k))
y = np.stack((fR,fG,fB),-1)

plt.figure(1);
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine input');
plt.subplot(1,2,2); plt.imshow(y); plt.title('Immagine mediata');

 #In realtà c'è una funzione apposita
y = ndi.uniform_filter(x, (k,k,1 ))
plt.figure(2);
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine input');
plt.subplot(1,2,2); plt.imshow(y); plt.title('Immagine mediata');

#Se volessimo effettuare il filtraggio solo sulla componente I di HSI
from color_convertion import rgb2hsi, hsi2rgb
w = rgb2hsi(x)
H = w[:,:,0]; S = w[:,:,1]; I = w[:,:,2];
fI = ndi.uniform_filter(I, (k,k))
w = np.stack((H,S,fI),-1)
y = hsi2rgb(w)
plt.figure(3);
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine input');
plt.subplot(1,2,2); plt.imshow(y); plt.title('Immagine mediata');

# Si consideri allora l’immagine lenac.jpg, utilizzate un filtro di smoothing di dimensioni 5 × 5 operando su
# ogni singola componente RGB, provate poi a realizzare questa stessa operazione nello spazio YUV solo sulla
# componente di intensit`a. Confrontate le immagini ottenute sia visivamente che mostrando a video la differenza.
# Noterete che le due immagini non sono perfettamente identiche, ci`o `e dovuto al fatto che nello spazio RGB
# ogni pixel `e pari al color medio dei pixel nella finestra 5 × 5, mentre mediare solo le intensit`a non altera il
# colore originale dei pixel (dato che tinta e saturazione non sono stati modificati). Questo effetto aumenta
# al crescere della dimensione del filtro. Ripetete l’esperimento usando l’immagine fiori.tif con una finestra di
# dimensioni 25 × 25.

plt.close('all')
x = io.imread('../immagini/lenac.jpg')
x = np.float64(x)/255 # convertiamo nel range [0,1]

k=5
y = ndi.uniform_filter(x, (k,k,1))

plt.figure(1);
plt.subplot(1,3,1); plt.imshow(x); plt.title('Input');
plt.subplot(1,3,2); plt.imshow(y); plt.title('Filtro di smoothing in RGB');

#RGB : SINGOLE COMPONENTI
R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

#opero nello spazio YUV solo su intensità

Y =  0.299*R + 0.587*G + 0.114*B
U = -0.14713*R - 0.28886*G + 0.436*B
V =  0.615*R - 0.51499*G - 0.10001*B

Y = ndi.uniform_filter(Y,(k,k))

R = Y + 1.13983 * V
G = Y - 0.39465 * U - 0.58060 * V
B = Y + 2.03211 * U

y = np.stack((R, G, B), axis=-1)

plt.subplot(1,3,3); plt.imshow(y); plt.title('Filtro di smth in YUV');
plt.tight_layout()

#RIPETO CON FIORI.JPG
plt.close('all')
x = io.imread('../immagini/fiori.jpg')
x = np.float64(x)/255 # convertiamo nel range [0,1]

k=25
y = ndi.uniform_filter(x, (k,k,1))

plt.figure(1);
plt.subplot(1,3,1); plt.imshow(x); plt.title('Input');
plt.subplot(1,3,2); plt.imshow(y); plt.title('Filtro di smoothing in RGB');

#RGB : SINGOLE COMPONENTI
R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

#opero nello spazio YUV solo su intensità

Y =  0.299*R + 0.587*G + 0.114*B
U = -0.14713*R - 0.28886*G + 0.436*B
V =  0.615*R - 0.51499*G - 0.10001*B

Y = ndi.uniform_filter(Y,(k,k))

R = Y + 1.13983 * V
G = Y - 0.39465 * U - 0.58060 * V
B = Y + 2.03211 * U

y = np.stack((R, G, B), axis=-1)

plt.subplot(1,3,3); plt.imshow(y); plt.title('Filtro di smth in YUV');
plt.tight_layout()


# Infine provate a realizzare un esperimento in cui effettuate l’enhancement di un’immagine a colori mediante
# un filtro di sharpening. Applicate il filtro laplaciano all’immagine fiori.jpg, lavorate sia su RGB che su I,
# e confrontate i risultati. Per eseguire il filtraggio nell’immagine RGB tramite un singolo comando dovete
# estendere la maschera 2D in 3D tramite la funzione np.expand dims():
# h = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]], np.float64) # maschera 2D
# h = np.expand dims(h, -1) # maschera 3D
plt.close('all')
x = io.imread('../immagini/fiori.jpg')
x = np.float64(x)/255 # convertiamo nel range [0,1]

h = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]], np.float64) # maschera 2D per il filtraggio laplaciano
H = np.expand_dims(h, -1) # maschera 3D
y = ndi.correlate(x, H)

plt.figure(1);
plt.subplot(1,3,1); plt.imshow(x); plt.title('Input');
plt.subplot(1,3,2); plt.imshow(y); plt.title('Filtro di Laplaciano in RGB');

#RGB : SINGOLE COMPONENTI
R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

#opero nello spazio YUV solo su intensità

Y =  0.299*R + 0.587*G + 0.114*B
U = -0.14713*R - 0.28886*G + 0.436*B
V =  0.615*R - 0.51499*G - 0.10001*B

Y = ndi.correlate(Y,h)

R = Y + 1.13983 * V
G = Y - 0.39465 * U - 0.58060 * V
B = Y + 2.03211 * U

y = np.stack((R, G, B), axis=-1)

plt.subplot(1,3,3); plt.imshow(y); plt.title('Filtro di Laplaciano in YUV');
plt.tight_layout()



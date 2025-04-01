# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 11:48:08 2025

@author: DavideDiMatteo
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml

# #FILTRI DI SHARPENING
# Obiettivo dei filtri di sharpening `e quello di evidenziare o enfatizzare i dettagli di un’immagine. A tal fine si
# utilizzano operazioni che coinvolgono derivazioni del primo e secondo ordine in termini di differenze tra i valori
# dei pixel di un’immagine. Provate il filtro laplaciano sull’immagine luna.jpg e visualizzate il risultato:
    
x = ml.leggiJpeg('../immagini/luna.jpg')
x = np.float64(x);
ml.showImage(x, 'luna')
plt.colorbar()

h = np.array ( [[0,1,0],[1,-4,1],[0,1,0]])
y = ndi.correlate(x,h);
ml.showImage(y, 'filtrata sharp')
plt.colorbar()

# #se provo ad invertire i segni della maschera del filtro che succede?
# h = np.array ( [[0,-1,0],[-1,4,-1],[0,-1,0]])
# y = ndi.correlate(x,h);
# ml.showImage(y, 'filtrata sharp invertita')
# plt.colorbar()

# #enfatizziamo dettagli dell'immagine originale sommando il laplaciano

# #ASCOLTA NOTA ORE 11:57 nella registrazione

z= x - y
ml.showImage(z, 'enanchement')

plt.close('all')


# #POINT e LINE DETECTION
x= ml.leggiJpeg('../immagini/turbina.jpg')
x = np.float64(x)
ml.showImage(x,'turbina')
plt.colorbar();

h = np.array([ [-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
y = ndi.correlate(x,h);

ml.showImage(y, 'filtraggio con prima maschera')

# #vediamo che il range è molto frande e i valori tra 0 e  500 sono prevalenti, quindi non vedrò quelli a -2000
# #per risolvere questo problema imposto una soglia di valori che mi limita l'intervallo di visualizzazione

z = np.abs(y)
th = 0.9*np.max(z)
mask = z>th

ml.showImage(mask, 'maschera')
plt.colorbar()

plt.close('all')

# #LINE DETECTION
#applico filtri all'immagine quadrato
x= ml.leggiJpeg('../immagini/quadrato.jpg')
x = np.float64(x)
ml.showImage(x,'quadrato')
plt.colorbar();

h1 = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
y1 = ndi.correlate(x,h1)
ml.showImage(y1,'filtro 1 - varizioni verticali')
plt.colorbar();

h2 = np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
y2 = ndi.correlate(x,h2)
ml.showImage(y2,'filtro 2 - varizioni diagonale 2')
plt.colorbar();

h3 = np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
y3 = ndi.correlate(x,h3)
ml.showImage(y3,'filtro 2 - varizioni diagonale 1')
plt.colorbar();

h4 = np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
y4 = ndi.correlate(x,h4)
ml.showImage(y4,'filtro 2 - varizioni orizzontali')
plt.colorbar();

# #Quindi effettuate l’elaborazione che vi permette di
# # produrre un’unica mappa in cui sono presenti linee di qualsiasi tipo nell’immagine. Fate attenzione alla scelta
# # della soglia e al fatto che le maschere cos`ı definite vi permettono di rilevare bordi spessi un pixel.

# #voglio fare una nuova immagine che per ogni pixel prende il massimo fra le 4
z= np.stack((y1,y2,y3,y4), -1 ) #impilo lungo la terza direzione
z= np.max(z, -1);

plt.imshow(z, clim=[0,255], cmap='gray')
plt.title ('filtraggio finale')
plt.colorbar();

plt.close('all')

# #FINIRE ESERCITAZIONE
# #2.2
# Realizzate l’edge detection dell’immagine house.y di dimensioni 512×512 usando le maschere di Sobel per il calcolo
# del gradiente e scegliendo il valore della soglia pari a T = 1.5*np.mean(grad). Visualizzate l’immagine
# originale, il gradiente e la mappa dei contorni.
x = np.fromfile('../immagini/house.y', np.uint8)
x = np.reshape(x, (512,512))

ml.showImage(x, 'input')

h = np.array( [[-1,-2,-1],[0,0,0],[1,2,1] ] ) #maschera di sobel
h = np.array( [[-2,-1,-0],[-1,0,1],[0,1,2] ] ) #maschera di sobel

y = ndi.correlate(x, h) #gradiente

ml.showImage(y, 'gradiente')

soglia = 1.5*np.mean(y) 

mask = y > soglia
x= mask*x
ml.showImage(x, 'contorni')

# h2 = np.array( [[0,1],[-1,0] ] ) ##maschera di roberts

# y = ndi.correlate(x, h2) #gradiente

# ml.showImage(y, 'gradiente2')

# soglia = 1.5*np.mean(y) 

# mask = y > soglia
# y= mask*y
# ml.showImage(y, 'contorni')

plt.close('all')

#ESERCITAZIONE 4 inizia da qui

#EDGE DETECION BASATA SUL GRADIENTE

x= ml.leggiJpeg('../immagini/lena.jpg')
x= np.float64(x)
ml.showImage(x, 'input')

#calcoliamo manualmente il gradiente
# h1 = np.array([[0,0],[-1,1]])
# h2 = np.array([[0,-1],[0,1]])
##proviamo altre maschere
h1= np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
h2= np.array([[-1,0,-1],[-2,0,2],[-1,0,1]])

y1 = ndi.correlate(x,h1)
y2= ndi.correlate(x,h2)

g= np.sqrt(y1**2+y2**2)
ml.showImage(g, 'gradiente') #notiamo che i bordi diagonali non si vedono bene

#se volessimo ottenere una mappa di segmentazione dobbiamo applicare il tresholding (sogliatura)
T = 1.5*np.mean(g)
msk = g > T
ml.showImage(msk, 'mask')
#l'aspetto negativo è che il ths prende anche il rumore (vedremo operazioni morfologiche per risolvere)

plt.close('all')

#proviamo a fare smoothing prima del calcolo del gradiente
#controlla perchè non mi trovo
x= ml.leggiJpeg('../immagini/angiogramma.jpg')
x= np.float64(x)
ml.showImage(x, 'input')

y=ndi.gaussian_filter(x, 3)

#calcoliamo manualmente il gradiente
# h1 = np.array([[0,0],[-1,1]])
# h2 = np.array([[0,-1],[0,1]])
##proviamo altre maschere
h1= np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
h2= np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

y1 = ndi.correlate(y,h1)
y2= ndi.correlate(y,h2)

g= np.sqrt(y1**2+y2**2)
ml.showImage(g, 'gradiente') #notiamo che i bordi diagonali non si vedono bene

#se volessimo ottenere una mappa di segmentazione dobbiamo applicare il tresholding (sogliatura)
T = 1.5*np.mean(g)
msk = g > T
ml.showImage(msk, 'mask')



#LAPLACIANO DI UNA GAUSSIANA
#seg utills sta sul team, scaricalo da la

plt.close('all')
#laplaciano di una gaussiana
x = ml.leggiJpeg('../immagini/angio.16bit.png')
sigma=5
y = ndi.gaussian_laplace(x, (sigma,sigma))
ml.showImage(y, 'gauss-laplace')

# # from seg_utils import zero_crossing
# # z = zero_crossing(y)

# # ml.showImage(z, 'zero cross')











# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:51:33 2025

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
from skimage.transform import warp

# Immagini contraffatte. Nell’immagine mare.png una parte della scogliera `e stata duplicata. Si vuole individuare
# la regione copiata calcolando il secondo picco dell’autocorrelazione dell’immagine. Per ottenere
# Rx(l, k), la la funzione di autocorrelazione dell’immagine x(m, n), calcolate la trasformata di Fourier
# F[x(m, n)] = X(μ, ν), prendete il modulo quadro, e infine effettuate l’antitrasformata (per ridurre la
# complessit`a non considerate zero-padding)

#Visualizzo Immagine input
x = io.imread('../immagini/mare.png')

plt.imshow(x,clim=None,cmap='gray')
plt.title('Immagine input')

#PUNTO 1
# Visualizzate (usando il comando mesh) la funzione di autocorrelazione, usando opportunamente il
# comando fftshift per avere il picco al centro dell’immagine. Le coordinate spaziali andranno
# cos`ı da −N/2 ad N/2 − 1, con N numero di righe/colonne. Sul grafico sar`a possibile notare un
# secondo picco lontano dall’origine.
X = np.fft.fft2(x)

Rx = np.real(np.fft.ifft2( np.abs(X)**2 )) #Calcolo Rxx
Rx = np.fft.fftshift(Rx) #Allineo Rxx sullo 0

#Sistemo coordinate spaziali
Nr,Nc= Rx.shape
n = np.arange(Nc) - Nc/2
m = np.arange(Nr) - Nr/2
n,m = np.meshgrid(n,m)


plt.subplot(2,2,2)
plt.imshow(Rx, clim=None, cmap='jet', extent = (- Nc/2, Nc/2-1, Nr/2-1, - Nr/2))
plt.colorbar()
plt.title('autocorrelazione')

fig, ax = plt.subplots(num=2, subplot_kw={"projection": "3d"}) # 3d plot
ax.plot_surface(n,m,Rx, cmap='jet')

#PUNTO 2 Individuazione picchi
# Per individuare i picchi, prendete per ogni punto una finestra 5 × 5 e marcate il punto come picco
# solo se `e il massimo nella finestra. Il secondo di tali picchi `e quello cercato.
L = ndi.generic_filter(Rx, np.max, (5,5))== Rx #restituisce mappa dei massimi locali
p = np.sort(Rx[L]) #ordina i max locali
mappa = L & ( Rx == p[-2] )

#Coordinate del picco di interesse
tn = n[mappa]
tm = m[mappa]
print(tn[0],tm[0])

#PUNTO 3
# A questo punto, note le coordinate (m0, n0) del secondo picco, calcolate la differenza fra l’immagine
# di partenza e quella traslata di tali coordinate e marcate i punti per cui tale differenza `e nulla.
# Nell’immagine risultante sar`a chiaramente visibile la regione duplicata.

#definisco matrice di traslazione
A = np.array([[1,0, tn[0]], [0, 1, tm[0]], [0, 0, 1]])
y = warp(x,A) *255

mask = (x==y)

plt.figure(3)
plt.subplot(2,2,3)
plt.imshow(y, clim=[0,1], cmap='gray')
plt.title('immagine traslata')
plt.subplot(2,2,4)
plt.imshow(mask, clim=[0,1], cmap='gray')
plt.title('mask')
plt.tight_layout()














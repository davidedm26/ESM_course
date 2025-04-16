"""
Created on Tue Apr 15 15:38:17 2025

@author: david
"""

# 4. Demosaicking. La maggior parte delle fotocamere digitali acquisisce una sola informazione di colore
# (rosso, verde, oppure blu) per ogni pixel, secondo il pattern mostrato nell’immagine Mosaic.bmp, e
# produce quindi, per ogni canale di colore, una matrice in cui solo alcuni dei valori sono non nulli. Gli
# altri valori sono poi ottenuti mediante interpolazione bilineare di quelli disponibili.
# L’immagine Fiori mosaic.bmp contiene appunto, nelle tre componenti, le matrici prima dell’interpolazione.
# Scrivete una funzione function y = demosa1(x) in cui estraete le tre componenti, effettuate l’interpolazione,
# ricomponete l’immagine e confrontate il risultato, sia visivamente che in termini di SNR,
# con l’immagine vera Fiori256.bmp.
# Si pu`o migliorare la qualit`a attraverso un’interpolazione adattativa. A tale scopo scrivete una nuova
# funzione function y = demosa2(x) in cui per ogni pixel da interpolare considerate i valori dei
# due pixel pi`u vicini disponibili sulla stessa riga (W ed E) e sulla stessa colonna (N e S) e calcolate le
# differenze |W − E| e |N − S|. Se |W − E| > 3|N − S|, usate solo N e S per l’interpolazione, se vale
# il contrario usate solo W ed E, altrimenti procedete normalmente.


import skimage.io as io
import skimage.exposure as exp
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

x = io.imread('../immagini/Fiori_mosaic.bmp')

r, g, b = x[:, :, 0], x[:, :, 1], x[:, :, 2]

plt.figure(1)
plt.subplot(1,3,1)
plt.imshow(r, clim=[0,255], cmap='gray')
plt.title('R')
plt.subplot(1,3,2)
plt.imshow(g, clim=[0,255], cmap='gray')
plt.title('G')
plt.subplot(1,3,3)
plt.imshow(b, clim=[0,255], cmap='gray')
plt.title('B')

k=3
R = ndi.uniform_filter(r,(k,k))
G = ndi.uniform_filter(g,(k,k))
B = ndi.uniform_filter(b,(k,k))

plt.figure(2)
plt.subplot(1,3,1)
plt.imshow(R, clim=[0,255], cmap='gray')
plt.title('R')
plt.subplot(1,3,2)
plt.imshow(G, clim=[0,255], cmap='gray')
plt.title('G')
plt.subplot(1,3,3)
plt.imshow(B, clim=[0,255], cmap='gray')
plt.title('B')

plt.figure(3)
y = np.stack((R,G,B), -1)
plt.imshow(y);

#Miglioro risultato tramite interpolazione adattiva
def interpol(x):
    w= x[3]
    e= x[5]
    n= x[1]
    s= x[7]
    d1 = np.abs(w-e)
    d2 = np.abs(n-s)
    if ( ( d1 - d2 ) > 3*d2 ): #usa solo n e s
       return (n + s) / 2 
    #altrimenti usa solo w e e
    else :
        return(w + e) / 2

R = ndi.generic_filter(r, interpol,(k,k))
G = ndi.generic_filter(g, interpol,(k,k))
B = ndi.generic_filter(b, interpol,(k,k))

plt.figure(4)
plt.subplot(1,3,1)
plt.imshow(R, clim=[0,255], cmap='gray')
plt.title('R')
plt.subplot(1,3,2)
plt.imshow(G, clim=[0,255], cmap='gray')
plt.title('G')
plt.subplot(1,3,3)
plt.imshow(B, clim=[0,255], cmap='gray')
plt.title('B')

plt.figure(5)
y = np.stack((R,G,B), -1)
plt.imshow(y);












# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:34:21 2025

@author: DavideDiMatteo
"""

import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml


x = np.float64( io.imread('../immagini/rettangolo.jpg'))
plt.figure(1); plt.imshow(x, clim=None, cmap='gray');

#mostro lo spettro del modulo
X = np.fft.fft2(x)
plt.figure(2); plt.imshow(np.abs(X), clim=None, cmap='gray');
plt.title('spettro del modulo as is')

#non si vede bene devo manipolarla

# # #faccio shift e logaritmo
Y = np.log(1+np.abs(np.fft.fftshift(X)))
plt.figure(3);
plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('spettro del modulo manipolato')

#voglio vedere ora lo spettro della fase
plt.figure(4);
plt.imshow(np.angle(X), clim=None, cmap='gray')
plt.title('spettro della fase')



plt.close('all')



# #visualizzare la FFT in 3D solo per curiosità

#qua facciamo la trasformata su piu punti
#in particolare il doppio
#lo facciamo perchè vogliamo fare un'interpolazione 
#piu tranquilla (altrimenti ci vorrebbe la sinc)
M,N = x.shape
P = 2*M; Q = 2*N
X = np.fft.fft2(x, (P,Q)) #trasforma su piu punti 

Y = np.log(1+np.abs((np.fft.fftshift(X)))) #sistemo spettro ampiezza

m = np.fft.fftshift(np.fft.fftfreq(Y.shape[0])) 
n = np.fft.fftshift(np.fft.fftfreq(Y.shape[1]))
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(plt.figure()); # crea una figura per i grafici 3d
l,k = np.meshgrid(n,m)
ax.plot_surface(l,k,Y, linewidth=0, cmap='jet')

plt.close('all')


#USO della DFT per il filtraggio lineare
#prima parte monodimensionale puoi saltare
#
#
#
#parte bidimensionale
#FILTRAGGIO CLASSICO (PRODOTTO = CONVOLUZIONE NEL TEMPO)
# Se si considera  un'immagine, x[m, n], di dimensioni M×N e un filtro h[m, n] di dimensioni A×B,
# `e necessario calolare la DFT-2D su un numero di punti P e Q che soddisfino le condizioni P ≥ M + A − 1 e
# Q ≥ N + B − 1.
# Vediamo un esempio di implementazione nel dominio della frequenza del filtro di Sobel per
# la rivelazione dei bordi verticali.

x = np.float64(io.imread('../immagini/lena.jpg'))
plt.figure();
io.imshow(x, clim=None, cmap='gray');
#definisco filtro di sobel per bordi verticali
h = np.array([[1,0,-1],[2,0,-2],[1,0,-1]], dtype=np.float64)
M,N = x.shape
# A,B = h.shape
# P = M + A -1
# Q = N + B -1  #si può anche eviatre --> metti dim default
# X = np.fft.fft2(x, (P,Q))
# H = np.fft.fft2(h, (P,Q))
X = np.fft.fft2(x,(M,N)) #calcola DFT di x
plt.figure(); plt.imshow(np.abs(X), cmap="gray")

H = np.fft.fft2(h, (M,N)) #calcola DFT di h
Y = H * X #applica prodotto in frequenza che equivale a convoluzione nello spazio
y = np.real(np.fft.ifft2(Y)) #trascura piccola parte immaginaria
plt.figure(); plt.imshow(y, clim=None, cmap='gray');

y= ndi.convolve(x, h)
plt.figure(); plt.imshow(y, clim=None, cmap='gray');


# #PROGETTO DI FILTRI IN FREQUENZA
plt.close('all');

x = np.float64(io.imread('../immagini/lena.jpg'))
plt.figure(1);
io.imshow(x, clim=None, cmap='gray');
plt.title("LENA - input")


M,N = x.shape #definisce le dimensioni el filtro in base a quelle dell'immagine in input
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m) #sposta le coordinate centrando il centro in 0.0
D = np.sqrt(k**2+ l**2) #definisce rho di ciascun pixel
D0 = 0.3; #fissa una soglia (contorno cerchio)
H = (D <= D0) #definisce H come i punti interni al cerchio
plt.figure(2);
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("filtro sintetizzato")

X = np.fft.fft2(x) #calcola DFT
X = np.fft.fftshift(X) #centra in 0.0
plt.figure(3)
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Spettro delle ampiezze')

Y = H * X #prodotto in frequenza (filtraggio)
plt.figure(4);
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Prodotto in frequenza - esito del filtraggio nel dominio della frequenza')

Y = np.fft.ifftshift(Y) #ricostruzione nello spazio
y = np.real(np.fft.ifft2(Y))
plt.figure(5);
plt.imshow(y, clim=[0,255], cmap='gray');
plt.title('Ricostruzione nello spazio del segnale filtrato')

#FILTRAGGIO DI RUMORE PERIODICO
plt.close('all')
#visualizza lena rumorosa
x = np.fromfile('../immagini/lenarumorosa.y', np.int16)
x = np.reshape(x, [512,512])
x = np.float64(x)
plt.figure(); plt.imshow(x, clim=[0,256], cmap='gray');
plt.title('immagine rumorosa');

#trasforma img
X = np.fft.fftshift(np.fft.fft2(x));
plt.figure();
plt.imshow(np.log(1+np.abs(X)), clim=None, \
cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Trasformata di Fourier immagine rumorosa');

# Definizione del filtro
nu = 0.2; B = 0.03;
m = np.fft.fftshift(np.fft.fftfreq(X.shape[0]))
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1]))
l,k = np.meshgrid(n,m)
D1 = np.sqrt(k**2+(l-nu)**2)
D2 = np.sqrt(k**2+(l+nu)**2)
H = (D1>B) & (D2>B)
plt.figure();
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Riposta in frequenza del filtro');
# Filtraggio
Y = X * H;
plt.figure();
plt.imshow(np.log(1+np.abs(Y)), clim=None, \
cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Trasformata di Fourier immagine filtrata');

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)));
plt.figure(); plt.imshow(y, clim=[0,256], cmap='gray');
plt.title('Immagine filtrata');
# Calcolo MSE
xo = np.fromfile('../immagini/lena.y', np.uint8)
xo = np.reshape(xo, [512,512])
xo = np.float64(xo)
plt.figure(); plt.imshow(xo, clim=[0,256], cmap='gray');
plt.title('immagine originale');
MSE = np.mean((xo-y) ** 2)
print('MSE primo filtraggio:', MSE)
# plt.close('all')

#alternativa
# Definizione del filtro
# Bk = 0.004; Bl = 0.02
# H1 = (-Bk <= k) & (k <= Bk)
# H2 = (-Bl <= l) & (l <= Bl)
# H = (~H1) | (H2 & H1)
# plt.figure();
# plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
# plt.title('Riposta in frequenza del filtro');
# Y = X * H
# y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)));
# plt.figure(); plt.imshow(y, clim=[0,256], cmap='gray');
# plt.title('Immagine filtrata');
# MSE = np.mean((xo-y) ** 2)
# print('MSE secondo filtraggio:', MSE)

#L'Esecuzione dell'assistente non è convincente
plt.close('all')
#Svolgimento personale
#TOGLIERE LE DUE DELTA DALL'IMMAGINE RUMOROSA
#filtro elimina banda
#potremmo progettarre un filtro che toglie la griglia tipo maschera

M, N = X.shape
cx, cy = M // 2, N // 2 #coordinate del centro

#maschera di tutti 1
H = np.ones_like(X)

#parametri dei notch
raggio = 20  #raggio dei cerchi
offset = 102  #distanza dal centro sulla diagonale

#coordinate griglia
M,N = np.meshgrid(np.arange(M), np.arange(N))

# Primo cerchio sulla diagonale principale
mask1 = (N - (cx + offset))**2 + (M - (cy - offset))**2 <= raggio**2

# Secondo cerchio (simmetrico rispetto al centro)
mask2 = (N - (cx - offset))**2 + (M - (cy + offset))**2 <= raggio**2

# Applica i notch
H[mask1] = 0
H[mask2] = 0

# Filtraggio
Y = X * H;
plt.figure();
plt.imshow(np.log(1+np.abs(Y)), clim=None, \
cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Filtro sintetizzato');

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)));
plt.figure(); plt.imshow(y, clim=[0,256], cmap='gray');
plt.title('Immagine filtrata');
MSE = np.mean((xo-y) ** 2)
print('MSE secondo filtraggio:', MSE)





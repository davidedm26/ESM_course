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


# x = np.float64( io.imread('../immagini/rettangolo.jpg'))
# plt.figure(1)
# Y = np.fft.fft2(x)
# plt.figure(); plt.imshow(np.abs(X), clim=None, cmap='gray');

# # #faccio shift e ...
# X = np.log(1+np.abs(np.fft.fftshift(X)))
# # plt.figure(2);
# plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));


# #visualizzare la FFT in 3D solo per curiosità

# #qua facciamo la trasformata su piu punti
# #in particolare il doppio
# #lo facciamo perchè vogliamo fare un'interpolazione 
# #piu tranquilla (altrimenti ci vorrebbe la sinc)
# M,N = x.shape
# P = 2*M; Q = 2*N
# X = np.fft.fft2(x, (P,Q))

# Y = np.log(1+np.abs((np.fft.fftshift(X))))
# m = np.fft.fftshift(np.fft.fftfreq(Y.shape[0]))
# n = np.fft.fftshift(np.fft.fftfreq(Y.shape[1]))
# from mpl_toolkits.mplot3d import Axes3D
# ax = Axes3D(plt.figure()); # crea una figura per i grafici 3d
# l,k = np.meshgrid(n,m)
# ax.plot_surface(l,k,Y, linewidth=0, cmap='jet')



#FILTRO A MEDIA ARITMETICA NEL DOMINIO DELLA FREQ
# k=3;
# h = np.ones((k,k)/(k**2))

# P=100; Q=100
# X = np.fft.fft2(x, (P,Q))
# ml.showImage(X, 'fft')

#sistemare




#USO della DFT per il filtraggio lineare

#prima parte monodimensionale puoi saltare

#parte bidimensionale

#FILTRAGGIO CLASSICO (PRODOTTO = CONVOLUZIONE NEL TEMPO)

#NON FUNZIONA CAPISCIE PERCHé
x = np.float64( io.imread('../immagini/lena.jpg'))
h = np.array([[1,0,-1],[2,0,-2],[1,0,-1]], dtype=np.float64)
M,N = x.shape
# A,B = h.shape
# P = M + A -1
# Q = N + B -1  #si può anche eviatre --> metti dim default
# X = np.fft.fft2(x, (P,Q))
# H = np.fft.fft2(h, (P,Q))
X = np.fft.fft2(x,(M,N))
H = np.fft.fft2(h, (M,N))
Y = H * X
y = np.real(np.fft.ifft2(Y))
plt.figure(); plt.imshow(y, clim=None, cmap='gray');


#PROGETTO DI FILITRI IN FREQUENZA
#RIVEDERE
M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)
D = np.sqrt(k**2+ l**2)
D0 = 0.1;
H = (D <= D0)
plt.figure();
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

x = np.float64(io.imread('../immagini/lena.jpg'))
X = np.fft.fft2(x)
X = np.fft.fftshift(X)
plt.figure();
plt.imshow(np.log(1+np.abs(X)), clim=None, \
cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
Y = H * X
plt.figure();
plt.imshow(np.log(1+np.abs(Y)), clim=None, \
cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
Y = np.fft.ifftshift(Y)
y = np.real(np.fft.ifft2(Y))
plt.figure();
plt.imshow(y, clim=[0,255], cmap='gray');



#FILTRAGGIO DI RUMORE PERIODICO
plt.close('all')

x = np.fromfile('../immagini/lenarumorosa.y', np.int16)
x = np.reshape(x, [512,512])
x = np.float64(x)
plt.figure(); plt.imshow(x, clim=[0,256], cmap='gray');
plt.title('immagine rumorosa');
X = np.fft.fftshift(np.fft.fft2(x));
plt.figure();
plt.imshow(np.log(1+np.abs(X)), clim=None, \
cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Trasformata di Fourier immagine rumorosa');

#TOGLIERE LE DUE DELTA DALL'IMMAGINE RUMOROSA
#filtro elimina banda
#potremmo progettarre un filtro che toglie la griglia tipo maschera









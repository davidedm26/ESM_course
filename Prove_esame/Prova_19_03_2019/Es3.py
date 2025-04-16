# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 19:59:02 2025

@author: david
"""
import skimage.io as io
import skimage.color as clr
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np


#Ex3
x = io.imread('./a.png')
plt.figure(1)
plt.imshow(x)
plt.title('input')




x= np.float64(x)

# Progettate un filtro passa-alto ideale nel dominio della frequenza di raggio 0,25 con risposta
# in frequenza come mostrata in figura filtro_HP.jpg
M= x.shape[0]
N= x.shape[1]
m = np.fft.fftfreq(M)
n = np.fft.fftfreq(N)

l,k = np.meshgrid(n,m)
r = 0.25
mask = (l**2+k**2) < r**2
plt.figure(2)
plt.imshow(mask, clim=[0,1], cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('mask sintetizzata')

#Converti immagine in scala di grigi
y = clr.rgb2gray(x)

#Filtriamo immagine in frequenza col filtro costruito
Y = np.fft.fftshift( np.fft.fft2(y))

plt.figure(3)
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('Trasformata della versione in scala di grigi')

Z = Y*mask

plt.figure(4)
plt.imshow(np.log(1+np.abs(Z)), clim=None, cmap='gray', extent=[-0.5,0.5,-0.5,0.5])
plt.title('Risultato del filtraggio')

#Calcola energia di Z nel dominio della frequenza
E = np.mean( np.abs(Z)**2 )
print(E)

if (E > 8000 ):
    print('IMMAGINE GENERATA SINTETICAMENTE')
else:
    print('IMMAGINE NATURALE')





# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:46:37 2025

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


# Spettro di fase. Per comprendere l’importanza dello spettro di fase provate a realizzare il seguente
# esperimento. Considerate l’immagine volto.tif e dopo averne calcolato e visualizzato spettro di ampiezza
# e di fase, ricostruite l’immagine con la sola informazione di ampiezza e poi solo con quella di fase e
# confrontate le due immagini.


x = np.float64( io.imread('../immagini/volto.tif'))
ml.showImage(x, 'input')

X = np.fft.fft2(x) #faccio trasformata
Y = np.log(1+np.abs(np.fft.fftshift(X))) #shift + modulo
plt.figure();
plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('modulo - spettro')

plt.figure();
Y = np.angle(np.fft.fftshift(X))
plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('modulo - fase')


X1 = np.abs(X) #cancello fase
X2 = np.exp(1j*np.angle(X)) #cancello ampiezza

y1 = np.real(np.fft.ifft2(np.fft.ifftshift(X1))) #la parte imm non ci dovrebbe stare ma faccio cast a real per sicurezza
y2 = np.real(np.fft.ifft2(np.fft.ifftshift(X2)))

ml.showImage(y1-np.min(y1)**0.1, 'ricostruzione da modulo')
ml.showImage(y2, 'ricostruzione da fase')

#rivedere script DC
















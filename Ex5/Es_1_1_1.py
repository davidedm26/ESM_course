
"""
1. Lo spazio CMY e CMYK. Se le componenti RGB sono state normalizzate nel range [0, 1] `e molto facile
ottenere le componenti nello spazio CMY (Cyan, Magenta, Yellow), dato che queste componenti sono
le complementari di quelle RGB.
Provate a scrivere una funzione con il seguente prototipo: rgb2cmy(x), che legge un’immagine a
colori e determina la rappresentazione CMY dell’immagine fragole.jpg visualizzandone le componenti.
Scrivete poi una funzione dal prototipo: rgb2cmyk(x) che legge un’immagine a colori e determina la
rappresentazione CMYK (Cyan, Magenta, Yellow, Black) di un’immagine visualizzandone le componenti.
Tenete presente che quando si usano i pigmenti, il nero si ottiene usando uguali quantit`a dei pigmenti
ciano, magenta e giallo, e quindi la componente K `e pari al minimo
"""

import sys
sys.path.append("../Librerie") 
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import scipy.ndimage as ndi
import mylib as ml
from matplotlib.colors import ListedColormap

#Visualizzo Immagine input
x = io.imread('../immagini/fragole.jpg')
x = np.float64(x) / 255
plt.figure(1)
plt.imshow(x) #non servono tag
plt.title('Immagine input')

z = ml.rgb2cmy(x)

c = z[:,:,0] # Ciano
m = z[:,:,1] # Magenta
y = z[:,:,2] # Giallo

plt.figure(2);
plt.subplot(1,3,1); plt.imshow(c,clim=[0,1],cmap='gray'); plt.title('Ciano');
plt.subplot(1,3,2); plt.imshow(m,clim=[0,1],cmap='gray'); plt.title('Magenta');
plt.subplot(1,3,3); plt.imshow(y,clim=[0,1],cmap='gray'); plt.title('Giallo');

L = np.arange(255,-1,-1)/255 # 256 valori tra da 1 ad 0
B = np.ones(256) # 256 valori unitary
cmap_c = ListedColormap(np.stack((L,B,B),-1)) # palette per il Ciano
cmap_m = ListedColormap(np.stack((B,L,B),-1)) # palette per il Magenta
cmap_y = ListedColormap(np.stack((B,B,L),-1)) # palette per il Giallo
plt.figure(3);
plt.subplot(1,3,1); plt.imshow(c,clim=[0,1],cmap=cmap_c); plt.title('Ciano');
plt.subplot(1,3,2); plt.imshow(m,clim=[0,1],cmap=cmap_m); plt.title('Magenta');
plt.subplot(1,3,3); plt.imshow(y,clim=[0,1],cmap=cmap_y); plt.title('Giallo');

y = ml.rgb2cmyk(x)
z = ml.rgb2cmyk(x)
c = z[:,:,0] # Ciano
m = z[:,:,1] # Magenta
y = z[:,:,2] # Giallo
k = z[:,:,3] # Nero

plt.figure(4);
cmap_k = ListedColormap(np.stack((L,L,L),-1)) # palette per il Nero
plt.subplot(1,4,1); plt.imshow(c,clim=[0,1],cmap=cmap_c); plt.title('Ciano');
plt.subplot(1,4,2); plt.imshow(m,clim=[0,1],cmap=cmap_m); plt.title('Magenta');
plt.subplot(1,4,3); plt.imshow(y,clim=[0,1],cmap=cmap_y); plt.title('Giallo');
plt.subplot(1,4,4); plt.imshow(k,clim=[0,1],cmap=cmap_k); plt.title('Nero');




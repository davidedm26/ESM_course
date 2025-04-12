# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:09:31 2025

@author: david
"""




import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.util import random_noise
import skimage.exposure as ex # importa il modulo Input/Output di SK-Image
plt.close('all')

'Ex.2'



def adapt_filter(x, k):
    
    local_var = ndi.generic_filter(x, np.var, (k, k))
    
    """
    local_var_flat = local_var.flatten()
    local_var_flat.sort()
    idx = int(0.7 * len(local_var_flat))  # 70% dei valori → soglia oltre la quale c'è il 30%
    T = local_var_flat[idx]
    """
    T = np.percentile(local_var.flatten(),70)
    
    mean_1 = ndi.generic_filter(x, np.mean, (k,k))
    mean_2 = ndi.generic_filter(x, np.mean, (k-2, k-2))
    
    mask = local_var < T
    filtered = np.zeros_like(x)
    filtered[mask] = mean_1[mask]
    filtered[~mask] = mean_2[~mask]
    
    return filtered


x = np.float64(io.imread('cigno.jpg'))
plt.figure()
plt.imshow(x, clim = [0, 255], cmap = 'gray')
plt.title('input')

    
M, N = x.shape
d = 25 
n = d*np.random.randn(M, N)
g = x+n
plt.figure()
plt.imshow(g, clim = None, cmap = 'gray')
plt.title('rumore gaussiano')

list_k = [3,5,7,9]

for k in list_k:
    
    immagine_filtrata = adapt_filter(g, k)
    mse = np.mean((x - immagine_filtrata)**2)
    psnr = 10 * np.log10((255**2) / mse)
    print("PSNR filtro adattativo per k = %d: %.2f dB" % (k, psnr))
    
    m = ndi.generic_filter(x, np.mean, (k, k))
    mse = np.mean((x - m)**2)
    psnr = 10 * np.log10((255**2) / mse)
    print("PSNR filtro media aritmetica per k = %d: %.2f dB" % (k, psnr))
    
    print('----------------------------------------------------')

    
'''
psnr_adattativi = []
psnr_classici = []

for k in list_k:
    # Filtro adattativo
    immagine_filtrata = adapt_filter(g, k)
    mse_adapt = np.mean((x - immagine_filtrata) ** 2)
    psnr_adapt = 10 * np.log10((255 ** 2) / mse_adapt)
    psnr_adattativi.append(psnr_adapt)

    # Filtro media classico
    m = ndi.generic_filter(g, np.mean, (k, k))
    mse_classico = np.mean((x - m) ** 2)
    psnr_classico = 10 * np.log10((255 ** 2) / mse_classico)
    psnr_classici.append(psnr_classico)

# Grafico PSNR
plt.figure()
plt.plot(list_k, psnr_adattativi, 'o-', label='Adattativo')
plt.plot(list_k, psnr_classici, 's--', label='Media classica')
plt.xlabel('k (dimensione finestra)')
plt.ylabel('PSNR [dB]')
plt.title('Confronto PSNR: Filtro adattativo vs Media')
plt.legend()
plt.grid(True)
'''   


m = ndi.generic_filter(x, np.mean, (5, 5))
immagine_filtrata = adapt_filter(g, 5)

plt.figure()
plt.subplot(1, 2, 1); plt.imshow(m, clim = None, cmap = 'gray'); plt.title('filtro media aritmetica')
plt.subplot(1, 2, 2); plt.imshow(immagine_filtrata, clim = None, cmap = 'gray'); plt.title('filtro adattativo')

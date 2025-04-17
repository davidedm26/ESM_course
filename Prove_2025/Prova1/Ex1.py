# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 15:34:36 2025

@author: david
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import random_noise
import scipy.ndimage as ndi

def smf(x,k,T):
    m =ndi.median_filter(x, (k,k))
    z = np.abs(m - x) > T
    print (np.abs(m-x))
    out = np.copy(x)
    out[z==1] = m[z==1]
    return out

#generazione maschera binaria (rumore/non_rumore)
x =np.float64(io.imread('../immagini/lena.jpg'))/255
#applico rumore sale e pepe
noisy = random_noise(x, 's&p', amount = 0.2 )
plt.figure(1)
plt.title('input')
plt.imshow(noisy, clim=[0,1], cmap='gray')

k=5
T=0.03
# y = smf(noisy, k, T)

# plt.figure(2)
# plt.title('output')
# plt.imshow(y, clim=[0,1], cmap='gray')

# z = ndi.median_filter(x, (k,k))
# plt.figure(3)
# plt.title('median filter classico')
# plt.imshow(z, clim=[0,1], cmap='gray') 

psnr_smf = []
psnr_median =[]

for i in [3,5,7,11]:
    y = smf(noisy, i, T)
    mse1 = np.mean( (x-y)**2)
    temp1 = 10*np.log10(255**2/mse1)                  #psnr = 10log10*(255**2/MSE)
    psnr_smf.append(temp1)
    
    z = ndi.median_filter(noisy, (i,i))
    mse2 = np.mean( (z-y)**2)
    temp2 = 10*np.log10(255**2/mse2)                  #psnr = 10log10*(255**2/MSE)
    psnr_median.append(temp2)

plt.figure(4)
plt.plot(([3,5,7,11]), psnr_smf, marker='o', label='SMF (Selective Median Filter)')
plt.plot(([3,5,7,11]), psnr_median, marker='s', label='Filtro Mediano Standard')
plt.legend()


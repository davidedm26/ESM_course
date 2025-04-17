# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:59:14 2025

@author: david
"""

# -- coding: utf-8 --
"""
Created on Wed Apr 16 15:50:22 2025

@author: dmdav
"""
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import skimage.util as ut

def smf(x,k,T):
    
    #z = np.zeros((M,N))
    
    median = ndi.median_filter(x, (k,k))
    
    mask = np.abs(median-x)>T
    #plt.figure(); plt.imshow(mask, clim=None, cmap="gray"); plt.title("mask")

    z = x.copy()
    z[mask] = median[mask]
                
    return z

def psnr(x,y):
    mse = np.mean((x-y)**2)
    psnr = 10*np.log10(255**2/mse)
    return psnr

x = np.float64(io.imread("../immagini/lena.jpg"))
plt.figure(); plt.imshow(x, clim=None, cmap="gray"); plt.title("input")

sp = ut.random_noise(x, mode="s&p")
noisy = x*sp
plt.figure(); plt.imshow(noisy, clim=None, cmap="gray"); plt.title("noise")

lista = [3,5,7,9,11]
psnrlist = np.zeros((2,5))

for i,k in enumerate(lista):
    z = smf(noisy,k,130)
    #plt.figure(); plt.imshow(z, clim=None, cmap="gray"); plt.title("output")
    
    psnri = psnr(x,z)
    psnrlist[0,i] = psnri
    
    m = ndi.median_filter(noisy, (k,k))
    psnri = psnr(x,m)
    psnrlist[1,i] = psnri

plt.figure(); plt.hist(psnrlist); plt.title("istogramma")

z = smf(noisy,5,130)
plt.figure(); plt.imshow(z, clim=None, cmap="gray"); plt.title("k=5 smf")
m = ndi.median_filter(noisy, (5,5))
plt.figure(); plt.imshow(m, clim=None, cmap="gray"); plt.title("k=5 median filter")
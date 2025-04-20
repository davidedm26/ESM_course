# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 14:09:02 2025

@author: david
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph
import skimage.color as color

#EX2
x=np.float64(io.imread("../Immagini/ala_ape.jpg"))/255

plt.figure("Originale")
plt.imshow(x)
x=color.colorconv.rgb2hsv(x)

plt.figure("Originale HSV")
plt.imshow(x)

HSV=[x[:,:,0],x[:,:,1],x[:,:,2]]
plt.figure("H")
plt.imshow(HSV[0],clim=[0,1],cmap='gray')
plt.figure("S")
plt.imshow(HSV[1],clim=[0,1],cmap='gray')
plt.figure("V")
plt.imshow(HSV[2],clim=[0,1],cmap='gray')

HSV[1]=ndi.median_filter(HSV[1],(5,5))
HSV[0]=ndi.median_filter(HSV[0],(5,5))

mask=(HSV[1]>0.15)|((HSV[0]>0.10)&(HSV[0]<0.11))
mask=ndi.median_filter(mask,(3,3))

plt.figure("Mask")
plt.imshow(mask,clim=[0,1],cmap='gray')

s= np.ones((5,5))

mask=morph.binary_closing(mask,s)

plt.figure("Mask morf")
plt.imshow(mask,clim=[0,1],cmap='gray')
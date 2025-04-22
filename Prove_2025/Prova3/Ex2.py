# EX. 2 Si vuole segmentare l’immagine dell’ala di un’ape (contenuta nel file ala ape.jpg). Realizzate
# tutte le operazione che ritenete necessarie (includendo eventuali operazioni morfologiche)
# per ottenere la mappa binaria di segmentazione in cui si evidenziano solo i bordi delle venature
# presenti.

import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.morphology as morph

plt.close('all')
x=io.imread('../Immagini/ala_ape.jpg')
x = np.mean(x, -1)


plt.figure(1)
plt.imshow(x, clim=None, cmap='gray')
plt.title('Immagine di input 1')

h = np.array([[0,1,0],[1,-5,1],[0,1,0]])

y= ndi.correlate(x,h)

y = ndi.median_filter(y, (3,3))
plt.figure(2)
plt.imshow(y, clim=None, cmap='gray')
plt.title('median')
y = y > -200
plt.figure(3)
plt.imshow(y, clim=None, cmap='gray')
plt.title('mask')

# # gradiente morfologico
# b = morph.rectangle(3, 3)
# x_dil = morph.dilation(x,b)
# x_ero = morph.erosion(x,b)
# y1 = x_dil ^ x_ero
y1 = morph.erosion(y, morph.rectangle(2,2))

# for i in range(1):
#     y1 = morph.opening(y1, np.array([[0,1],[1,0]]))

b = morph.diamond(2)
y2 = morph.opening(y1, b)
y1 = y1 ^ y2
# # gradiente morfologico
# b = morph.rectangle(3, 3)
# x_dil = morph.dilation(y1,b)
# x_ero = morph.erosion(y1,b)
# y1 = x_dil ^ x_ero

plt.figure(4)
plt.imshow(y1, clim=None, cmap='gray')
plt.title('erosion')

# #provo k_means
# from sklearn.cluster import k_means
# d = np.reshape(y, (-1,1))
# centroid, idx, sum_var = k_means(d,2)
# y1 = np.reshape(idx, x.shape)

# plt.figure(3)
# plt.imshow(y1, clim=None, cmap='gray')
# plt.title('post k_means')

# # y2 = np.copy(y1)
# # y2[200:,:] = y1[200:,:] >70
# # y2[:200,:] = y1[:200,:] >35
# # plt.figure(4)
# # plt.imshow(y2, clim=[0,1], cmap='gray')
# # plt.title('mask')

# b = np.array([[0,0,1],[0,1,0],[1,0,0]])
# # y3 = morph.binary_opening(y2,b)
# y3 = morph.binary_closing(y1,b)
# y3 = morph.binary_closing(y3,b)
# y3 = morph.binary_closing(y3,b)
# c = morph.rectangle(1,2)
# y3 = morph.binary_erosion(y3,c)
# y3 = morph.binary_opening(y3,b)
# y3 = morph.binary_opening(y3,b)
# y3 = morph.binary_opening(y3,b)
# plt.figure(5)
# plt.imshow(y3, clim=[0,1], cmap='gray')
# plt.title('opening')


# # #Estrarre solo i bordi delle venature
# # h = np.array([[0,1,0],[1,-5,1],[0,1,0]])

# # y3= ndi.correlate(y2,h)

# # plt.figure(5)
# # plt.imshow(y3, clim=[0,1], cmap='gray')
# # plt.title('mask')


# # plt.figure(2)
# # plt.imshow(x, clim=None, cmap='gray')
# # plt.title('elab')



# # b = morph.rectangle(1, 3)
# # y = morph.opening(x,b)


# # # b = morph.rectangle(3, 3)
# # # x_dil = morph.dilation(x,b)
# # # x_ero = morph.erosion(x,b)
# # # y = x_dil - x_ero

# # plt.figure(3)
# # plt.imshow(y, clim=None, cmap='gray')
# # plt.title('elab2')

# # y = y > -220

# # plt.figure(4)
# # plt.imshow(y, clim=None, cmap='gray')
# # plt.title('binaria')

# # b = morph.rectangle(1, 1)
# # y = morph.erosion(y,b)

# # plt.figure(5)
# # plt.imshow(y, clim=None, cmap='gray')
# # plt.title('binaria elab1')





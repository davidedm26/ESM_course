# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 11:02:09 2025

@author: david
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import bitop as bo
import mylib as ml


# Le operazioni aritmetiche (somma/sottrazione, prodotto/divisione) coinvolgono una o pi`u immagini e si effettuano
# pixel per pixel. Per esempio, fare la sottrazione tra due immagini vi permette di scoprire le differenze
# che esistono tra due immagini. Provate allora a visualizzare l’immagine frattale.jpg, e quella in cui sono stati
# posti a zero i 4 bit-plane meno significativi. Noterete come da un punto di vista visivo sono molto simili,
# fatene allora la differenza e visualizzatela a schermo.

x = ml.leggiJpeg('../immagini/frattale.jpg');
ml.showImage(x, 'frattale')

y = np.copy(x);
for i in range(0, 3):
    y = bo.bitset(y, i, 0)

ml.showImage(y, 'rimossi bitplane 0:3')

diff = x - y;
ml.showImage(diff, 'differenza')



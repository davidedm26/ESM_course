# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 10:02:57 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from glob import glob
plt.close('all')

for filename in glob('*.tif'):
    x = io.imread(filename)
    print(filename, x.dtype, x.shape)
    if filename.endswith('_bool.tif'):
        assert x.dtype==np.bool_
        clim=[0,1]
    else:
        assert x.dtype==np.uint8
        clim=[0,255]
    plt.figure()
    plt.imshow(x, clim=clim, cmap='gray')
    plt.title(filename)

#!/usr/bin/env python

import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv( sys.argv[1], index_col=0 )

n, p = df.shape

# df = df.T

pca = PCA()
fit = pca.fit( df )

x = pca.transform( df )

plt.figure()
plt.plot( fit.components_.T[:,:2], label=["PC1", "PC2"] )
plt.xticks( range(len(df.columns)), df.columns, rotation=90 )
plt.legend()

plt.show()









#!/usr/bin/env python

import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv( sys.argv[1], index_col=0 )

corr = np.corrcoef( df.values.T )
corr = pd.DataFrame( corr, columns=df.columns )

print corr

plt.figure()
plt.pcolor( corr )
plt.colorbar()
plt.yticks( range(len(corr.columns)), 
    corr.columns )
plt.show()
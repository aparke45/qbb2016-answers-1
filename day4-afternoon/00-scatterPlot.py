#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )

plt.figure()
plt.xscale( "log" )
plt.yscale( "log" )
plt.scatter( df[ "FPKM" ] +1, df2[ "FPKM" ] +1, alpha=0.1 )
#plt.hexbin( df[ "FPKM" ] +1, df2[ "FPKM" ] +1, gridsize=50, bins='log', )
plt.savefig( "scatterplot.png" )
plt.close()
#!/usr/bin/env python

"""
  Usage: ./01-timecourse.py <metadata.csv> <ctab_dir>
    e.g. ./01-timecourse.py samples.csv ~/data/results/stringtie
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta = pd.read_csv( sys.argv[1] )
ctab_dir = sys.argv[2] 

fem_Sxl = []

df_roi = df_meta[ "sex" ] == "female"
for sample in df_meta[ df_roi ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi2 = df[ "t_name" ] == "FBtr0331261"
    fem_Sxl.append( df[ df_roi2 ][ "FPKM" ].values )
    
plt.figure()
plt.plot( fem_Sxl )
plt.savefig( "timecourse.png" )
plt.close()








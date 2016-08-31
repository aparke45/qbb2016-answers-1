#!/usr/bin/env python

import sys
import numpy as np
from statsmodels.stats.weightstats import ttest_ind as ttest

def load_fpkm_from_ctab( my_ctab_filename ):
    fpkm_values = []
    for i, line in enumerate( open( my_ctab_filename ) ):
        if i == 0:
            continue
        fields = line.rstrip( "\r\n" ).split( "\t" )
        fpkm = float( fields[11] )
        fpkm_values.append( fpkm )
    return np.array( fpkm_values )
    
# a = np.array( fpkm_values )

a = load_fpkm_from_ctab( sys.argv[1] )
b = load_fpkm_from_ctab( sys.argv[2] ) 
    
print "Correlation: {}".format( np.corrcoef( a, b )[0,1] )

## t = ttest( a, b )
## print "t-test t-statistic: {}, p-value: {}, dof: {}".format( t[0], t[1], t[2] )
 
#print "t-test t-statistic: {}, p-value: {}, dof: {}".format( *ttest( a, b ) )
print "t-test t-statistic: {0[0]}, p-value: {0[1]}, dof: {0[2]}".format( ttest( a, b ) )









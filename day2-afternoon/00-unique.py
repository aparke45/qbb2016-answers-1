#!/usr/bin/env python

"""
Prints the unique gene names from a t_data.ctab file.
"""

import sys

## gene_names_seen = [] # list()
gene_names_seen = {} # dict()
## gene_names_seen = set()

for i, line in enumerate( sys.stdin ):
    if i == 0:
        continue
    fields = line.rstrip( "\r\n" ).split( "\t" )
    gene_name = fields[9]
    if gene_name not in gene_names_seen:
        ## gene_names_seen.append( gene_name ) # list
        ## gene_names_seen[ gene_name ] = True # dict
        ## gene_names_seen.add( gene_name )
        gene_names_seen[ gene_name ] = 1
    else:
        gene_names_seen[ gene_name ] += 1
        
## for gene_name in gene_names_seen:
##    print gene_name, gene_names_seen[ gene_name ]
    
# [ ( "sxl", 13 ), ( "ss", 2 ), ... ]
    
for gene_name, count in gene_names_seen.iteritems():
    print gene_name, count
    
iterator = gene_names_seen.iteritems()
while 1:
    tuple_value = iterator.next()
    gene_name = tuple_value[0]
    count = tuple_value[1]
    <rest of for loop>
        
        
    
    
    
    
    
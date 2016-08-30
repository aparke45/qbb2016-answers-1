#!/usr/bin/env python

## Option 1 

# f = open( "temp.fa" )

## Option 2
# import sys
# f = sys.stdin

## Option 3
import sys
f = open( sys.argv[1] )

# print f
# print type( f )
# print f.read()

## Question -- open any number of files?

# file_handles = []
# for filename in sys.argv[1:]:
#    file_handles.append( open( filename ) )
    
for i, line in enumerate( f.readlines() ):
    line = line.rstrip( "\r\n" )
    if line.startswith( ">" ): # Same as if line[0] == ">"
        continue
    # Must be a sequence line
    print i, line[10:30]
    
    























   
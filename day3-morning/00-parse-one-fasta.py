#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""

import sys

line = sys.stdin.readline()
# Verify is header line
assert line.startswith( ">" )
# Extract id -- whole line
## identifier = line[1:].rstrip( "\r\n" )
# Extract id -- space
identifer = line[1:].split()[0]

sequences = []

while True:
    line = sys.stdin.readline().rstrip("\r\n")
    if line.startswith( ">" ) or line == "":
        break
    else:
        sequences.append ( line )
        
print identifer, "".join( sequences )
    
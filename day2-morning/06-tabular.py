#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
    if line.startswith( "t_id" ):
        print line.rstrip( "\r\n" )
        continue
    # Split fields on tab
    fields = line.rstrip( "\r\n" ).split( "\t" )
    # Convert and compute length
    length = int( fields[4] ) - int( fields[3] )
    # Write out with new field tab separated
    fields.append( str( length ) )
    # For debugging
    print repr(fields)
    # Join fields back into a tab separated string
    print string.join( fields, "\t" )
    
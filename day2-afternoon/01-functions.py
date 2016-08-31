#!/usr/bin/env python

test_string = [ "foo", "bar", "baz", "quux" ]

## print "\t".join( test_string )

# def print_sep( a_string=[ "the", "default" ], sep="\t" ):
#     val = sep.join( a_string )
#     print val
#     ## return val
#
# print_sep( test_string )
# print_sep( test_string, ":" )
# v = print_sep( a_string=test_string, sep="WORD" )
# print v

# print_sep( sep=":" )

def join_sep( a_string=[ "the", "default" ], sep="\t" ):
    v = sep.join( a_string )
    return v
    
our_joined_value = join_sep( test_string, ":" )
print v
print our_joined_value
    
    
    
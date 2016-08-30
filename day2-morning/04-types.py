#!/usr/bin/env python

print "Basic types"

a_string = "this is a string"

print "String item six is", a_string[6] 

a_string = "this is a xtring"

an_integer = 7

i_as_s = str( an_integer )

s_as_i = int( "1" )

a_real = 5.689

s_as_r = float( "5.678" )

truthy = True
falsish = False

for value in ( a_string, an_integer, a_real, truthy ):
    print value, type( value )

print "Lists and tuples"
    
a_list = [ 1, 2, 4, 5, 6 ]

a_tuple = ( 1, 2, 3, 4, 5, 6 )


print a_list, type( a_list )
print a_tuple, type( a_tuple )

a_list[3] = 777
print a_list

# Throws exception
# a_tuple[3] = 777
# print a_tuple


my_var_a = [1,2,3,4]

my_var_b = my_var_a

my_var_c = list(my_var_a)

my_var_a[ 2 ] = 99999

print my_var_b

print my_var_c


print list(tuple(tuple(list([2,2]))))



















































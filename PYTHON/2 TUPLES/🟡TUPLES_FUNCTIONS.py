# TUPLES FUNCTIONS 


# Immutable → safe
# Faster than lists
# Can be used as dictionary keys


# 1. COUNT 
# Counts how many times a value appears in the tuple.

#     0   1   2   3   4   5
a = ( 1 , 2 , 3 , 3 , 5 , 3)
print(a.count(3)) # -- > 3




# 2. INDEX 
# Returns the index of the first occurrence of a value.

#     0   1   2   3   4   5
a = ( 1 , 2 , 3 , 3 , 5 , 3)
print(a.index(3)) # --> 2

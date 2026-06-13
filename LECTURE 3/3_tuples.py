# TUPLES {IMMUTABLE}

# a build in data type that lets us create immutable sequence of values

#       0   1   2   3 
tup = ( 1 , 3 , 2 , 4 )

print(tup[2])
print(tup[0])

tup[2] = 4   #this is not allowed


# EMPTY TUPLE

tup = ()

print(tup)
print(type(tup))


# if 

tup = (1)

print(tup)        #no brackets will be displayed
print(type(tup))  #not this is a integer


tup = (1,)   #now this is a tuple and now the output will have brackets



# slicing works in tuple same as list

#       0   1   2   3 
tup = ( 1 , 3 , 2 , 4 )

print(tup[0:2])  #output --> 1 , 3 
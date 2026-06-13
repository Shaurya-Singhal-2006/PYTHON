# SLICING 
# accessing parts of string


# str[starting_idx : ending_idx] 

str = "shaurya"

print(str[1:4]) #output will be {hau} the ending index will not be included

# we can also write 

print(str[0:4])    #shau
#    OR
print(str[:4])  #both are same 



print(str[0:len(str)]) #this will print the whole string
#    OR 
print(str[0:])         #this will also print the whole string



# NEGATIVE SLICING

#    A  P  P  L  E 
#   -5 -4 -3 -2 -1 

str = "apple"

print(str[-4:-1]) # the output is ppl
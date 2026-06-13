# BUILD IN FUCNTIONS THAT WORKS ON TUPLES 


# 1. LEN
# return the length of the tuple 

#     0   1   2   3   4   5
a = ( 1 , 2 , 3 , 3 , 5 , 3)
print(len(a))  # --> 6




# 2. MAX  
# returns the max value present in the tuple 

#     0   1   2   3   4   5
a = ( 1 , 2 , 3 , 3 , 5 , 3)
print(max(a)) # --> 5




# 3. MIN
# returns the min value present in the tuple 

#     0   1   2   3   4   5
a = ( 1 , 2 , 3 , 3 , 5 , 3)
print(min(a)) # --> 1

# USING  MIN AND MAX WITH KEY 

a = ("apple" , "kiwi" , "banana" , "orange")
print(max(a))  # --> orange
print(min(a))  # --? apple
# this is sorting on the basics of the first alphabet of the string

print(max(a,key=len)) # --> banana
print(min(a,key=len)) # --> kiwi
# now it sorting them on the basics of the length of the string




# 4. SUM
# returns the sum of all the element present in the tuple

#     0   1   2   3   4   5
a = ( 1 , 2 , 3 , 3 , 5 , 3)
print(sum(a)) # --> 17




# 5. SORTED
# it return sorted LIST not a tuple 

#     0   1   2   3   4   5
a = ( 1 , 2 , 3 , 3 , 5 , 3)
b = sorted(a)
print(b)  # --> [1, 2, 3, 3, 3, 5]
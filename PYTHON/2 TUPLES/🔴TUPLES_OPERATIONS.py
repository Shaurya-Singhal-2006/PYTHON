# TUPLE OPEARTIONS 


# 1. INDEXING 

#     0    1    2
a = ( 10 , 20 , 30 )
print(a[1]) # --> 20




# 2. SLICING 

#     0   1   2   3   4   5 
a = ( 1 , 2 , 3 , 4 , 5 , 6 )
print(a[1:4])  # --> (2, 3, 4)




# 3. CONCATINATION 

t1 = ( 1 , 2 , 3 )
t2 = ( 4 , 5 , 6 )
print(t1 + t2) # --> (1, 2, 3, 4, 5, 6)




# 4. REPETITION

print(( 1 , 2 ) * 3) # --> (1, 2, 1, 2, 1, 2)




# 5. MEMBERSHIP

print(2 in (1,2,3))  # --> True
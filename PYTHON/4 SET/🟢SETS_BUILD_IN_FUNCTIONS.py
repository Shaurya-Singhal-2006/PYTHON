# BUILD IN FUNCTIONS TO USE WITH SETS


# 1. LEN
# returns the length of the set

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
print(len(s)) # --> 4 




# 2. MAX / MIN
# return the max value present in the set
# return the min value present in the set 

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
print(max(s)) # --> 4  
print(min(s)) # --> 1




# 3. SUM
# sum all the element present in the set

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
print(sum(s))  # --> 10




# 4. SORTED
# return a sorted list

#     0   1   2   3
s = { 2 , 1 , 4 , 3 }
b = sorted(s) 
print(b)   # --> [1, 2, 3, 4]



#   | Operation      | Operator |   
#   | -------------- | -------- |   
#   | Union          |    `     |   
#   | Intersection   |   `&`    |   
#   | Difference     |   `-`    |   
#   | Symmetric diff |   `^`    |   
#   | Subset         |   `<=`   |   
#   | Superset       |   `>=`   |  
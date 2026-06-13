# BUILD IN FUNCTIONS THAT WORKS ON LIST 

# 1. LEN
# returns the length of the string

#     0   1   2
a = [ 1 , 2 , 3 ]
print(len(a))  # --> 3




# 2. MAX
# returns the maximum value present in the list 

#     0   1   2   3
a = [ 5 , 6 , 2 , 8 ]
print(max(a))  # --> 8




# 3. MIN
# returns the minimum value present in the string

a = [ 5 , 6 , 2 , 8 ]
print(min(a))  # --> 2

# using min and max with key

a = ["apple", "kiwi" , "banana"]
print(min(a,key=len)) # --> kiwi 
print(max(a,key=len)) # --> banana
# it is now taking the min and max string on the basic of there length




# 4. SUM
# return the sum of all element in a list

#     0   1   2   3
a = [ 5 , 6 , 2 , 8 ]
print(sum(a)) # --> 21




# 5. SORTED
# Returns a new sorted list (does NOT modify original)

#     0   1   2   3
a = [ 4 , 6 , 2 , 8 ]

b = sorted(a)
print(a) # --> [4, 6, 2, 8]   the original list is still present 
print(b) # --> [2, 4, 6, 8]




# EXTRA INFO 

# 1. APPEND ELEMENT IN A 2D LIST 

a = [[1,2,3],  # 0
     [4,5,6],  # 1
     [7,8,9]]  # 2
a[1].append(4)
print(a)  # --> [[1, 2, 3], [4, 5, 6, 4], [7, 8, 9]] it adds 4 at the last of the 1 index list in the 2d list 

# 2. INSERT ELEMENT IN A 2D LIST

a = [[1,2,3],  # 0
     [4,5,6],  # 1
     [7,8,9]]  # 2

a[1].insert(1,80)   
print(a) # --> [[1, 2, 3], [4, 80, 5, 6], [7, 8, 9]]  

# it adds 80 at 1st index of the 1 indexed list in a 2D list
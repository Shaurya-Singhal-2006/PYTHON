#  LIST FUNCTIONS


# Lists = simple & fast
# Heavy processing = functions + comprehensions
# Cleaner syntax, fewer methods to memorize


# 1. APPEND
# Adds one element at the end of the list.

#     0   1   2
a = [ 1 , 2 , 3 ]
a.append(4)
print(a)      # --> [1, 2, 3, 4]




# 2. EXTEND
# Adds multiple elements from another iterable.

#     0   1   2
a = [ 1 , 2 , 3 ]

a.extend([ 4 , 5 ])  # --> [1, 2, 3, 4, 5]
print(a)

# DIFFERENCE BETWEEN APPEND AND EXTEND

# a.append([3,4])  # [1, 2, [3, 4]]
# a.extend([3,4])  # [1, 2, 3, 4]




# 3. INSERT 
# Inserts an element at a specific index.

#     0   1   2
a = [ 1 , 3 , 4 ]
a.insert(1,2)     # --> (position , data)
print(a)  # -->  [1, 2, 3, 4]




# 4. REMOVE
# Removes the first occurrence of a value.

#     0   1   2
a = [ 1 , 2 , 3 ]
a.remove(2)
print(a)   # --> [1, 3]

# error if the value is not found 
# ValueError




# 5. POP
# Removes and returns an element.

#     0   1   2
a = [ 1 , 2 , 3 ]
b = a.pop()
print(b)  # --> 3
print(a)  # --> [1, 2]

b = a.pop(0)   # --> 1 (index 0)
print(b)




# 6. CLEAR 
# removes all the element from the list

#     0   1   2
a = [ 1 , 2 , 3 ]
a.clear()
print(a) # --> []




# 7. INDEX 
# return the index of the first occurance of a value

#     0   1   2   3
a = [ 1 , 2 , 3 , 1 ]
print(a.index(1)) # --> 0

# error if the value is not found 
# ValueError




# 8. COUNT 
# count how many times a value appears and returns it 

#     0   1   2   3
a = [ 1 , 2 , 3 , 1 ]
print(a.count(1)) # --> 2




# 9. SORT
# Sorts the list in place.

#     0   1   2   3
a = [ 3 , 2 , 4 , 1 ]
a.sort()
print(a)  # --> [1, 2, 3, 4]

# DESCENDING ORDER
a.sort(reverse=True)  
print(a) # --> [4, 3, 2, 1]

# WITH KEY 
a = ["apple", "kiwi" , "banana"]
a.sort()
print(a) # --> ['apple', 'banana', 'kiwi']  it is comparing the first alphabet of the word

a = ["apple", "kiwi" , "banana"]
a.sort(key=len)
print(a) # --> ['kiwi', 'apple', 'banana'] now it is sorted according to the length of the string




# 10. REVERSE
# reverse the list in place 

#     0   1   2   3
a = [ 1 , 2 , 7 , 1 ]
a.reverse()
print(a) # -->  [1, 7, 2, 1] it reverse the list not sort it 




# 11. COPY 
# creates a shollow copy of the list 

#     0   1   2
a = [ 1 , 2 , 3 ]
b = a.copy()
print(b) # --> [1, 2, 3]

# SAME AS b = a[:]
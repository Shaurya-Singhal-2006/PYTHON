# SET FUNCTIONS 

# No duplicates
# No indexing or slicing
# Very fast membership checking → O(1)
# Elements must be immutable


# 1. ADD
# adds one element

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }

s.add(5)
print(s) # --> {1, 2, 3, 4, 5}





# 2. UPDATE
# adds multiple element from iteration 

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
s.update({5,6})
print(s)  # --> {1, 2, 3, 4, 5, 6}




# 3. REMOVE 
# removes an element

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
s.remove(2)
print(s) # --> {1, 3, 4}
# error if element not found




# 4. DISCARD 
# removes element without error

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
s.discard(5)
print(s)  # --> {1, 2, 3, 4}
# it will not give any error even if the element is not found




# 5. POP
# removes and return a random element (order is unpridicted)

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
a = s.pop()
print(s)  # --> {2, 3, 4}
print(a)  # --> 1




# 6. CLEAR
# removes all element in the set 

#     0   1   2   3
s = { 1 , 2 , 3 , 4 }
s.clear()
print(s) # --> set()
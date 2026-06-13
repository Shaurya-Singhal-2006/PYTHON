# SET OPERATIONS (VERYYYY IMPORTANT)


# 1. UNION
a = { 1 , 2 , 3 , 4 }
b = { 5 , 6 , 7 , 8 }
print(a.union(b)) # --> {1, 2, 3, 4, 5, 6, 7, 8}




# 2. INTERSECTION 
# return commom elements

a = { 1 , 2 , 3 , 4 }
b = { 5 , 1 , 3 , 8 }
print(a.intersection(b)) # --> {1, 3}




# 3. DIFFERENCE 
# element in a but not in b

a = { 1 , 2 , 3 , 4 }
b = { 5 , 1 , 3 , 8 }
print(a.difference(b)) # --> {2, 4}  (these are the element which are present in a but not in b)




# 4. SYMMETRIC_DIFFERENCE 
# elements in either but not in both 

a = { 1 , 2 , 3 , 4 }
b = { 5 , 1 , 3 , 8 }
print(a.symmetric_difference(b)) # --> {2, 4, 5, 8} (it removes the common elements in both )




# 5. INTERSECTION_UPDATE
# update set with common elements

a = { 1 , 2 , 3 , 4 }
b = { 5 , 1 , 3 , 8 }
a.intersection_update(b)
print(a) # --> {1, 3}




# 6. DIFFERENCE_UPDATE
# removes elements found in another set

a = { 1 , 2 , 3 , 4 }
b = { 5 , 1 , 3 , 8 }
a.difference_update(b)
print(a) # --> {2, 4}




# 7. SYMMETRIC_DIFFERENCE_UPDATE
# keep only non common elements

a = { 1 , 2 , 3 , 4 }
b = { 5 , 1 , 3 , 8 }
a.symmetric_difference_update(b)
print(a) # -->  {2, 4, 5, 8}




# 8. UPDATE 
# in place union

a = { 1 , 2 , 3 , 4 }
b = { 5 , 1 , 3 , 8 } 
a.update(b)
print(a) # --> {1, 2, 3, 4, 5, 8}




#  RELATIONSHIP / CHECK METHOD


# 9. ISSUBSET
# checks if the set is subset

a = { 1 , 2 }
b = { 1 , 2 , 3 , 4 , 5 }
print(a.issubset(b)) # --> True (all a elements are present in b)




# 10. ISSUPERSET
# check if set contains another set 

a = { 1 , 2 }
b = { 1 , 2 , 3 , 4 , 5 }
print(a.issuperset(b))  # --> false (a does not contain the b )




# 11. ISDISJOINT
# checks if sets have no common elements 

a = { 1 , 2 }
b = { 1 , 2 , 3 , 4 , 5 }
print(a.isdisjoint(b)) # --> false (1,2 are common)
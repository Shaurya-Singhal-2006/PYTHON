# SET METHOD

# SET --> MUTABLE
# SET ELEMENTS --> IMMUTABLE

set = { 1 , 2 , 3 , 4 }

# 1. ADD
# adds an element

set.add(5)
print(set)   #output --> {1, 2, 3, 4, 5}



# 2. REMOVE
# removes the element 

set.remove(5)
print(set)   #output -->{1, 2, 3, 4}



# 3. POP
# removes a random value

print(set.pop())



# 4. CLEAR
# empties the set

set.clear()
print(set)     #output --> set()


# UNHASHABLE --> (which values can change) dictionary,lists,set



# 5. UNION
# combine both set value and return new (return unique values)

set1 = { 1 , 2 , 3 }
set2 = { 3 , 4 , 5 } 

print(set1.union(set2))  #output --> {1, 2, 3, 4, 5}



# 6. INTERSECTION
# combines comman values and return new (return common values)

print(set1.intersection(set2))  #output --> {3}
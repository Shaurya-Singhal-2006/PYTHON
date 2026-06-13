# SETS IN PYTHON

# set is a collection of the unordered items 
# each element in the set must be unique and immutable
# list and dictionary cannot be stored in set

nums = { 1 , 2 , 3 , 4 }

print(nums)
print(type(nums))

set1 = { 1 , 2 , 2 , 2 }
# repeated element stored only once, so it resolved to {1,2}
print(set1)  

# empty set syntax
null_set = set()
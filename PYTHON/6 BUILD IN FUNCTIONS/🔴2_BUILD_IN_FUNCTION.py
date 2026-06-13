# SEQUENCE AND ITERABLE FUNCTIONS 


# 1. LEN 
# returns the length 




a = "hello my name is shaurya"
print(len(a)) # --> 24




# 2. RANGE
# generate sequence of numbers

print(list(range(5))) # --> [0, 1, 2, 3, 4]




# 3. ENUMERATE
# return index + value

for i, v in enumerate(["a","b","c","d"]):
    print(i,v,end=" ")  # --> 0 a 1 b 2 c 3 d 
print()




# 4. ZIP
# combines iterable

print(list(zip([1,2],[3,4]))) # --> [(1, 3), (2, 4)]




# 5. SORTED
# returns sorted list

a = [4,1,6,5]
b = sorted(a)
print(b) # --> [1, 4, 5, 6]




# 6. REVERSED 
# return revered iterator

a = [1,2,3,4]
print(list(reversed(a))) # --> [4, 3, 2, 1]




# LOGICAL / CONDITIONAL FUNCTIONS

# 1. ALL
# true if all elements are true

a = [True,True]
print(all(a)) # --> True




# 2. ANY
# true if any statement is true

a = [True,False,False]
print(any(a))  # --> True


# OBJECT / MEMORY FUNCTIONS


# 1. ID
# returns memory address

a = 11
print(id(a)) # --> 140733076448696




# 2. TYPE 
# returns the type of data

a = "ab"
b = 12

print(type(a)) # --> <class 'str'>
print(type(b)) # --> <class 'int'>




# 3. ISINSTANCE
# checks object type

a = 10
print(isinstance(a,int)) # --> True




# 4. DIR 
# returns attribute of object

print(dir(int))
print(dir(list))
print(dir(str))




# 5. VARS
# returns object dict

print(vars(object))
# BUILD IN PYTHON FUNCTIONS

# to get all the functions exists in python 
print(dir(__builtins__))



# INPUT / OUTPUT FUNCTIONS

# 1. PRINT
# display output

print("123") # --> 123




# 2. INPUT
# takes input from user

a = int(input("enter a number :"))
print(a) # --> the number u will input 




# TYPE CONVERSION


# 1. INT 
# convert to integer

a = "10"
print(int(a)) # --> 10
print(type(int(a))) # --> <class 'int'>




# 2. FLOAT
# convert to flaot 

a = "3.14"
print(float(a)) # --> 3.14
print(type(float(a))) # --> <class 'float'>




# 3. STR
# convert to string

a = "354.67"
print(str(a)) # --> 354.67
print(type(str(a))) # --> <class 'str'>




# 4. BOOL
# convert to bool

print(bool(0)) # --> false
print(bool(10)) # --> true




# 5. LIST
# convert iterable to list

a = (1,2,3)
print(list(a)) # --> [1, 2, 3]
print(type(list(a))) # --> <class 'list'>




# 6. TUPLE 
# convert iterable to tuple 

a = [1,2,3,4] 
print(tuple(a)) # --> (1, 2, 3, 4)
print(type(tuple(a))) # --> <class 'tuple'>




# 7. SET
# convert iterable to set

a =  [1,2,3,4]
print(set(a)) # --> {1, 2, 3, 4}
print(type(set(a))) # --> <class 'set'>




# 8. DICT
# create dictionary

print(dict(a=1,b=2)) # --> {'a': 1, 'b': 2}



# NUMERIC AND MATH FUNCTIONS


# 1. ABS
# returns absolute value

a = -10
print(abs(a)) # --> 10




# 2. ROUND
# rounds a number

a = 3.456
b = 1.5
print(round(a,2))  # --> 3.46
print(round(a))  # --> 3
print(round(b)) # --> 2




# 3. POW
# power function

print(pow(2,3)) # --> 8




# 4. DIVMOD
# returns (quotient , remainder)

print(divmod(10,3)) # --> (3, 1)




# 5. SUM
# adds element of iterable 

a = (1,2,3,4,5)
print(sum(a)) # --> 15




# 6. MAX / MIN
# returns the max and min value present in the iterable 

a = (1,2,3,4,8,9)
print(min(a)) # --> 1
print(max(a)) # --> 9
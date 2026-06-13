# STRINGS 

# string is data type that stores a sequence of characters

str1 = "this is a string"
str2 = 'this is a string'
str3 = """this is a string"""

# ALL THE ABOVE STRINGS ARE VALID 

# escape sequence character

# \n --> next line

str1 = "hello my name is shaurya \nand i am 18 years old"

print(str1)

# 1. CONCATINATION

str1 = "hello"
str2 = " world"

# we can also do 

final_string = str1 + " " + str2    
#this will add a space as " " is a empty string

print(final_string)
print(str1 + str2)

# 2. LENGTH OF STRING

print(len(str1))
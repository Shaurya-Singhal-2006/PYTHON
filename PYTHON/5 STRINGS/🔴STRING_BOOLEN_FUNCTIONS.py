# BOOLEN CHECKING FUNCTION (TRUE / FALSE)


# 1. ISALNUM
# checks if the string have both char and num

a = "Shaurya123"
print(a.isalnum()) # --> true (it does not work with spaces)




# 2. ISAPLHA
# only alphabets

a = "Shaurya"
print(a.isalpha()) # --> true (it does not work with spaces)




# 3. ISDIGIT
# only digit (0-9)

a = "1234567890"
print(a.isdigit()) # --> true




# 4. ISDECIMAL
# only decimal digit

a = "34"
print(a.isdecimal()) # --> true

"123".isdecimal()     # True
"1.23".isdecimal()    # false




# 5. ISNUMERIC
# digit + unicodes

a = "½"
print(a.isnumeric())  # --> true 
"123".isnumeric()      # True
"00123".isnumeric()    # True

"-123".isnumeric()     # False
"12.3".isnumeric()     # False
"1e3".isnumeric()      # False




# 6. ISLOWER
# check all of the string is in lowercase

a = "hello my name is shaurya"
print(a.islower()) # --> true




# 7. ISUPPER
# check if all of the string is upper case

a = "HELLO MY NAME IS SHAURYA"
print(a.isupper()) # --> true




# 8. ISSPACE
# check only the spaces

a = "  "
print(a.isspace()) # --> true




# 9. ISTITLE
# check if all the worlds first char is uppercase or not

a = "Hello World"
print(a.istitle()) # --> true




# 10. ISIDENTIFIERS
# valid python identifier

a = "1_ab"
b = "adc_1"
print(a.isidentifier())  # --> false
print(b.isidentifier())  # --> true




# 11. ISPRINTABLE
# printable character

a = "hello world\n"
print(a.isprintable()) # --> false
# TYPE CONVERSION   (automatic conversion)

a = 1
b = 2.0

sum = a + b 
print(sum)  #output --> 3.0

a = "2"
b = 4.75

sum = a + b
print(sum)    #error



# TYPE CASTING (manual caonversion)

a = int("2")
b = 4.75

sum = a + b 
print(sum)  #now no error

# we can also type cast int to string

a = 2 
b = str(a)

print(type(b))
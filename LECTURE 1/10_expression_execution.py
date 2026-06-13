# EXPRESION EXECUTION

# 1. string & numeric values can operate together with *

a = 5 
b = 2

text = "@"

print(a*text*b)

# 2. string & string can operate with +

c = "2"
d = 3

print((c+text)*d)

# 3. numeric values can operate with all arithmetic operators

e = 10
f = 15 
g = 2

print(e + f * g)

# 4. arithmetic expression with integer and float will result in float

h = 10
i = 5.0

print(h * i)

# 5. result of division operator with two integer will be float 

e = 10 
f = 15

print(f / e)

# 6. integer division ( // ) with float and int displayed as float 

j = 1.5
k = 3
l = j // k 

print(l , j/k)  # answer --> 0.0  0.5

# 7. FLOOR

# floor gives closesst integer,  which is lesser than or equal to the float values
# result of (a//b) is same as floor (a/b)

# 0.1 --> 0
# 3.99 --> 3
# 5.0 --> 5
# -5.2 --> -6 

# 8. remainder in negative when denominator is negative

#   numerator       +     -     +     -  
#   denominator     +     -     -     +

# answer            +     +     -     +


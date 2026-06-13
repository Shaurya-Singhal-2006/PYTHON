# logical operators ( NOT , AND , OR )

a = 30
b = 60 

print(not False)    #answer is true 
print(not True)     #answer is false 


val1 = True 
val2 = True 
val3 = False 
val4 = False 

print( val1 and val2)      # answer is true when both the values are true 
print(val1 and val3)       # if one value is false the the answer will also be false


print(val1 or val3)       # even if one value is true the answer is true 
print (val3 or val4)      # if none of the values are true then the answer is false 



print("are a and b equal :", (a==b))                   #false
print("is a greater than equal to b :",(a>=b))         #false
print("is b greater then a :", (a<b))                  #true


print(not(a==b))                    #answer is false but because of (not operator)  the result is true
print((a==b) and (a<b))             #answer is false because (a==b) is false 
print((a==b) or (a>b) or (a<b))     #answer is true because (a<b) is true 
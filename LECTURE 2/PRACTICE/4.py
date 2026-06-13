# WAP to find the greatest of 3 numbers entered by the user

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third numeber: "))

if(a >= b  and a >= c):
    print("the greatest number is : ",a)
elif( b >= c): # we just need to check b because first statement is false which means a is not the greatest number
    print("the greatest number is : ",b)
else:
    print("the greatest number is : ",c)

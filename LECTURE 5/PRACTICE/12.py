#  WAP to find the factorial of first n numbers (using for)

x = int(input("enter a number: "))

fact = 1

for val in range(1,x+1):
    fact *= val

print("the factorial is: ",fact)
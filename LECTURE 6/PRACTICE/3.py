# WAF to find the factorial of n. (n  is the parameter)

def fact(x):
    mul = 1
    for i in range(1,x+1):
        mul *= i
    print(mul)

x = int(input("enter a number: "))

fact(x)
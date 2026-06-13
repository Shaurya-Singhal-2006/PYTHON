#  WAF to check if the number is ODD or EVEN

def check(x):
    if(x%2==0):
        print("EVEN")
    else:
        print("ODD")
    

x = int(input("enter a number to check if the number entered is even or odd: "))

check(x)
# write a recursice function to calculate the sum of first n natural numbers

def sum(n):
    if(n == 0):
        return 0
    else:
        return sum(n-1) + n
    
n = int(input("enter a number: "))

print(sum(n))
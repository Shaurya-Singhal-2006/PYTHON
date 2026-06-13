# WAP to find the sum of first n numbers (using while)

x = int(input("enter a number: "))

i = 1
sum = 0
while i <= x:
    sum += i
    i += 1

print("the sum is: ",sum)
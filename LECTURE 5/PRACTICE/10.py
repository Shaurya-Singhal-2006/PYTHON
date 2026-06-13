# print the multiplication table of n number

num = int(input("enter a number: "))

for el in  range(num,num*10+1,num):
    print(el)

print("\n") #  OR

for i in range(1,11):
    print(num*i)
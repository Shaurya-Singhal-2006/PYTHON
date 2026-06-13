# seach for value x in this tuple using loop

# LINEAR SEARCH

tup = (1,4,9,16,25,36,49,64,81,100)

num = int(input("enter the number you want to find: "))

for val in tup:
    if(val == num):
        found = 1
        break
    else:
        found = 0

if(found == 1):
    print("value found")
else:
    print("value not found")
# seach for value x in this tuple using loop

# LINEAR SEARCH

tup = (1,4,9,16,25,36,49,64,81,100)

num = int(input("enter the number you want to find: "))

i = 0

while i < len(tup) :
    if(num == tup[i]):
        print("FOUND")
    i += 1
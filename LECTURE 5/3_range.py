# RANGE

# range function returns a sequence of numbers, starting from 0 by deafult, and increments by 1 (by deafult), 
# and stops beofre a specified number

# range ( start? , stop , step? )
#           1        5      2

for el in range(5):   # range ( start )
    print(el)

print("\n")

for el in range(1,5):    # range ( start , stop )
    print(el)

print("\n")

for el in range(1,5,2):   # range ( start , stop , step )
    print(el)


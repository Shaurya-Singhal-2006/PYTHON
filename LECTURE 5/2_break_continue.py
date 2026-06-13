# BREAK AND CONTINUE

# BREAK
# (used to terminate the loop when encountered)

list = [1,2,3,4,5,6,7,8,9]

i = 0
while i < len(list):
    if(list[i] == 6):
        break
    else:
        print(list[i])
    i += 1

# the loop break when the value of i reached 6



# CONTINUE
# terminate execution in the current iteration and continues execution of the loop with the next iteration

list = [1,2,3,4,5,6,7,8,9]

j = 0
while j < len(list):
    if(list[j] == 9):
        j += 1
        continue
    print(list[j])
    j += 1
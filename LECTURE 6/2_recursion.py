# RECURSION
# when the sunction calls itself repeatedly 

# print n to 1 backwords

def call(n):
    if(n == 0):
        return
    print(n)
    call(n-1)   #calling the function again and again till n reaches 0


# factorial

def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * fact(n-1)


n = int(input("enter a number: "))
call(n)
   
print(fact(n))





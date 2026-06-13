# write a recursive function to print all element in a list (hint use list and index as parameters)

def pri(list , ind = 0):
    if(ind == len(list)):
        return
    print(list[ind])
    pri(list,ind+1)

num = [1,4,9,16,25,36,49,64,81,100]

pri(num)
    
# WAF to rpint the element of a list in a singlt line (list is the parameter)

def print_list(list):
    for el in list:
        print(el,end=" ")

grades = [ "C" , "D" , "A" , "A" , "B" , "B" , "A" ]

print_list(grades)
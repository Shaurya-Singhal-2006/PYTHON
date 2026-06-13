# WAP to check if a list contains a palindrome of elements (hint use copy() method)


# [1,2,3,2,1]
list1 = [ 1 , 2 , 3 , 2 , 1 ]

list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("the list is palindrome")
else:
    print("the list is not palindrome")
    


#[1,"abc","abc",1]

list1 = [ 1 , "abc" , "abc" , 1 ]
list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("the list is palindrome")
else:
    print("the list is not palindrome")

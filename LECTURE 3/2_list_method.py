# LIST METHODS



# 1. APPEND  
#( adds one element at the end )

#        0   1   2   3   4
list = [ 2 , 1 , 3 , 5 , 4 ]

list.append(6)
print(list)    #output --> [ 2 , 1 , 3 , 5 , 4 , 6] 




# 2. SORT   
# ( sort the list in ascending order )

#        0   1   2   3   4
list = [ 2 , 1 , 3 , 5 , 4 ]

list.sort()
print(list)   #output --> [ 1 , 2 , 3 , 4 , 5 ]




# 3. SORT (REVERSE)   
# ( sort the list in descending order )

#        0   1   2   3   4
list = [ 2 , 1 , 3 , 5 , 4 ]

list.sort(reverse=True)
print(list)      # output --> [ 5 , 4 , 3 , 2 , 1 ]




# 4. REVERSE  
#  ( reverse the list )

#        0   1   2   3   4
list = [ 2 , 1 , 3 , 5 , 4 ]

list.reverse()
print(list)    #output --> [ 4 , 5 , 3 , 1 , 2 ]




# 5. INSERT (INDEX , ELEMENT)   
# { insert element at index }

#        0   1   2   3   4
list = [ 2 , 1 , 3 , 5 , 4 ]

list.insert( 5 , 6 )
print(list)       #output --> [2 , 1 , 3 , 5 , 4 , 6 ]




# 6. REMOVE  
# ( removes the first occurence of the element )

#        0   1   2   3
list = [ 2 , 1 , 4 , 1 ]

list.remove(1)
print(list)   #output --> [ 2 , 4 , 1]




# 7. POP   
# ( removes element at index)

#        0   1   2   3
list = [ 2 , 1 , 4 , 1 ]

list.pop(1)
print(list)  #output --> [ 2 , 4 , 1 ]




# 8. COUNT
# ( count the occurance of a element)

#        0   1   2   3
list = [ 2 , 1 , 4 , 1 ]

print(list.count(1))   #output --> 2




fruits = [ "b" , "e" , "d" , "a" , "c" ]
fruits.sort(reverse=True)
print(fruits)    
# it will print [ e , d , c , b , a ]




# 9. INDEX

#        0   1   2   3
list = [ 2 , 1 , 4 , 1 ]
print(list.index(4))    # it will give output --> 2 



# 10. SPLIT

#        0   1   2   3
list = [ 2 , 1 , 4 , 1 ]
# to input values in the list 

# eg num = input().split()
# list = num
# it should be space seperated


# 11. JOIN
arr = ["shaurya","singhal"]
name = " ".join(arr)
print(name)


# to make a excel file in CSV format 

# n = ",".join(excel file name)

# L STRIP AND R STRIP 


# EXTENT 
#        0   1   2   3
list = [ 2 , 1 , 4 , 1 ]
# add two list together
list1= [ 5 ,6 , 7]

list.extend(list1)
print(list)

# DEEPCOPY
# TO SAVE MEMORY IT GIVE THE POINT OF A ARRAY TO ANOTHER ONE 



# COPY  
l = [ 2 , 1 , 4 , 1 ]
l1= [ 5 ,6 , 7]

l = l1.copy()
print(l)
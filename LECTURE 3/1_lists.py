# LISTS    {MUTABLE}

# a build in data type that stores set of value
# it can store elements of different types (integer, float, string, etc)

#         0   1   2  3  4
marks = [90,95.1,56,78,89]  #LIST

print(marks)
print(type(marks))   #list

# we can access perticular element in list

print(marks[2])  # 56

print(len(marks))  #prints the length of the list

# we can store multiple data types in list

student = [ "shaurya" , 80 , "meerut"]


# STRINGS --> inmutable (can not change)

# LIST --> mutable (can be changed)
# EG 

print(student)

student[1] = 85
print(student)   # now the marks are changed


# LIST SLICING

# list_name[ starting_idx : ending_idx ] 
# here also the ending index in not included

#         0  1  2  3  4
marks = [50,60,70,80,90]
#        -5 -4 -3 -2 -1

print(marks[1:3]) # output --> 60 , 70

print(marks[:4])  #output --> 50 , 60 , 70 , 80

print(marks[2:])  #output --> 70 , 80 , 90 {same as marks[1:len(marks)]}

print(marks[-5:-2]) #output --> 50 , 60 , 70
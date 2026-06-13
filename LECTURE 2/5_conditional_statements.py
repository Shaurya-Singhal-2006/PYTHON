# CONDITIONAL STATEMENT

# if-elif-else (SYNTAX)

#  if(condition):
#      statement 1
#  elif(condition):
#      statement 2
#  else:
#      statement 3



light = "red"

if(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("WAIT")
elif(light == "green"):
    print("GO")
else:
    print("the traffic light is broken")

# INDENTATION
# indentation means proper spacing 

marks = int(input("enter student marks: "))

if(marks >= 90):
    print(" grade A")
elif(marks < 90 and marks >=80):
    print("grade B")
elif(marks < 80 and marks >=70):
    print("grade C")
else:
    print("grade D")

# NESTED CONDITION

# if(condition):
#     if(condition):
#         statement

# EG

age = int(input("enter users age : "))

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
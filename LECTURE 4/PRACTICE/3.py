# WAP to enter marks of 3 subject from the user and store them in a dictionary 
# start with an empty dictionary and add one by one 
# use subject name as key and marks as values

marks = {}

c = int(input("enter the marks of c: "))
marks.update({"c" : c})

prob = int(input("enter the marks of problem solving: "))
marks.update({"problem solving" : prob})

linux = int(input("enter the marks of linux: "))
marks.update({"linux" : linux})

print(marks)
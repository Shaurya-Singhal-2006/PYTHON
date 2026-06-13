# create student class that takes name and marks of 3 subjects as arguments in constructor
# then create a method to print the average

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        avg = sum/3
        print("hello :",self.name,"your average is:",avg)


s1 = student("shaurya" , [92,85,70])
s1.average()
        
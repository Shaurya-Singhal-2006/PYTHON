# METHODS
# methods are functions that beongs to objects

class student:

    #constructor
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    
    # methods
    def welcome(self):
        print("welcome student:",self.name)
    
    # methods
    def get_marks(self):
        return self.marks


s1 = student("shaurya",92)
s1.welcome()
print(s1.get_marks())

s2 = student("karan",85)
s2.welcome()
print(s2.get_marks())
# _init_ function

# CONSTRUCTOR

# all classes have a function called _init_(), which is always executed when the object is being initiated

class student:
    def __inti__():
        print("adding students to database")

# creating class

# class student:
#  def __init__(self,fullname):
#     self.name = fullname

# the self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class

class student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding students info to database..")

s1 = student("shaurya" , 92)
print(s1.name , s1.marks) #shaurya 92

s2= student("aman" , 85)
print(s2.name , s2.marks)  #aman 85

# attributes --> data stored inside the the class or object



class student:

    # default constructors
    def __init__(self):
        pass


    # parameterized constructors
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding students info to database..")

# CLASS AND INSTANCE ATTRIBUTES

# things which which are common among all data we make them class attribute

class student:

    college = "UPES"

    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding students info to database..")

s1 = student("shaurya" , 92)
print(s1.name , s1.marks) #shaurya 92

s2= student("aman" , 85)
print(s2.name , s2.marks)  #aman 85

print(student.college)
print(s1.college)

# object attri >> class attribute
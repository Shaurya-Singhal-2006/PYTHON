# PRIVATE (LIKE) ATTRIBUTE AND METHODS

# conceptual implementations in python
# private attribute and methods are meant to be used only within the class
# and are not accessible from outside the class


# this is public(we can use it outside class)
class student:
    def __init__(self,name):
        self.name = name

s1 = student("shaurya")
print(s1.name)


# private 
class account:
    def __init__(self,acc_no,pasw):
        self.acc_no = acc_no
        self.__pasw = pasw    #now we can not access the password outside the class

user1 = account("12345","abcd")

print(user1.acc_no)
# print(user1.__pasw) this will give error



class greeting:

    def __hello(self):
        print("hello user")   #we cannot access it from outside

    def welcome(self):
        self.__hello()      #but this can be accessed inside the class
    
s1 = greeting()
s1.welcome()
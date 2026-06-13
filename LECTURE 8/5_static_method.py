# STATIC METHOD
# method that don't use self parameter (work at class level)

class student:
    @staticmethod   #decorator
    def college():
        print("UPES")

# self is used for object

# decorator aalows us to wrap another function 
# inorder to extend the behavior of the wrapped function, 
# without permanently modifying it

s1 = student()
s1.college()
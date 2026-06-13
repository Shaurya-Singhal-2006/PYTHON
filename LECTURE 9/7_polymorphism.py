# POLYMORPHISM : operator overloading
# when the same operator is allowed to have different meaning according to the context

print(1 + 3) #4
print("hello " + "world") #concatination
print([1,2,3] + [4,5,6]) #merge

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

num1 = complex(1,2)
num1.shownumber()

num2 = complex(3,6)
num2.shownumber 

# dunder function (__function__)

# a + b addition  a__add__(b)
# a - b subtraction  a__sub__(b)
# a * b multiply  a__mul____(b)
# a / b divide  a__truediv____(b) 
# a % b modulo  a__mod____(b)

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal,newimg)
    
num1 = complex(1,2)
num1.shownumber()

num2 = complex(3,6)
num2.shownumber 

num3 = num1 + num2 
num3.shownumber()


    

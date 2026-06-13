# SUPER METHOD
# super() method is used to access methods of the parents class

class car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("csr stopped")


class toyotacar(car):
    def __init__(self,name ,type):
        super().__init__(type)           #we this to call parent class in child class
        self.name =  name
        super().start()

car1 = toyotacar("pirus","electric")
print(car1.type)

# The super() method in Python is primarily used in object-oriented programming to access and call methods 
# or attributes of a parent 
# or sibling class from within a subclass
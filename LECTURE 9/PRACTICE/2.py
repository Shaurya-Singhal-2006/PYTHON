# define a employee class with attribute role,department and salary this class also has
# a showdetail() method

# create an engineer class that inherits properties from employee abd has additional attributs
# name and age

class employee:
    def __init__(self,role,depart,salary):
        self.role = role
        self.department = depart
        self.salary = salary

    def showdetail(self):
        print("role =",self.role)
        print("department =",self.department)
        print("salary =",self.salary)

class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("engineer","IT","50,000")


# emp1 = employee("engineer","IT","50,000")
# emp1.showdetail()


eng1 = engineer("rohan",28)
eng1.showdetail()
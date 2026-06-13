# INHERITANCE
# when our class(child/derived) derives the properties and method of another class(parent/base)


# parent
class car:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")


# child
class toyotacar(car):
    def __init__(self,name):
        self.name = name



car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

car1.start()
car1.stop()  


# TYPES

# 1. single inheritance          {base(parent) --> derived(child)}
# 2. multi-level inheritance     {base(parent) --> derived(child) --> derived(child)}
# 3. multiple inheritance        {base(parent) --> derived(child) <-- base(parent)}

class A:
    varA = "classA"

class B:
    varB = "classB"

class C(A,B):
    varC = "classC"

s1 = C()
print(s1.varA)
print(s1.varB)
print(s1.varC)
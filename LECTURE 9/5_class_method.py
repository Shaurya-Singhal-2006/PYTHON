# CLASS METHOD
# a class method is bpund to the class and receive the class as an implicit first argument

# NOT --> static method cant access or modify class state and generally for utility 

class person:
    name = "anonymous"

    def changename(self,name):
        self.name = name
    

p1 = person()
p1.changename("shaurya")
print(p1.name)          # shaurya
print(person.name)      # anonymous




# we want to make changes to the class so

class person:
    name = "anonymous"

    def changename(self,name):
        person.name = name    #we can do this to save the changes to the class
    
p1 = person()
p1.changename("shaurya")
print(p1.name)          # shaurya
print(person.name)      # shaurya


# OR

class person:
    name = "anonymous"

    @classmethod
    def changename(cls,name):
        cls.name = name   #this is going to make changes to the class

p1 = person()
p1.changename("shaurya")
print(p1.name)          # shaurya
print(person.name)      # shaurya


# 1. static method ()
# 2. class method (cls)
# 3. instance method (self)


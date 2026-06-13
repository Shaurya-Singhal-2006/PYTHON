# PROPERTY DECORATOR
# we use @property decorator on any method in the class to use the method as a property

class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy+self.chem+self.math)/3) + "%"
        
    # def cal_per(self):
    #     self.percentage = str((self.phy+self.chem+self.math)/3) + "%"


    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"


s1 = student(95,91,84)
print(s1.percentage)


s1.phy = 90
print(s1.phy)
print(s1.percentage)    #because of property method now the percentage is getting updated


# even if we change marks the percentage remains the same


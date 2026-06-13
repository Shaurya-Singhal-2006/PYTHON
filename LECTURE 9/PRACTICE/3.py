# create a class order which stores item and its price
# use dunder function __gt__() to convey that:
# arder 1 > arder 2 if the price od order 1 > order 2

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price
    
odr1 = order("chips",30)
odr2 = order("chai",15)

print(odr1 > odr2)
# IMPORTANT

# ABSTRACTION
# hinding the implementation deatils of a class and only showing the essential features to the user
# (hiding the unnecessary details)

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True        #unnecessary things
        self.clutch = True     #unnecessary things
        print("car started")

car1 = car()
car1.start()


# ENCAPSULATION
# wrapping data and sunctions into a single unit (object).
# FUNCTIONS IN PYTHON
# block of statement that perform a specific task
# reduntant code --> bad code (convert it into a function)

# EG

# def function_name(para 1 , para 2 ...):
#  some work
#  return value

def sum(a,b):
    s = a + b
    return s

# function_name(argument 1 ,argument 2 ...)

print(sum(5,7))


def printhello():
    print("hello world")

printhello()



# BUILD IN FUNCTIONS --> print() , len() , type() , range()

# PRINT FUNCTION

# (function) def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False
# ) -> None

print("hello ", end=" ")  # this will remove the next line argument
print("world")  # no next line will we there 


# DEFAULT PARAMETERS
# assignign a default value to parameter which is used when no argument is passed

def add(a , b):
    s = a + b
    return s

# print(add())   #it will error that 2 argument missing

# SO

def add(a = 1 , b = 2):
    s = a + b 
    return s

print(add()) #this will give output --> 3


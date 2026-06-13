# DICTIONARY OPERATION


# 1. ACCESS VALUES 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(d["name"]) # --> shaurya singhal




# 2.ADD/UPDATE

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}

d["age"] = 18
print(d) # --> {'name': 'shaurya singhal', 'age': 18, 'batch': 60}      




# 3. DELETE

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}

del d["name"]
print(d) # --> {'age': 19, 'batch': 60}




# 4. MEMBERSHIP 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}

print("age" in d) # --> True 
print("year" in d) # --> False




# 5. LOOPING TROUGH DICT..

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}

for i in d:
    print(i)  

# name
# age
# batch

for i in d.keys():  # prints all the keys of the dict..
    print(i)

for i in d.values():  # prints all the values of the dict..
    print(i)
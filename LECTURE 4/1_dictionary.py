# DICTIONARY IN PYTHON
# dictionaries are used to store data values in key:type pairs
# they are unordered, mutable(can be changed) and dont allow duplicate keys

dict = {
    "name": "shaurya",
    "age": 19,
    "marks" : [92,85,70],
}

# "KEY" : VALUE,

print(dict)

print(dict["name"])
print(dict["age"])
print(dict["marks"])

# to change values
dict["age"] = 20

print(type(dict))  #dict


# null dictionary
null_dict = {}  

# we can add values in it
null_dict["names"] = "shaurya"


# NESTED DICTIONARY

info = {
    "name" : "shaurya",
    "marks" : {
        "linux": 85,
        "C" : 92,
        "problem_solving" : 70,
    }
}

# to access marks of a perticular subject

print(info["marks"]["linux"]) 
print(info["marks"]["C"])   
print(info["marks"]["problem_solving"]) 
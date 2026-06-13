# DICTIONARY FUNCTIONS 

# Keys must be immutable
# Values can be anything
# Dictionaries preserve insertion order (Python 3.7+)


# 1. KEYS
# return all the keys 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(d.keys()) # --> dict_keys(['name', 'age', 'batch'])




# 2. VALUE 
# return all value 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(d.values()) # --> dict_values(['shaurya singhal', 19, 60])




# 3. ITEMS
# return key value paired as tuples

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(d.items()) # --> dict_items([('name', 'shaurya singhal'), ('age', 19), ('batch', 60)])




# 4. GET 
# get values safely (no error)

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(d.get("name")) # --> shaurya singhal
print(d.get("batch")) # --> 60




# 5. UPDATE 
# adds and updates key-value pairs

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
d.update({"college":"UPES"})
print(d.items()) # --> dict_items([('name', 'shaurya singhal'), ('age', 19), ('batch', 60), ('college', 'UPES')])




# 6. POP
# removes a key and returns it value 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(d.pop("name")) # --> shaurya singhal
print(d.items()) # --> dict_items([('age', 19), ('batch', 60)])




# 7. POPITEM 
# remove and returns last inserted key value pair

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
d.popitem()
print(d.items()) # --> dict_items([('name', 'shaurya singhal'), ('age', 19)])




# 8. CLEAR 
# removes everything from the dictionary and return empty one 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
d.clear()
print(d.items()) # --> dict_items([])




# 9. COPY 
# creates a shallow copy of the original dictionary 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
d2 = d.copy()
print(d2) # --> {'name': 'shaurya singhal', 'age': 19, 'batch': 60}




# 10. SETDEAULT
# gets value if exists , otherwise insert key with deafult values

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(d.setdefault("year",2006)) # --> 2006
print(d)  # --> {'name': 'shaurya singhal', 'age': 19, 'batch': 60, 'year': 2006}
print(d.setdefault("age",18))  # --> 19




# 11. FROMKEY
# creates a new distionary from keys 

d = ["a","b","c"]
a = dict.fromkeys(d,0)
print(a) # --> {'a': 0, 'b': 0, 'c': 0} 

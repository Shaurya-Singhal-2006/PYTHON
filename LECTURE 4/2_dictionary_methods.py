# DICTIONARY METHODS

info = {
    "name":"shaurya",
    "age":19,
    "subject": "CSE",
}

# 1. KEYS
# return all keys
  
print(info.keys())        #output --> ['name', 'age', 'subject']
print(list(info.keys()))



# 2. VALUES
# return all values

print(info.values())   #output --> ['shaurya', 19, 'CSE']



# 3. ITEMS
# returns all (key , val) pairs as tuple

print(info.items())  #output --> [('name', 'shaurya'), ('age', 19), ('subject', 'CSE')]



# 4. GET
# return the key according to values

print(info.get("name"))  #output --> shaurya

print(info["name2"])  #error
print(info.get("name2")) #no error --> None



# 5. UPDATE
# inserts the specified items to the dictionary

info.update({"city" : "meerut"})     
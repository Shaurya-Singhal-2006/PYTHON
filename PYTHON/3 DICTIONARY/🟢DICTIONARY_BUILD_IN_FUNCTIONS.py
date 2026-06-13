# BUILD IN FUNCTION USED WITH DICTIONARY

# 1. LEN 
# returns the length of the dictionary 

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(len(d)) # --> 3




# 2. MAX/MIN
# returns the max and min value present in the dictionary ( works only on keys )

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(max(d)) # --> name
print(min(d)) # --> age
# beacuse of the first alphabet of the string (key) (n,a)
# we can change it by using the key function to change the sorting type 




# 3. SORTED 
# return sorted dictionary (workd only on keys )

d = {
    "name":"shaurya singhal",  # key : value
    "age": 19,
    "batch": 60,
}
print(sorted(d)) # --> ['age', 'batch', 'name'] (sorted according to the first alphabet of the string)
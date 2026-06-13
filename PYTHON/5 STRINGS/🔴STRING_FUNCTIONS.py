#  STRING FUNCTIONS


# Important fact
# Strings are immutable → every function returns a new string 


# 1. UPPER 
# converts all character to upper case

a = "hello my name is shaurya"
print(a.upper()) # --> HELLO MY NAME IS SHAURYA




# 2. LOWER
# convert all character to lower case

a = "Hello My Name IS Shaurya"
print(a.lower()) # --> hello my name is shaurya




# 3. CAPITALIZE
# makes the first character uppercase , rest lowercase

a = "hello my name is shaurya"
print(a.capitalize()) # --> Hello my name is shaurya (only the h in hello is capitalized)




# 4. TITLE 
# capatilize the first letter of each word  

a = "hello my name is shaurya"
print(a.title()) # --> Hello My Name Is Shaurya




# 5. SWAPCASE
# swaps upper case with lowercase

a = "Hello My Name Is Shaurya"
print(a.swapcase()) # --> hELLO mY nAME iS sHAURYA




# 6. CASEFOLD
# aggresive lowercase 

s = "straße"
print(s.lower())     # straße
print(s.casefold())  # strasse




# SEARCH AND POSITION FUNCTION


# 1. FIND
# returns the index of first occurence , else -1

a = "Hello My Name Is Shaurya"
print(a.find("N")) # --> 9
print(a.find("z")) # --> -1




# 2. RFIND 
# searches from the right 

a = "Hello My Name Is Shaurya"
print(a.rfind("S"))  # --> 17




# 3. INDEX 
# same as find but raises error if the char is not found

a = "Hello My Name Is Shaurya"
print(a.index("e")) # --> 1




# 4. RINDEX
# right side version of index

a = "Hello My Name Is Shaurya"
print(a.rindex("a")) # --> 23




# 5. COUNT 
# count occurences
a = "Hello My Name Is Shaurya"
print(a.count("a")) # --> 3





# MODIFING STRINGS


# 1. REPLACE
# replace substring

a = "hello my name is shaurya"
print(a.replace("a","x")) # --> hello my nxme is shxuryx




# 2. STRIP 
# remove spaces from both ends

a = "   hello   "
print(a.strip())  # --> hello 




# 3. LSTRIP 
# removes lefy spaces

a = "      hello"
print(a.lstrip()) # --> hello




# 4. RSTRIP
# removes the spaces from the right

a = "hello         "
print(a.rstrip()) # --> hello




# 5. SPLIT
# split string into list

a = "h,e,l,l,o"
print(a.split(",")) # --> ['h', 'e', 'l', 'l', 'o']




# 6. RSPLIT
# split from right

a = "h,e,l,lo"
print(a.split(",")) # --> ['h', 'e', 'l', 'lo']




# 7. SPLITLINES
# split at line break

a = "hello\nbye"
print(a.splitlines()) # --> ['hello', 'bye']




# 8. JOIN 
# join elements using string as seperator

a = ["hello","guys","my","name","is","shaurya"]
print("-".join(a)) # --> hello-guys-my-name-is-shaurya




# 9. CENTER
# centers the string

a = "hi"
print(a.center(6,"-")) # -- > --hi--




# 10. LJUST
# left align string

a = "hello"
print(a.ljust(10,"-")) # --> hello-----




# 11. RJUST
# right align string

a = "hello"
print(a.rjust(10,"-")) # --> -----hello




# 12. ZFILL
# pads with zeros

a = "hello"
print(a.zfill(10)) # --> 00000hello





# 13. STARTWITH
# checks starting substring

a = "hello"
print(a.startswith("he")) # --> True




# 14. ENDSWITH
# checks ending substring

a = "hello"
print(a.endswith("lo")) # --> True




# 15. REMOVEPREFIX
# removes prefix

a = "unhappy"
print(a.removeprefix("un")) # --> happy




# 16. REMOVESUFFIX
# remove suffix

a = "file.txt"
print(a.removesuffix(".txt")) # --> file




# 17. FORMAT
# formating string

print("{} + {} = {}".format(1,2,3)) # --> 1 + 2 = 3




# FORMAT_MAP
# uses dictionary for formatting

data = {
    "name":"shaurya singhal",
    "age":19,
}
s = "hello my name is {name} and i am {age} years old"
print(s.format_map(data)) # --> hello my name is shaurya singhal and i am 19 years old


# 19. ENCODE
# convert string to bytes

a = "hello my name is"
print(a.encode("utf-8")) # --> b'hello my name is'





# 20. MAKETRANS
# Creates translation table.
# Maps each character in from to the corresponding character in to.

s = "abc cab"
table = str.maketrans("abc","123")
print(s.translate(table)) # --> 123 312 (gave value to abc and printed it)




# 21. TRANSLATE
# Replaces characters using table.

# replaces characters
# removes characters
# using a translation table created by str.maketrans()

table = str.maketrans("abc", "123")
s = "cab"
print(s.translate(table)) # --> 312





# 22. EXPANDTABS
# replace tab with spaces

a = "hello\tguys"
print(a.expandtabs(20)) # --> hello               guys
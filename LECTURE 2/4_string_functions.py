# STRING FUNCTIONS

str = "i am coder"

str.endswith( "er" ) 
# returns true if string ends with substr

str.capitalize()
#capitilizes 1st char

str.replace( "old" , "new" )
# replaces all occurrences of old with new

str.find( "word" )
# returns 1st index of 1st occurrence

str.count( "am" )
# counts the occurence of substr in string



print(str.endswith("er"))        # --> True
print(str.capitalize())          # --> I am coder
print(str.replace("a" , "o"))    # --> i om coder
print(str.find("a"))             # --> 2
print(str.count("am"))           # --> 1
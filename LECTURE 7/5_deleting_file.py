# DELETING A FILE

# using the os module
# module (like a code library) is a file written by another programmer 
# that generally has a functions we can use

# pip (package installer for python) install (library name)

import os

with open("PYTHON/LECTURE 7/delete.txt" , "w") as f:
    f.write("this file will be deleted")

answer = input("ready to delete the file :")

if(answer == 'yes'):
    os.remove("PYTHON/LECTURE 7/delete.txt")
else:
    print("cancelled")
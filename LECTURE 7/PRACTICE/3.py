# search if the word "learning" exists in the file or not

with open("PYTHON/LECTURE 7/PRACTICE/practice.txt", "r") as f:
    data = f.read()
    
found = data.find("learning")
if(found != -1):
    print("exists")
else:
    print("not exist")
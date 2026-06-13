# WRITTING

# w : write mode
# a : append mode

f = open("PYTHON/LECTURE 7/demo.txt" , "w")
f.write("this is a new line")  # overwrites the entire file
f.close

a = open("PYTHON/LECTURE 7/append.txt" , "a")
a.write("this is a new file and it is append\n")
a.write("this is the next line")
a.close
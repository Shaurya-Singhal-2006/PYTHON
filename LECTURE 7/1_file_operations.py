# FILE I/O
# python can be used to perform operations on a file (read and write)


# types of file

# Text file : txt , docx , log etc
# Binary files: mp4 , mov , png , jpeg etc



# OPEN 

# f = open("file name " , "r") 

# r : read mode
# w : write mode


f = open("PYTHON/LECTURE 7/demo.txt", "r")
data = f.read()

print(data)
print(type(data))
f.close

# 'r' --> open for reading (default) 
# 'w' --> open for writting truncating the file first (overwrite)
# 'x' --> create a new file and open it for writting
# 'a' --> open for writting, appending to the end of the file if it exists
# 'b' --> binary mode
# 't' --> text mode (default)
# '+' --> open a disk file for updating (reading and writting)

# 'r+' --> read + overwrite (pointer start) --> no truncate
# 'w+' --> read + overwrite                 --> truncate(start with empty file)
# 'a+' --> read + append (pointer end)      --> no truncate
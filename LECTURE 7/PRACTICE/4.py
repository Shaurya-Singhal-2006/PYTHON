# WAF to find in which line of the file does the word "learning" occur first
# print -1 if word not found

def line():
    word = "learning"
    data = True
    line_no = 1
    with open("PYTHON/LECTURE 7/PRACTICE/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1        


line()
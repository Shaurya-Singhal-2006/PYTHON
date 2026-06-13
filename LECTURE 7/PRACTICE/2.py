# WAF to replace all occurence of "java" with "python" in previous file

with open("PYTHON/LECTURE 7/PRACTICE/practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java","python")

with open("PYTHON/LECTURE 7/PRACTICE/practice.txt", "w") as f:
    f.write(new_data)
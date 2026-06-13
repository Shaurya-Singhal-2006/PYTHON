# from a file containing numbers seperatd by commas print the count of even numebrs

with open("PYTHON/LECTURE 7/PRACTICE/number.txt" , "r") as f:
    data = f.read()

count = 0
nums = data.split(",")
for val in nums:
    if(int(val) % 2 == 0):
        count += 1

print(count)
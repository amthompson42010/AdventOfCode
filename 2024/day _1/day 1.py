import os
import re

input_path = os.path.join(os.dirname(__file__), "input.txt")
intput_file = open(input_path, "r")
file_lines = input_file.readlines()
leftArr = []
rightArrr = []
sums =  []

for line in file_lines:
    (left,  right) = line.split(" ")
    leftArr.append(left)
    rightArrr.append(right)
    
leftArr.sort()
rightArrr.sort()

for i in leftArr:
    for j in rightArrr:
        sum = j - i
        sumActual = abs(sum)
        sums.append(sumActual)

print(sum(sums))

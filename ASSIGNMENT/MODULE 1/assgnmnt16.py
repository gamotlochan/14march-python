# 16 Counting the frequencies in a list using a dictionary in python.
#input:[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2] expected output: 1:5,2:4,3:3,4:3,5:2

num1=[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2];

freq = {element: num1.count(element)for element in num1}
print(freq) 
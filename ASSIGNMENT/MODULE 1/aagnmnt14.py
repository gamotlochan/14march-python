#14 write a python program to find the highest 3 values in a dictionary.


from heapq import nlargest
my_dict = {'a':200,'b':500,'c':3055,'d':1000,'e':80}
three_largest = nlargest(3,my_dict, key=my_dict.get)
print(three_largest)

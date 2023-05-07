#8 write a python program to check whether a list contains a sublist.

list=['a','x',[1,3,4,5,'lochan']]

for i in list:
    if len(i) > 1:
        print("sublist is present in list")
        continue

    else:
        print("sublist is not present in list")

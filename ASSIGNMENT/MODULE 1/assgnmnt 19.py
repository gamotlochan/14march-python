#19 write a python function that takes a list and returns a new list with unique elements of the first list.

def uniquelst(dat1):
    x=[]
    for p in dat1:
        if p not in x:
            x.append(p)
        return x
datalist=[]
n=int(input("enter total elements in a list "))
for k in range (n):
    dat=int(input("enter in data list: "))
    datalist.append(dat)

print("original List",datalist)
print(uniquelst(datalist))

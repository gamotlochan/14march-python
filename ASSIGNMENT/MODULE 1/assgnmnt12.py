#12 write a python program to convert a list of tuples into a dictionary.

lst=[('a',14),('b',16),('c',12),('d',10),('a',15)]

d={}
for a,b in lst:
    d.setdefault(a,[]).append(b)
print(d)


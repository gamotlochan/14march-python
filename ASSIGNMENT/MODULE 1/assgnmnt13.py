#13 write a python program to sort a dictionary(ascending/descending)by value.


import operator
d ={1:2, 4:3, 5:6, 7:8, 0:0}
print("original dictionary:",d)

asc = dict(sorted(d.items(), key=operator.itemgetter(1)))
print("dictionary in ascending order by value:",asc)

dsc = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("dictionary in decending order by value:",dsc)

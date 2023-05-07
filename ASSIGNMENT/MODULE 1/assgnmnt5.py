#5 write a python program to add 'ing'at the end of a given string (length should be at least 3).if the given string already ends with 'ing' then add 'ly' instead if the sring length of the
#given string is less than 3,leave it unchanged

a = "ride"
if len(a) > 3:
    if a.endswith('ing'):
        a += 'ly'
    else:
        a += 'ing'
print(a)

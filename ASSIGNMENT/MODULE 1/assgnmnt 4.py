
#4 write a python program to get a single string from two given strings, separated by a space and swap the first two character of each string.

v2,v1="abcd","uvwx"
t = v2
v2=v1[0:2]+ v2[2:]
v1=t [0:2] +v1[2:]
print(v2+' '+v1)

#15 Given a number n, write a python program to make and print the list of fibonacci series up to n.
#input: n=7 hint: first 7 numbers are 0,1,1,2,3,5,8,13

n=int(input("enter number"))
x=0
y=1
z=0
while z<=n:
    print(z)
    x=y
    y=z
    z=x+y

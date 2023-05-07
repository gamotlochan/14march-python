#18 python program to find factorial of number using recursion.

def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))
n=int(input("enter a number here: "))
res=fact(n)
print("factorial of ",n,"is",res)

#17 write a python program using function to find the sum of odd series and even series
#odd series: 12/1! + 32/3! + 52/5!+.....n
#even series:22/2! + 42/4! + 62/6!+.....n

numbers=[12/1 + 32/3 + 52/5,22/2 + 42/4 + 62/6]
eventotal=0
oddtotal=0

for number in numbers:
    if (number % 2==0):
        eventotal += number
    else:
        oddtotal += number

print("the sum of even numbers=",eventotal)
print("the sum of odd numbers=",oddtotal)
 

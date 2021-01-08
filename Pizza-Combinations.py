'''
On any given day, a pizza company offers the choice of a certain
number of toppings for its pizzas. Depending on the day, it provides
a fixed number of toppings with its standard pizzas.

Write a program that prompts the user (the manager) for the number of
possible toppings and the number of toppings offered on the standard
pizza and calculates the total number of different combinations of toppings.

Recall that the number of combinations of k items from n possibilities
is given by the formula nCk = n!/k!(n−k)!.
'''


'''
prompt user for number of possible toppings x
prompt user for number of toppings on standard pizza y

get factorial of x

get factorial of y

if y = x
  print possible combinations 1
if y is greater than x
  print possible combinations 0
if y is 1
  print possible combinations y
else use binomial coefficient to get possible combinations
print possible combinations

'''

x = int(input('Enter number of possible toppings: '))
y = int(input('Enter number of toppings on standard pizza: '))


if x == 0:
    xfact = 1
elif x == 1:
    xfact = 1
else:
    xfact = 1
    for i in range(1, x + 1):
           xfact *= i
           continue

if y == 0:
    yfact = 1
elif x == 1:
    yfact = 1
else:
    yfact = 1
    for i in range(1, y + 1):
           yfact *= i
           continue
        
import sys       

if y == x :
    print('Possible Combinations: 1')
    sys.exit()
if  y > x:
    print('Possible Combinations: 0')
    sys.exit()
if y == 1:
    print('Possible Combinations: ', x)
else:
    posscomb = xfact // (yfact*(x-y))
    print('Possible Combinations:', posscomb)

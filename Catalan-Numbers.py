'''
Write a program that prompts the user for an integer and calculates
that number of Catalan Numbers.
'''


'''
define factorial function

define catalan function

prompt user for number

set i to 0

while i is less than number
    print catalan number of i
    increment i

'''



def fact(x):
   """Function that returns the factorial of its argument
   Assumes that its argument is a non-negative integer """
   res = 1
   for i in range(1, x+1):
       res *= i
   return res


def catalan(x):
   """Function that returns the catalan of its argument
   Assumes that its argument is a non-negative integer """
   res = (fact(2*x)) // ((fact(x + 1)) * (fact(x)))
   return res

number = int(input('Enter number: '))

i = 0

while i < number:
    print(catalan(i))
    i += 1

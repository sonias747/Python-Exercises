'''
A perfect number is a positive integer thatis equal to
the sum of its proper factors (its positive integer factors
excluding the number itself). For example, 6 (with proper
factors 1, 2 and 3) and 28 (with proper factors 1, 2, 4, 7 and 14)
are perfect numbers.

Write a program that prompts the user for a positive integer and
finds all the perfect numbers up to and including that number.
'''



'''
define function findDivisors(num)
initialise divisors
for i from 1 to num do
    if num1 mod i == 0 then
        add i to divisors
return divisors

prompt user for integer
initialise perfnums

if number is less than or equal to 0
  print number should be greater than 0
else
  for i in range 1 to number plus 1
  call findDivisors function for i
  initialise total
  for d in divisors
    increment total by d
  if total is equal to i
    add i to tuple perfnums
  print perfnorms tuple  

'''



def findDivisors(num):
    """Finds the divisors of num

    Assumes that num is a positive integer
    Returns a tuple containing the divisors of num """

    divisors = ()
    for i in range(1, (num)):
        if num % i == 0:
            divisors += (i,)
    return divisors


number = int(input('Enter a positive integer: '))
perfnums = ()

if number <= 0:
    print('Numbers should be > 0.')
else:
    for i in range(1, number+1):
        divisors = findDivisors(i)
        total = 0
        for d in divisors:  #finds the sum of the divisors of i
            total += d
        if total == i:
            perfnums += (i,)
        
    print('The perfect numbers up to and including', number, 'are', perfnums) 


'''
Write a program that searches for prime numbers in a range of integers.
The program should print out an appropriate message if a number is a prime number.
However, instead of printing out the first pair of factors that it discovers
for a non-prime number, this program should print out all the pairs of factors.
'''



'''
define function primenumber(x)       
  if x is greater or equal than 2
    for y in range (2, x)
       if number is equally divisible by number other than 1 and itself
          return false
  else if number is less than 2
    return false
  if none of the previous conditions apply return true

for number in range (2, 20)
   if primenumber(number) is true
      print number is a prime number
   else
      for i in range (1, number)
          if mod number and i equals zero
             print number equals i multiplied by number divided by i
print finished             

'''
def primenumber(x):
    """Function that tests whether a number is prime or not

    Assumes that its argument is a non-negative integer 
    """
    if x >= 2:
        for y in range(2,x):
            if not (x % y):
                return False
    else:
        return False
    return True


for number in range (2, 20):
    if primenumber(number) == True:
        print(number, 'is a prime number.')
    else:
        for i in range (1, number):
            if number % i == 0:
               print(number, 'equals', i, '*', number//i)


print('Finished!')





            
            


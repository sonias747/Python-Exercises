'''
Write a program that prompts the user for a series of positive
integers and, for each of the numbers entered, uses a while loop
to calculate the factorial of that number.

The program should stop when a negative number is entered.
'''


'''  
prompt user for number

while number is more than or equal to zero
   if number is 0
     factorial is 1
   else if number is 1
    factorial is 1   
   else
    factorial is 1
   for i in range (1, number +1)
    factorial is factorial * 1
   print(Factorial of number is factorial)
   prompt user for number again
else:   
print program finished

'''

number = int(input('Enter number: '))

while number >= 0:  
    if number == 0:
          fact = 1
    elif number == 1:
          fact = 1
    else:
          fact = 1
          for i in range(1, number + 1):   
              fact *= i
    print('Factorial of', number, 'is', fact)
    number = int(input('Enter number: ')) 
else:
     print('Program Finished')   

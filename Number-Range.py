'''
Write a program that takes as input an integer and prints out one of
the following messages indicating whetherthe number is in one of the specified ranges:

• Number is equal to 0
• Number is greater than 0 and less than or equal to 20
• Number is greater than 20 and less than or equal to 40
• Number is greater than 40 and less than or equal to 60
• Number is greater than 60 and less than or equal to 80
• Number is greater than 80 and less than or equal to 100
• Number is greater than 100

If the number entered is less than 0, a message should be printed out to that effect.
'''



number = int(input('Enter a number:'))

if number == 0:
    print('Number is equal to zero')
elif 0 < number <= 20:
    print('Number is greater than 0 and less than or equal to 20')
elif 20 < number <= 40:
    print('Number is greater than 20 and less than or equal to 40')
elif 40 < number <= 60:
    print('Number is greater than 40 and less than or equal to 60')
elif 60 < number <= 80:
    print('Number is greater than 60 and less than or equal to 80')
elif 80 < number <= 100:
    print('Number is greater than 80 and less than or equal to 100')
elif number > 100:
    print('Number is greater than 100')
else:
    print('Number is less than 0')
    
    

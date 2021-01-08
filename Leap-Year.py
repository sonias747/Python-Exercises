'''
Write a program that prompts the user for a year and checks whether
the year is a leap year.
'''


'''
prompt user for year

if (year is not exactly divisible by 4) then (it is a common year)
else
if (year is not exactly divisible by 100) then (it is a leap year)
else
if (year is not exactly divisible by 400) then (it is a common year)
else (it is a leap year)
'''

year = int(input('Enter year: '))

if year % 4 != 0:
    print(year, 'is not a leap year')
elif year % 100 != 0:
     print(year, 'is a leap year')    
elif year % 400 != 0:
     print(year, 'is not a leap year')
else:
    print(year, 'is a leap year')
     

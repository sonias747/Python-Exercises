'''
Write a program that takes as input a string and checks whether the
string entered is the name of a town or city known to the program.
The towns and cities should include: Dublin, Belfast, Cork, Limerick,
Derry, Galway, Lisburn, Kilkenny, Waterford and Sligo.

If the name of one of these towns or cities is entered, the program
should print out the string “You entered x. x is in y.”, where x is
the name of the town or city and y is the province (Ulster, Munster,
Leinster or Connacht) in which the town or city is situated.

If the string entered is not recognised, the message “Sorry, I didn’t
recognise that name.” should be printed out.
'''


town = input('Enter a city or town: ')

w = 'Ulster'
x = 'Munster'
y = 'Leinster'
z = 'Connacht'

if town == 'Dublin':
    print('You entered ' + town + '. ' + town + ' is in ' + y + '.')
elif town == 'Belfast':
    print('You entered ' + town + '. ' + town + ' is in ' + w + '.')
elif town == 'Cork':
    print('You entered ' + town + '. ' + town + ' is in ' + x + '.')
elif town == 'Limerick':
    print('You entered ' + town + '. ' + town + ' is in ' + x + '.')
elif town == 'Derry':
    print('You entered ' + town + '. ' + town + ' is in ' + w + '.')   
elif town == 'Galway':
    print('You entered ' + town + '. ' + town + ' is in ' + z + '.')
elif town == 'Lisburn':
    print('You entered ' + town + '. ' + town + ' is in ' + w + '.')
elif town == 'Kilkenny':
    print('You entered ' + town + '. ' + town + ' is in ' + y + '.')
elif town == 'Waterford':
    print('You entered ' + town + '. ' + town + ' is in ' + x + '.')
elif town == 'Sligo':
    print('You entered ' + town + '. ' + town + ' is in ' + z + '.')
else:
    print('Sorry, I didn’t recognise that name.')
   

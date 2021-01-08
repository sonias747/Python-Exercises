'''
Write a password checking program to keep track of how
many times a user has entered their password incorrectly.
Store a password in your program. If the user enters the
password incorrectly more than three times,
print “You have been denied access.” and terminate the program.
If the password is correct, print “You have successfully logged in.”
and terminate the program.
'''



'''
set password
set counter

while counter is less than or equal to 3
   promt user for password
   if the correct password is entered
     print You have successfully logged in
     end the program
   else if the wrong password is entered
     increase counter by 1 and loop
else
   print You have been denied access
   print program finished
'''



password = 'Tree'
counter = 0

while counter <= 3:
    password_attempt = input('Enter password: ')
    if password == password_attempt:
       print('You have successfully logged in.')
       break
    elif password != password_attempt:
       counter += 1
else:
      print('You have been denied access.')
      print('Program finished.')

     

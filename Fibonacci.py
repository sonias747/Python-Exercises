'''
Write a program that prompts the user for an integer and uses
a while loop to calculate that number of terms of the Fibonacci Series.
'''


'''
set f_0 to 0
set f_1 to 1

prompt user for number of terms to calculate - limit

if limit is less than or equal to 0
   print number is less than or equal to 0
else if limit is 1
   print series is 0
else if limit is 2
   print series is 0, 1
else print series is 0, 1
   set a to f_0
   set b to f_1
   set i to 2
   while i is less than limit
      fibonaccis series = a + b
      print space fibonacci series..
      set a to b
      set b to fibonacci series
      increment i by 1
Program finished      
'''


f_0 = 0
f_1 = 1

limit = int(input('Enter number: '))

if limit <= 0:
     print('Number entered is less than or equal to 0')
elif limit == 1:
     print('Series is:', f_0)
elif limit == 2:
     print('Series is: ', f_0, ', ', f_1, sep = "")
else:
     print('Series is: ', f_0, ', ', f_1, sep = "", end = "")
     a = f_0
     b = f_1
     i = 2
     while i < limit:
         fib = b + a
         print(' ,', fib, end = "")        
         a = b
         b = fib
         i += 1
print()
print('Program Finished.')

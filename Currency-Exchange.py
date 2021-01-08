'''
Write a program that takes as input an amount of currency (a float) and
an exchange rate to another currency (a float) and prints out the value
of the original amount in the other currency. For the exchange rate, pick
two currencies and use today’s exchange rate.

When the currency amount is entered by the user, the program should check
that the amount is non-negative. If the amount is negative, the message
“Amount must be >= 0. Please try again.” should be printed out and the
program should exit.
'''


euro_pln_conversion = 4.48716
   # Number of Polish Zlotych per euro
   # According to xe.com, 06.10.2020

euro_gbp_conversion = 0.910537
   # Number of British Pounds per euro
   # According to xe.com, 06.10.2020   

euro_amount = float(input('Enter Euro Amount: '))   # Number of Euro

if euro_amount >= 0:
    print('Amount in Polish Zlotych:', euro_amount * euro_pln_conversion)
    print('Amount in British Pounds:', euro_amount * euro_gbp_conversion)
else:
    print('Amount must be >= 0. Please try again.')
    print('Finished!')



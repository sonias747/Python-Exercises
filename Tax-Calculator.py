'''
Write a program that takes as input an amount of income (a float),
divides the amount in the ratio 60:40, calculates the tax due
according to two different tax rates (23% on the larger amount and 41% on the smaller),
and prints out the initial amount, the two different tax amounts,
the total tax and the total nett income (initial amount less taxes).

When the amount is entered by the user, the program should check that
it is non-negative.If the amount of income is negative, the message
“Amount of income must be >= 0. Please try again.” should be printed out
and the program should exit.
'''

income_amount = float(input('Enter income amount: '))
larger_amount = income_amount / 100 * 60
smaller_amount = income_amount / 100 * 40

larger_tax_rate = 23
smaller_tax_rate = 41

larger_amount_tax_due = larger_amount * larger_tax_rate / 100
smaller_amount_tax_due = smaller_amount * smaller_tax_rate /100
total_tax_due = larger_amount_tax_due + smaller_amount_tax_due
total_nett_income = income_amount - total_tax_due

if income_amount >= 0:
     print('Income amount:', income_amount)
     print('Larger amount tax due:', larger_amount_tax_due)
     print('Smaller amount tax due:', smaller_amount_tax_due)
     print('Total tax due:', total_tax_due)
     print('Total nett income:', total_nett_income)
else:
     print('Amount of income must be >= 0. Please try again.')
     print('Finished!')


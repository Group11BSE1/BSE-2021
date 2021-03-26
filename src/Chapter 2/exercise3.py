# Exercise 3
# This program prompts the user for hours and rate per hour
# then computes and prints the Gross pay

# Enter hours
hours = input('Enter Hours: ')

# Enter rate
rate = input('Enter rate: ')

# Compute Gross pay
Gross_pay = int(hours) * float(rate)

pay = str(Gross_pay)
print('Gross_pay: ' + pay)

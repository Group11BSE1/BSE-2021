# Exercise 6
# This program prompts a user for hours worked and the hourly rate
# Then computes the Gross Pay
# Gross Pay is computed with 1.5 times the hourly rate for overtime

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

def computepay(hours, rate):
    gross_pay = hours * rate
    return gross_pay

if hours > 40:
    above_40 = (hours - 40) * (1.5 * rate)
    Pay = (rate * 40) + above_40
    print(round(Pay, 1))
else:
    x = computepay(hours, rate)
    print(round(x, 1))


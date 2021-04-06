# Exercise 1
# This program prompts a user for hours worked and the hourly rate
# Then computes the Gross Pay
# Gross pay is computed with 1.5 times the hourly rate for hours worked above 40

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    above_40 = (hours - 40) * (1.5 * rate)
    Pay = (rate * 40) + above_40
    print(round(Pay, 1))
else:
    Pay = rate * hours
    print(round(Pay, 1))

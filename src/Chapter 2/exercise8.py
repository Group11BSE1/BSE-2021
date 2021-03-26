# Exercise 8
# This program reads the value of C, r, n and t from the user and
# computes and then prints the final value of the investment to the nearest penny
# (Nearest penny means up to 2 decimal places)


C = int(input('Enter initial amount of investment: '))
r = float(input('Enter yearly rate of interest: '))
t = int(input('Enter the number of years: '))
n = int(input('Enter number of times interest is compounded per year: '))

# Compute final value of investment
x = (1 + (r/n))
P = (C * (x ** (n * t)))
print(round(P, 2))

# Exercise 2
# This program reads the value of C, r, n and t from the user and
# computes and then prints the final value of the investment to the nearest penny
# (Nearest penny means up to 2 decimal places)

C = int(input("Enter initial amount of investment: "))
r = float(input("Enter yearly interest rate: "))
t = int(input("Enter number of years: "))
n = int(input("Enter number of times interest is compounded: "))

def investment(C, r, t, n):
    p = (C * (1 + (r / n))) ** (t*n)
    print(round(p, 2))
    return p

investment(C, r, t, n)

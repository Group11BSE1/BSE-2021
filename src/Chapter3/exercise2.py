# Exercise 2
# This program prompts a user for hours worked and the hourly rate
# Then computes the Gross Pay
# The program handles non-numeric input gracefully by printing a message and exiting the program

try:
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    Pay = (hours * rate)
    print(Pay)
except:
    print("Error, please enter numeric input")

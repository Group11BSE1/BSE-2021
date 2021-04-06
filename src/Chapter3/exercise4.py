# Exercise 4
# This program reads an integer value from input, representing someone's age
# and prints out whether they can vote, are too young to vote or are time travellers

try:
    age = int(input("Enter age here: "))

    if age < 0:
        print("You are a time traveller")
    elif 0 <= age <= 17:
        print("Too young to vote")
    else:
        print("You can vote")

except:
    print("Please enter a numeric age value")


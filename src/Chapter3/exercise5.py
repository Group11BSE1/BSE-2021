# Exercise 5: How Much The Wedding Costs (if...else)
# This program prompts a user for the number of people attending their wedding
# and then prints the corresponding price in the console

try:
    number_of_people = int(input("Enter the number of people attending the wedding: "))

    if number_of_people <= 50:
        print("It must cost $4,000 dollars")
    else:
        if number_of_people <= 100:
            print("It must cost $10,000 dollars")
        else:
            if number_of_people <= 200:
                print("It must cost $15,000 dollars")
            else:
                print("It must cost $20,000 dollars")

except:
    print("Number of people should be a numeric integer value")

# Exercise 7
# This program lets the user to enter "location" and "pay" and it evaluates
# what John's decision will be.

try:
    location = input("Enter location: ")
    pay = int(input("Enter pay: "))

    if location == 'Mbarara' and pay <= 4000000:
        print("No Thanks, I can find something better")
    elif location == 'Space' and pay >= 0:
        print("Without a doubt, I'll take it")
    elif location == 'Kampala' and pay < 10000000:
        print("No way!")
    elif location != ('Mbarara' and 'Kampala' and 'Space') and pay < 6000000:
        print("No Thanks, I can find something better")
    else:
        print("Sure, I can work with this")

except:
    print("Enter a numeric integer value for pay")

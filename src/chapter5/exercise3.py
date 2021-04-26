# Exercise 3

#                   GROUP 11 MEMBERS
#       1. NIWAGABA CLEVER      2020/BSE/055/PS
#       2. AINEBYONA ALBERT     2020/BSE/003/PS
#       3. LEMI MANOAH JUNGO    2020/BSE/145/PS

# So far from 20th/04/21 - 25th/04/21

# This program will simulate a simple change maker for a vending machine. It will start with
# a stock of coins and dollars. It will then repeatedly request the price for an item to be
# purchased or to quit. If given a price, it will accept nickels, dimes, quarters, one-dollar and
# five-dollar bills—deposited one at a time—in payment. When the user has deposited enough
# to cover the cost of the item, the program will calculate the coins to be dispensed in change.
# Alternately, the user can cancel the purchase up until full payment has been deposited, in
# which case, the program will calculate the coins to be dispensed to refund any partial
# payment already deposited. With each purchase, the program will update the stock of coins
# and dollars. Before quitting, it will output the remaining stock of coins and dollars.

print(">"*3, "="*20, " RESTART ", "="*20)
print(">"*3)
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")

# 1. At program start, assume a stock of 25 nickels, 25 dimes, and 25 quarters. Print the
# contents of the stock.
# Initializing the stock
nickel = 25
dime = 25
quarter = 25
one = 0
five = 0
total = 0

# Print contents of the stock
print("Stock contains:")
print(nickel, " nickels")
print(dime, " dimes")
print(quarter, " quarters")
print(one, " ones")
print(five, " fives")

# 2. Repeatedly prompt the user for a price in the form xx.xx, where x denotes a digit, or
# to enter ‘q’ to quit.
while True:
    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    if price == 'q':
        print("Thank you for using the vending machine")
        break

    # Checking that the price entered is a (non-negative) multiple of .05 (i.e., it is payable
    # in nickels). If not, then print an error message and start over requesting either a
    # new price or to quit (indicated by entering a ‘q’).

    price = float(price)
    new_price = (round(price * 100))
    multiple = new_price % 5    # For a value to be a multiple, it must return a remainder of zero(0) when divided by a given value
    total = total + price

    # Checking that the price entered is a (non-negative) multiple of .05
    if price < 0 or multiple > 0:
        print("Illegal price: Must be a non-negative multiple of 5 cents.")
        continue

    # Print a menu for indicating the coin/bill deposited or to cancel payment
    else:
        print("""Menu for deposits:
                'n' - deposit a nickel
                'd' - deposit a dime
                'q' - deposit a quarter
                'o' - deposit a one dollar bill
                'f' - deposit a five dollar bill
                'c' - cancel the purchase""")

    dollars = round(price // 1)     # dollars represents absolute value from the price
    cents = round((price % 1) * 100)    # cents is the remainder after the absolute value for dollars is found
    nickels = 0     # nickels represents amount of change in nickels
    dimes = 0       # dimes represents amount of change to be returned in dimes
    quarters = 0    # quarters represents amount of change to be returned in quarters
    deposit1 = 0    # deposit1 is the variable which stores the amount that is deposited. At program start, deposit1 is 0
    while True:
        if dollars <= 0:
            print("Payment due: ", cents, " cents")
        elif cents < 0:
            cents = (dollars * 100) - (-cents)
            print("Payment due: ", cents, " cents")
        else:
            print("Payment due: ", dollars, "dollars and ", cents, " cents")

        deposit = input("Indicate your deposit: ")
        if deposit == 'n':
            nickel = nickel + 1
            cents = cents - 5
            deposit1 = deposit1 + 0.05
        elif deposit == 'd':
            dime = dime + 1
            cents = cents - 10
            deposit1 = deposit1 + 0.10
        elif deposit == 'q':
            quarter = quarter + 1
            cents = cents - 25
            deposit1 = deposit1 + 0.25
        elif deposit == 'o':
            dollars = dollars - 1
            deposit1 = deposit1 + 1
            one = one + 1
        elif deposit == 'f':
            dollars = dollars - 5
            deposit1 = deposit1 + 5
            five = five + 1
        elif deposit == 'c':
            break
        else:
            print("Illegal selection: ", deposit)
            continue

    if deposit1 == price:
        print("""Please take the change below.
                    No change due.""")
    elif deposit1 > price:
        print("Please take the change below.")
        balance = round((deposit1 - price) * 100)
        if balance <= quarter or balance >= quarter:
            quarters = balance // 25
            rem_q = balance % 25
            dimes = rem_q // 10
            rem_d = rem_q % 10
            nickels = rem_d // 5
            print(quarters, " quarters")
            print(dimes, " dimes")
            print(nickels, " nickels")
        elif balance <= dime or balance >= dime:
            dimes = balance // 10
            rem_d = balance % 10
            nickels = rem_d // 5
            print(dimes, " dimes")
            print(nickels, " nickels")
        elif balance <= nickel or balance >= nickel:
            nickels = balance // 5
            print(nickels, " nickels")
    elif deposit1 < price:
        print("Please take the change below.")
        balance = round((deposit1) * 100)
        if quarter <= balance or quarter >= balance:
            quarters = balance // 25
            rem_q = balance % 25
            dimes = rem_q // 10
            rem_d = rem_q % 10
            nickels = rem_d // 5
            print(quarters, " quarters")
            print(dimes, " dimes")
            print(nickels, " nickels")
        elif dime <= balance or dime >= balance:
            dimes = balance // 10
            rem_d = balance % 10
            nickels = rem_d // 5
            print(dimes, " dimes")
            print(nickels, " nickels")
        elif nickel <= balance or nickel >= balance:
            nickels = balance // 5
            print(nickels, " nickels")

    # Updating the stock
    nickel = nickel - nickels
    dime = dime - dimes
    quarter = quarter - quarters
    print("Stock contains:")
    print(nickel, " nickels")
    print(dime, " dimes")
    print(quarter, " quarters")
    print(one, " ones")
    print(five, " fives")

# Calculating the total amount/ price which has been entered
total_dollars = round(total // 1)
total_cents = round((total % 1) * 100)
print("Total: ", total_dollars, "dollars and ", total_cents, " cents")








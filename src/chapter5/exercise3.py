# Exercise 3

#          GROUP 11 MEMBERS
#       1. NIWAGABA CLEVER      2020/BSE/055/PS
#       2. AINEBYONA ALBERT     2020/BSE/003/PS
#       3. LEMI MANOAH JUNGO    2020/BSE/145/PS

# So far from 20th/04/21- 22nd/04/21

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
nickel = 25
dime = 25
quarter = 25
one = 0
five = 0

print("Stock contains:")
print(nickel, " nickels")
print(dime, " dimes")
print(quarter, " quarters")
print(one, " ones")
print(five, " fives")

# 2. Repeatedly prompt the user for a price in the form xx.xx, where x denotes a digit, or
# to enter ‘q’ to quit.
while True:
    price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    if price == 'q':
        quit()

    price = float(price)
    new_price = (round(price * 100))
# Checking that the price entered is a (non-negative) multiple of .05 (i.e., it is payable
# in nickels). If not, then print an error message and start over requesting either a
# new price or to quit (indicated by entering a ‘q’).
    multiple = (new_price % 5)
    if price < 0 or multiple > 0:
        print("Illegal price: Must be a non-negative multiple of 5 cents.")
        continue

# Print a menu for indicating the coin/bill deposited or to cancel payment
    else:
# Defining functions
# Function for printing the menu
        def menu():
            print("""Menu for deposits:
            'n' - deposit a nickel
            'd' - deposit a dime
            'q' - deposit a quarter
            'o' - deposit a one dollar bill
            'f' - deposit a five dollar bill
            'c' - cancel the purchase""")
# Function for Please take the change below
        def change():
            print("Please take the change below.")
            quarters = new_price // 25
            rem_q = new_price % 25
            dimes = rem_q // 10
            rem_d = rem_q % 10
            nickles = rem_d // 5
            print(quarters, " quarters")
            print(dimes, " dimes")
            print(nickles, " nickles")
# Function for deposit and payment due
        def deposit():
            due_pay = int(price // 1)
            due_pay1 = float(price % 1)

            while True:
                print("Payment due: ", due_pay, " dollars and ", due_pay1, " cents")
                deposit1 = input("Indicate your deposit: ")
                if deposit1 == 'n':
                    due_pay1 = round(due_pay1 - 0.05, 2)
                elif deposit1 == 'd':
                    due_pay1 = round(due_pay1 - 0.1, 2)
                elif deposit1 == 'q':
                    due_pay1 = round(due_pay1 - 0.25, 2)
                elif deposit1 == 'o':
                    due_pay = due_pay - 1
                elif deposit1 == 'f':
                    due_pay = due_pay - 5
                elif deposit1 == 'c':
                    break
                else:
                    print("Illegal selection: ", deposit1)
                    continue
            change()
        menu()
        deposit()

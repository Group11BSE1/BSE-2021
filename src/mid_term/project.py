# The program will compute and display information for a utility company which supplies water to its customers. #
# For a specified customer, the program will compute and display #
# the amount of money which the customer will be billed for water usage during the current billing period.

# This program is the work product of Group 11 BSE 1 for their mid-semester assignment
#                   GROUP 11 MEMBERS
#       1. NIWAGABA CLEVER      2020/BSE/055/PS
#       2. AINEBYONA ALBERT     2020/BSE/003/PS
#       3. LEMI MANOAH JUNGO    2020/BSE/145/PS

gallons_used = 0
amount = 0

while True:
    code = input("Enter customer code: ")
    if code == 'c' or code == 'r' or code == 'i' or code == 'C' or code == 'R' or code == 'I':
        beginning_meter = int(input("Enter beginning meter reading: "))
        ending_meter = int(input("Enter ending meter reading: "))
        if ending_meter >= beginning_meter:
            gallons_used = round(((ending_meter - beginning_meter) * 0.1), 1)
        elif beginning_meter > ending_meter:
            remaining = beginning_meter - ending_meter
            gallons_used = round(((1000000000 - remaining) * 0.1), 1)

        if code == 'r' or code == 'R':
            amount = 5.00 + (0.0005 * gallons_used)
        elif code == 'c' or code == 'C':
            if gallons_used <= 4000000:
                amount = 1000.00
            else:
                amount = 1000.00 + ((gallons_used - 4000000) * 0.00025)
        elif code == 'i' or code == 'I':
            if gallons_used <= 4000000:
                amount = 1000.00
            elif 4000000 < gallons_used <= 10000000:
                amount = 2000.00
            elif gallons_used > 10000000:
                amount = 2000.00 + ((gallons_used - 10000000) * 0.1)

        print("Customer code: ", code)
        print("Beginning meter reading: ", beginning_meter)
        print("Ending meter reading: ", ending_meter)
        print("Gallons of water used: ", gallons_used)
        print("Amount billed: $", round(amount, 2))

    else:
        print("End of the line!")
        quit()

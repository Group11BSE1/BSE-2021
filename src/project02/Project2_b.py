# PROJECT 02 - PART B
# This program displays one summary report to the user

# This program is the work product of Group 11 BSE 1
#                   GROUP 11 MEMBERS
#       1. NIWAGABA CLEVER      2020/BSE/055/PS
#       2. AINEBYONA ALBERT     2020/BSE/003/PS
#       3. LEMI MANOAH JUNGO    2020/BSE/145/PS

# This function returns a file object after prompting the user to enter the name of the input file
def open_file():
    while True:

        # Prompts the user to enter name of input file
        input_file = input("Enter name of input file: ")
        try:

            # Opening the input file
            file_handle = open(input_file, "r")
            break
        except:

            # If program is unable to open the file, it prints an error message and prompts the user till a valid file name is entered
            print("Invalid file name or file doesn't exist! Try to Include the file extension in the file name")
            continue
    return file_handle

# This Function performs the processing to read the input file and display the report.
def process_file(file_handle):
    while True:

        # Prompts the user to enter a year
        year = input("Enter year: ")
        if len(year) == 4:  # this ensures that the year has four characters
            break
        else:
            print("Invalid year. Year Must be four digits")  # this makes it reprompt for a four character year
            continue
    while True:

        # List of selection for entry of income level
        print("""Please make a selection for income levels from the list below:
                        1 - Low Income
                        2 - Low Middle Income
                        3 - Upper Middle Income
                        4 - High Income""")

        # Prompts the user to enter an income level
        income = input("Enter income level: ")
        if income == "1":
            income = "WB_LI"
            break
        elif income == "2":
            income = "WB_LMI"
            break
        elif income == "3":
            income = "WB_UMI"
            break
        elif income == "4":
            income = "WB_HI"
            break
        else:
            # Incase an invalid input is entered, program reprompts till the right one is made
            print("Invalid income level entered! Entry must be one of the listed values i.e. 1, 2, 3, 4")
            continue

    count = 0
    percentages = []
    countries = []
    for line in file_handle:
        if (line[88:92] == year) and (line[51:56] == income or line[51:57] == income):  # Ensures the criteria is met
            count += 1
            percentages.append(int(line[59:61]))  # adds percentages to the list percentages
            country = line[0:51]
            country = str(country)
            country = country.strip()
            countries.append(country)  # adds percentages to the list of countries
            continue

    # Creates a dictionary with country as the key and percentage as values
    country_percentage = dict(zip(countries, percentages))

    if count > 0:
        percent_sum = sum(percentages)
        percent_avg = percent_sum / count  # average of percentages
        max_percentage = max(percentages)
        min_percentage = min(percentages)

        # this gets countries for maximum percentages to this list
        max_country = [country for country, percentage in country_percentage.items() if percentage == max_percentage]
        # this gets countries for minimum percentages to this list
        min_country = [country for country, percentage in country_percentage.items() if percentage == min_percentage]

        print(f"Nunber of countries in the record: {count}")
        print(f"Average percentage for {year} with {income} is {percent_avg:.1f}%")

        print(f"Country(ies) have maximum percentage in {year} with {income} of {max_percentage}%")
        for i in max_country:  # prints contries with maximum percentages
            print("   >", i)
        print(f"Country(ies) have minimum percentage in {year} with {income} of {min_percentage}%")
        for i in min_country:  # prints contries with minimum percentages
            print("   >", i)

    else:  # if there is no item in the list, it prints this
        print(f"The year {year} does not exist in the record...")

# defining the main function which invokes the other two functions and closes the file object
def main():
    file_handle = open_file()
    process_file(file_handle)
    file_handle.close()

# Calling the main function
main()
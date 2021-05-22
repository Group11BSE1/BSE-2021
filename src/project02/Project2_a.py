# PROJECT 02 - PART A

# This program is the work product of Group 11 BSE 1
#                   GROUP 11 MEMBERS
#       1. NIWAGABA CLEVER      2020/BSE/055/PS
#       2. AINEBYONA ALBERT     2020/BSE/003/PS
#       3. LEMI MANOAH JUNGO    2020/BSE/145/PS

try:
    # The program will always read from measles.txt
    file_handle = open('measles.txt')
    print(file_handle)

    # Program prompts the user for name of output file
    output_file = input("Enter name of output file: ")
    file_out = open(output_file, 'w')

    # Program prompts the user for the year
    year = input("Enter a year: ").lower()
    if len(year) > 4:
        print("Invalid entry for year")
        quit()

    for line in file_handle:

        # Checking whether the year input is in the Year Field
        pyear = len(line)
        if year in line[pyear-5:]:
            file_out.write(line)
        elif year == 'all' or year == ' ':
            file_out.write(line)
    print("Check your output file: ", output_file)

except:
    # If program is unable to open measles.txt file
    print("Unable to open specified file!!!")
    quit()

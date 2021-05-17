# The program will always read from measles.txt
try:
    file_handle = open('measles.txt')
    print(file_handle)
    output_file = input("Enter name of output file: ")
    file_out = open(output_file, 'w')
    year = input("Enter a year: ")

    for line in file_handle:
        pyear = len(line)
        if year in line[pyear-5:]:
            file_out.write(line)
        elif year == 'all' or year == 'ALL' or year == 'All' or year == '':
            file_out.write(line)

except:
    print("Unable to open specified file!!!")
    quit()

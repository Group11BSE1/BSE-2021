# The program will always read from measles.txt
file_handle = open('measles.txt')
print(file_handle)
output_file = input("Enter name of output file: ")
file_out = open(output_file, 'w')

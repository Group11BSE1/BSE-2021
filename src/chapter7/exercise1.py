# Exercise 1
# This program reads through a file and prints the contents
# of the file (line by line) all in upper case.

fname = input("Enter a file name: ")
try:
    handle = open(fname)
    for line in handle:
        line = line.rstrip().upper()
        print(line)
except:
    print("Invalid file name. File may not exist. Please consider including file extension")
    quit()

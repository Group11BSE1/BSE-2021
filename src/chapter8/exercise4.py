# Exercise 4
# This program opens the file romeo.txt and reads it line by line

# List of unique words created
uniqueWords = []

# Open the file rome.txt and read line by line
try:
    readfile = open('romeo.txt')
    for line in readfile:

        # Split line into a list of words
        words = line.split()
        for word in words:

            # Check if word is already in the list of unique words
            if word in uniqueWords:
                continue
            uniqueWords.append(word)

    # Prints the sorted list of unique words in alphabetical order
    print(sorted(uniqueWords))
except:
    print("Unable to open file romeo.txt.")
    print("Please check and ensure the file is in the same directory")

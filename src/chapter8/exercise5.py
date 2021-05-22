# Exercise 5
# lists the email of the senders in the user’s Inbox and counts the number of emails.

mailFile = input("Enter a file name: ")
# Read through the mail box data
try:
    fhandle = open(mailFile)
    count = 0
    for line in fhandle:
        # Split the line into words
        words = line.split()
        if len(words) < 3 or words[0] != "From":
            continue
        # Print the second word for each From line
        print(words[1])
        count = count + 1
        # Print out a count at the end
    print("There were %d lines in the file with From as the first word." % count)
except:
    print("Error 117. Unable to open file or the file u are trying to open does not exist.")
    print("Please include the file extension in the file name")
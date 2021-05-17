# Exercise 3
# This program prompts for a file name, and then reads
# through the file and looks for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When it encounters a line that starts with “X-DSPAM-Confidence:”
# the program pulls apart the line to extract the floating-point number on the line.
# These lines are counted and then the total of the spam confidence is computed
# from these lines. At the end of the file, the average spam confidence is printed out
# This program prints a funny message when the user types in the file name “na na boo boo”.
# The program behaves normally for all other files which exist and don’t exist.

count = 0
total_spam_confidence = 0
average_spam_confidence = 0
file_name = input("Enter a file name: ")
try:
    file_handle = open(file_name)
    for line in file_handle:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            new_line = line.find(' ')
            num = line[(new_line + 1):]
            num = float(num)
            count = count + 1
            total_spam_confidence = total_spam_confidence + num
            average_spam_confidence = round((total_spam_confidence / count), 12)
    print("Average Spam Confidence: ", average_spam_confidence)
except:
    if file_name == 'na na boo boo':
        print("NA NA BOO BOO TO YOU!- You just got sucker punched")
        quit()
    else:
        print("Invalid file name. File may not exist. Please consider including file extension")
        quit()

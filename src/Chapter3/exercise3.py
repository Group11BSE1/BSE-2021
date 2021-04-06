# Exercise 3
# This program prompts for a score between 0.0 and 1.0
# If the score is out of range, it prints an error message
# If the score is between 0.0 and 1.0, it prints a grade

try:
    score = float(input("Enter score: "))
    if 0.0 <= score < 0.6:
        print("F")
    elif score < 0.7:
        print("D")
    elif score < 0.8:
        print("C")
    elif score < 0.9:
        print("B")
    elif score <= 1.0:
        print("A")
    else:
        print("Bad score")
except:
    print("Bad score")

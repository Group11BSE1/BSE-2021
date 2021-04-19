# Exercise 7
# This program prompts for a score between 0.0 and 1.0
# If the score is out of range, it prints an error message
# If the score is between 0.0 and 1.0, it prints a grade

score = float(input("Enter score: "))

def computegrade(score):
    try:
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
        return
    except:
        print("Please enter a numeric value for score")

x = computegrade(score)
if 0.0 <= score <= 1.0:
    print(x)
else:
    print("Enter a correct numeric value")

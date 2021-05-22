# Exercise 6
# This program prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end
# when the user enters 'done'

numList = []
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print("Invalid input")
        quit()
    numList.append(number)

print("Maximum: ", max(numList))
print("Minimum: ", min(numList))

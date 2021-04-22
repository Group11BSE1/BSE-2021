# Exercise 2
# This program repeatedly reads numbers until the user enters "done"
# Then it prints out the total, count, the maximum and the minimum of the numbers
# If the user enters anything other than a number, the program prints an error message and skips to the next number

total = 0
count = 0
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break

    else:
        try:
            num = int(num)
            total = total + num
            count = count + 1
            if smallest is None or num < smallest:
                smallest = num
                continue
            if largest is None or num > largest:
                largest = num
                continue

        except:
            print("Invalid input")
            continue

print("Total: ", total)
print("Count: ", count)
print("Maximum: ", largest)
print("Minimum: ", smallest)

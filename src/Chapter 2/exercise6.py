# Exercise 6
# This program reads two points from the user and computes and
# prints the distance between the two points

# Point 1
x1 = int(input('Enter value of x1: '))
y1 = int(input('Enter value of y1: '))

# Point 2
x2 = int(input('Enter value of x2: '))
y2 = int(input('Enter value of y2: '))

# Compute the distance
x = ((x2 - x1) ** 2)
y = ((y2 - y1) ** 2)
d = ((x + y) ** 0.5)
print(d)

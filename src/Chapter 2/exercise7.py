# Exercise 7
# This program lets a User input an amount of money that they need to make change for
# and dispenses the correct amount of change (in U.S. currency)

amount = input('Enter an amount to make change for: ')

a = (float(amount) // 20)
a1 = (float(amount) % 20)

b = a1 // 10
b1 = a1 % 10

c = b1 // 5
c1 = b1 % 5

d = c1 // 1
d1 = c1 % 1

e = d1 // 0.25
e1 = d1 % 0.25

f = e1 // 0.1
f1 = e1 % 0.1

g = f1 // 0.05
g1 = f1 % 0.05

h = g1 // 0.01

print(f'{round(a)}  twenties')
print(f'{round(b)}  tens')
print(f'{round(c)}  fives')
print(f'{round(d)}  ones')
print(f'{round(e)}  quarters')
print(f'{round(f)}  dimes')
print(f'{round(g)}  nickles')
print(f'{round(h)} pennys')

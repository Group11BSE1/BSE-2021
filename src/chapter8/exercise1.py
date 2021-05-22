# Exercise 1
# This program contains a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then
# another function called middle takes a list and returns a new list that
# contains all but the first and last elements.

# This list is taken by both functions
house_founders = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
print(house_founders)

# This function returns a new list that contains all but the first and last elements
def middle(house):
    x = len(house_founders)
    new_house_founders = house_founders[1:(x-1)]
    return new_house_founders

# This function modifies the list by removing the first and last elements and returns None
def chop(founder):
    house_founders.remove('Gryffindor')
    house_founders.remove("Hufflepuff")

# Calling the functions
y = middle(house_founders)
print(y)
z = chop(house_founders)
print(z)

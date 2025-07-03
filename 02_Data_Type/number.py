# # Python Numbers
# There are three numeric types in Python:

# int
# float
# complex

import random
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:


m = 1    # int
n = 2.8  # float
o = 1j   # complex

# convert from int to float:
a = float(m)

# convert from float to int:
b = int(n)

# convert from int to complex:
c = complex(m)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:


print(random.randint(1, 10))  # Returns a random integer between 1 and 10

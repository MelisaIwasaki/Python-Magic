"""Numbers"""

"""To verify the type of any object in Python,use the type() function"""

x = 1 #int
x = 2.8 #float
x = 1j #complex

print(type(x))
print(type(y))
print(type(z))

"""int or integer:is a whole number,positive or negative without decimals,of unlimited length"""

x = 1
y = 274324689976543222
z = -25468976

print(type(x))
print(type(y))
print(type(z))

"""Float or 'floating point number':is a number positive or negative,containing one or more decimals"""

x = 2.9
y = -95.9
# Float can also be scientific numbers with an "e" to indicate the power of 10.
z = 87.7e100

print(type(x))
print(type(y))
print(type(z))

"""Complex numbers are written with a 'j' as the imaginary part"""

x = 3+5j
y = 7j
z = -5j

print(type(x))
print(type(y))
print(type(z))

"""Type conversion"""
"""You can convert from one type to another with the int(), float() and complex() methods."""
x = 8 #int
y = 3.3 #float
z = 5j #complex

#convert from int to float
a = float(x)
#convert from float to int
b = int(y)
#convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""Random number"""

from argparse import BooleanOptionalAction
import random
print(random.randrange(1,10))

"""Casting"""
"""Specify a variable type"""

x = int(1)   #x will be 1
y = int(2.8) #y will be 2
z = int("3") #z will be 3

x = float(1)     #x will be 1.0
y = float(2.8)   #y will be 2.8
z = float("3")   #z will be 3.0
w = float("4.2") #w will be 4.2

x = int("s1") #x will be 's1'
y = int(2)    #y will be '2'
z = int(3.0)  #z will be '3.0'


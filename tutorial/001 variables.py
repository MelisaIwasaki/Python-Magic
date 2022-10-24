"""Assign Multiples Values"""

x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)


x = y = z = "orange"
print(x)
print(y)
print(z)


fruits = ["apple","banana","cherry"] # Unpack a list
x, y, z = fruits
print(x)
print(y)
print(z)

"""Output Variables"""

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x + y) #ERROR int + str

x = 5
y = "John"
print(x, y)

"""Global Variables"""

x = "awesome"
def myfunc():
    print("Python is "+ x)    # Python is awesome
myfunc()


x = "awesome"                 # global
def myfunc():
    x = "fantastic"           # local
    print("Python is" + x)    # Python is fantastic
myfunc()
print("Python is"+ x)         # Python is awesome


def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is"+ x)         # Python is fantastic


x = "awesome"                 # global
def myfunc():
    global x                  # global
    x = "fantastic"
myfunc()
print("Python is"+ x)         # Python is fantastic


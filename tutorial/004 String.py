"""String are arrays"""

from cgitb import text
from turtle import end_fill


a = "Hello, World!"
print(a[1])

"""Looping Through a String"""
# Loop through the letters in the word "banana":

for x in banana:
    print(x)

"""String Length"""
# To get the length of a string, use the len() function 

a = "Hello, World!"
print(len(a))

"""Check string"""
# To check in a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in the life is free!"
print("free" in txt)

"""Use it in an if statement"""

txt = "The best things in the life is free!"
if "free" in txt
    print("Yes, 'free' is present.")

"""Check if not"""
# To check if a certain phrase or character is not present in a string, we can use the keyword not in.

txt = "The best things in the life is free!"
print("expensive" not in txt)

# Use it in an if statement

txt = "The best things in the life is free!"
if "expensive" not in txt:
    print("No, 'expensive'is not present.")

"""Slicing Strings"""
#Get the characters from position 2 to position 5(not included):

b = "Hello, World!"
print(b[2:5])

"""Slice From the start"""
#Get the characters from the start to position 5(not included):

b = "Hello, World!"
print(b[:5])

"""Slice to the end"""
#Get the characters from position 2, and all the way to the end.

b = "Hello, World"
print(b[2:])

"""Negative indexing"""
#Get the characters: from o in "World!"(position -5)
#to, but not included:d in"World!"(position -2)

b = "Hello, World!"
print(b[-5:-2])

"""Modify Strings"""
#Upper case: the upper() method return the string in upper case:

a = "Hello World!"
print(a.upper())

#Lower case: the lower() method return the string in lower case:

a = "Hello, World!"
print(a.lower())

#Remove whitespace: the strip() method removes any whitespace from the beginnig or the end:

a = "Hello, World!"
print(a.strip())   #return "Hello World!"

#Replace string

a = "Hello, World!"
print(a.replace("H","J"))

#Split String: the split() methods splits the string into substrings if it finds instance of the separator:

a = "Hello, World!"
print(a.split(","))   #return ['Hello', 'World!']

"""String Concatenation"""
#To concatenate, or combine, two string you can use the + operator.
#Merge variable a with variable b into variable c.

a = "Hello"
b = "World"
c = a + b
c = a + " " + b  #To add a space
print(c)

"""String Format"""
#We cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)

#But we can combine strings and numbers by using the format() method!
"""The format() method takes the passed arguments,formats them, and places them in the string where the placeholders {}
are:"""
#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I'm {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

#you can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity,itemno,price))

"""Escape Character"""
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north" #ERROR

#To fix this problem, use the escape character /":

txt = "We are the so-called \"Vikings\" from the north"

"""code     result

\'          single quote
\\          backslash
\n          new line
\r          carriage return
\t          tab
\b          backspace
\f          form feed
\ooo        octal value
\xhh        hex value
"""

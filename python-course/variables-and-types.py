# Numbers

myint = 5
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(3)
print(myfloat)

# Strings

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostraphes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)
print(a + b)

# This will not work!

one = 1
two = 2
hello = "hello"
# print(one + two + hello)

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
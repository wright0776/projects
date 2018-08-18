x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# Boolean operators

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The "in" operator

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal two.")

# A statement is true if 
# 1. The "True" boolean variable is given, or calculated using an expression, such as arithmentic comparison.
# 2. An object which is not considered "empty" is passed
    # such as an empty string "", and empty list [], the number 0, the boolean False

# The "is" operator

x = [1,2,3]
y = [1,2,3]
print(x == y) # prints out True
print(x is y) # prints out False

# The "not" operator

print(not False) # prints out True
print((not False) == (False)) # prints out True

# exercise

number = 16
second_number = False
first_array = [1,5,6]
second_array = [1,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
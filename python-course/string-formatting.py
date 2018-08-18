# This prints out "Hello, Matt!"
name = "Matt"
print("Hello, %s!" % name)

# This prints out "Matt is 26 years old."
name = "Matt"
age = 26
print("%s is %d years old." % (name, age))

# This prints out: A list: [1,2,3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# %s string (or any object with a string representation, like numbers)
# %d integers
# %f floating point numbers
# %.<number of digits>f - floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)
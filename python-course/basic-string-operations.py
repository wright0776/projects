astring = "Hello world!"
astring2 = 'Hello world!'

print("single quotes are ' '")

print(len(astring)) 
# length of string

print(astring.index("o")) 
# first index of o

print(astring.count("l")) 
# number of l's in the string

print(astring[3:7]) 
# prints a slice of the string, starting at index 3 and ending at index 6

print(astring[3:7:2])
# prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax: [start:stop:step]

print(astring[-1])
# prints the last character of a string

print(astring[::-1])
# prints a string reversed

print(astring.upper())
print(astring.lower())
# prints upper and lower cased string

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# prints true or false based on if the string starts or ends with the argument

afewwords = astring.split(" ")
print(afewwords)
# splits a string based on the arg into an array of items

######################################
############# Exercise ###############
######################################

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
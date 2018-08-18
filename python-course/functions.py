def my_function():
    print("Hello from My Function!")

my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s, from My Function. I wish you %s!" %(username,greeting))

my_function_with_args("matwright2010","a good morning")

def sum_two_numbers(a,b):
    return a + b

print(sum_two_numbers(5,6))

# Exercise

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

print(list_benefits())
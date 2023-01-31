# Week 2 is functions. We've covered alot of this before 
# but we're going to go over it again.
# Define a function with the following syntax:
# def function_name(arguments):
#     #Do stuff
#     return #Return something

# Functions are useful for:
# 1. Reusing code
# 2. Making code more readable
# 3. Making code more maintainable
# 4. Making code more testable
# 5. Making code more debuggable

# Functions are defined with snake_case
# Functions need something called a docstring
# A docstring is a string that describes what the function does
# A docstring is defined with triple quotes
# A docstring is defined immediately after the function definition
# A docstring is optional but highly recommended
# A docstring is used by the help() function

# Functions can have arguments
# Arguments are variables that are passed into the function

# Let's make a basic function
def add(x:int,y:int):
    """
    This function adds two integers, x and y, and returns the sum
    """

    sum = x + y
    return sum
print(add(1,2))
#Easy




# A Variable is a container for a value, which can be of various types

'''
This is a
multiline comment
or docstring (used to define a function purpose)
can be single or double quotes
'''

"""
VARIABLE RULES
    - Variable names are case sensitive (name and NAME are different variables)
    - Must start with a letter or an underscore
    - Can have numbers but can not start with one
"""

x = 1           # No semicolons. No special symbols for variable declaration. Cast as int by default
y = 2.5         # float
name = 'John'   # str. Can be either in single or double quotes
is_cool = True  # bool. Capital first letter of the boolean True or False

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

print(x, y, name, is_cool)
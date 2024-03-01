'''How to create and use your own functions'''
# This is the syntax for creating your very own function
def myFunction(a, b):
    return a - b

# To use your function, you need to type its name out in your code.
# This is known as CALLING a function
print(myFunction(10, 5))

# You can calculate things with the results of your function too
print(myFunction(10, 5) * 5)

# Or assign them to a variable for later use
results = myFunction(10,5)
print(results * 5)

# You can make them as complex as you like, with many parameters
def manyParams(a, b, c, d, e, f, g):
    return a + b - c * d + e - f / g

print(manyParams(1,2,3,4,5,6,7))

# You can also create functions that have no parameters (and thus take no arguments)
def noParams():
    return print("Look ma no parameters!")

noParams()

# You are very likely to need to use variables as part of your functions
# A function can use any variable that has already been declared outside of it
# You can declare variables inside functions, but they are only accessible there
# This is call the SCOPE of the variable

# This is a GLOBAL variable - it will be available outside the function
x = 5

def localVarUse(a, b):
    # This is a LOCAL variable - it is inaccessible outside the function
    sum = a + b
    sum *= x
    return sum

print(localVarUse(5,5))

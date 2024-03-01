'''How to use control flow to better your code'''

# Conditional statements are the bedrock of control flow
# If-else statements are likely very familiar already
# x = 4
# y = 5

# if x > y:
#     print(f"{x} is greater than {y}")
# else:
#     print(f"{x} is less than or equal to {y}")

# In Python, you add extra conditions with elif
# if x > y:
#     print(f"{x} is greater than {y}")
# elif x < y:
#     print(f"{x} is less than {y}")
# else:
#     print(f"{x} is equal to {y}")

# You can also use a switch statement. These are really useful for lots of conditions
# user_input = input("What's the best programming language? ").lower()

# match user_input:
#     case "javascript":
#         print("Nice! The language of the web")
#     case "python":
#         print("Excellent! A future in data science beckons")
#     case "r":
#         print("Woohoo! You're a big stats fan then")    
#     case _:
#         print("Great! I'm sure that's a fantastic language")

# You won't get far into programming without learning how to use loops
# A loop will repeat a task until it is told to stop, a technique known as ITERATION 
# There are two main types of loop - a FOR loop and a WHILE loop
        
# For loops work on a defined limit
# Python can figure out the length of an ITERABLE data structure itself 
# pets = ["Dog", "Cat", "Rhino","Budgie"]

# for pet in pets:
#     print(pet)

# You can also set the limit manually yourself
# This can be useful in a few circumstances, like if you want to use more than one data structure
# owners = ["Tim", "Jane", "Skeletor","Amelia"]
# for i in range(0, len(pets)):
#     print(f"{owners[i]} owns a {pets[i]}")

# While loops will run until a specific condition is met
# BE CAREFUL! While powerful, they can be dangerous too - be specific with your conditions!
# a = 0
# while a < 10:
#     print(a)
#     a += 1

# You can use conditional statements inside your loops too (or vice versa)
# on = True
# b = 0
# while on:
#     print(b)
#     b += 1
#     if b == 10:
#         on = False

# Remember our functions? These can be used as part of control flow too
def makingNumbers(num):
    iterator = num
    num_array = []
    while iterator < 100:
        num_array.append(iterator)
        iterator += 1
    
    return num_array

some_numbers = makingNumbers(10)
print(some_numbers)

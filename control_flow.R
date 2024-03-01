# How to use control flow to better your code -------
  
# Conditional statements are the bedrock of control flow
# If-else statements are likely very familiar already
x <- 6
y <- 5

if (x > y){
  print(sprintf("%s is greater than %s", x, y))
} else {
  print(sprintf("%s is less than or equal to %s", x, y))
}

# In R, you add extra conditions with if else
if (x > y){
  print(sprintf("%s is greater than %s", x, y))
} else if (x < y){
  print(sprintf("%s is less than %s", x, y))
} else {
  print(sprintf("%s is equal to %s", x, y))
}

# You can also use a switch statement. These are really useful for lots of conditions
user_input <-  tolower(readline("What's the best programming language? "))

switch(
  user_input,
  "javascript" = print("Nice! The language of the web"),
  "python" = print("Excellent! A future in data science beckons"),
  "r" = print("Woohoo! You're a big stats fan then")
  )

# You won't get far into programming without learning how to use loops
# A loop will repeat a task until it is told to stop, a technique known as ITERATION 
# There are two main types of loop - a FOR loop and a WHILE loop
        
# For loops work on a defined limit
# Like Python, R's for loop figures out the length of an ITERABLE data structure itself
pets <- c("Dog", "Cat", "Rhino","Budgie")

for(i in pets){
  print(i)
}

# You can also set the limit manually yourself
# This can be useful in a few circumstances, like if you want to use more than one data structure
owners <-  c("Tim", "Jane", "Skeletor","Amelia")

for(i in 1:length(pets)){
  print(sprintf("%s owns a %s", owners[i], pets[i]))
}

# While loops will run until a specific condition is met
# BE CAREFUL! While powerful, they can be dangerous too - be specific with your conditions!
a <- 0
while (a < 10){
  print(a)
  a <-  a + 1
}

# You can use conditional statements inside your loops too (or vice versa)
on <- TRUE
b <-  0
while (on){
  print(b)
  b <-  b + 1
  if (b == 10){
    on <-  FALSE
  }
}

# Remember our functions? These can be used as part of control flow too
makingNumbers <- function (num){
  iterator <- num
  num_array <-c()
  while (iterator < 100){
    num_array <- append(num_array,iterator)
    iterator <- iterator + 1
  }
  
  return(num_array)
}

some_numbers <- makingNumbers(80)
print(some_numbers)

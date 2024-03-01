/*************How to use control flow to better your code*************/

// Conditional statements are the bedrock of control flow
// If-else statements are likely very familiar already
let x = 6;
let y = 5;

if (x > y) {
    console.log(`${x} is greater than ${y}`);
} else {
    console.log(`${x} is less than or equal to ${y}`);
}

// In JavaScript, you add extra conditions with if else
if (x > y) {
    console.log(`${x} is greater than ${y}`);
} else if (x < y) {
    console.log(`${x} is less than ${y}`);
} else {
    console.log(`${x} is equal to ${y}`);
}

// You can also use a switch statement. These are really useful for lots of conditions
let userInput = "JavaScript".toLowerCase();

switch(userInput) {
    case "javascript":
        console.log("Nice! The language of the web");
        break;
    case "python":
        console.log("Excellent! A future in data science beckons");
        break;
    case "r":
        console.log("Woohoo! You're a big stats fan then");
        break;    
    default:
        console.log("Great! I'm sure that's a fantastic language");
}
    
// You won't get far into programming without learning how to use loops
// A loop will repeat a task until it is told to stop, a technique known as ITERATION 
// There are two main types of loop - a FOR loop and a WHILE loop
        
// For loops work on a defined limit
// Unlike Python/R, JavaScript's for loop does not know the length of a data structure itself
// However, you can use a forEach loop to achieve the same effect
// forEach uses an anonymous function, aka a function without a name
let pets = ["Dog", "Cat", "Rhino","Budgie"];

pets.forEach(function(pet) {
    console.log(pet);
});

// With normal for loops you need to set some variables yourself
owners = ["Tim", "Jane", "Skeletor", "Amelia"];

for(let i = 0; i < pets.length; i++) {
    console.log(`${owners[i]} owns a ${pets[i]}`);
}
    
// While loops will run until a specific condition is met
// BE CAREFUL! While powerful, they can be dangerous too - be specific with your conditions!
let a = 0;
while (a < 10) {
    console.log(a);
    a += 1;
}

// You can use conditional statements inside your loops too (or vice versa)
let on, b;
on = true;
b = 0;
while (on) {
    console.log(b);
    b += 1;
    if (b == 10) {
        on = false;
    }
}

// Remember our functions? These can be used as part of control flow too
function makingNumbers(num) {
    let iterator, numArray;
    iterator = num;
    numArray = [];
    while (iterator < 100){
        numArray.push(iterator);
        iterator += 1;
    }
    
    return numArray;
}
    
someNumbers = makingNumbers(80);
console.log(someNumbers);

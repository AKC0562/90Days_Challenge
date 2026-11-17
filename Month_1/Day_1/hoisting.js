console.log(a);

var a = 10;
// output will be undefined because the declaration of variable a is hoisted to the top but not the assignment. So when we try to log a before its assignment, it will return undefined.
console.log(b);

let b = 20;
// output will throw a ReferenceError because the declaration of variable b is hoisted to the top but it is in a temporal dead zone until its assignment. So when we try to log b before its assignment, it will throw an error.




const user = "Ankit";

user = "Developer";

console.log(user);

// output will throw a TypeError because we are trying to reassign a value to a constant variable. Constant variables cannot be reassigned after their initial assignment.
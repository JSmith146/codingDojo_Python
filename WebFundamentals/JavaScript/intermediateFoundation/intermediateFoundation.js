// Problem: Sigma
// Implement function sigma(num) that, given a number, returns the sum 
// of all positive integers up to the given number (inclusive).  
// Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).
function sigma(n){
    var sigma = 0;
    for(var i=0; i<=n; i++){
        sigma += i;
    }
    return sigma;
}
// console.log(sigma(3));
// console.log(sigma(5));

// Problem: Factorial
// Write a function factorial(num) that, given a number, returns the product 
// (multiplication) of all positive integers from 1 up to the given number (inclusive).  
// For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).
function factorial(n){
    var sol = 1;
    for(var i=1; i<=n; i++){
        sol *= i;
    }
    return sol;
}
// console.log(factorial(3));
// console.log(factorial(5));

// Problem: Fibonacci
// Create a function to generate Fibonacci numbers.  In this famous mathematical sequence,
// each number is the sum of the previous two, starting with values 0 and 1.  Your function 
// should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 
// 4 corresponds to the value four later, etc).  Examples: fibonacci(0) = 0 (given), 
// fibonacci(1) = 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), 
// fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8).  
// Do this without using recursion first.  If you don't know what a recursion is yet, don't worry as 
// we'll be introducing this concept in Part 2 of this assignment.
function fibonacci(n){
    // console.log("Current n:",n);
    if(n==0){
        return 0;
    }
    if(n==1){
        return 1;
    }
    return fibonacci(n-1)+fibonacci(n-2)
}
// console.log("Answer:",fibonacci(0));
// console.log("Answer:",fibonacci(1));
// console.log("Answer:",fibonacci(3));
// console.log("Answer:",fibonacci(7));


// Problem: Array Second-to-Last 
// Second-to-Last: Return the second-to-last element of an array. 
// Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return null.
var arr=[42, true, 4, "Liam", 7];
function Array(arr){
    if(arr.length<=2){
        return null;
    }else{
        return arr[arr.length-2];
    }
}
// console.log(Array(arr));
// console.log(Array(["Liam"]))
// console.log(Array(["Liam","Name"]));

// Array: Nth-to-Last
// Return the element that is N-from-array's-end. Given 
// ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.
function nthToLast(arr,n){
    if(n> arr.length){
        return null;
    }
    return arr[arr.length-(n)];
}
// console.log(nthToLast([5,2,3,6,4,9,7],8));

// Array: Second-Largest: 
// Return the second-largest element of an array. 
// Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.
function secondLargest(arr){
    var subMax = -Infinity;
    var max = -Infinity;
    var temp;
    for(var i=0; i<arr.length; i++){
        if(arr[i]> max){
            max = arr[i];
        }
        else if((arr[i]>subMax) && (arr[i]<max)){
            subMax = arr[i];
        }
    }
    return subMax;
}
// console.log(secondLargest([42,1,4,3.14,7]))


// Double Trouble: 
// Create a function that changes a given array to list each existing 
// element twice, retaining original order.  Convert [4, "Ulysses", 42, false] to 
// [4,4, "Ulysses", "Ulysses", 42, 42, false, false].
function doubleTrouble(arr){
    var newArray = [];
    for(var i=0;i<arr.length-1;i++){
        for(var j=0; j<2; j++){
            newArray.push(arr[i]);
        }
    }
    return newArray;
}
// console.log(doubleTrouble([4, "Ulysses", 42, false]));
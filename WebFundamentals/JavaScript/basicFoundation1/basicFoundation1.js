// Problem 1:
// Get 1 to 255 - Write a function that returns an
// array with all the numbers from 1 to 255.
function p1(){
    var arr =[];
    for(var i=1; i<=255;i++){
        arr.push(i);
    } 
    return arr;
}
// Answer
// var x = p1();
// console.log(x);

// Problem 2:
// Get even 1000 - Write a function that would get the sum of all the
// even numbers from 1 to 1000. You may use a modulus operator for this
// exercise.
function evenSum(){
    var sum=0;
    for(var i=1;i<=1000;i++){
        if(i%2==0){
            sum +=i;
        }
    }
    return sum;
}
// console.log(evenSum());

// Problem 3:
// Sum odd 5000 - Write a function that returns the sum
// of all the odd numbers from 1 to 5000.
// (e.g. 1+3+5+...+4997+4999).
function sumOdd5000(){
    var sum = 0;
    for(var i=1;i<=5000;i++){
        if(i%2!=0){
            sum+=i;
        }
    }
    return sum;
}
// console.log(sumOdd5000());

// Problem 4:
// Iterate an array - Write a function that returns the sum 
// of all the values within an array. (e.g. [1,2,5] returns 
// 8. [-5,2,5,12] returns 14).
function p4(arr){
    
}
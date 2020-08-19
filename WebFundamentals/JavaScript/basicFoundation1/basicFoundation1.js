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
var arr1 = [1,2,5];
var arr2 = [-5,2,5,12];
function p4(arr){
    var sum=0;
    for(var i=0;i<arr.length;i++){
        sum += arr[i];
    }
    console.log(sum)
}
// p4(arr1);
// p4(arr2);

// Problem 5: Find max
var arr = [-3,3,9,5,7];
function p5(arr){
    var max = -Infinity;
    for(var i = 0;i < arr.length;i++){
        if(arr[i]>max){
            max = arr[i];
        }
    }
    console.log(max);
}
// p5(arr);

// Problem 6: Find average
var arr = [1,3,5,7,20];
function p6(arr){
    var sum = 0;
    for(var i=0; i < arr.length; i++){
        sum += arr[i];
    }
    console.log(sum/arr.length);
}
// p6(arr);

// Problem 7: Array odd
function p7(){
    var arr =  [];
    for(var i = 1; i<=50; i+=2){
        arr.push(i);
    }
    console.log(arr);
}
// p7();

// Problem 8: Greater than Y
var arr = [1, 3, 5, 7];
var y = 3;
function p8(arr,y){
    var count = 0;
    for(var i=0; i<arr.length;i++){
        if(arr[i]>y){
            count++;
        }
    }
    console.log(count);
}
// p8(arr,y);

// Problem 9: Squares
var arr=  [1,5,10,-2] ;
function p9(arr){
    for(var i=0;i<arr.length;i++){
        arr[i] =arr[i]**2;
    }
    console.log(arr);
}
// p9(arr);

// Problem 10: Negatives
var arr =[1,5,10,-2];
function p10(arr){
    var newArr=[];
    for(var i=0; i < arr.length; i++){
        if(arr[i]<0){
            newArr.push(0);
        }
        else{
            newArr.push(arr[i]);
        }
    }
    console.log(newArr)
}
// p10(arr);


// Problem 11: Max/Min/Avg
var arr = [1,5,10,-2];
function p11(arr){
    var max = -Infinity;
    var min = Infinity;
    var sum  = 0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]>max){
            max = arr[i];
        }
        if(arr[i]<min){
            min = arr[i];
        }
        sum+=arr[i];
    }
    console.log([max, min, sum/arr.length]);
}
p11(arr);

// Problem 12: Swap Values
var arr = [1,5,10,-2];
function p12(arr){
    var temp = arr[arr.length-1];
    arr[arr.length-1] = arr[0];
    arr[0] = temp;
    console.log(arr)
}
// p12(arr);

// Problem 13: Number to String
var arr = [-1,-3,2];
function p13(arr){
    for(var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i] = "Dojo";
        }
    }
    console.log(arr);
}
p13(arr);




// Algorithm Practice - Arrays

// Print Values and Sum
// Print each array value and the sum so far
var testArr = [6,3,5,1,2,4];

function printValAndSum(arr){
    var sum=0;
    for(var i=0;i<arr.length;i++){
        sum +=arr[i];
        console.log("Num",arr[i]+",","Sum",sum);
    }
}
// Uncomment for output
// printValAndSum(testArr);

// Value * Position
// Multiply each value in the array by its array position
function valueByPosition(arr){
    for(var i=0;i<arr.length;i++){
        arr[i] = arr[i]*i;
    }
    console.log(arr);
}
// Uncomment for output
// valueByPosition(testArr);
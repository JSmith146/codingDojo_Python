// Predict 1:
// Prediction: [0,1,2,...,14]
function predict1(){
    for(var num=0; num<15; num++){
        console.log(num)
    }
}
// Uncomment for output
// predict1();

// Predict 2:
// Prediction: 3, 9
function predict2(){
    for(var i=1; i<10; i+=2){
        if(i % 3 ==0){
            console.log(i);
        }
    }
}
// Uncomment for output
// predict2();

// Predict 3:
// Prediction: [1,4,5,8,10,11,14,16]
function predict3(){
    for(var j = 1; j<=15; j++){
        if(j % 2 ==0){
            j+=2;
        }
        else if(j % 3 == 0){
            j++;
        }
        console.log(j);
    }
}
// Uncomment for output
// predict3();
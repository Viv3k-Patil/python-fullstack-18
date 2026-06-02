
//Javascripts function

function sayHello(){
    console.log("Hello World!!")
}
sayHello()

function sayMyName(name){
       console.log("Hello there!! "+ name)
}
sayMyName("Akshata")


// arguments 
function add(a,b){
    console.log(a+b)
}
add(10,15)


// function with return value

function addAndReturn(d, e){
    return d+e;
}
let c = addAndReturn(20,25)
console.log(c)

//

let b = function myFunctionB(){
    console.log("myfunction B");
}

console.log(typeof b);
b()
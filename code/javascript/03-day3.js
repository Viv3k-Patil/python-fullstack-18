// javascript function
function sayHello(){
    console.log("hello world!!");
    console.log("hello world!!");
    console.log("hello world!!");
    console.log("hello world!!");
}

sayHello()
// name here is a function parameter
function sayMyName(name){
    console.log("hello there!!" + name);
}

// argument is "Vivek"
sayMyName("Vivek")

function add(a, b){
    console.log(a+b)
}

// add(15,15);

// function with return value
function addAndReturn(a, b){
    return a+b;
}

let c = addAndReturn(15,15)
console.log(c)


let my_func_var=function MyFunc(){
    console.log("my_func");
}

my_func_var()



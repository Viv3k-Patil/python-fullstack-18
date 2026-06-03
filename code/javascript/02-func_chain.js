function x(my_func){
    my_func()
    console.log("hey there");
}

let a=function y(){
    console.log("inside y para");
}

a(x)


//default parameters
function add(a=0,b){
    console.log(a+b);
}

add(10,10)

function greet(name="user"){
    console.log("hey there, " + name);
}

greet("Vivek")


function add(...numbers){
    console.log(numbers)
    return numbers[0] + numbers[1]
}

console.log(add(10,20));
let a = function(){
    console.log("hey there!!");
}
a()

let b = () => {
    console.log("inside arrow function")
}
b()

let z = () => console.log("hey");
z()


function add(a=0,b){
    console.log(a+b);
}

add(10,10)

function greet(name="user"){
    console.log("hey , " + name, "welcome to javascript");
}

greet("sameeeeeeer")

function add(...numbers){
    return numbers[0] + numbers[1]
}

console.log(add(10,10));
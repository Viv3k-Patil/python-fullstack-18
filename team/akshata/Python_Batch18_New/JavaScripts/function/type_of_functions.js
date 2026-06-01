
//Annonomus Function
let a = function(){
    console.log("hey there!!");
}


//Arrow Function
let b = () => {
    console.log("Hey")
}

b()


function add(a=0,b){
    console.log(a+b);
}

add(10,10)

function greet(name="user"){
    console.log("hey there, " + name);
}

greet("Akshata")

function add(...numbers){
    return numbers[0] + numbers[1]
}

console.log(add(10,10));


function add(...numbers){
   return numbers[0] + numbers[1] +numbers[2]
}
console.log(add(10,10, "AKshu"))
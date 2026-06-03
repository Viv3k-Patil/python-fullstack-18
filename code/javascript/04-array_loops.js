for(let i=0;i<15;i++){
    console.log("statement: " + i);
    console.log("statement: " + i);
    break;
    console.log("statement: " + i);
    console.log("statement: " + i);
    console.log("statement: " + i);
    console.log("statement: " + i);
}

console.log("statement: " + i);



let a = ['apple', 'banana', 1, true];
console.log(a);

// CRUDI

console.log(a[1]);
console.log(a.length);

a.push(10);
console.log(a)
a.pop()
console.log(a)

a.unshift("vivek");
console.log(a);
a.shift()
console.log(a)



let a = ['apple', 'banana', 1, true];
console.log(a);

// CRUDI

console.log(a[1]);
console.log(a.length);

a.push(10);
console.log(a)
a.pop()
console.log(a)

a.unshift("vivek");
console.log(a);
a.shift()
console.log(a)
// pearl -- read about shift/unshift
console.log(a.includes("apple"))


let str = "smash hulk";
// "hulk smash"
'smash hulk'.split(" ").reverse().join(" ")

let l = [1,2,3,4,5,6];
console.log(l);

for(let li of l){
    console.log(li);
}
console.log("_________________________________________")
l.forEach((el)=>{
    console.log(el+5);
});


let p = ['apple', 'banana', 'cherry'];

// plain old for loop
// for item of p
// foreach
for(let i = 0; i<p.length;i++){
    console.log(p[i]);
}
for(let i of p){
    console.log(i);
}
p.forEach((item)=>{console.log(item)});
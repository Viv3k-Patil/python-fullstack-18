console.log("hello");

// let a = 10;
// console.log(a);

// three ways to create variable
// let b = 10;
// var c = 15;
// const d = 50;
// const PI=3.1415
// const myName="rahul"


// console.log(b);
// console.log(c);
// console.log(d);
// console.log(PI)
// console.log(typeof(myName))
console.log("________________________________")

// let score=0

// score=score+10;
// score +=10
// score -=5
// score *=2
// score /=2

// //increment and decrement
// //score++;
// score--;

// console.log(score);

// let firstName="prathmesh";
// let lastName="patil";

// console.log( firstName + " " + lastName);
// console.log(`myself ${firstName} ${lastName}`);

// console.log(5>=5);
// console.log(5<=4);

// console.log(5=="5")
// console.log(5==="5")

// // let age=16;
// // let hasticket=true;

// // let canenter= age>= 18 && hasticket
// //     console.log(canenter);

// // let temperature=25;

// // if (temperature>=30){
// //     console.log(`whether is very hotyy and current temp is ${temperature} celcies`)
// // }
// // else{
// //     console.log("whether is normal")
// // }

// let score=50;

// if (score>90){
//     console.log("grade A");
// }
// else if(score>70){
//     console.log("grade B");
// }
// else if(score<70){
//     console.log("grade c")
// }
// else console.log("grade F")

// let day=""

// switch(day){
//     case "sunday":
//         console.log("today is sunday");
//     break;    

//     case "monday":
//         console.log("Yeahh..! today is monday") ; 
//     break;     

//     default:
//         console.log("day not found!!");
// }

// let age=16;

// let status= age>=18 ? "Adult" : "Minor"
// console.log(status);

// age>=20 ? console.log("Adult") : console.log("chalo accha nahhi")

// function showcount(name,count){
//     console.log(`${name} you get ${count} messages`)
// }
// showcount("pp",18)
// showcount("vp",25)
// showcount("sp",17)

// function value(num){
//     let v= ` you have ${num} Rs`;
//     return v
// }
// let rs=value(2000);
//     console.log(rs);


// function ab(a,b){
//     return a+b
// }    
// let sum=ab(10,10)
// console.log(sum+5);

let a=10;
let b=20;

const add=function(x,y){return x+y;};
console.log(add(a,b));


let u=20;
let v=2;

let multi=u*v;
console.log(multi)

aa=10;
bb=10;

let aadd=(xx,yy)=>{return xx+yy}
console.log(aadd(aa,bb));

let m=50;
let double=(num)=>num*2;
console.log(double(m))

function sum(...numbers){
    let total=0;
    for(let n of numbers){
        total+=n;
    }
    console.log(total);
    return total;
}
sum(10,20,30)


function heyy(func){
    func()
    func()
}

function sayHello(){
    console.log("hello there")
}

heyy(sayHello);



let nums = [3, 1, 4, 1, 5, 9, 2, 6];

// Sort (careful — sorts as strings by default!)
nums.sort((a, b) => a - b);  // [1, 1, 2, 3, 4, 5, 6, 9] ascending
nums.sort((a, b) => b - a);  // [9, 6, 5, 4, 3, 2, 1, 1] descending

// Find
nums.find(n => n > 4);       // 5 — returns first match
nums.findIndex(n => n > 4);  // returns index of first match

// Check if any/all pass a test
nums.some(n => n > 8);       // true — at least one is > 8
nums.every(n => n > 0);      // true — all are > 0


// pnject with functions
let mummymovie = {
    name: 'The Mummy',
    year: 1999,
    actors: [
        'Brendan Fraser',
        'Rachel Weisz'
    ],
    details:{
        description: 'The 1999 action-adventure film The Mummy stars Brendan Fraser as dashing adventurer Rick OConnell and Rachel Weisz as the brilliant Egyptologist Evelyn Carnahan. Directed by Stephen Sommers, the cult classic features a memorable supporting ensemble of treasure hunters, Medjai warriors, and cursed villains.',
        'Running time': '2h 4m'
    },
    getmoviedesc: function (){
        return this.details;
    }
}


console.log(mummymovie);


let post2 = {
    votes: 0,

    upvote: function (){
        this.votes+=1;
    },

    downvote: function(){
        this.votes-=1;
    }
}

post2.upvote();
console.log(post2);

let passward="";

while(passward!=="Action@123"){
    passward="Action@123";
    console.log("checking passward...");
};
console.log("access granted !!");

let count=0;

do{
    console.log(`count ${count}`);
    count++;
}while(4>count);


for(i=0; i<5; i++){
    if(i===3)break;
    console.log(i)
}

for(i=0; i<6; i++){
    if(i==3)continue;
    console.log(i)
}

// let fruits=["mango","banana","apple","orange"]

// console.log(fruits);
// console.log(fruits.length);
// console.log(fruits[0]);
// console.log(fruits[2]);


// console.log(list)
// list.push("f");
// console.log(list)
// list.pop()
// console.log(list)

// list.unshift("z"); //add element to start
// console.log(list); 
// list.shift() //remove element to starting position





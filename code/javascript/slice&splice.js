// let list=["a","b","darray","e"]
// console.log(list.splice(1, 0, "X"));
// console.log(list)
// console.log(list.indexOf("d")); //gives poistion of index
// console.log(list.includes("d"));//gives true or false

// console.log(list.slice(0,2));//gives slice elements in array

// console.log(list.splice(0,3));
// console.log(list.splice(1, 0, "X"));

// let scores = [85, 72, 91, 68, 95];

// for(let i=0;i<scores; i++){
//     console.log(scores[i]);
// };
// console.log("______________________");
// for (let score of scores){
//     console.log(score);
// };
// console.log("______________________");

// scores.forEach(function(score){
//     console.log(score);
// });

// console.log("_________________________");
// scores.forEach((scored)=>console.log(scored));

// let passward='';

// while(passward!=="isactive"){
//     passward="isactive";
//     console.log("chhecking passward");
// };
// console.log("access denied");
// let count=0

// do{
//     console.log("hey there");
//     count++;
// }while(count<3);

// let list=[1,2,3,4,5]
// let a=list.slice(0,2);
// let lis=list.splice(0,1,"patil");
// console.log(list);
// console.log(lis);
// console.log(a);



// let a=["patil","saheb","chaloo!!"].join("");
// console.log(a);


let num=[1,2,3,4,5,6]

let sum=num.map((numbers)=>numbers+2);
console.log(sum);

let prices=[100,200,402,250]

let total=prices.filter((price)=>price>100)
                .reduce((accu,curr)=>accu+curr,0);
console.log(prices);
console.log(total);

let ages=[20,18,15,22,17]

let age= ages.filter((age)=>age>=18).reduce((accu,curr)=>accu+curr,0);
console.log(age);




// let pricewithGST=prices.map((price)=>price*1.18);
// console.log(prices);
// console.log(pricewithGST);

let products = [
  { name: "Shirt", price: 800, inStock: true },
  { name: "Shoes", price: 2500, inStock: false },
  { name: "Belt", price: 400, inStock: true },
  { name: "Watch", price: 5000, inStock: true },
];

let pro=products.filter(p=>p.inStock==true && p.price>500)

        .map(p=>p.price)

        .reduce((price,total)=>price+total);
console.log(pro);
console.log("____________________");

let students = [
  { name: "Rahul",  marks: 85, passed: true  },
  { name: "Priya",  marks: 42, passed: false },
  { name: "Amit",   marks: 91, passed: true  },
  { name: "Sneha",  marks: 38, passed: false },
];

let stud=students.filter(s=>s.passed==true && s.marks>40)
        .map(s=>s.marks)
        .reduce((total,mark)=>total+mark/200)
console.log(stud);        
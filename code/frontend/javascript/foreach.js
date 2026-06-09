

let a = [1,2,3,4,5]


// function name(){}
// () => {}
// let ar = a.forEach((num)=>{
//     console.log(num);
// });

let ar = a.map((num)=>{return num+10});
console.log(ar);

// prices = [100,256,145,899,199]

let prices = [100,256,145,899,199];

let pricesWithGst = prices.map((i)=>{
    let priceWithGst = i + (i*0.18);
    return priceWithGst;
});

console.log(pricesWithGst);

// filter

let b = ['alice', 'barbara', 'charlie', 'bob'];

let br = b.filter((name)=>{
    // if(name.startsWith('a')) return true;
    // return false;
    return name.startsWith('b') ? true : false; 
});
console.log(br);

// ages
let ages = [14,18,25,29,16,17];

let agesEligible = ages.filter((age)=> age >= 18);
console.log(agesEligible);

// reduce
let c = [1,5,6,8,4,7,9];
// c.reduce(()=>{});

let sum = 0;
for(let num of c){
    sum += num;
}
console.log(sum);

// reduce
let rs = c.reduce((sum, curr)=>{
    return sum + curr;
}, 0);
console.log(rs);


// Get total value of in-stock items over ₹500

let products = [
  { name: "Shirt", price: 800, inStock: true },
  { name: "Shoes", price: 2500, inStock: false },
  { name: "Belt", price: 400, inStock: true },
  { name: "Watch", price: 5000, inStock: true },
];
// filter by instock - check
// filter by price - [800,2500,400,5000]
// get total

let total = products
    .filter((p)=>p.inStock && p.price>500)
    .map((i)=>i.price)
    .reduce((acc,curr)=>acc+curr,0);

console.log(total);

// products.forEach((item)=>{
//     console.log(item.price);
// });

// let filterdItem = products.filter((item)=>{
//     return item.inStock && item.price>500;
// });
// console.log(filterdItem);

// mappedPrice = filterdItem.map((item)=>{
//     return item.price;
// });
// console.log(mappedPrice);

// let totalPrice = mappedPrice.reduce((acc, curr)=>{
//     return acc + curr
// }, 0);

// console.log(totalPrice);

const emailList = [
  {
    id: 1,
    name: "Aarav Sharma",
    email: "aarav.sharma@example.in",
    subscriptionDate: "2026-02-14",
    status: "active",
    preferences: {
      newsletter: true,
      promotions: false
    }
  },
  {
    id: 2,
    name: "Priya Patel",
    email: "priya.patel@example.co.in",
    subscriptionDate: "2026-03-01",
    status: "active",
    preferences: {
      newsletter: true,
      promotions: true
    }
  },
  {
    id: 3,
    name: "Rahul Deshmukh",
    email: "rahul.desh@example.com",
    subscriptionDate: "2026-01-18",
    status: "unsubscribed",
    preferences: {
      newsletter: false,
      promotions: false
    }
  },
  {
    id: 4,
    name: "Neha Gupta",
    email: "neha.gupta@example.in",
    subscriptionDate: "2026-05-12",
    status: "pending",
    preferences: {
      newsletter: true,
      promotions: true
    }
  }
];

let filterar = emailList.filter((item)=>item.status == 'active');
let emailar = emailList.map((item)=>item.email);
console.log(filterar);

// give me email of those people who are active
// filter by active, transform email
let d = emailList
    .filter((item)=>item.status == 'active')
    .map((item)=>item.email);
console.log(d);
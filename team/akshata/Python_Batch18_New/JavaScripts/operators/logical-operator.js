

// 3.Logical Operators
// AND operators - && ---ALL conditions must be true
let username = 'admin';
let password = 'admin123';

if(username == 'admin' && password == 'admi123'){
  console.log(`Successfully logged in user : ${username}`)
}
else{
    console.log(`Access Denied! Invalid Credentials.`)
}

// OR operators : || -- at least one condition is true

let hasCash = false;
let hasCard = true;

if (hasCash === true || hasCard === true) {
    console.log(`Payment Successful`);    //one is true → runs
} else {
    console.log(`Payment Failed.`);
}

// !(not) --Reverse the condition

let isLoggedIn = false;

if (!isLoggedIn) {
    console.log(`Please Login First`);  // !false = true → runs
} else {
    console.log(`Welcome Back!`);
}

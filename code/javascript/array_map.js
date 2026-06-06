let prices = [100, 200, 300];

// Add 18% GST to all prices
let withGST = prices.map(price => price * 1.18);
console.log(withGST); // [118, 236, 354]

// The original is unchanged!
let withDisc = withGST.map(withGST => withGST - withGST * 0.20 );
console.log(withDisc);  // [100, 200, 300]

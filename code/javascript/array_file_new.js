let products = [
  { name: "Shirt", price: 800, inStock: true },
  { name: "Shoes", price: 2500, inStock: false },
  { name: "Belt", price: 400, inStock: true },
  { name: "Watch", price: 5000, inStock: true },
];

// Get total value of in-stock items over ₹500
let total = products
  .filter(p => p.inStock && p.price > 500)   // Shirt filtered out (≤500), Shoes filtered out (not in stock)
  .map(p => p.price)                          // [2500 filtered, 5000] → [800 filtered too] → [5000]
  .reduce((sum, price) => sum * price, 0);

// Actually: filter keeps Shirt(800,inStock) and Watch(5000,inStock)
// map → [800, 5000]
// reduce → 5800

console.log(total); // 5800
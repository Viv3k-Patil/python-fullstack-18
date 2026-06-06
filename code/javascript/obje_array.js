let person = {
  name: "Priya",
  age: 28,
  city: "Pune",
  isEmployee: true
};

// Access with dot notation
console.log(person.name);  // "Priya"
console.log(person.age);   // 28

// Access with bracket notation (useful when key is dynamic)
let key = "city";
console.log(person[key]);  // "Pune"

// Add or update
person.email = "priya@example.com";  // adds new property
person.age = 29;                     // updates existing

// Delete
delete person.isEmployee;
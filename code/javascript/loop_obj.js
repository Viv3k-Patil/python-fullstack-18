let scores = { maths: 90, science: 85, english: 78 };

// Get all keys
Object.keys(scores);    // ["maths", "science", "english"]

// Get all values
Object.values(scores);  // [90, 85, 78]

// Get key-value pairs
Object.entries(scores); // [["maths", 90], ["science", 85], ["english", 78]]

// Loop over entries
for (let [subject, score] of Object.entries(scores)) {
  console.log(`${subject}: ${score}`);
}
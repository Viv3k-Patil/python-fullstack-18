let password = "";

while (password !== "secret123") {
  password = "secret123"; // In real code, you'd get this from user input
  console.log("Checking password...");
}

console.log("Access granted!");
console.log(false);
console.log(0==false);
console.log(""==false);

// Todo: reconfirm this.
if(null == false)
console.log(null==false);
console.log(NaN===false);
console.log(undefined===false)

// ======================================
// FALSY VALUES IN CONDITIONAL STATEMENTS
// ======================================

console.log("\n--- FALSY IN CONDITIONALS ---");

// FALSE - most obvious falsy
if(false) {
  console.log("false: runs");
} else {
  console.log("false: doesn't run ✓");
}

// NULL - falsy
if(null) {
  console.log("null: runs");
} else {
  console.log("null: doesn't run ✓");
}

// UNDEFINED - falsy
if(undefined) {
  console.log("undefined: runs");
} else {
  console.log("undefined: doesn't run ✓");
}

// NaN - falsy
if(NaN) {
  console.log("NaN: runs");
} else {
  console.log("NaN: doesn't run ✓");
}

// 0 - falsy
if(0) {
  console.log("0: runs");
} else {
  console.log("0: doesn't run ✓");
}

// EMPTY STRING - falsy
if("") {
  console.log("empty string: runs");
} else {
  console.log("empty string: doesn't run ✓");
}

// ======================================
// TRUTHY VALUES IN CONDITIONALS
// ======================================

console.log("\n--- TRUTHY IN CONDITIONALS---");

// Non-zero numbers - truthy
if(1) {
  console.log("1: runs ✓");
}

if(-5) {
  console.log("-5: runs ✓");
}

// Non-empty strings - truthy
if("hello") {
  console.log("non-empty string: runs ✓");
}

// Objects and arrays - truthy (even empty ones!)
if({}) {
  console.log("empty object: runs ✓");
}

if([]) {
  console.log("empty array: runs ✓");
}

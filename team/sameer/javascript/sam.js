


// CREATE
let sameerInfo = {
    name: "sameer",
    location: "pune",
    age: 20,
    hobbies: [
        'playing cricket',
        'mahi'
    ],
    skills: [
        'python',
        'fastapi'
    ]   
}

// READ
console.log(sameerInfo.name);
console.log(sameerInfo.hobbies);
console.log(sameerInfo['age']);

// UPDATE
sameerInfo.batch = 'batch 18';


// DELETE
delete sameerInfo.hobbies

console.log(sameerInfo);

Object.keys(sameerInfo);
Object.values(sameerInfo);
Object.entries(sameerInfo);
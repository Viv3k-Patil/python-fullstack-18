// CREATE
let prathmInfo = {
    name: "prathmesh",
    location: "Kolhapur",
    age: 22,
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
console.log(prathmInfo.name);
console.log(prathmInfo.hobbies);
console.log(prathmInfo['age']);

// UPDATE
prathmInfo.batch = 'batch 18';


// DELETE
delete prathmInfo.hobbies

Object.keys(prathmInfo);
Object.values(prathmInfo);
//show entries
Object.entries(prathmInfo);

console.log(keys)
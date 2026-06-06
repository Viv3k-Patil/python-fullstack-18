<<<<<<< HEAD
// CREATE
let prathmInfo = {
    name: "prathmesh",
    location: "Kolhapur",
    age: 22,
=======

// CREATE
let sameerInfo = {
    name: "sameer",
    location: "pune",
    age: 20,
>>>>>>> 34a4b420be5d30e78c807cbf1beedaf3506f6b6b
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
<<<<<<< HEAD
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
=======
console.log(sameerInfo.name);
console.log(sameerInfo.hobbies);
console.log(sameerInfo['age']);

// UPDATE
sameerInfo.batch = 'batch 18';


// DELETE
delete sameerInfo.hobbies

// ITERATE
Object.keys(sameerInfo);
Object.values(sameerInfo);
Object.entries(sameerInfo);

// pnject with functions
let mummymovie = {
    name: 'The Mummy',
    year: 1999,
    actors: [
        'Brendan Fraser',
        'Rachel Weisz'
    ],
    details:{
        description: 'The 1999 action-adventure film The Mummy stars Brendan Fraser as dashing adventurer Rick OConnell and Rachel Weisz as the brilliant Egyptologist Evelyn Carnahan. Directed by Stephen Sommers, the cult classic features a memorable supporting ensemble of treasure hunters, Medjai warriors, and cursed villains.',
        'Running time': '2h 4m'
    },
    getmoviedesc: function (){
        return this.details;
    }
}


console.log(mummymovie.getmoviedesc()["Running time"])


let post2 = {
    votes: 0,

    upvote: function (){
        this.votes+=1;
    },

    downvote: function(){
        this.votes-=1;
    }
}
>>>>>>> 34a4b420be5d30e78c807cbf1beedaf3506f6b6b

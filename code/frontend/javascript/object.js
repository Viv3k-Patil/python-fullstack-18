
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
let movie = {
    name: 'The Mummy',
    year: 1999,
    actors: [
        'brenden fraser',
        'rachel weisz'
    ],
    details:{
        description: 'The 1999 action-adventure film The Mummy stars Brendan Fraser as dashing adventurer Rick OConnell and Rachel Weisz as the brilliant Egyptologist Evelyn Carnahan. Directed by Stephen Sommers, the cult classic features a memorable supporting ensemble of treasure hunters, Medjai warriors, and cursed villains.',
        'running time':'2h 4m'
    },

}
console.log(movie.name);

// Print year
console.log(movie.year);

// Print actors
console.log(movie.actors);

// Print first actor
console.log(movie.details.description);

from datetime import datetime

favourite_movies = [
    {
        "title": "Deadpool",
        "year": 2016,
        "rating": 8.1,
        "description": "A wisecracking mercenary gets experimented on and becomes immortal yet hideously scarred, and sets out to track down the man who ruined his looks.",
        "directors": ["Tim Miller"],
        "writers": ["Rhett Reese", "Paul Wernick"],
        "actors": ["Ryan Reynolds", "Morena Baccarin", "T.J. Miller"],
        "genres": ["Action", "Adventure", "Comedy"]
    },
    {
        "title": "The Nun",
        "year": 2018,
        "rating": 5.3,
        "description": "A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.",
        "directors": ["Corin Hardy"],
        "writers": ["Gary Dauberman", "James Wan"],
        "actors": ["Demián Bichir", "Taissa Farmiga", "Jonas Bloquet"],
        "genres": ["Horror", "Mystery", "Thriller"]
    },
    {
        "title": "Hacksaw Ridge",
        "year": 2016,
        "rating": 8.1,
        "description": "World War II American Army Medic Desmond T. Doss, serving during the Battle of Okinawa, refuses to kill people and becomes the first man in American history to receive the Medal of Honor without firing a shot.",
        "directors": ["Mel Gibson"],
        "writers": ["Robert Schenkkan", "Andrew Knight"],
        "actors": ["Andrew Garfield", "Sam Worthington", "Luke Bracey"],
        "genres": ["Biography", "Drama", "History"]
    },
    {
        "title": "Warcraft",
        "year": 2016,
        "rating": 6.7,
        "description": "As an Orc horde invades the planet Azeroth using a magic portal, a few human heroes and dissenting Orcs must attempt to stop the true evil behind this war.",
        "directors": ["Duncan Jones"],
        "writers": ["Charles Leavitt", "Duncan Jones"],
        "actors": ["Travis Fimmel", "Paula Patton", "Ben Foster"],
        "genres": ["Action", "Adventure", "Fantasy"]
    }
]


total_rating = sum(movie["rating"] for movie in favourite_movies)
average_rating = total_rating / len(favourite_movies)


current_year = datetime.now().year
total_age = sum(current_year - movie["year"] for movie in favourite_movies)
average_age = total_age / len(favourite_movies)


print("The title of the first movie is:", favourite_movies[0]["title"])
print("The release year of the second movie is:", favourite_movies[1]["year"])
print("The IMDB rating of the third movie is:", favourite_movies[2]["rating"])
print("The short description of the fourth movie is:", favourite_movies[3]["description"])


print("\nAdditional Details:")
print("The lead director of the first movie is:", favourite_movies[0]["directors"][0])
print("The lead writer of the second movie is:", favourite_movies[1]["writers"][0])
print("The lead star of the third movie is:", favourite_movies[2]["actors"][0])
print("The main genre of the fourth movie is:", favourite_movies[3]["genres"][0])


print("\nCalculated Values:")
print("Average Rating of the movies:", average_rating)
print("Average Age of the movies:", average_age)

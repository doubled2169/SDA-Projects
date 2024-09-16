from datetime import datetime

# Create favorite movies list
# Choose your four favorite movies, and collect the following information about them: title, year of release, IMDB rating, and short description. Create a favourite_movies variable as a list of four dictionaries (representing the movies), and add the movie details to the dictionaries using the title, year, rating, and description keys.

# The data.py file contains a variable named favourite_movies. The value of the variable is a list which contains four dictionaries.

# All dictionaries in the list include the following keys, based on the movie data: title, year, rating, description.

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

# Present some data
# Display the following pieces of data in the terminal when running the data.py file: title of the first movie, year of the second movie, rating of the third movie, and the description of the fourth movie.

# The title of the first movie is displayed in the terminal when the data.py file is run.

# The year of the second movie is displayed in the terminal when the data.py file is run.

# The rating of the third movie is displayed in the terminal when the data.py file is run.

# The description of the fourth movie is displayed in the terminal when the data.py file is run.

# Present some context
# Extend the previously displayed data fields by adding a string before each field.

# The title of the first movie is preceded by the text "The title of the first movie is: " when data.py is run in the terminal.

# The year of the second movie is preceded by the text "The release year of the second movie is: " when data.py is run in the terminal.

# The rating of the third movie is preceded by the text "The IMDB rating of the third movie is: " when data.py is run in the terminal.

# The description of the fourth movie is preceded by the text "The short description of the fourth movie is: " when data.py is run in the terminal.

print("The title of the first movie is:", favourite_movies[0]["title"])
print("The release year of the second movie is:", favourite_movies[1]["year"])
print("The IMDB rating of the third movie is:", favourite_movies[2]["rating"])
print("The short description of the fourth movie is:", favourite_movies[3]["description"])

# Include more data
# Extend the movie dictionaries with more data. Collect the director(s), writer(s), stars, and genres of the movies, and add them to the dictionaries as lists (even if a movie has only one director or writer). Use the following keys: directors, writers, actors, and genres.

# All dictionaries in the favourite_movies list include the directors, writers, actors, and genres keys.

# All values of the newly-defined keys are of type list.

# Present some new data
# Present the first director of the first movie, the first writer of the second movie, the first star of the third movie, and the first genre of the fourth movie.

# The first director of the first movie is preceded by the text "The lead director of the first movie is: " when data.py is run in the terminal.

# The first writer of the second movie is preceded by the text "The lead writer of the second movie is: " when data.py is run in the terminal.

# The first star of the third movie is preceded by the text "The lead star of the third movie is: " when data.py is run in the terminal.

# The first genre of the fourth movie is preceded by the text "The main genre of the fourth movie is: " when data.py is run in the terminal.

print("\nAdditional Details:")
print("The lead director of the first movie is:", favourite_movies[0]["directors"][0])
print("The lead writer of the second movie is:", favourite_movies[1]["writers"][0])
print("The lead star of the third movie is:", favourite_movies[2]["actors"][0])
print("The main genre of the fourth movie is:", favourite_movies[3]["genres"][0])

# Calculate the average rating of the movies
# Calculate the average rating of the movies and save it to a new variable named average_rating.

# The data.py file contains a variable named averageRating the value of which is the calculated average rating of the four movies.

# Calculate the average age of the movies
# Calculate the average age of the movies and save it to a new variable named average_age. Calculate the age of each movie based on the release year before evaluating the average value.

# The data.py file contains a variable named average_age, which is the average age of the four movies.

print("\nCalculated Values:")
print("Average Rating of the movies:", average_rating)
print("Average Age of the movies:", average_age)

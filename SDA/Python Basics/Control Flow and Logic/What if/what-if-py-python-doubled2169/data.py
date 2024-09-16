# WRITE YOUR CODE HERE

# List of movies
# In a previous project, you created a list of your four favorite movies. Copy that list into the data.py file in this project's repository.

# The data.py file contains a variable named fav_movies which holds a list derived from the 'My Top 4 Movies' project.

fav_movies = [
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

# The for loop
# Use a for loop and print function to display all the movie titles in the terminal.

# All movie titles are displayed in the terminal using a for loop and the print function.

for movies in fav_movies:
    print(movies["title"])

# The while loop
# Perform the same task with a while loop.

# All movie titles are displayed in the terminal using a while loop and the print function.

i = 0
while i < len(fav_movies):
    print(fav_movies[i]["title"])
    i += 1

# Average rate
# Calculate the average rating using a loop. Create a total_rate variable outside the loop with a starting value of 0. Add each movie's rating to this variable within the loop. After the loop, calculate the average rating.

# An average_rate variable exists, calculated as the average rating of the movies. The summing occurs inside the loop, and the average is computed outside the loop.

# The average rating is printed to the terminal.

total_rate = 0
for movies in fav_movies:
    total_rate += movies["rating"]
average_rate = total_rate / len(fav_movies)
print(average_rate)

# Newest movie
# Identify the newest movie by combining a for loop with an if/else statement. Initialize a newest_movie variable with the first movie object, then update it as you find newer movies. Print the newest movie's title after the loop.

# A newest_movie variable exists that holds the newest movie object after the loop.

# The title of the newest movie is printed to the terminal.

newest_movie = fav_movies[0]
for movies in fav_movies:
    if movies["year"] >  newest_movie["year"]:
        newest_movie = movies
    else:
        continue
print(newest_movie)

# Combined loops
# Combine loops to log all movie stars. Initialize a stars_by_movies variable as an empty string. Use nested loops to concatenate movie titles and their stars to this variable, separating entries with line breaks.

# A stars_by_movies variable contains a concatenated string of movie titles and stars.

# The stars_by_movies variable's content is printed to the terminal.

stars_by_movies = ""
for movies in fav_movies:
    stars_by_movies += movies["title"] + "\n\n"
    for actor in movies["actors"]:
        stars_by_movies += actor + ",\n"
    stars_by_movies += "\n______________________\n\n"
print(stars_by_movies)
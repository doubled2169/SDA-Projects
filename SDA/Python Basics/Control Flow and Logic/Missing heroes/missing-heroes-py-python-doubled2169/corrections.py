from data import movies

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE

# Missing Martin
# Martin Scorsese is missing from the data of his movies. Wherever there is an empty string as the value of the 'director' key, add Martin Scorsese.

# There are no objects in the movies list with an empty string as the value of the 'director' key.

# Martin Scorsese appears four times as director.

for movie in movies:
    if movie["director"] == "":
        movie["director"] = "Martin Scorsese"
print(movies)

# Correct wrong release years
# The release year is incorrect for five films. Each is one thousand or two thousand years less than it should be. Correct the years by adding 1000 or 2000 to them.

# The 'year' key value for every movie is greater than 1900.

for movie in movies:
    if movie["year"] < 30:
        movie["year"] += 2000
    if movie["year"] > 30 and movie["year"]< 1000:
        movie["year"] += 1000
print(movies)

# Leonardo is mixed up
# Instead of Leonardo DiCaprio, Leonardo da Vinci is listed among the actors. Correct this mistake.

# Leonardo da Vinci is not listed as an actor in any of the movies.

# Leonardo DiCaprio is listed as an actor in six movies.

error = "Leonardo da Vinci"
replacer = "Leonardo DiCaprio"

for movie in movies:
    if error in movie["actors"]:
        movie["actors"] = [replacer if actor == error else actor for actor in movie["actors"]]
print(movies)

# Add drama
# The 'Drama' genre is missing from the genre lists of several movies. Wherever there is an empty string as an item of the 'genres' list, add the 'Drama' genre.

# There are no empty strings in the genres lists.

# The genre 'Drama' appears 98 times in the genres lists of the movies.

blank = ""
genre = "Drama"
for movie in movies:
    if blank in movie["genres"]:
        movie["genres"] = [genre if genres == blank else genres for genres in movie["genres"]]
print(movies)

# How many actors are in the list?
# Count how many actors are in the list. Store the result in the 'allTheActors' variable. First, count all names without worrying about duplicate names. Then, if you feel up for the challenge (optional), try filtering out duplicates!

# There is an 'allTheActors' variable the value of which is the number of all the actors in the list.

allTheActors = set()
for movie in movies:
    allTheActors.update(movie["actors"])
print("There are", len(allTheActors), "actors and they are:", allTheActors)
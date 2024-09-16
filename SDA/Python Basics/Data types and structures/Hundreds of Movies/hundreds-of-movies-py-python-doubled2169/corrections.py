from data import movies

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE

# Add missing plots
# Complete the five missing plots (empty strings) in the data.

# The value of the plot key for the Beetlejuice movie (id: 1) in the movies list is filled in with the movie plot.

# The value of the plot key for the Inception movie (id: 22) in the movies list is filled in with the movie plot.

# The value of the plot key for the The Hobbit: The Desolation of Smaug movie (id: 52) in the movies list is filled in with the movie plot.

# The value of the plot key for the Vicky Cristina Barcelona movie (id: 53) in the movies list is filled in with the movie plot.

# The value of the plot key for the The Rum Diary movie (id: 105) in the movies list is filled in with the movie plot.

movies[0].update({'plot' : 'A recently deceased couple, trapped in their own home as ghosts, hire a mischievous spirit named Beetlejuice to scare away the obnoxious new owners, only to face chaotic consequences.'})
movies[21].update({'plot' : "A skilled thief, who steals corporate secrets through the use of dream-sharing technology, is offered a chance to have his criminal history erased if he can successfully implant an idea into a target's subconscious."})
movies[51].update({'plot' : 'Bilbo Baggins, along with Thorin Oakenshield and his company of dwarves, continue their quest to reclaim Erebor, facing dangerous creatures and the formidable dragon Smaug who guards the treasure they seek.'})
movies[52].update({'plot' : 'Two American women vacationing in Spain become romantically entangled with a charismatic painter, while dealing with the unpredictable and fiery presence of his ex-wife.'})
movies[104].update({'plot' : 'A journalist takes on a freelance job in Puerto Rico, where he struggles with a corrupt business environment, love interests, and his own growing addiction to rum.'})

# Correct wrong release years
# Correct the release year for five films by updating the original (wrong) year with the correct year.

# The value of the year key for the The Beach movie (id: 18) in the movies list is filled in with the correct release year.

# The value of the year key for the American Beauty movie (id: 27) in the movies list is filled in with the correct release year.

# The value of the year key for the Slumdog Millionaire movie (id: 54) in the movies list is filled in with the correct release year.

# The value of the year key for the WALL-E movie (id: 81) in the movies list is filled in with the correct release year.

# The value of the year key for the Dallas Buyers Club movie (id: 102) in the movies list is filled in with the correct release year.

movies[17].update({'year' : 2000})
movies[26].update({'year' : 1999})
movies[53].update({'year' : 2008})
movies[80].update({'year' : 2008})
movies[101].update({'year' : 2013})

# Add missing actor names
# Complete the missing actor names in the data.

# The first actor for The Shawshank Redemption movie (id: 3) in the movies list is updated with the missing actor's name.

# The last actor for No Country for Old Men movie (id: 13) in the movies list is updated with the missing actor's name.

# The first actor for Shutter Island movie (id: 35) in the movies list is updated with the missing actor's name.

# The second actor for The Pianist movie (id: 66) in the movies list is updated with the missing actor's name.

# The third actor for The Hateful Eight movie (id: 144) in the movies list is updated with the missing actor's name.

missing_actors = ['Tim Robbins', 'Woody Harrelson', 'Leonardo DiCaprio', 'Thomas Kretschmann', 'Walton Goggins']

for entry in movies:
    actors = entry['actors']

    for i in range(len(actors)):
        if actors[i] == '' and missing_actors:
            actors[i] = missing_actors.pop(0)

# Add missing directors
# Five directors are missing – add the director keys with the correct names.

# The Memento movie (id: 8) in the movies list has a director key added with the director's name.

# The Lock, Stock and Two Smoking Barrels movie (id: 31) in the movies list has a director key added with the director's name.

# The Midnight in Paris movie (id: 38) in the movies list has a director key added with the director's name.

# The God Bless America movie (id: 64) in the movies list has a director key added with the director's name.

# The The Wolf of Wall Street movie (id: 82) in the movies list has a director key added with the director's name.

movies[7].update({'director' : 'Christopher Nolan'})
movies[30].update({'director' : 'Guy Ritchie'})
movies[37].update({'director' : 'Woody Allen'})
movies[63].update({'director' : 'Bobcat Goldthwait'})
movies[81].update({'director' : 'Martin Scorsese'})

# Add missing genres
# Complete the missing genres keys with the correct data for two movies.

# The Kiss Kiss Bang Bang movie (id: 96) in the movies list has a genres key added with the movie's genres.

# The The Big Short movie (id: 146) in the movies list has a genres key added with the movie's genres.

movies[95].update({'genres' : ['Comedy, Crime, Mystery, Thriller']})
movies[145].update({'genres' : ['Biography, Comedy, Drama']})

# Add missing movie
# The V for Vendetta movie is missing; add it to the movies list with id = 90, between Oblivion and Gattaca.

# The movies list includes the V for Vendetta movie object with all required properties, positioned correctly.

v_for_vendetta = {
    "id": 90,
    "title": "V for Vendetta",
    "year": 2005,
    "runtime": 132,
    "genres": ["Action", "Drama", "Sci-Fi"],
    "director": "James McTeigue",
    "actors": ["Hugo Weaving", "Natalie Portman", "Rupert Graves", "Stephen Rea"],
    "plot": "In a future British tyranny, a shadowy freedom fighter known only by the alias of 'V' plots to overthrow it with the help of a young woman."
}
movies[89].update(v_for_vendetta)
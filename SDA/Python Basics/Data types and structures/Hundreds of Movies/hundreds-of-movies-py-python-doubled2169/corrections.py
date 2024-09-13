from data import movies

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE

movies[0].update({'plot' : 'A recently deceased couple, trapped in their own home as ghosts, hire a mischievous spirit named Beetlejuice to scare away the obnoxious new owners, only to face chaotic consequences.'})
movies[21].update({'plot' : "A skilled thief, who steals corporate secrets through the use of dream-sharing technology, is offered a chance to have his criminal history erased if he can successfully implant an idea into a target's subconscious."})
movies[51].update({'plot' : 'Bilbo Baggins, along with Thorin Oakenshield and his company of dwarves, continue their quest to reclaim Erebor, facing dangerous creatures and the formidable dragon Smaug who guards the treasure they seek.'})
movies[52].update({'plot' : 'Two American women vacationing in Spain become romantically entangled with a charismatic painter, while dealing with the unpredictable and fiery presence of his ex-wife.'})
movies[104].update({'plot' : 'A journalist takes on a freelance job in Puerto Rico, where he struggles with a corrupt business environment, love interests, and his own growing addiction to rum.'})

movies[17].update({'year' : 2000})
movies[26].update({'year' : 1999})
movies[53].update({'year' : 2008})
movies[80].update({'year' : 2008})
movies[101].update({'year' : 2013})

missing_actors = ['Tim Robbins', 'Woody Harrelson', 'Leonardo DiCaprio', 'Thomas Kretschmann', 'Walton Goggins']

for entry in movies:
    actors = entry['actors']

    for i in range(len(actors)):
        if actors[i] == '' and missing_actors:
            actors[i] = missing_actors.pop(0)

movies[7].update({'director' : 'Christopher Nolan'})
movies[30].update({'director' : 'Guy Ritchie'})
movies[37].update({'director' : 'Woody Allen'})
movies[63].update({'director' : 'Bobcat Goldthwait'})
movies[81].update({'director' : 'Martin Scorsese'})

movies[95].update({'genres' : ['Comedy, Crime, Mystery, Thriller']})
movies[145].update({'genres' : ['Biography, Comedy, Drama']})

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
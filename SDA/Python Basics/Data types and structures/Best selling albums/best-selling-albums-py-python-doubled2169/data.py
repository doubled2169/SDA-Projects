bestSellingAlbums = [
    {
        "artist": "Michael Jackson",
        "title": "Thriller",
        "year": 1982,
        "genres": ["pop", "post-disco", "funk", "rock"],
        "sale": 70000000,
    },
    {
        "artist": "AC/DC",
        "title": "Back in Black",
        "year": 1980,
        "genres": ["hard rock"],
        "sale": 50000000,
    },
    {
        "artist": "Whitney Houston",
        "title": "The Bodyguard",
        "year": 1992,
        "genres": ["r&b", "soul", "pop", "soundtrack"],
        "sale": 45000000,
    },
    {
        "artist": "Pink Floyd",
        "title": "The Dark Side of the Moon",
        "year": 1973,
        "genres": ["progressive rock"],
        "sale": 45000000,
    },
    {
        "artist": "Eagles",
        "title": "Their Greatest Hits (1971 - 1975)",
        "year": 1976,
        "genres": ["country rock", "soft rock", "folk rock"],
        "sale": 44000000,
    },
    {
        "artist": "Eagles",
        "title": "Hotel California",
        "year": 1976,
        "genres": ["soft rock"],
        "sale": 42000000,
    },
    {
        "artist": "Shania Twain",
        "title": "Come On Over",
        "year": 1997,
        "genres": ["country", "pop"],
        "sale": 40000000,
    },
    {
        "artist": "Fleetwood Mac",
        "title": "Rumours",
        "year": 1977,
        "genres": ["soft rock"],
        "sale": 40000000,
    },
]

# WRITE YOUR CODE HERE

# Calculate average sales income
# Calculate the average sales income of the albums. Assign this calculation to a new variable named average_sale.

# The data.py file contains a variable named average_sale whose value is the calculation of the average sale of the eight albums.

total_sales = sum(i["sale"] for i in bestSellingAlbums)
average_sale = total_sales / len(bestSellingAlbums)

print(average_sale)

# Calculate average age
# Calculate the average age of the albums. First, store the current year in a variable named current_year, then calculate the average age and assign it to another variable called average_age.

# The data.py file contains a variable named average_age whose value is the calculation of the average age of the eight albums.

current_year = 2024
total_age = sum(i["year"] for i in bestSellingAlbums)
average_age = (2024 * len(bestSellingAlbums) - total_age) / len(bestSellingAlbums)

print(average_age)

# Newest and oldest album
# Create a variable named newest_album and assign the most recently released album (dictionary) as its value. Create another variable named oldest_album and assign the oldest album to it.

# The data.py file contains a variable named newest_album whose value is the most recently released album dictionary from the best_selling_albums list.

# The data.py file contains a variable named oldest_album whose value is the oldest released album dictionary from the best_selling_albums list.

newest_album = max(bestSellingAlbums, key=lambda album: album["year"])
oldest_album = min(bestSellingAlbums, key=lambda album: album["year"])

print("Newest album is : ", newest_album)
print("Oldest album is : ", oldest_album)

# Albums of Eagles
# The band Eagles has two albums on the list. Create a new variable albums_eagles as a dictionary. Then add a sales key with the sum of the sales of the two albums. Add another key named is_both_soft_rock, and set its value to true by comparing the "soft rock" genres of both albums.

# The data.py file contains a variable named albums_eagles whose value is a dictionary.

# One key of the dictionary is sales, with its value being the sum of the sales of the two Eagles albums.

# Another key of the dictionary is is_both_soft_rock whose value is true if both Eagles albums are classified under "soft rock" genre.

eagles_albums = [album for album in bestSellingAlbums if album["artist"] == "Eagles"]

albums_eagles = {}

albums_eagles['sales'] = sum(album["sale"] for album in eagles_albums)

albums_eagles['is_both_soft_rock'] = all("soft rock" in album["genres"] for album in eagles_albums)

print(albums_eagles)

# Add an extra album
# Find another album of your choice, collect similar data as the albums in the best_selling_albums list. Make a dictionary out of it and set it as the value of the ninth item in the best_selling_albums list.

# The best_selling_albums list has a ninth item which is a dictionary containing the same keys as the others. The ninth item is added using the assignment operator and list indexing.

best_selling_albums = {
        "artist": "Lorna Shore",
        "title": "Pain Remains",
        "year": 2022,
        "genres": ["Deathcore"],
        "sale": 6000,
}

bestSellingAlbums.insert(8, best_selling_albums)

print(bestSellingAlbums)

# Like it or not
# Add a new i_like_it key to each album dictionary with a boolean value: true if you like the album and false if you do not.

# Each album dictionary in the best_selling_albums list contains an i_like_it key with a boolean value. The new key is added using the assignment operator, list indexing, and dictionary key assignment.

like_album_flags = [True, True, False, True, True, True, False, False, True]

for i in range(len(bestSellingAlbums)):
    bestSellingAlbums[i]['i_like_it'] = like_album_flags[i]

for album in bestSellingAlbums:

    print(bestSellingAlbums)
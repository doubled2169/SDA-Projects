# WRITE YOUR CODE HERE

# Reuse the array
# Copy the array of your two favorite books from a previous project into the data.py file in this project's repository.

# The data.py file contains a variable favourite_books with the array from the "Data around us" project.

year = 2024

favourite_books = [
    {
        "title" : "Dark Souls: The Complete Collection" ,
        "author" : "George Mann" ,
        "year" : 2021 ,
        "is_published_after_2000" : True ,
        "age" : 2024 - year,
        "characters" : ["Artorias" , "Gwyn Lord of Cinder" , "Solaire of Astora" , "Siegward of Catarina" , "Chaos Witch Quelaag" , "Andre of Astora" , "Sif"]
    },
    {
        "title" : "The Last Wish" ,
        "author" : "Andrzej Sapkowski" ,
        "year" : 1992 ,
        "is_published_after_2000" : False ,
        "age" : 2024 - year ,
        "characters" : ["Geralt" , "Foltest" , "Ostrit" , "Adda"]
    }
]

# Display titles using 'for' loop
# Make both book titles visible in the terminal using only one print() inside a for loop.

# Both book titles are displayed in the terminal using a for loop and a print() inside it.

for books in favourite_books:
    print(books["title"])

# Display authors using 'for' loop
# Display the authors of both books in the terminal using a simple for loop.

# The authors of both books are displayed in the terminal using a for loop and a print() inside it.

for books in favourite_books:
    print(books["author"])

# Check the age of books using 'if'
# Check if the first book is newer than 2000 using its is_published_after_2000 key and display the title only if it's True.

# The title of the first book is displayed in the terminal if the is_published_after_2000 key is True.

if favourite_books[0]["is_published_after_2000"] == True:
    print(favourite_books[0]["title"])

# Check the age of books using 'if/else'
# Concatenate the title of the books with a string indicating if the book is newer or older than 2000.

# The title of the first book is displayed with appropriate text indicating if it's newer or older than 2000.

# The title of the second book is displayed with appropriate text indicating if it's newer or older than 2000.

if favourite_books[0]["is_published_after_2000"] == True:
    print("This book is newer than 2000:", favourite_books[0]["title"])
else:
    print("This book is older than 2000:", favourite_books[0]["title"])
if favourite_books[1]["is_published_after_2000"] == True:
    print("This book is newer than 2000:", favourite_books[1]["title"])
else:
    print("This book is older than 2000:", favourite_books[1]["title"])

# Check the age of books switched
# Use the not-equal operator (!=) for the same result as the previous task.

# The title of the first book is displayed with appropriate text indicating its publication year relative to 2000.

# The title of the second book is displayed with appropriate text indicating its publication year relative to 2000.

if favourite_books[0]["is_published_after_2000"] != True:
    print("This book is older than 2000:", favourite_books[0]["title"])
else:
    print("This book is newer than 2000:", favourite_books[0]["title"])
if favourite_books[1]["is_published_after_2000"] != True:
    print("This book is older than 2000:", favourite_books[1]["title"])
else:
    print("This book is newer than 2000:", favourite_books[1]["title"])

# Compare the publishing year
# Use inequality operators to display the book title with a prefix indicating if it's newer or older than 2000.

# The title of the first book is displayed with text indicating if it's newer or older than 2000.

# The title of the second book is displayed with text indicating if it's newer or older than 2000.

if favourite_books[0]["year"] <= 2000:
    print("This book is older than 2000:", favourite_books[0]["title"])
else:
    print("This book is newer than 2000:", favourite_books[0]["title"])
if favourite_books[1]["year"] <= 2000:
    print("This book is older than 2000:", favourite_books[1]["title"])
else:
    print("This book is newer than 2000:", favourite_books[1]["title"])

# Combine the results using loops and conditionals
# Combine a loop and a conditional statement to perform the same task as the last time for each book.

# The titles of both books are displayed with text indicating their publication year relative to 2000 using a for loop.

# The titles of both books are displayed with text indicating their publication year relative to 2000 using a for of loop.

for book in favourite_books:
    if book["year"] <= 2000:
        print("This book is older than 2000:", book["title"])
    else:
        print("This book is newer than 2000:", book["title"])
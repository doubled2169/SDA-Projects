title = "Dark Souls: The Complete Collection"
author = "George Mann"
year = 2021
isNewerThan2000 = True
age = 2024 - year
characters = ["Artorias" , "Gwyn Lord of Cinder" , "Solaire of Astora" , "Siegward of Catarina" , "Chaos Witch Quelaag" , "Andre of Astora" , "Sif"]
print(title)
print(author)
print(year)
print(isNewerThan2000)
print(age)
print(characters)
print(characters[0], "," ,characters[1])

favoriteBook = {
    "title" : "Dark Souls: The Complete Collection" ,
    "author" : "George Mann" ,
    "year" : 2021 ,
    "isNewerThan2000" : True ,
    "age" : 2024 - year ,
    "characters" : ["Artorias" , "Gwyn Lord of Cinder" , "Solaire of Astora" , "Siegward of Catarina" , "Chaos Witch Quelaag" , "Andre of Astora" , "Sif"]
}

print(favoriteBook.get("author") , favoriteBook.get("year"))
print(favoriteBook.get("characters")[0])

favoriteBooks = [
    {
        "title" : "Dark Souls: The Complete Collection" ,
        "author" : "George Mann" ,
        "year" : 2021 ,
        "isNewerThan2000" : True ,
        "age" : 2024 - year ,
        "characters" : ["Artorias" , "Gwyn Lord of Cinder" , "Solaire of Astora" , "Siegward of Catarina" , "Chaos Witch Quelaag" , "Andre of Astora" , "Sif"]
    },
    {
        "title" : "The Last Wish" ,
        "author" : "Andrzej Sapkowski" ,
        "year" : 1992 ,
        "isNewerThan2000" : False ,
        "age" : 2024 - year ,
        "characters" : ["Geralt" , "Foltest" , "Ostrit" , "Adda"]
    }
]

print(favoriteBooks[1].get("title"))
print(favoriteBooks[1].get("characters")[0])

age_difference = favoriteBooks[0].get("year") - favoriteBooks[1].get("year")

if age_difference << 0:
    age_difference = abs(age_difference)

print(age_difference)
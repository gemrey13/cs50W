people = [
    {'name': "Luffy", "power": "pirate"},
    {'name': "Goku", "power": "saiyan"},
    {"name": "Naruto", "power": "ninja"}
]

#def f(person):
#    return person["power"]

# Like a arrow function in javascript
#people.sort(key=f)
people.sort(key=lambda person: person["name"])

print(people)
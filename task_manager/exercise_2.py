name = 'George'
age = 25
height = '185cm'
hobbies = ['coding', 'watching football', 'gaming']
like_python = True
books_1 = {
    'name': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'year': 1925,
    'genre': 'Fiction',
    'rating': 4.5,
    'interesting_facts': [
        'The novel is set in the Roaring Twenties, a period of economic prosperity in the United States.',
        'It explores themes of decadence, idealism, resistance to change, social upheaval, and excess.'
    ]
}

books_2 = {
    'name': 'Mob Psycho 100',
    'author': 'ONE',
    'year': 2012,
    'genre': 'Manga',
    'rating': 4.8,
    'interesting_facts': [
        'The series was adapted into an anime that aired in 2016.',
        'It has received critical acclaim for its unique art style and storytelling.'
    ]
}

new_hobby = input("what is your new hobby? ")
hobbies.append(new_hobby)

print(f"{books_1} is a type of {type(books_1)}")
print(f"{books_2} is a type of {type(books_2)}")
print(f"{like_python} is a type of {type(like_python)}")
print(f"{hobbies} is a type of {type(hobbies)}")
print(f"{name} is a type of {type(name)}")
print(f"{age} is a type of {type(age)}")
print(f"{height} is a type of {type(height)}")
print(f"My name is {name}, I am {age} years old, and my height is {height}.")
print(f"My hobbies include: {', '.join(hobbies)}.")
print(f"I have two favorite books: '{books_1['name']}' and '{books_2['name']}'.")
print(f"'{books_1['name']}' was published in {books_1['year']} and is a {books_1['genre']} novel with a rating of {books_1['rating']} stars.")
print(f"Interesting facts about '{books_1['name']}': {', '.join(books_1['interesting_facts'])}.")
print(f"'{books_2['name']}' was published in {books_2['year']} and is a {books_2['genre']} with a rating of {books_2['rating']} stars.")
print(f"Interesting facts about '{books_2['name']}': {', '.join(books_2['interesting_facts'])}.")
print(f"Do I like Python? {'Yes' if like_python else 'No'}")
print(f"My hobbies are: {', '.join(hobbies)}.")
print(f"My name is {name}, I am {age} years old, and my height is {height}.")
print(f"My hobbies include: {', '.join(hobbies)}.")
print(f"I have two favorite books: '{books_1['name']}' and '{books_2['name']}'.")
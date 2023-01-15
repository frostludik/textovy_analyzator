"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ludek Mraz
email: ludek.mraz@centrum.cz
discord: Luděk M.#5570
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
separator = "-" * 45

#registered users
# +------+-------------+
# | user |   password  |
# +------+-------------+
# | bob  |     123     |
# | ann  |   pass123   |
# | mike | password123 |
# | liz  |   pass123   |
# +------+-------------+

registered_users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
    }

#login process
username = input("Enter your username: ")
password = input("Enter your password: ")

if registered_users.get(username) == password:
    print(separator, f"Welcome to the app, {username}", "We have 3 texts to be analyzed.", separator, sep="\n")
else:
    print(separator, "Unregistered user, terminating the program..", sep="\n")
    quit()

# text choice
choice = input("Enter a number btw. 1 and 3 to select text: ")
if choice.isalpha():
    print("Selected option is not number, terminating program..")
    quit()
elif int(choice) > 0 and int(choice) < 4:
    chosen_text = TEXTS[int(choice) - 1]
else:
    print("Selected option not between 1 and 3, terminating program..")
    quit()

#prepare and format text
cleared_words = list()
for word in chosen_text.split():
    cleared_words.append(word.strip(",.;:"))

#count individual cases
word_occurence = {"total" : [], "titled": [] , "upper" : [], "lower" : [] , "numbers" : []}
for word in cleared_words:
    if word is not "":
        word_occurence["total"].append(word)
    if word.istitle():
        word_occurence["titled"].append(word)
    elif word.isupper():
        word_occurence["upper"].append(word)
    elif word.islower():
        word_occurence["lower"].append(word)
    elif word.isnumeric():
        word_occurence["numbers"].append(int(word))

number_of_words = len(word_occurence["total"])
number_of_title = len(word_occurence["titled"])
number_of_upper = len(word_occurence["upper"])
number_of_lower = len(word_occurence["lower"])
number_of_numbers = len(word_occurence["numbers"])
sum_of_numbers = sum(word_occurence["numbers"])

print(separator)
print(f"There are {number_of_words} words in the selected text.")
print(f"There are {number_of_title} titlecase words.")
print(f"There are {number_of_upper} uppercase words.")
print(f"There are {number_of_lower} lowercase words.")
print(f"There are {number_of_numbers} numeric strings")
print(f"The sum of all numbers is {sum_of_numbers}")
print(separator)

#get words lengths
words_length = []
for word in cleared_words:
    words_length.append(len(word))

counts = {}
for length in words_length:
    if length not in counts:
        counts[length] = 1
    else:
        counts[length] += 1

#formated output lengths
header = ["LEN", "OCCURENCES", "NR"]
print(separator)
print(f"{header[0]: <3} | {header[1]: <19}| {header[2]}")
print(separator)
for key, value in sorted(counts.items()):
    chart = value * "*"
    print(f"{key: <3} | {chart: <19}| {value}")


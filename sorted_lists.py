# The given list of dictionaries represents people in the format
# [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}].

# a) Create a list and put there the name(s) of the youngest person.
# If ages are the same, put all the names of the youngest.
# b) Create a list and put there the longest name(s). If the length of names is the same, put such names.
# c) Calculate the average age of all people from the initial list.

list_of_people = [{"name": "John", "age": 15},
                  {"name": "Jack", "age": 45},
                  {"name": "Sofia", "age": 23},
                  {"name": "Jose", "age": 54},
                  {"name": "Julia", "age": 15},
                  {"name": "Luis", "age": 45},
                  ]

# youngest people
youngest_people = []
minimum_age = 150   # the oldest person in history was 122 years old
for person in list_of_people:
    if person["age"] < minimum_age:
        minimum_age = person["age"]
        youngest_people = [person["name"]]
    elif person["age"] == minimum_age:
        youngest_people.append(person["name"])

print(youngest_people)

# longest name(s)
longest_names = []
max_length = 0
for person in list_of_people:
    if len(person["name"]) > max_length:
        max_length = len(person["name"])
        longest_names = [person["name"]]
    elif len(person["name"]) == max_length:
        longest_names.append(person["name"])

print(longest_names)

# average age
total_age = 0
for person in list_of_people:
    total_age += person["age"]

average_age = total_age/len(list_of_people)
print(average_age)

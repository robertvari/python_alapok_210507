import json

phonebook = {
    "06206667788": {"name": "Robert", "address": "Budapest"},
    "06206667733": {"name": "Tamás", "address": "Debrecen"},
    "06206667711": {"name": "Csilla", "address": "Pécs"},
}

# my_name = "Kriszta"

# f = open("my_name.txt", "a")
# f.write(my_name)
# f.close()

# write json file
with open("my_phonebook.json", "w") as f:
    json.dump(phonebook, f)


# read file
with open("my_phonebook.json") as f:
    data = json.load(f)
    print(data["06206667733"])
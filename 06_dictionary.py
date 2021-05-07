phonebook = {
    "06206667788": {"name": "Robert", "address": "Budapest"},
    "06206667733": {"name": "Tamás", "address": "Debrecen"},
    "06206667711": {"name": "Csilla", "address": "Pécs"},
    "numbers": [1, 2, 3, 4]
}

print(phonebook["06206667711"]["address"])

phonebook["06206661111"] = {"name": "Kriszta", "address": "Nyíregyháza"}
print(phonebook)


phonebook_list = [
    {"phone": "01234", "name": "Robert"},
    {"phone": "5678", "name": "Csaba"},
    {"phone": "5678", "name": "Csaba"},
]

print(phonebook_list[-1]["name"])


# replace data
phonebook["06206667788"] = {"name": "Tom", "address": "London"}
print(phonebook)

# delete
del phonebook["06206667788"]
print(phonebook)
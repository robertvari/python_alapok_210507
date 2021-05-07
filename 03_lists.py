             # 0        1         2
my_list = ["Robert", "Csaba", "Kriszta"]

# print(len(my_list))
# print(my_list[-1])

# add items
my_list.append("Tamás")
print(my_list)

my_list.insert(0, "Csilla")
print(my_list)

# replace item
my_list[1] = "Tom"
print(my_list)

my_list[my_list.index("Kriszta")] = "Chris"
print(my_list)

# delete item from list
print(my_list)
del my_list[my_list.index("Chris")]
print(my_list)

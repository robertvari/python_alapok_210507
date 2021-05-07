my_numbers = {1, 2, 3}
mixed_data = {"Robert", 1, 2, 3, 3.14}
my_set = {1, 2, 3, (4, 5, 6)}

my_set_02 = {1, 2, 3, 4, 5, 3, 6, 7}

name_list = ["Kriszta", "Csaba", "Kriszta", "Tamás"]
name_list = list(set(name_list))
# print(name_list)

# add item
my_set = {1, 3}
my_set.add(2)
my_set.update([4, 5, 6], [7, 8, 9])
print(my_set)

my_set.remove(9)
print(my_set)

# combine two sets
A = {1, 2, 3, 4}
B = {4, 5, 6, 7}
print(A | B)

# intersection
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)

# difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)
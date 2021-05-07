my_list = ["Csaba", "Kriszta", "Tamás", "Tom", "Balázs", "Marci"]

# for index, i in enumerate(my_list):
#     print(index, i)

for i in my_list:
    if i == "Tamás":  # skip this item
        continue

    print(i)

for i in my_list:
    if i == "Tamás":  # break out at Tamás
        break

    print(i)

print("End of code")
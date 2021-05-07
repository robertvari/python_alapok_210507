# my_age = 140

# if my_age < 100:
#     print("You are young!")
# elif my_age > 100 and my_age < 150:
#     print("You are a bit older!")
# else:
#     print("You are dead... :(")

username = "robertvari"
password = "testpas123"

_username = input("username:")
_password = input("password:")


if _username == username and _password == password:
    print("You are logged in as:", username)
else:
    print("Wrong username or password")
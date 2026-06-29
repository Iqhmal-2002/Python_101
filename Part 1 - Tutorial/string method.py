name = input("Enter your name: ")

name_length = len(name)
print(name_length)

#print(help(str))

username = input("Enter username: ")

# if len(username) < 12 and not any(char.isdigit() for char in username) and username.rfind(" ") < 0:
#     print(f"Username is valid. Username is: {username}")
# else:
#     print(f"Username is not valid")

# using rfind() is 
if len(username) < 12 and not any(char.isdigit() for char in username) and " " not in username:
    print(f"Username is valid. Username is: {username}")
else:
    print(f"Username is not valid")
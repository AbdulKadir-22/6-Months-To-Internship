#validate User Name
#1. Username should not exceed 12 letters
#2. USername should not contain spaces
#3. Username must not contain digits

username = input("Enter Username: ")

if len(username) > 12:
    print("Your Username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your Username cannot contain spaces")
elif username.isdigit == True:
    print("Your Username cannot contain digits")
else:
    print(f"Welcome {username}")
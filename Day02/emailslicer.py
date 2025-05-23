email = input("Enter Your Email: ")

index = email.index("@")

username = email[:index ]
domain =  email[index + 1: ]

print(f"Your Username is {username} and Domain is {domain}")
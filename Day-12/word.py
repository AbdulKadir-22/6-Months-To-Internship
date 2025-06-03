
file_path = "Day-12/Team.txt"

try: 
    with open(file_path, "r") as file:
        content = file.read()
        word_list = content.split() 
        word_count = len(word_list)
        print(f"Your file has {word_count} words")

except PermissionError:
    print("You don't have permission to open this file")
except FileNotFoundError:
    print(f"File not Found")


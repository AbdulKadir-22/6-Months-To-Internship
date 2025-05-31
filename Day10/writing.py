
text = "Hello, World!"
team = ["Yusuf", "Zed", "ALfisha", "Ruksana"]
file_path = "Day10/team.txt"
# w = write
# x = if it exist then shows error, if it doesn't exist it will create  
# a = append to the existing file

try:
    with open(file_path,"w") as file:
        for member in team:
            file.write(member + "\n")
        print("Mission accomplished")
except FileExistsError:
    print("That file already Exist so Mission Failed")


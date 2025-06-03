import json

team = {
        "Yusuf" : "leader", 
        "Zed" : "Backend",
        "ALfisha" : "Frontend",
        "Ruksana" : "Database"
}
file_path = "Day10/team.json"

try:
    with open(file_path,"w") as file:
        json.dump(team,file,indent=4)
        print("Mission accomplished")
except FileExistsError:
    print("That file already Exist so Mission Failed")
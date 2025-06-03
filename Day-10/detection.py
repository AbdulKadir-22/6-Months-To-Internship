import os

file_path = "C:/Users/Zeron/Desktop/script"

if os.path.exists(file_path):
    print("Yes this does exist")
    if os.path.isfile(file_path):
        print("This is a File")
    elif os.path.isdir(file_path):
        print("This is a Folder")
else:
    print("This doesn't exist")

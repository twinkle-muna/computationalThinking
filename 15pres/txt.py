import os

folder_path = input(" ")

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))

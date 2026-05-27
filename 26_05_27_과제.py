import os

dir1 = input("First directory: ")
dir2 = input("Second directory: ")

files1 = []
files2 = []

# get files from the first directory
with os.scandir(dir1) as entries:
    for entry in entries:
        if entry.is_file():
            files1.append(entry.name)

# get files from the second directory
with os.scandir(dir2) as entries:
    for entry in entries:
        if entry.is_file():
            files2.append(entry.name)

# compare number of files
if len(files1) != len(files2):
    print("Different number of files")

else:
    same = True

    # compare files
    for name in files1:

        # check if file exists in the second directory
        if name not in files2:
            print(name, "does not exist in the second directory")
            same = False
            continue

        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)

        # compare file sizes
        size1 = os.stat(path1).st_size
        size2 = os.stat(path2).st_size

        if size1 != size2:
            print(name, "has different size")
            same = False
            continue

        # compare file contents
        with open(path1, "r") as f1:
            text1 = f1.read()

        with open(path2, "r") as f2:
            text2 = f2.read()

        if text1 != text2:
            print(name, "has different content")
            same = False

    if same:
        print("Files are identical")

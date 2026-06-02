import os

base = input()

def listAll(path):\

    try:
        dirfiles = os.listdir(path)
    except PermissionError:
        print(path, "<< NOT ALLOWED")
        return
    
    subdirs = [path + "/" + x for x in dirfiles if os.path.isdir(path + "/" + x)]
    print(path)
    for subdir in subdirs:
        listAll(subdir)

listAll(base)

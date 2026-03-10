import os

def create_folder(name):

    os.mkdir(name)

def create_file(name):

    with open(name, "w") as f:
        f.write("")
import os

def current_directory():
    cwd = os.getcwd()
    print(cwd)

def file_path(filename):
    path = os.path.abspath((filename))

current_directory()
filename = 'sample.txt'
file_path(filename)
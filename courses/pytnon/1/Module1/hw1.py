#& C:/Users/alex/AppData/Local/Programs/Python/Python37-32/python.exe d:/My/nanshannia_2/cources/devops-2/pytnon/1/Module1/hw1.py D:\My\nanshannia_2\cources\devops-2\pytnon\1\Module1 usr 22 777

import os, sys

def make_dir(path, name,permissions):
    full_path = os.path.join(path, name)
    permissions = "0" + permissions
    try:
        os.mkdir(full_path, int(permissions))
    except OSError:
        print('Folder ' + full_path + ' is already exists! (or other error)')

if __name__ == '__main__':
    path = sys.argv[1]
    name = sys.argv[2]
    numeric = sys.argv[3]
    permissions = sys.argv[4]
    for i in range (0, int(numeric)):
        make_dir(path, (name + str(i + 1)), permissions)
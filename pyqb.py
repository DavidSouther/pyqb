import sys

def write(string):
    sys.stdout.write(string)

def cls():
    write('\033[2J')

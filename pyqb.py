import sys

def write(string):
    sys.stdout.write(string)

def cls():
    write('\033[2J')

def color(fg, bg=0):
    light = 0
    if fg > 7:
        light = 1
        fg -= 8
    bg = bg % 8
    write('\033['+ str(light) +';3' + str(fg) + 'm')
    write('\033[4' + str(bg) + 'm')


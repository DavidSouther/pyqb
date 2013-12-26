import pyqb
import random

pyqb.cls()

for r in range(0, 10):
    for c in range(0, 50):
        pyqb.locate(r, c)
        pyqb.write(chr(random.randint(32, 137)))

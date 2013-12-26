import pyqb

pyqb.cls()

pyqb.locate(1, 1)
pyqb.color(15)
pyqb.write("pyqb - DOS, brah!")

pyqb.locate(4, 1)
pyqb.write(chr(201))
for i in range(2, 10):
    pyqb.locate(4, i)
    pyqb.write(chr(205))
pyqb.locate(4, 10)
pyqb.write(chr(209))
for i in range(11, 20):
    pyqb.locate(4, i)
    pyqb.write(chr(205))
pyqb.locate(4, 20)
pyqb.write(chr(209))
for i in range(21, 30):
    pyqb.locate(4, i)
    pyqb.write(chr(205))
pyqb.locate(4, 30)
pyqb.write(chr(187))

for i in range(0, 8):
    pyqb.locate(5+i, 1)
    pyqb.color(7, 0)
    pyqb.write(chr(186))

    pyqb.locate(5 + i, 3)
    pyqb.color(i)
    pyqb.write('Hello')

    pyqb.locate(5+i, 10)
    pyqb.color(7, 0)
    pyqb.write(chr(179))

    pyqb.locate(5 + i, 13)
    pyqb.color(i + 8)
    pyqb.write('Hello')

    pyqb.locate(5+i, 20)
    pyqb.color(7, 0)
    pyqb.write(chr(179))

    pyqb.locate(5 + i, 23)
    pyqb.color(0, i)
    pyqb.write('Hello')

    pyqb.locate(5+i, 30)
    pyqb.color(7, 0)
    pyqb.write(chr(186))

pyqb.color(7, 0)

pyqb.locate(13, 1)
pyqb.write(chr(200))
for i in range(2, 10):
    pyqb.locate(13, i)
    pyqb.write(chr(205))
pyqb.locate(13, 10)
pyqb.write(chr(207))
for i in range(11, 20):
    pyqb.locate(13, i)
    pyqb.write(chr(205))
pyqb.locate(13, 20)
pyqb.write(chr(207))
for i in range(21, 30):
    pyqb.locate(13, i)
    pyqb.write(chr(205))
pyqb.locate(13, 30)
pyqb.write(chr(188))

pyqb.locate(20, 1)

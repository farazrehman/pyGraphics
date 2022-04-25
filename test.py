from graphics import *
import time

win = GraphWin('Practice', 600, 600)
win.setCoords(0, 0, 600, 600)

u = 0
v = []

for u in range (100):
    v.append(u*u)
    print(u)

for x in range(len(v)):
    print(x, v[x])
    pt = Point(x, v[x])
    pt.draw(win)

win.getMouse()  # Pause to view result
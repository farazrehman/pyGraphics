
from graphics import *
import time
#http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html
#https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html


def main():
    win = GraphWin('Practice', 600, 600)
    win.setCoords(0,0,600,600)

    x = 300
    y = 300
    r = 10
    t = 10

    for j in range (t):
        cir = Circle(Point(x,y), r)
        cir.setOutline('red')
        cir.draw(win)
        time.sleep(1)
        r = r + 20

    x = 300
    y = 300

    ln = Line (Point(x, y), Point (x+100, y+100))
    ln.draw(win)





    # head = Circle(Point(40, 100), 25)  # set center and radius
    # head.setFill("yellow")
    # head.draw(win)
    #
    # rect = Rectangle(Point(20, 10), pt)
    # rect.draw(win)

    win.getMouse()  # Pause to view result



main()
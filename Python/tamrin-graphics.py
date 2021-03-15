from graphics import *
win = GraphWin()
win.close()
win = GraphWin()
win.close()
win = GraphWin('test', 400, 400)
p1 = Point(10,10)
p1.draw(win)
Point(10.0, 10.0)
# draw dade vared shode ra be dakhel tarhe graphic ma mi barad
p2 = Point(80,90)

p2.draw(win)

# dar gam baadi mikhahim yek khat rasm konim
b1 = Line(p1,p2)
b1.draw(win)
Line(Point(10.0, 10.0), Point(80.0, 90.0))
# dar pain ravesh behtari ra bray keshidan khat anjam midahim


b2 = Line(Point(40,40),Point(190,200))
b2.draw(win)

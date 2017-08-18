from turtle import *

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ((p1[0]+ p2[0])/2, (p1[1]+ p2[1])/ 2)

def sierpinski(points, degree, myTurtle):
    myTurtle.speed(5)
    colormap = ["blue", "red", "green","white","yellow", "violet", "orange","grey","gold","indigo"]
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree - 1, myTurtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)

myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [(-500,-150), (0,250), (500,-150)]
sierpinski(myPoints,8,myTurtle)
myWin.exitonclick()

import turtle
def draw_dotted_line(axis, angle=0,color="red"):
    turtle.color(color)
    if axis == "x":
        turtle.penup()
        turtle.goto(-300, 0)
        turtle.pendown()
        for i in range(40):
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
    elif axis == "y":
        turtle.penup()
        turtle.goto(0, -400)
        turtle.pendown()
        turtle.left(90)
        for i in range(40):
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
    elif axis == "o":
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.left(angle)
        for i in range(20):
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
        turtle.penup()
        turtle.goto(0, 0)
        for i in range(20):
            turtle.backward(10)
            turtle.penup()
            turtle.backward(10)
            turtle.pendown()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.right(angle)
        turtle.color("black")

def fill(x1, y1, x2, y2,color="black"):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x2, y1)
    turtle.goto(x2, y2)
    turtle.goto(x1, y2)
    turtle.goto(x1, y1)
    turtle.end_fill()
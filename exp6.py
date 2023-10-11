# Aryan Singh (0901AM211015)
# Experiment 6 - Basic 2D Transformations
import turtle
from math import sin, cos, pi
from turtleutils import draw_dotted_line

polygon = [
    [0, 0],  # (x1,y1)
    [200, 0],  # (x2,y2)
    [200, 140],  # (x3,y3)
    [0, 140],  # (x4,y4)
]


def draw():
    turtle.penup()
    turtle.goto(polygon[0][0], polygon[0][1])
    turtle.pendown()
    for i in range(1, len(polygon)):
        turtle.goto(polygon[i][0], polygon[i][1])
    turtle.goto(polygon[0][0], polygon[0][1])


def translate(tx, ty):
    for i in range(len(polygon)):
        polygon[i][0] += tx
        polygon[i][1] += ty


def scale(sx, sy):
    for i in range(len(polygon)):
        polygon[i][0] *= sx
        polygon[i][1] *= sy


def rotate(angle):
    angle = angle * pi / 180
    R = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
    global polygon
    new_polygon = []
    for point in polygon:
        x, y = point
        new_x = R[0][0] * x + R[0][1] * y
        new_y = R[1][0] * x + R[1][1] * y
        new_polygon.append([new_x, new_y])
    polygon = new_polygon


def reflect(axis):
    matrix = []
    if axis == "x":
        matrix = [[1, 0], [0, -1]]
        draw_dotted_line("x")
    elif axis == "y":
        matrix = [[-1, 0], [0, 1]]
        draw_dotted_line("y")
    elif axis == "o":
        matrix = [[-1, 0], [0, -1]]
        draw_dotted_line("o", angle=135)

    global polygon
    new_polygon = []
    for point in polygon:
        x, y = point
        new_x = matrix[0][0] * x + matrix[0][1] * y
        new_y = matrix[1][0] * x + matrix[1][1] * y
        new_polygon.append([new_x, new_y])
    polygon = new_polygon


def shear(shx, shy):
    matrix = [[1, 0], [0, 1]]
    if shx != 0:
        matrix[0][1] = shx
    if shy != 0:
        matrix[1][0] = shy

    global polygon
    new_polygon = []
    for point in polygon:
        x, y = point
        new_x = matrix[0][0] * x + matrix[0][1] * y
        new_y = matrix[1][0] * x + matrix[1][1] * y
        new_polygon.append([new_x, new_y])
    polygon = new_polygon


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=1.0, height=1.0)

    draw()
    # 1. Translation
    # translate(100, 100)
    # draw()

    # 2. Scaling
    # scale(1.5, 0.8)
    # draw()

    # 3. Rotation
    # rotate(45)
    # draw()

    # 4. Reflection
    # reflect("x")
    # reflect("y")
    # reflect("o")
    # draw()

    # 5. Shearing
    # shear(0.5, 0)
    # shear(0, 0.4)
    # shear(0.4, 0.4)
    # draw()

    turtle.done()


if __name__ == "__main__":
    main()

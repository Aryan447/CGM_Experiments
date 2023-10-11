# Aryan Singh (0901AM211015)
# Experiment 8 - Color Filling using Algorithms
import turtle
from turtleutils import fill
from collections import deque


def set_window(x1, y1, x2, y2):
    global x_min, y_min, x_max, y_max
    x_min, y_min = x1, y1
    x_max, y_max = x2, y2


def draw_Window():
    turtle.penup()
    turtle.goto(x_min, y_min)
    turtle.pendown()
    turtle.goto(x_max, y_min)
    turtle.goto(x_max, y_max)
    turtle.goto(x_min, y_max)
    turtle.goto(x_min, y_min)
    turtle.penup()

def check(x, y):
    if x_min <= x <= x_max and y_min <= y <= y_max:
        return True
    return False

def floodFill(x, y, color):
    q = deque()
    visited = set()
    q.append((x, y))
    visited.add((x, y))
    turtle.penup()
    turtle.color(color)
    while q:
        print(q,"\n")
        curr_pixel = q.popleft()
        x, y = curr_pixel
        # Up
        if check(x-5,y) and (x - 5, y) not in visited:
            fill(x-5,y,x,y,color)
            q.append((x - 5, y))
            visited.add((x - 5, y))
        # Down
        if check(x+5,y) and (x + 5, y) not in visited:
            fill(x+5,y,x,y,color)
            q.append((x + 5, y))
            visited.add((x + 5, y))
        # Right
        if check(x,y+5) and (x, y + 5) not in visited:
            fill(x,y+5,x,y,color)
            q.append((x, y + 5))
            visited.add((x, y + 5))
        # Left
        if check(x,y-5) and (x, y - 5) not in visited:
            fill(x,y-5,x,y,color)
            q.append((x, y - 5))
            visited.add((x, y - 5))
    fill(x_min, y_min, x_max, y_max, color=color)


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=900, height=700)

    # Draw the window
    set_window(-100, -100, 100, 100)
    draw_Window()

    set_window(-30, -30, 30, 30)
    draw_Window()

    floodFill(0, 0, color="yellow")
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

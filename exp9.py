# Aryan Singh (0901AM211015)
# Experiment 9 - Line Clipping using Cohen-Sutherland Algorithm
import turtle
from time import sleep

# Define the constants for region codes
INSIDE = 0  # 0000
TOP = 8  # 1000
BOTTOM = 4  # 0100
RIGHT = 2  # 0010
LEFT = 1  # 0001

# Define the window coordinates
x_min, y_min = 0, 0
x_max, y_max = 0, 0


# Define the function to calculate region code for a point (x, y)
def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code


# Define the function to clip a line segment
def cohen_sutherland(x1, y1, x2, y2):
    # STEP 1 : Assign the region codes to both endpoints.
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    # STEP 2 : Perform OR operation on both of these endpoints.
    OR_RES = code1 | code2

    # STEP 3 :  if  OR = 0000, then it is completely visible (inside the window).

    if OR_RES == 0:
        return x1, y1, x2, y2

    # else Perform AND operation on both these endpoints.
    AND_RES = code1 & code2
    # if  AND ≠ 0000,then the line is invisible and not inside the window. Also, it can’t be considered for clipping.
    if AND_RES != 0:
        return None, None, None, None

    # else AND = 0000, the line is partially inside the window and considered for clipping.

    # STEP 4 : After confirming that the line is partially inside the window, then we find the intersection with the boundary of the window
    # By using the following formula:- Slope:- m= (y2-y1)/(x2-x1)
    while code1 | code2:
        x, y = 0, 0
        code_out = code1 if code1 != 0 else code2

        #  a) If the line passes through top or the line intersects with the top boundary of the window.
        # x = x + (y_wmax – y)/m
        # y = y_wmax
        if code_out & TOP:
            x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            y = y_max

        #  b) If the line passes through bottom or the line intersects with the bottom boundary of the window.
        # x = x + (y_wmin – y)/m
        # y = y_wmin
        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            y = y_min

        # c) If the line passes through the right region or the line intersects with the right boundary of the window.
        # y = y + (x_wmax -x)*m
        #  x = x_wmax
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            x = x_max

        # d) If the line passes through the left region or the line intersects with the left boundary of the window.
        # y = y+ (x_wmin – x)*m
        # x = x_wmin
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            x = x_min

        # STEP 5 : Replace the outside point with the intersection point.
        if code_out == code1:
            x1, y1 = x, y
            code1 = compute_code(x1, y1)
        else:
            x2, y2 = x, y
            code2 = compute_code(x2, y2)
        # STEP 6 : Repeat the 4th step till your line doesn’t get completely clipped
    return x1, y1, x2, y2


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


# Define a function to draw a line segment
def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.dot()
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.dot()


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=900, height=700)
    # Draw the window
    set_window(50, 50, 150, 150)
    draw_Window()
    lines = [
        [90, 90, 140, 140],
        [30, 30, 30, 200],
        [00, 130, 200, 130],
        [100, 0, 100, 100],
        [40, 70, 80, 40],
    ]
    # Draw the line segments
    for line in lines:
        draw_line(*line)

    # Clip the line segments using Cohen-Sutherland algorithm
    clipped_lines = []
    for line in lines:
        x1, y1, x2, y2 = cohen_sutherland(*line)
        if x1 != None:
            clipped_lines.append([x1, y1, x2, y2])
    sleep(2)
    # Clear the screen
    turtle.clear()

    # Draw the window
    draw_Window()
    # Draw the clipped line segments
    for line in clipped_lines:
        draw_line(*line)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

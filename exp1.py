# Aryan Singh (0901AM211015)
# Experiment 1 - DDA Line Drawing Algorithm
import turtle


# Step 1 :
# Input the two endpoints of the line segment, (x1,y1) and (x2,y2).
def DDA(x1, y1, x2, y2):
    # Step 2 :
    # Calculate the difference between the x-coordinates and y-coordinates of the endpoints as dx and dy respectively.
    dx = x2 - x1
    dy = y2 - y1

    # Step 3 :
    # Calculate the steps to be performed in the algorithm as steps.
    steps = max(abs(dx), abs(dy))

    # Step 4 :
    # calculate the increment in x and y
    x_increment = dx / steps
    y_increment = dy / steps

    # Step 5 :
    # Put the first point (x1,y1) on the output screen.
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()

    # Step 6 :
    # Assign the initial value of x and y as x=x1 and y=y1 respectively.
    x, y = x1, y1
    turtle.dot()  # Draw the initial point

    # Step 7 :
    # Calculate the next points to be plotted, that is, the next value of x and y as x=x+x_increment and y=y+y_increment.
    # Repeat steps 7 and 8 until the last point (x2,y2) is reached.
    while x != x2 or y != y2:
        x = x + x_increment
        y = y + y_increment

        # Step 8 :
        # Put the calculated pixel on the output screen.
        turtle.goto(x, y)
    turtle.dot()  # Draw the final point


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=800, height=600)

    # Example 1 : Horizontal Line
    DDA(0, 0, 200, 0)

    # Example 2 : Vertical Line
    DDA(0, 0, 0, 200)

    # Example 3 : Diagonal Line
    DDA(0, 0, 200, 200)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

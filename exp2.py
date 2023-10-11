# Aryan Singh (0901AM211015)
# Experiment 2 - Bresenham Line Drawing Algorithm
import turtle


def BresenhamLine(x1=0, y1=0, x2=200, y2=400):
    # Step 1 :
    # Plot the initial point (x1,y1) on the output screen.
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()

    # Step 2 :
    # Find dx,dy and p0 = 2dy-dx
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx

    # Step 3 :
    # Assign the initial value of x and y as x=x1 and y=y1 respectively.
    x, y = x1, y1
    turtle.dot()  # Draw the initial point

    # Handling the Vertical Line Case
    if dx == 0:
        for k in range(abs(dy)):
            y = y + 1 if y < y2 else y - 1
            turtle.goto(x, y)
        turtle.dot()
        return

    # Step 4 :
    # Start an iteration k = 0 at each step.
    # Repeat steps 5 and 6 abs(dx) times.
    for k in range(abs(dx)):
        # Step 5 :
        # If pk < 0, then plot(xk+1,yk) set pk+1 = pk + 2dy.
        if p < 0:
            p = p + 2 * dy
            x = x + 1 if x < x2 else x - 1
        # Step 6 :
        # If pk >= 0, then plot(xk+1,yk+1) set pk+1 = pk + 2dy - 2dx.
        else:
            p = p + 2 * dy - 2 * dx
            x = x + 1 if x < x2 else x - 1
            y = y + 1 if y < y2 else y - 1

        turtle.goto(x, y)
    turtle.dot()  # Draw the final point


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=800, height=600)

    # Example 1 : Horizontal Line
    BresenhamLine(0, 0, 200, 0)

    # Example 2 : Vertical Line
    BresenhamLine(0, 0, 0, 200)

    # Example 3 : Diagonal Line
    BresenhamLine(0, 0, 200, 200)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

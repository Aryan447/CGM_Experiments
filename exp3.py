# Aryan Singh (0901AM211015)
# Experiment 3 - Bresenham Circle Drawing Algorithm
import turtle


# Step 1 : Determine the radius of the circle
def BresenhamCircle(radius=100):
    # Step 2 : Ensure the origin is at (0,0) origin
    x, y = 0, 0

    # Step 3 : Plot the initial point of the circle as (x0,y0) = (0,r)
    x, y = 0, radius
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()
    coors = [(x, y)]

    # Step 4 : Calculate the initial value of the decision parameter d0 = 3 - 2r
    d = 3 - 2 * radius

    # Step 5 : Repeat till x <= y
    while x <= y:
        # {i} If dk < 0, then set dk+1 = dk + 4xk + 6 and xk+1 = xk + 1
        if d < 0:
            d = d + 4 * x + 6
            x = x + 1
        # {ii} If dk >= 0, then set dk+1 = dk + 4(xk - yk) + 10, xk+1 = xk + 1 and yk+1 = yk - 1
        else:
            d = d + 4 * (x - y) + 10
            x = x + 1
            y = y - 1

        # Step 6 : Plot the points (xk,yk) and (yk,xk)
        turtle.goto(x, y)
        coors.append((x, y))  # type: ignore

    # Step 7 : Draw this Quarter of the Circle
    for x, y in coors[::-1]:
        turtle.goto(y, x)
        coors.append((y, x))  # type: ignore

    # Step 8 : Draw the Right Half of the Circle
    for x, y in coors[::-1]:
        turtle.goto(x, -y)
        coors.append((x, -y))

    # Step 9 : Draw the Left Half of the Circle
    for x, y in coors[::-1]:
        turtle.goto(-x, y)

    # Step 10 : Circle is drawn
    return


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=800, height=600)

    BresenhamCircle()

    # BresenhamCircle(200)

    # BresenhamCircle(400)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

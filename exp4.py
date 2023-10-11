# Aryan Singh (0901AM211015)
# Experiment 4 - Mid-Point Circle Drawing Algorithm
import turtle


# Step 1 : Determine the radius of the circle
def midPointCircle(radius=100):
    # Step 2 : Ensure the origin is at (0,0) origin
    x, y = 0, 0

    # Step 3 : Plot the initial point of the circle as (x0,y0) = (0,r)
    x, y = 0, radius
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()
    coors = [(x, y)]

    # Step 4 : Calculate the initial value of the decision parameter p0 = 1 - r
    p = 1 - radius

    # Step 5 : Repeat till x <= y
    while x <= y:
        # {i} If pk < 0, then set pk+1 = pk + 2xk + 3
        if p < 0:
            p = p + 2 * x + 3
            x = x + 1
        # {ii} If pk >= 0, then set pk+1 = pk + 2(xk - yk) + 5 and yk+1 = yk - 1
        else:
            p = p + 2 * (x - y) + 5
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
    return coors


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=800, height=600)

    midPointCircle()

    # midPointCircle(200)

    # midPointCircle(400)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

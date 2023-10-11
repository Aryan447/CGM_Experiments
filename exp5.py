# Aryan Singh (0901AM211015)
# Experiment 5 - Mid-Point Ellipse Drawing Algorithm
import turtle


# Step 1: Determine the major and minor axes of the ellipse
def midPointEllipse(a=200, b=100):
    # a = major axis
    # b = minor axis
    # Step 2: Ensure the origin is at (0, 0)
    x, y = 0, 0

    # Step 3: Plot the initial point of the ellipse
    x, y = 0, b
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()
    coordinates = [(x, y)]

    # (Region 1) : Region of the ellipse where x > 0
    # Step 4: Calculate the initial value of the decision parameter p10
    # P10 = b^2 + (a^2)/4 - a^2*b
    p1 = b**2 + ((a**2) / 4) - a**2 * b

    # dx = 2 * b^2 * x
    # dy = 2 * a^2 * y
    dx = 2 * b**2 * x
    dy = 2 * a**2 * y

    # Step 5: Repeat until the gradient of the curve becomes zero
    while dx < dy:
        x += 1
        if p1 < 0:
            dx += 2 * b**2
            p1 += dx + b**2
        else:
            y -= 1
            dx += 2 * b**2
            dy -= 2 * a**2
            p1 += dx - dy + b**2
        coordinates.append((x, y))  # type: ignore

    # (Region 2) : Region of the ellipse where x < 0
    # Step 6: Calculate the initial value of the decision parameter p20
    # P20 = b^2 ( x+ (1 / 2) )^2 + a^2 (y-1)^2 - a^2b^2
    p2 = b**2 * (x + 0.5) ** 2 + a**2 * (y - 1) ** 2 - a**2 * b**2

    # Step 7: Repeat until the entire ellipse is drawn
    while y >= 0:
        y -= 1
        if p2 > 0:
            dy -= 2 * a * a
            p2 += a * a - dy
        else:
            x += 1
            dx += 2 * b * b
            dy -= 2 * a * a
            p2 += dx - dy + a * a
        coordinates.append((x, y))  # type: ignore

    # Step 8: Draw the upper right quadrant of the ellipse
    for x, y in coordinates:
        turtle.goto(x, y)

    # Step 9: Mirror the ellipse to draw the bottom right quadrant of the ellipse
    for x, y in coordinates[::-1]:
        turtle.goto(x, -y)
        coordinates.append((x, -y))

    # Step 10 : Mirror the ellipse to draw the Left Half of the ellipse
    for x, y in coordinates:
        turtle.goto(-x, -y)

    print(coordinates)
    return


# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=800, height=600)

    midPointEllipse(200, 100)  # You can change the major and minor axes here

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

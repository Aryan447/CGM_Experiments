# Aryan Singh (0901AM211015)
# Experiment 10 - Polygon Clipping using Sutherland Hodgeman Algorithm
import turtle
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


def x_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

def y_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

def clip(poly_points, x1, y1, x2, y2):
    new_points = []
    new_poly_size = 0
    poly_size = len(poly_points)

    for i in range(poly_size):
        k = (i+1) % poly_size
        ix, iy = poly_points[i]
        kx, ky = poly_points[k]

        i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)
        k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)

        if i_pos < 0 and k_pos < 0:
            new_points.append([kx, ky])
            new_poly_size += 1
        elif i_pos >= 0 and k_pos < 0:
            new_points.append([x_intersect(x1, y1, x2, y2, ix, iy, kx, ky), 
                              y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)])
            new_poly_size += 1
            new_points.append([kx, ky])
            new_poly_size += 1
        elif i_pos < 0 and k_pos >= 0:
            new_points.append([x_intersect(x1, y1, x2, y2, ix, iy, kx, ky), 
                              y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)])
            new_poly_size += 1

    return new_points

def suthHodgClip(poly_points, clipper_points):
    for i in range(len(clipper_points)):
        k = (i+1) % len(clipper_points)
        poly_points = clip(poly_points, clipper_points[i][0], clipper_points[i][1],
                           clipper_points[k][0], clipper_points[k][1])

    return poly_points

def draw_points(coords):
    # Draw the points
    turtle.penup()
    x0,y0 = coords[0]
    turtle.goto(x0, y0)
    turtle.pendown()
    for x, y in coords:
        turtle.goto(x, y)
        turtle.dot(5)  # Draw a small dot at the coordinate
    turtle.goto(x0,y0)
# Main Function
def main():
    # Set up the Turtle screen
    turtle.speed(1)
    turtle.setup(width=900, height=700)
    
    # Defining clipper window vertices in clockwise order
    clipper_window = [[-100, -100], [-100, 100], [100, 100], [100, -100]]
    set_window(-100, -100, 100, 100)
    draw_Window()
    
    # Defining polygon vertices in clockwise order
    poly_points = [[-50, -150], [50, 80], [200, 100], [50, -150]]
    draw_points(poly_points)
    # Calling the clipping function
    clipped_polygon = suthHodgClip(poly_points, clipper_window)
    turtle.color('red')
    draw_points(clipped_polygon)

    # Printing vertices of clipped polygon
    for point in clipped_polygon:
        print(f'({point[0]}, {point[1]})')
        
    turtle.hideturtle()
    turtle.done()

# Driver code
if __name__ == "__main__":
    main()
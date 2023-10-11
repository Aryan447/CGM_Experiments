# Aryan Singh (0901AM211015)
# Experiment 7 - Basic 3D Transformations
import numpy as np
import matplotlib.pyplot as plt


# Define a function to plot points in 3D
def plot_points_3d(points, ax, color="blue"):
    x, y, z = zip(*points)
    ax.scatter(x, y, z, c=color, s=100)


# Define a function to connect points with lines in 3D
def connect_points_3d(points, ax, color="blue"):
    x, y, z = zip(*points)
    ax.plot(x + (x[0],), y + (y[0],), z + (z[0],), c=color)


# Define a function for 3D translation
def translate_3d(points, dx, dy, dz):
    return [(x + dx, y + dy, z + dz) for x, y, z in points]


# Define a function for 3D rotation (counterclockwise) about the z-axis
def rotate_3d(points, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array(
        [
            [np.cos(angle_radians), -np.sin(angle_radians), 0],
            [np.sin(angle_radians), np.cos(angle_radians), 0],
            [0, 0, 1],
        ]
    )
    return [(x, y, z) @ rotation_matrix for x, y, z in points]


# Define a function for 3D scaling
def scale_3d(points, sx, sy, sz):
    return [(x * sx, y * sy, z * sz) for x, y, z in points]

# Define a function for 3D mirror reflection
def reflect_3d(points, axis):
    if axis == "x":
        reflection_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    elif axis == "y":
        reflection_matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    elif axis == "z":
        reflection_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    else:
        raise ValueError("Invalid axis. Use 'x', 'y', or 'z'.")

    return [(x, y, z) @ reflection_matrix for x, y, z in points]

# Main Function
def main():
    # Original points in 3D
    original_points_3d = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]

    # Create a 3D plot
    fig = plt.figure(figsize=(12, 8))

    # 1. Original points for reference
    ax = fig.add_subplot(231, projection="3d")
    plot_points_3d(original_points_3d, ax, color="brown")
    connect_points_3d(original_points_3d, ax, color="brown")
    ax.set_title("Original")

    # 2. 3D Translation
    ax = fig.add_subplot(232, projection="3d")
    translated_points_3d = translate_3d(original_points_3d, dx=1, dy=2, dz=3)
    plot_points_3d(translated_points_3d, ax, color="red")
    connect_points_3d(translated_points_3d, ax, color="red")
    ax.set_title("3D Translation")

    # 3. 3D Scaling
    ax = fig.add_subplot(233, projection="3d")
    scaled_points_3d = scale_3d(original_points_3d, sx=2, sy=2, sz=1)
    plot_points_3d(scaled_points_3d, ax, color="blue")
    connect_points_3d(scaled_points_3d, ax, color="blue")
    ax.set_title("3D Scaling")

    # 4. 3D Rotation around the z-axis
    ax = fig.add_subplot(234, projection="3d")
    rotated_points_3d = rotate_3d(original_points_3d, angle_degrees=45)
    plot_points_3d(rotated_points_3d, ax, color="green")
    connect_points_3d(rotated_points_3d, ax, color="green")
    ax.set_title("3D Rotation")

    # 5. 3D Mirror Reflection
    ax = fig.add_subplot(235, projection="3d")
    reflected_points_3d_x = reflect_3d(original_points_3d, axis="x")
    plot_points_3d(reflected_points_3d_x, ax, color="orange")
    connect_points_3d(reflected_points_3d_x, ax, color="orange")
    ax.set_title("3D Mirror Reflection (X-axis)")

    # 6. 3D Shearing
    ax = fig.add_subplot(236, projection="3d")
    sheared_points_3d = translate_3d(original_points_3d, dx=1, dy=1, dz=1)
    plot_points_3d(sheared_points_3d, ax, color="purple")
    connect_points_3d(sheared_points_3d, ax, color="purple")
    ax.set_title("3D Shearing")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

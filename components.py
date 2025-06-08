def vector_from_points():
    print("Enter coordinates of the initial point A (x1, y1, z1):")
    x1, y1, z1 = map(float, input("A: ").split())

    print("Enter coordinates of the terminal point B (x2, y2, z2):")
    x2, y2, z2 = map(float, input("B: ").split())

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    print(f"\nVector AB = <{dx}, {dy}, {dz}>")
    print(f"Parametric equations:")
    print(f"x = {x1} + {dx}t")
    print(f"y = {y1} + {dy}t")
    print(f"z = {z1} + {dz}t")


def vector_from_direction():
    print("Enter coordinates of a point P on the line (x0, y0, z0):")
    x0, y0, z0 = map(float, input("P: ").split())

    print("Enter direction vector components <dx, dy, dz>:")
    dx, dy, dz = map(float, input("Direction vector: ").split())

    print(f"\nVector direction = <{dx}, {dy}, {dz}>")
    print(f"Parametric equations:")
    print(f"x = {x0} + {dx}t")
    print(f"y = {y0} + {dy}t")
    print(f"z = {z0} + {dz}t")


def main():
    print("How would you like to define the line?")
    print("1. Using two points")
    print("2. Using a point and a direction vector")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        vector_from_points()
    elif choice == '2':
        vector_from_direction()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

import math

def cartesian_to_polar(x, y):
    # radius
    r = math.sqrt(x**2 + y**2)
    
    # angle in radians (atan2 handles quadrant automatically)
    theta = math.atan2(y, x)
    
    # also convert to degrees if you want
    theta_deg = math.degrees(theta)
    
    return r, theta, theta_deg

# Example usage:
if __name__ == "__main__":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    r, theta, theta_deg = cartesian_to_polar(x, y)

    print(f"Radius r = {r}")
    print(f"Theta (radians) = {theta}")
    print(f"Theta (degrees) = {theta_deg}")

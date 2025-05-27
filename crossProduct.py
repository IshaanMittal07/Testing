import numpy as np

def get_vector(name):
    print(f"Enter components of vector {name} (x y z):")
    components = input().strip().split()
    if len(components) != 3:
        raise ValueError("Each vector must have exactly 3 components.")
    return np.array([float(c) for c in components])

def main():
    print("=== Cross Product of Two Vectors ===")
    
    try:
        a = get_vector("A")
        b = get_vector("B")

        cross_product = np.cross(a, b)
        print(f"\nCross product (A × B): {cross_product}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

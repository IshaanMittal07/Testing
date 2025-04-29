from scipy.stats import hypergeom

def solve_hypergeometric(N, K, n, k):
    """
    Solve the hypergeometric probability P(X = k)
    
    Parameters:
    - N: total population size
    - K: total number of success states in the population
    - n: number of draws
    - k: number of observed successes

    Returns:
    - Probability P(X = k)
    """
    probability = hypergeom.pmf(k, N, K, n)
    return probability

def main():
    print("Hypergeometric Distribution Solver")
    N = int(input("Enter population size (N): "))
    K = int(input("Enter number of successes in population (K): "))
    n = int(input("Enter number of draws (n): "))
    k = int(input("Enter number of observed successes (k): "))

    prob = solve_hypergeometric(N, K, n, k)
    print(f"\nP(X = {k}) = {prob:.5f}")

if __name__ == "__main__":
    main()

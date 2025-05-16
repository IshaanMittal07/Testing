import math
from scipy.stats import norm

def normal_approximation_to_binomial(n, p):
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    return mu, sigma

def probability_normal(x, mu, sigma, continuity=False, inequality='<='):
    if continuity:
        if inequality == '<=':
            x += 0.5
        elif inequality == '<':
            x -= 0.5
        elif inequality == '>=':
            x -= 0.5
        elif inequality == '>':
            x += 0.5
    z = (x - mu) / sigma
    if inequality == '<=' or inequality == '<':
        return norm.cdf(z)
    elif inequality == '>=' or inequality == '>':
        return 1 - norm.cdf(z)

def probability_between(a, b, mu, sigma, continuity=False):
    if continuity:
        a -= 0.5
        b += 0.5
    z1 = (a - mu) / sigma
    z2 = (b - mu) / sigma
    return norm.cdf(z2) - norm.cdf(z1)

# === Example Usage ===
n = 50         # number of trials
p = 0.6        # probability of success
x = 30         # value to calculate P(X <= x)
inequality = '<='

mu, sigma = normal_approximation_to_binomial(n, p)

print("=== Normal Approximation to Binomial ===")
print(f"Without continuity correction: P(X {inequality} {x}) = {probability_normal(x, mu, sigma, continuity=False, inequality=inequality):.4f}")
print(f"With continuity correction:    P(X {inequality} {x}) = {probability_normal(x, mu, sigma, continuity=True, inequality=inequality):.4f}")

# Example for range: P(a <= X <= b)
a, b = 25, 35
print(f"\nP({a} <= X <= {b}) without continuity correction = {probability_between(a, b, mu, sigma, continuity=False):.4f}")
print(f"P({a} <= X <= {b}) with continuity correction = {probability_between(a, b, mu, sigma, continuity=True):.4f}")

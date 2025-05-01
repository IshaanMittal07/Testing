import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Example: dy/dt = -2y (exponential decay)

def ode(t, y):
    return -2 * y

# Time span and initial condition
t_span = (0, 5)         # From t=0 to t=5
y0 = [1]                # Initial value y(0) = 1
t_eval = np.linspace(*t_span, 100)  # Time points to evaluate at

# Solve the ODE
solution = solve_ivp(ode, t_span, y0, t_eval=t_eval)

# Plot the solution
plt.plot(solution.t, solution.y[0], label='y(t)')
plt.xlabel('Time')
plt.ylabel('y')
plt.title('Solution of dy/dt = -2y')
plt.grid(True)
plt.legend()
plt.show()

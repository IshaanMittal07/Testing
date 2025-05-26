import numpy as np
import matplotlib.pyplot as plt

# Sample data (you can change these values or take user input)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Calculate the coefficients (slope m and intercept b)
m, b = np.polyfit(x, y, 1)

# Create the best fit line
best_fit_line = m * x + b

# Plotting
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, best_fit_line, color='red', label=f'Best Fit Line: y = {m:.2f}x + {b:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line of Best Fit')
plt.legend()
plt.grid(True)
plt.show()

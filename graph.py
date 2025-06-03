import matplotlib.pyplot as plt

# Example table of values (X and Y)
# You can change these to any values you want
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 1, 3, 7]

# Plotting the graph
plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')

# Adding title and labels
plt.title("Graph from Table of Values")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Displaying the grid
plt.grid(True)

# Show the chart
plt.show()

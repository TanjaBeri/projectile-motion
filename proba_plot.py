import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initialize an empty list to collect 3D data after each loop
data_collections = []

# Simulate a loop where 3D data is generated
for i in range(5):
    # Generate new 3D data points (x, y, z)
    new_data = [i, i**2, i**3]  # Example: (x, y, z) = (i, i^2, i^3)
    
    # Append the new 3D point to the collection
    data_collections.append(new_data)

# Convert the collected data into a 2D NumPy array
data_array = np.array(data_collections)

# Plotting the 3D data
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Extract x, y, z coordinates from the array
x = data_array[:, 0]
y = data_array[:, 1]
z = data_array[:, 2]

# Plot the 3D points
ax.plot(x, y, z, marker='o', label='Trajectory')

# Adding labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Data Plot')

# Show the legend
ax.legend()

# Display the plot
plt.show()

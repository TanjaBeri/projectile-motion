import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.81
dt = 0.01
b = 0.001 # drag coefficient

# Initial conditions
v0 = 50
angle = 45
vx = v0 * np.cos(np.radians(angle))
vy = v0 * np.sin(np.radians(angle))
x, y = 0, 0

# Lists to store positions
x_positions, y_positions = [], []

while y >= 0:
    # Update velocities with drag
    v = np.sqrt(vx**2 + vy**2)
    drag = b * v**2
    angle_of_velocity = np.arctan2(vy,vx)
    vx -= drag * np.cos(angle_of_velocity) * dt
    vy -= (g + drag * np.sin(angle_of_velocity)) * dt

    # Update positions
    x += vx * dt
    y += vy * dt
    x_positions.append(x)
    y_positions.append(y)

plt.plot(x_positions,y_positions)
plt.title("Projectile motion with air resistance")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

v0, angle = 50,45 # initial conditions
g = 9.81
theta = np.radians(angle)
t = np.linspace(0,2 * v0 * np.sin(theta) / g,100)

plt.plot(v0 * np.cos(theta) * t, v0 * np.sin(theta) * t - 0.5 * g * t**2)
plt.title("Quick projectile motion using numpy")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.show()
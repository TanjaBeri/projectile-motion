import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(v0, angle):
    g = 9.81
    theta = np.radians(angle)
    v0x = v0 * np.cos(theta)
    v0y = v0 * np.sin(theta)
    tf = (2 * v0y) / g
    t = np.linspace(0,tf,num=100)
    x = v0x * t;
    y = v0y * t - 0.5 * g * t**2
    return x,y,tf

x, y, time_of_flight = projectile_motion(20,23)
plt.plot(x,y)
plt.title("Projectile motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.show()
print(f'Time of flight = {time_of_flight} s')
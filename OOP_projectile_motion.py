import matplotlib.pyplot as plt
import numpy as np

class Projectile:
    def __init__(self, v0, angle):
        self.x = 0
        self.y = 0
        self.v_x = v0 * np.cos(np.radians(angle))
        self.v_y = v0 * np.sin(np.radians(angle))
        self.g = 9.81

    def update(self, dt):
        self.x += self.v_x * dt
        self.y += self.v_y * dt
        self.v_y -= self.g * dt

    def plot_trajectory(self):
        total_time = 2 * self.v_y / self.g
        timesteps = int(total_time / dt)
        x_vals, y_vals = [], []

        for _ in range(timesteps):
            self.update(dt)
            if self.y < 0: break
            x_vals.append(self.x)
            y_vals.append(self.y)

        plt.plot(x_vals,y_vals)
        plt.title("Projectile motion (OOP approach)")
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.show()


dt = 0.01
projectile = Projectile(50,45)
projectile.plot_trajectory()

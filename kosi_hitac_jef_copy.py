import numpy as np
import matplotlib.pyplot as plt
from moving_average_filter import X_kol1,Y_kol1,Z_kol1
from moving_average_filter import X_list,Y_list,Z_list


# Parameters

#x0, y0, z0 = X_list[i], Y_list[i],Z_list[i]       # Initial position
#x1, y1, z1 = X_list[i+1],Y_list[i+1],Z_list[i+1]
g = 9810                                          # Acceleration due to gravity (mm/s^2)
dt = 0.01
'''v0x = (x1 - x0) / dt
v0y = (y1 - y0) / dt
v0z = (z1 - z0) / dt'''



# Time intervals
#t = np.linspace(0, T, num=120)

# Equations of motion

i = 0


trajectories = []

n_samples = len(X_list)
# time of flight
T = n_samples/100
for i in range(1,n_samples): 
    x = X_list[:i]
    y = Y_list[:i]
    z = Z_list[:i]
    traj = []
    t = i*dt
    x0, y0, z0 = X_list[i-1], Y_list[i-1],Z_list[i-1]       
    x1, y1, z1 = X_list[i],Y_list[i],Z_list[i]
    # x.append(x0)
    # x.append(x1)
    # y.append(y0)
    # y.append(y1)
    # z.append(z0)
    # z.append(z1)
    v0x = (x1 - x0) / dt
    v0y = (y1 - y0) / dt
    v0z = (z1 - z0) / dt


    k = 0

    while t <= T:
    
        x_novo = x0 + v0x * (t+dt)
        #print(f"X novo {k+1} prolaz: {x_novo}")
        x.append(x_novo)
        y_novo = y0 + v0y * (t+dt)
        y.append(y_novo)
        z_novo = z0 + v0z * (t+dt) - 0.5 * g * (t+dt)**2
        z.append(z_novo)
        t += dt

        #v0x = (x_trenutno - x_prethodno) / dt
        #v0y = (y_trenutno - y_prethodno) / dt
        #v0z = (z_trenutno - z_prethodno) / dt

        k += 1
    
    trajectories.append([x,y,z])
   


trajectories = np.array(trajectories)
print("Estimirane trajektroije: ",trajectories)
trajectories.tofile('estimirani podaci.csv',sep=',')

X_arr = np.array(X_list)
Y_arr = np.array(Y_list)
Z_arr = np.array(Z_list)
#print("Tip x",type(x))
#print("Tip x list",type(X_arr))







fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X_arr,Y_arr,Z_arr, label = "Snimljeni podaci")


# ax.plot(trajectories[:, 0], trajectories[:, 1], trajectories[:, 2])

# Extract x, y, z coordinates from the array for plotting
X = trajectories[:, 0]
Y = trajectories[:, 1]
Z = trajectories[:, 2]

# Plot the 3D trajectory
for i in range(n_samples-5,n_samples-1):
    ax.scatter(X[i], Y[i], Z[i], linewidths = 0.1)
# ax.scatter(X[-1], Y[-1], Z[-1])
# Adding labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Plot of Combined Data')

# Show the legend
ax.legend()

# Display the plot
plt.show()


